import FWCore.ParameterSet.Config as cms

process = cms.Process('jetToolbox')

process.load('PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

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

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)


#--------------------- Input data  ----------------------------
#------ Note: For grid operation, the provided input below is irrelevant as input data is managed independently within the grid system (e.g., CRAB).
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root'
    )
)


process.TFileService = cms.Service("TFileService",
                                 fileName=cms.string('test_scouting.root'),
                                 #fileName=cms.string(THISROOTFILE),
                                 closeFileFast = cms.untracked.bool(True),
                                 #compressionAlgorithm = cms.untracked.string("ZSTD"),
                                 #compressionLevel = cms.untracked.int32(5)
                                 )



#--------------------- Output  edm format ---------------------------
process.out = cms.OutputModule('PoolOutputModule',                                                                                                                  
                               fileName = cms.untracked.string('jettoolbox.root'),                                                                              
                               outputCommands = cms.untracked.vstring([
                                'keep *_slimmedJets_*_*', 
                                'keep *_slimmedJetsPuppi_*_*',
                                ]) )



#------ Added 'vertexRef().isNonnull() &&' check for compatibility.
process.chs = cms.EDFilter('CandPtrSelector', src = cms.InputTag('packedPFCandidates'), cut = cms.string('vertexRef().isNonnull() && fromPV'))


process.load("EventFilter.L1TRawToDigi.gtStage2Digis_cfi")
process.gtStage2Digis.InputLabel = cms.InputTag( "hltFEDSelectorL1" )


#--------------------- Gen Particles ---------------------------
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets

#------ Pruner
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.prunedGenParticlesDijet = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("prunedGenParticles"),
    select = cms.vstring(
    "drop  *  ", # by default
    "keep ( status = 3 || (status>=21 && status<=29) )", # keep hard process particles
    )
)


#------ Recluster Gen Jets to access the constituents
#------ Already in toolbox, just adding 'keep' statements
process.out.outputCommands.append("keep *_slimmedGenJets_*_*")



#-------------------- User analyzer  --------------------------------
L1Info = ["L1_DoubleMu_15_7","L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7","L1_DoubleMu8_SQ","L1_DoubleMu4er2p0_SQ_OS_dR_Max1p6","L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4","L1_DoubleMu4p5_SQ_OS_dR_Max1p2","L1_DoubleMu0_Upt6_SQ_er2p0","L1_DoubleMu0_Upt7_SQ_er2p0","L1_DoubleMu0_Upt8_SQ_er2p0", "L1_DoubleMu0_Upt15_Upt7", "L1_DoubleMu0_Upt6_IP_Min1_Upt4", "L1_DoubleMu3er2p0_SQ_OS_dR_Max1p6"]

# https://cmshltinfo.app.cern.ch/summary?search=DST_&year=2024&paths=true&prescaled=false&stream-types=Scouting
HLT_Info = cms.vstring("DST_PFScouting_JetHT_v", "DST_PFScouting_SingleMuon_v", "DST_PFScouting_ZeroBias_v", "DST_PFScouting_AXOTight_v", "DST_PFScouting_AXOVLoose_v", "DST_PFScouting_AXOLoose_v", "DST_PFScouting_AXOVTight_v", "DST_PFScouting_SinglePhotonEB_v", "DST_PFScouting_CICADAVLoose_v", "DST_PFScouting_CICADALoose_v", "DST_PFScouting_CICADAMedium_v", "DST_PFScouting_CICADATight_v", "DST_PFScouting_CICADAVTight_v")

HLT_Alias = cms.vstring([ (s.replace("DST_", "")[:-2] if s.endswith("_v") else s.replace("DST_", "")) for s in HLT_Info ]) #------ Remove prefix and suffixes ()"DST_" and "_v") for trigger alias


process.scoutingTree = cms.EDAnalyzer('ScoutingTreeMakerRun3',
                            isData                   =  cms.bool(True),
                            #------ JETS/MET
                            pfjets                   =  cms.InputTag("hltScoutingPFPacker"                             ),
                            rho                      =  cms.InputTag("hltScoutingPFPacker"             ,"rho"          ),
                            pfMet                    =  cms.InputTag("hltScoutingPFPacker"             ,"pfMetPt"      ),
                            pfMetPhi                 =  cms.InputTag("hltScoutingPFPacker"             ,"pfMetPhi"     ),
                            primaryVertices          =  cms.InputTag("hltScoutingPrimaryVertexPacker"  ,"primaryVtx"   ),
                            ptMinPF                  =  cms.double(10),

                            muonsNoVtx               =  cms.InputTag("hltScoutingMuonPackerNoVtx"                      ), # hltScoutingMuonPackerNoVtx && hltScoutingMuonPackerVtx 
                            muonsVtx                 =  cms.InputTag("hltScoutingMuonPackerVtx"                        ), 
                            electrons                =  cms.InputTag("hltScoutingEgammaPacker"                         ),
                            photons                  =  cms.InputTag("hltScoutingEgammaPacker"                         ),
                            pfcands                  =  cms.InputTag("hltScoutingPFPacker"                             ),
                            tracks                   =  cms.InputTag("hltScoutingTrackPacker"                          ),
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
                            l1GtSrc                  =  cms.InputTag('gtStage2Digis'  ,'' ,'HLT'),  #---- Perform edmDumpEventContent to check
                            l1tResults               =  cms.InputTag('','',''),
                            UnprefirableEventToken   =  cms.InputTag('simGtExtUnprefireable','','PAT'),
                            daqPartitions            =  cms.uint32(1),
                            l1tIgnoreMaskAndPrescale =  cms.bool(False),
                            throw                    =  cms.bool(True),
                            usePathStatus            =  cms.bool(False),
)

process.p = cms.Path(process.gtStage2Digis+process.scoutingTree)

