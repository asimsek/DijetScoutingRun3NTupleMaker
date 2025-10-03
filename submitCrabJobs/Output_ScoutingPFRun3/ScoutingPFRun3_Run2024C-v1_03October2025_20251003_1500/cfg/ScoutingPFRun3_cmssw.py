import FWCore.ParameterSet.Config as cms
import os, re

# --- year/era for JECs
era_     = '2024C'
jecMode_ = 'txt' # 'es'| 'txt' | 'none' 
doJetVetoMap = True

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
#process.GlobalTag = GlobalTag(process.GlobalTag, '150X_dataRun3_HLT_v1', '') ## 2025C
#process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_HLT_v3', '') ## 2024H
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_dataRun3_HLT_v3', '')


#--------------------- Report and output ---------------------------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True) ## --- Set False to suppress long output
)
process.MessageLogger.cerr.FwkSummary.reportEvery = 100000
process.MessageLogger.cerr.FwkReport.reportEvery  = 100000

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
        'root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root' ## 2025C
        #'root://cms-xrd-global.cern.ch//store/data/Run2024H/ScoutingPFRun3/HLTSCOUT/v1/000/385/836/00000/003ca643-43f8-40dd-92b3-4c6a4ccdc894.root' ## 2024H
        #'root://cms-xrd-global.cern.ch//store/data/Run2024I/ScoutingPFMonitor/RAW/v1/000/386/478/00000/07e75911-a7bc-4ac2-be24-323d49b07ba0.root', ## 2024H ScoutingPFMonitor
        #'root://cms-xrd-global.cern.ch//store/mc/RunIII2024Summer24DRPremix/QCD_Bin-PT-50to80_TuneCP5_13p6TeV_pythia8/AODSIM/140X_mcRun3_2024_realistic_v26-v2/120000/005210b9-bf51-4f56-be43-814a093fc0af.root'
        #'root://cms-xrd-global.cern.ch//store/mc/RunIII2024Summer24DRPremix/RSGravitonTo2G_kMpl-001_M-450_TuneCP5_13p6TeV_pythia8/AODSIM/140X_mcRun3_2024_realistic_v26-v2/2530000/0bf5c319-aa53-4d83-bd9b-0bb4fbc3446d.root'
    )
)

#-----------------------------------------------------------------------#
#------------------ JEC reading from config file  -----------------------
#-----------------------------------------------------------------------#
from DijetScoutingRun3NTupleMaker.ScoutingNtuplizer.configs.jec_utils import (
    infer_era_from_filenames,
    load_jec_config_text,
    get_era_block,
)

#------ load JEC config db and pick the block
data_jec_list = "data_jec_list.txt"
mc_jec_list   = "mc_jec_list.txt"

data_block = get_era_block(
    load_jec_config_text(os.path.join(os.path.dirname(__file__), '../../data/cfg', data_jec_list)),
    era_
)
mc_block = get_era_block(
    load_jec_config_text(os.path.join(os.path.dirname(__file__), '../../data/cfg', mc_jec_list)),
    era_
)

#------ Assemble base TXT (no Residual here by design)
base_txt_data = [data_block.get('L1FastJet',''),
                 data_block.get('L2Relative',''),
                 data_block.get('L3Absolute','')]
base_txt_data = [p for p in base_txt_data if p]

base_txt_mc   = [mc_block.get('L1FastJet',''),
                 mc_block.get('L2Relative',''),
                 mc_block.get('L3Absolute','')]
base_txt_mc   = [p for p in base_txt_mc if p]

#------ Residual run maps (list of min:max:file strings)
residual_map_data = list(data_block.get('L2L3Residual', []))
residual_map_mc   = list(mc_block.get('L2L3Residual', []))  # will be ignored for MC in C++

#------ Uncertainty files
unc_file_data = data_block.get('Unc','')
unc_file_mc   = mc_block.get('Unc','')

#------ Jet veto map files (accept string or list)
def _norm_vetomap(block):
    v = block.get('JetVetoMap', [])
    if isinstance(v, str): v = [v]
    return [str(x).strip() for x in v if str(x).strip()]

vetomap_files_data = _norm_vetomap(data_block)
vetomap_files_mc   = _norm_vetomap(mc_block)
#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#
#-----------------------------------------------------------------------#


process.TFileService = cms.Service("TFileService",
                                 #fileName=cms.string('test_scouting.root'),
                                 fileName=cms.string('ScoutingPFRun3__Run2024C-v1__HLTSCOUT.root'),
                                 closeFileFast = cms.untracked.bool(True),
                                 #compressionAlgorithm = cms.untracked.string("ZSTD"),
                                 #compressionLevel = cms.untracked.int32(5) # try 5-8: larger = smaller & slower
                                 )


#-------------------- User analyzer  --------------------------------
L1Info = ['L1_HTT120er', 'L1_HTT160er', 'L1_HTT200er', 'L1_HTT255er', 'L1_HTT280er', 'L1_HTT320er', 'L1_HTT400er', 'L1_HTT450er', 'L1_ZeroBias']

# https://cmshltinfo.app.cern.ch/summary?search=DST_&year=2024&paths=true&prescaled=false&stream-types=Scouting
HLT_Info = cms.vstring("DST_PFScouting_JetHT_v", "DST_PFScouting_SingleMuon_v", "HLT_Mu50_v", "HLT_Mu55_v", "HLT_IsoMu24_v", "HLT_IsoMu20_v", "HLT_IsoMu27_v",
    "HLT_PFHT180_v", "HLT_PFHT180_v", "HLT_PFHT350_v", "HLT_PFHT370_v", "HLT_PFHT430_v", "HLT_PFHT510_v", "HLT_PFHT590_v",
    "HLT_PFJet40_v", "HLT_PFJet60_v", "HLT_PFJet80_v", "HLT_PFJet140_v", "HLT_PFJet200_v", "HLT_PFJet260_v", "HLT_PFJet320_v", "HLT_PFJet400_v", "HLT_PFJet450_v", "HLT_PFJet500_v", "HLT_PFJet550_v", 
    "DST_PFScouting_ZeroBias_v", "DST_PFScouting_AXOTight_v", "DST_PFScouting_AXOVLoose_v", "DST_PFScouting_AXOLoose_v", "DST_PFScouting_AXOVTight_v", "DST_PFScouting_SinglePhotonEB_v", 
    "DST_PFScouting_CICADAVLoose_v", "DST_PFScouting_CICADALoose_v", "DST_PFScouting_CICADAMedium_v", "DST_PFScouting_CICADATight_v", "DST_PFScouting_CICADAVTight_v")

HLT_Alias = cms.vstring([ (s.replace("DST_", "")[:-2] if s.endswith("_v") else s.replace("DST_", "")) for s in HLT_Info ]) #------ Remove prefix and suffixes ("DST_" and "_v") for trigger alias


process.dijetScouting = cms.EDAnalyzer('ScoutingTreeMakerRun3',
                            ptMinPF                  =  cms.double(15),

                            # --- Jet veto maps ---
                            applyJetVetoMap          =  cms.bool(doJetVetoMap),

                            # --- JEC options ---
                            applyJEC                 =  cms.bool(True),
                            jecUncFallbackToTxt      =  cms.bool(True),          # ES-mode uncertainty fallback control
                            jecResidualFallbackToTxt =  cms.bool(True),          # ES-mode residual (L2L3Residual) TXT fallback control
                            jecMode                  =  cms.string(jecMode_),
                            jecPayload               =  cms.string("AK4PFHLT"),  # e.g. 'AK4PFHLT' or 'AK8PFHLT' `conddb list <YourGlobalTag> | grep JetCorrectionsRecord`
                            jecLevels                =  cms.vstring("L1FastJet","L2Relative","L3Absolute","L2L3Residual"),

                            # --- Provide both sources; C++ will choose once based on 'isData'
                            jecTxtFilesData          =  cms.vstring(base_txt_data),
                            jecResidualMapData       =  cms.vstring(residual_map_data),
                            jecUncTxtFileData        =  cms.string(unc_file_data),
                            jetVetoMapFilesData      =  cms.vstring(vetomap_files_data),

                            jecTxtFilesMC            =  cms.vstring(base_txt_mc),
                            jecResidualMapMC         =  cms.vstring(residual_map_mc),     # will be ignored for MC residuals
                            jecUncTxtFileMC          =  cms.string(unc_file_mc),
                            jetVetoMapFilesMC        =  cms.vstring(vetomap_files_mc),

                            # --- Keep the original single-set params as empty; c++ script fills them after it picks
                            # --- DON'T CHANGE ANYTHING HERE --- #
                            jecTxtFiles              =  cms.vstring(),
                            jecResidualByRun         =  cms.bool(False),
                            jecResidualMap           =  cms.vstring(),
                            applyJECUncertainty      =  cms.bool(True),
                            jecUncTxtFile            =  cms.string(""),
                            jetVetoMapFiles          =  cms.vstring(),
                            # ---------------------------------- #

                            # --- Print controls (for ES/TXT alike)
                            printJECInfo             =  cms.bool(True),    # set True to print
                            printJECFirstNJets       =  cms.uint32(6),     # print at most this many jets (total)

                            # --- JETS/MET
                            pfjets                   =  cms.InputTag("hltScoutingPFPacker"                             ),
                            pfcands                  =  cms.InputTag("hltScoutingPFPacker"                             ), # just to be safe...
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

                            # --- MC
                            pu                       =  cms.untracked.InputTag('slimmedAddPileupInfo' ),
                            ptHat                    =  cms.untracked.InputTag('generator'            ),
                            genParticles             =  cms.InputTag('prunedGenParticlesDijet'        ),
                            genJetsAK4               =  cms.InputTag('slimmedGenJets'                 ),

                            # --- Trigger
                            doL1                     =  cms.bool(True),
                            doTriggerObjects         =  cms.bool(True),
                            ReadPrescalesFromFile    =  cms.bool(False),
                            l1Seeds                  =  cms.vstring(L1Info),
                            triggerSelection         =  HLT_Info,
                            TriggerResultsTag        =  cms.InputTag('TriggerResults' ,'' ,'HLT' ),
                            NoiseFilterResultsTag    =  cms.InputTag('TriggerResults' ,'' ,'HLT'),
                            l1GtSrc                  =  cms.InputTag('gtStage2Digis'  ,'' ,'HLT'),
                            l1tResults               =  cms.InputTag('','',''),
                            l1tIgnoreMaskAndPrescale =  cms.bool(False),
                            throw                    =  cms.bool(True),
                            usePathStatus            =  cms.bool(False),
)


process.p = cms.Path(process.gtStage2Digis+process.dijetScouting)


