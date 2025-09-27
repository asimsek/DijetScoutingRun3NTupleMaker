import FWCore.ParameterSet.Config as cms
import os, re

# --- year/era for JECs
era_     = '2025C'
jecMode_ = 'txt' # 'es'| 'txt' | 'none' 

process = cms.Process('jetToolbox')

process.load('PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.load("EventFilter.L1TRawToDigi.gtStage2Digis_cfi")
process.gtStage2Digis.InputLabel = cms.InputTag( "hltFEDSelectorL1" )

## ----------------- Global Tag ------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_HLT_v1', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, THISGLOBALTAG, '')


#--------------------- Report and output ---------------------------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True) ## --- Set False to suppress long output
)
process.MessageLogger.cerr.FwkSummary.reportEvery = 1000
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

#------Show JEC logs from the analyzer
process.MessageLogger.cerr.threshold = 'INFO'  # allow LogInfo/LogVerbatim
process.MessageLogger.cerr.default = cms.untracked.PSet(limit=cms.untracked.int32(0))
process.MessageLogger.cerr.JEC = cms.untracked.PSet(limit = cms.untracked.int32(1000000000))

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


#--------------------- Input data  ----------------------------
#------ Note: For grid operation, the provided input below is irrelevant as input data is managed independently within the grid system (e.g., CRAB).
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root'
    )
)


#------------------ JEC reading from config file  -----------------------
from DijetScoutingRun3NTupleMaker.ScoutingTreeMakerRun3.configs.jec_utils import (
    infer_era_from_filenames,
    load_jec_config_text,
    get_era_block,
)

#------ load JEC config db and pick the block
era_block = get_era_block(load_jec_config_text(os.path.join(os.path.dirname(__file__), 'configs', 'jec_config.txt')), era_)

#------ Assemble base TXT (no Residual here by design)
base_txt = [era_block.get('L1FastJet',''),
            era_block.get('L2Relative',''),
            era_block.get('L3Absolute','')]
base_txt = [p for p in base_txt if p]  # drop empties

#------ Residual run map (list of (min,max,file))
residual_map = [ ':'.join(t) for t in era_block.get('L2L3Residual', []) ]
unc_file = era_block.get('Unc','')
#--------------------------------------------------------------------------

process.TFileService = cms.Service("TFileService",
                                 fileName=cms.string('test_scouting.root'),
                                 #fileName=cms.string(THISROOTFILE),
                                 closeFileFast = cms.untracked.bool(True),
                                 #compressionAlgorithm = cms.untracked.string("ZSTD"),
                                 #compressionLevel = cms.untracked.int32(5) # try 5-8: larger = smaller & slower
                                 )


#-------------------- User analyzer  --------------------------------
L1Info = ['L1_HTT120er', 'L1_HTT160er', 'L1_HTT200er', 'L1_HTT255er', 'L1_HTT280er', 'L1_HTT320er', 'L1_HTT400er', 'L1_HTT450er', 'L1_ZeroBias']

# https://cmshltinfo.app.cern.ch/summary?search=DST_&year=2024&paths=true&prescaled=false&stream-types=Scouting
HLT_Info = cms.vstring("DST_PFScouting_JetHT_v", "DST_PFScouting_SingleMuon_v", 
    "HLT_PFHT180_v", "HLT_PFHT180_v", "HLT_PFHT350_v", "HLT_PFHT370_v", "HLT_PFHT430_v", "HLT_PFHT510_v", "HLT_PFHT590_v",
    "HLT_PFJet40_v", "HLT_PFJet60_v", "HLT_PFJet80_v", "HLT_PFJet140_v", "HLT_PFJet200_v", "HLT_PFJet260_v", "HLT_PFJet320_v", "HLT_PFJet400_v", "HLT_PFJet450_v", "HLT_PFJet500_v", "HLT_PFJet550_v", 
    "DST_PFScouting_ZeroBias_v", "DST_PFScouting_AXOTight_v", "DST_PFScouting_AXOVLoose_v", "DST_PFScouting_AXOLoose_v", "DST_PFScouting_AXOVTight_v", "DST_PFScouting_SinglePhotonEB_v", "DST_PFScouting_CICADAVLoose_v", "DST_PFScouting_CICADALoose_v", "DST_PFScouting_CICADAMedium_v", "DST_PFScouting_CICADATight_v", "DST_PFScouting_CICADAVTight_v")

HLT_Alias = cms.vstring([ (s.replace("DST_", "")[:-2] if s.endswith("_v") else s.replace("DST_", "")) for s in HLT_Info ]) #------ Remove prefix and suffixes ("DST_" and "_v") for trigger alias


process.scoutingTree = cms.EDAnalyzer('ScoutingTreeMakerRun3',
                            isData                   =  cms.bool(True),
                            ptMinPF                  =  cms.double(15),

                            # --- JEC options ---
                            applyJEC                 =  cms.bool(True),
                            jecMode                  =  cms.string(jecMode_),
                            jecPayload               =  cms.string("AK4PFHLT"),  # e.g. 'AK4PFHLT' or 'AK4PFPuppiHLT'
                            jecLevels                =  cms.vstring("L1FastJet","L2Relative","L3Absolute","L2L3Residual"),

                            # TXT base files (L1/L2/L3) from file only if txt mode; otherwise empty
                            jecTxtFiles              =  cms.vstring(base_txt),

                            # TXT per-run residual mapping (enabled only in txt mode)
                            jecResidualByRun         =  cms.bool(len(residual_map)>0),
                            jecResidualMap           =  cms.vstring(residual_map),
                            applyJECUncertainty      =  cms.bool(True),
                            jecUncTxtFile            =  cms.string(unc_file),

                            # --- Print controls (for ES/TXT alike)
                            printJECInfo             =  cms.bool(True),    # set True to print
                            printJECFirstNJets       =  cms.uint32(6),     # print at most this many jets (total)

                            #------ JETS/MET
                            pfcands                  =  cms.InputTag("hltScoutingPFPacker"                             ),
                            rho                      =  cms.InputTag("hltScoutingPFPacker"             ,"rho"          ),
                            pfMet                    =  cms.InputTag("hltScoutingPFPacker"             ,"pfMetPt"      ),
                            pfMetPhi                 =  cms.InputTag("hltScoutingPFPacker"             ,"pfMetPhi"     ),
                            primaryVertices          =  cms.InputTag("hltScoutingPrimaryVertexPacker"  ,"primaryVtx"   ),

                            tracks                   =  cms.InputTag("hltScoutingTrackPacker"                          ),
                            electrons                =  cms.InputTag("hltScoutingEgammaPacker"                         ),
                            photons                  =  cms.InputTag("hltScoutingEgammaPacker"                         ),
                            muonsVtx                 =  cms.InputTag("hltScoutingMuonPackerVtx"                        ),
                            muonsNoVtx               =  cms.InputTag("hltScoutingMuonPackerNoVtx"                      ),
                            displacedVertices        =  cms.InputTag("hltScoutingMuonPackerNoVtx"      ,"displacedVtx" ),

                            #------ MC
                            pu                       =  cms.untracked.InputTag('slimmedAddPileupInfo' ),
                            ptHat                    =  cms.untracked.InputTag('generator'            ),
                            genParticles             =  cms.InputTag('prunedGenParticlesDijet'        ),
                            genJetsAK4               =  cms.InputTag('slimmedGenJets'                 ),

                            #------ Trigger
                            doL1                     =  cms.bool(False),
                            doTriggerObjects         =  cms.bool(True),
                            ReadPrescalesFromFile    =  cms.bool(False),
                            l1Seeds                  =  cms.vstring(L1Info),
                            triggerSelection         =  HLT_Info,
                            TriggerResultsTag        =  cms.InputTag('TriggerResults' ,'' ,'HLT' ),
                            NoiseFilterResultsTag    =  cms.InputTag('TriggerResults' ,'' ,'HLT'),
                            l1GtSrc                  =  cms.InputTag('gtStage2Digis'  ,'' ,'HLT'),
                            l1tResults               =  cms.InputTag('','',''),
                            UnprefirableEventToken   =  cms.InputTag('simGtExtUnprefireable','','PAT'),
                            daqPartitions            =  cms.uint32(1),
                            l1tIgnoreMaskAndPrescale =  cms.bool(False),
                            throw                    =  cms.bool(True),
                            usePathStatus            =  cms.bool(False),
)


process.p = cms.Path(process.scoutingTree)
#process.p = cms.Path(process.gtStage2Digis+process.scoutingTree)


