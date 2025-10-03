import FWCore.ParameterSet.Config as cms

process = cms.Process("jetToolbox")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root')
)
process.AODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*'
     ) )
)

process.AODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*'
     ) ),
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

process.BeamSpotAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.BeamSpotFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.BeamSpotRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_offlineBeamSpot_*_*')
)

process.CommonEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_logErrorHarvester_*_*')
)

process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.DATAMIXEREventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep CSCDetIdCSCALCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCALCTDigi_*',
        'keep CSCDetIdCSCCLCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCCLCTDigi_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_muonCSCDigis_MuonCSCComparatorDigi_*',
        'keep CSCDetIdCSCCorrelatedLCTDigiMuonDigiCollection_csctfDigis_*_*',
        'keep CSCDetIdCSCCorrelatedLCTDigiMuonDigiCollection_muonCSCDigis_MuonCSCCorrelatedLCTDigi_*',
        'keep CSCDetIdCSCRPCDigiMuonDigiCollection_muonCSCDigis_MuonCSCRPCDigi_*',
        'keep CSCDetIdCSCStripDigiMuonDigiCollection_muonCSCDigis_MuonCSCStripDigi_*',
        'keep CSCDetIdCSCWireDigiMuonDigiCollection_muonCSCDigis_MuonCSCWireDigi_*',
        'keep DTLayerIdDTDigiMuonDigiCollection_muonDTDigis_*_*',
        'keep PixelDigiedmDetSetVector_siPixelDigis_*_*',
        'keep SiStripDigiedmDetSetVector_siStripDigis_*_*',
        'keep RPCDetIdRPCDigiMuonDigiCollection_muonRPCDigis_*_*',
        'keep HBHEDataFramesSorted_hcalDigis_*_*',
        'keep HFDataFramesSorted_hcalDigis_*_*',
        'keep HODataFramesSorted_hcalDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_*_*',
        'keep QIE11DataFrameHcalDataFrameContainer_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep CastorDataFramesSorted_castorDigis_*_*',
        'keep EBDigiCollection_ecalDigis_*_*',
        'keep EEDigiCollection_ecalDigis_*_*',
        'keep ESDigiCollection_ecalPreshowerDigis_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.DQMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_MEtoEDMConverter_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.DigiToRawFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*'
    )
)

process.EvtScalersAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*'
    )
)

process.EvtScalersRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*'
    )
)

process.FASTPUEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_fastSimProducer_*_*',
        'keep *_MuonSimHits_*_*',
        'drop *_fastSimProducer_VertexTypes_*',
        'keep *_generalTracksBeforeMixing_*_*',
        'drop *_generalTracksBeforeMixing_MVAValues_*',
        'drop *_generalTracksBeforeMixing_QualityMasks_*',
        'keep edmHepMCProduct_generatorSmeared_*_*'
    )
)

process.FEVTDEBUGEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_simCscTriggerPrimitiveDigis_*_*',
        'keep *_simDtTriggerPrimitiveDigis_*_*',
        'keep *_simRpcTriggerDigis_*_*',
        'keep *_simRctDigis_*_*',
        'keep *_simCsctfDigis_*_*',
        'keep *_simCsctfTrackDigis_*_*',
        'keep *_simDttfDigis_*_*',
        'keep *_simGctDigis_*_*',
        'keep *_simCaloStage1Digis_*_*',
        'keep *_simCaloStage1FinalDigis_*_*',
        'keep *_simCaloStage2Layer1Digis_*_*',
        'keep *_simCaloStage2Digis_*_*',
        'keep *_simGmtDigis_*_*',
        'keep *_simBmtfDigis_*_*',
        'keep *_simKBmtfDigis_*_*',
        'keep *_simOmtfDigis_*_*',
        'keep *_simEmtfDigis_*_*',
        'keep *_simGmtStage2Digis_*_*',
        'keep *_simGtDigis_*_*',
        'keep *_simGtStage2Digis_*_*',
        'keep *_cscTriggerPrimitiveDigis_*_*',
        'keep *_dtTriggerPrimitiveDigis_*_*',
        'keep *_rpcTriggerDigis_*_*',
        'keep *_rctDigis_*_*',
        'keep *_csctfDigis_*_*',
        'keep *_csctfTrackDigis_*_*',
        'keep *_dttfDigis_*_*',
        'keep *_gctDigis_*_*',
        'keep *_gmtDigis_*_*',
        'keep *_gtDigis_*_*',
        'keep *_gtEvmDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep *_simSiPixelDigis_*_*',
        'keep *_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_trackingParticleRecoTrackAsssociation_*_*',
        'keep *_assoc2secStepTk_*_*',
        'keep *_assoc2thStepTk_*_*',
        'keep *_assoc2GsfTracks_*_*',
        'keep *_assocOutInConversionTracks_*_*',
        'keep *_assocInOutConversionTracks_*_*',
        'keep *_TTClusterAssociatorFromPixelDigis_*_*',
        'keep *_TTStubAssociatorFromPixelDigis_*_*',
        'keep *_simHitTPAssocProducer_*_*',
        'keep *_simMuonCSCDigis_*_*',
        'keep *_simMuonDTDigis_*_*',
        'keep *_simMuonRPCDigis_*_*',
        'keep *_simEcalDigis_*_*',
        'keep *_simEcalPreshowerDigis_*_*',
        'keep *_simEcalTriggerPrimitiveDigis_*_*',
        'keep *_simEcalEBTriggerPrimitiveDigis_*_*',
        'keep *_simEcalEBTriggerPrimitivePhase2Digis_*_*',
        'keep *_simHcalDigis_*_*',
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*',
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*',
        'keep *_simHcalTriggerPrimitiveDigis_*_*',
        'keep *_mix_HcalSamples_*',
        'keep *_mixData_HcalSamples_*',
        'keep *_mix_HcalHits_*',
        'keep *_mixData_HcalHits_*',
        'keep *_DMHcalTriggerPrimitiveDigis_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTDEBUGHLTEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_simCscTriggerPrimitiveDigis_*_*',
        'keep *_simDtTriggerPrimitiveDigis_*_*',
        'keep *_simRpcTriggerDigis_*_*',
        'keep *_simRctDigis_*_*',
        'keep *_simCsctfDigis_*_*',
        'keep *_simCsctfTrackDigis_*_*',
        'keep *_simDttfDigis_*_*',
        'keep *_simGctDigis_*_*',
        'keep *_simCaloStage1Digis_*_*',
        'keep *_simCaloStage1FinalDigis_*_*',
        'keep *_simCaloStage2Layer1Digis_*_*',
        'keep *_simCaloStage2Digis_*_*',
        'keep *_simGmtDigis_*_*',
        'keep *_simBmtfDigis_*_*',
        'keep *_simKBmtfDigis_*_*',
        'keep *_simOmtfDigis_*_*',
        'keep *_simEmtfDigis_*_*',
        'keep *_simGmtStage2Digis_*_*',
        'keep *_simGtDigis_*_*',
        'keep *_simGtStage2Digis_*_*',
        'keep *_cscTriggerPrimitiveDigis_*_*',
        'keep *_dtTriggerPrimitiveDigis_*_*',
        'keep *_rpcTriggerDigis_*_*',
        'keep *_rctDigis_*_*',
        'keep *_csctfDigis_*_*',
        'keep *_csctfTrackDigis_*_*',
        'keep *_dttfDigis_*_*',
        'keep *_gctDigis_*_*',
        'keep *_gmtDigis_*_*',
        'keep *_gtDigis_*_*',
        'keep *_gtEvmDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep *_simSiPixelDigis_*_*',
        'keep *_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_trackingParticleRecoTrackAsssociation_*_*',
        'keep *_assoc2secStepTk_*_*',
        'keep *_assoc2thStepTk_*_*',
        'keep *_assoc2GsfTracks_*_*',
        'keep *_assocOutInConversionTracks_*_*',
        'keep *_assocInOutConversionTracks_*_*',
        'keep *_TTClusterAssociatorFromPixelDigis_*_*',
        'keep *_TTStubAssociatorFromPixelDigis_*_*',
        'keep *_simHitTPAssocProducer_*_*',
        'keep *_simMuonCSCDigis_*_*',
        'keep *_simMuonDTDigis_*_*',
        'keep *_simMuonRPCDigis_*_*',
        'keep *_simEcalDigis_*_*',
        'keep *_simEcalPreshowerDigis_*_*',
        'keep *_simEcalTriggerPrimitiveDigis_*_*',
        'keep *_simEcalEBTriggerPrimitiveDigis_*_*',
        'keep *_simEcalEBTriggerPrimitivePhase2Digis_*_*',
        'keep *_simHcalDigis_*_*',
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*',
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*',
        'keep *_simHcalTriggerPrimitiveDigis_*_*',
        'keep *_mix_HcalSamples_*',
        'keep *_mixData_HcalSamples_*',
        'keep *_mix_HcalHits_*',
        'keep *_mixData_HcalHits_*',
        'keep *_DMHcalTriggerPrimitiveDigis_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_*_MergedTrackTruth_*',
        'keep *_*_StripDigiSimLink_*',
        'keep *_*_PixelDigiSimLink_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTHLTALLEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep *_*_*_HLT'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.FEVTSIMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.GENEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep *_externalLHEProducer_LHEScriptOutput_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_randomEngineStateProducer_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.GENRAWEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep recoGenMETs_*_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_logErrorHarvester_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.GeneratorInterfaceAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*'
    )
)

process.GeneratorInterfaceLHE = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep *_externalLHEProducer_LHEScriptOutput_*'
    )
)

process.GeneratorInterfaceRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*'
    )
)

process.GeneratorInterfaceRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*'
    )
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.HLTDEBUGEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_logErrorHarvester_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.HLTDebugFEVT = cms.PSet(
    outputCommands = cms.vstring(
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.HLTDebugRAW = cms.PSet(
    outputCommands = cms.vstring(
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.HLTONLYEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'drop  FEDRawDataCollection_rawDataCollector_*_*',
        'drop  FEDRawDataCollection_source_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.HLTONLYSIMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'drop  FEDRawDataCollection_rawDataCollector_*_*',
        'drop  FEDRawDataCollection_source_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.HLTSCOUTEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.HLTScouting = cms.PSet(
    outputCommands = cms.vstring(
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.HLTriggerAOD = cms.PSet(
    outputCommands = cms.vstring(
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.HLTriggerMINIAOD = cms.PSet(
    outputCommands = cms.vstring(
        'drop *_hlt*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.HLTriggerRAW = cms.PSet(
    outputCommands = cms.vstring(
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.HLTriggerRECO = cms.PSet(
    outputCommands = cms.vstring(
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.IOMCRAW = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_randomEngineStateProducer_*_*')
)

process.L1SCOUTEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.L1TriggerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiSummary_lumiProducer_*_*'
    )
)

process.L1TriggerFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_simCscTriggerPrimitiveDigis_*_*',
        'keep *_simDtTriggerPrimitiveDigis_*_*',
        'keep *_simRpcTriggerDigis_*_*',
        'keep *_simRctDigis_*_*',
        'keep *_simCsctfDigis_*_*',
        'keep *_simCsctfTrackDigis_*_*',
        'keep *_simDttfDigis_*_*',
        'keep *_simGctDigis_*_*',
        'keep *_simCaloStage1Digis_*_*',
        'keep *_simCaloStage1FinalDigis_*_*',
        'keep *_simCaloStage2Layer1Digis_*_*',
        'keep *_simCaloStage2Digis_*_*',
        'keep *_simGmtDigis_*_*',
        'keep *_simBmtfDigis_*_*',
        'keep *_simKBmtfDigis_*_*',
        'keep *_simOmtfDigis_*_*',
        'keep *_simEmtfDigis_*_*',
        'keep *_simGmtStage2Digis_*_*',
        'keep *_simGtDigis_*_*',
        'keep *_simGtStage2Digis_*_*',
        'keep *_cscTriggerPrimitiveDigis_*_*',
        'keep *_dtTriggerPrimitiveDigis_*_*',
        'keep *_rpcTriggerDigis_*_*',
        'keep *_rctDigis_*_*',
        'keep *_csctfDigis_*_*',
        'keep *_csctfTrackDigis_*_*',
        'keep *_dttfDigis_*_*',
        'keep *_gctDigis_*_*',
        'keep *_gmtDigis_*_*',
        'keep *_gtDigis_*_*',
        'keep *_gtEvmDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*'
    )
)

process.L1TriggerRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*'
    )
)

process.L1TriggerRAWDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*'
    )
)

process.L1TriggerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*'
    )
)

process.LHEEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep *_externalLHEProducer_LHEScriptOutput_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.METSignificanceParams = cms.PSet(
    dRMatch = cms.double(0.4),
    jetThreshold = cms.double(15),
    jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
    jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
    pjpar = cms.vdouble(-0.2586, 0.6173)
)

process.MEtoEDMConverterAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.MEtoEDMConverterFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConverter_*_*')
)

process.MEtoEDMConverterRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.MINIAODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.MINIAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep patPackedGenParticles_packedGenParticles_*_*',
        'keep recoGenParticles_prunedGenParticles_*_*',
        'keep *_packedPFCandidateToGenAssociation_*_*',
        'keep *_lostTracksToGenAssociation_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_*_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep recoGenParticles_genPUProtons_*_*',
        'keep *_slimmedGenJetsFlavourInfos_*_*',
        'keep *_slimmedGenJets__*',
        'keep *_slimmedGenJetsAK8__*',
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*',
        'keep *_genMetTrue_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep *_genParticles_xyz0_*',
        'keep *_genParticles_t0_*',
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*',
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*',
        'drop *_hlt*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    )
)

process.MINIGENEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep patPackedGenParticles_packedGenParticles_*_*',
        'keep recoGenParticles_prunedGenParticles_*_*',
        'keep *_packedPFCandidateToGenAssociation_*_*',
        'keep *_lostTracksToGenAssociation_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_*_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep recoGenParticles_genPUProtons_*_*',
        'keep *_slimmedGenJetsFlavourInfos_*_*',
        'keep *_slimmedGenJets__*',
        'keep *_slimmedGenJetsAK8__*',
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*',
        'keep *_genMetTrue_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep *_genParticles_xyz0_*',
        'keep *_genParticles_t0_*'
    )
)

process.MIXINGMODULEEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_cfWriter_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.MicroEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*'
    )
)

process.MicroEventContentGEN = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep patPackedGenParticles_packedGenParticles_*_*',
        'keep recoGenParticles_prunedGenParticles_*_*',
        'keep *_packedPFCandidateToGenAssociation_*_*',
        'keep *_lostTracksToGenAssociation_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_*_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep recoGenParticles_genPUProtons_*_*',
        'keep *_slimmedGenJetsFlavourInfos_*_*',
        'keep *_slimmedGenJets__*',
        'keep *_slimmedGenJetsAK8__*',
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*',
        'keep *_genMetTrue_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep *_genParticles_xyz0_*',
        'keep *_genParticles_t0_*'
    )
)

process.MicroEventContentMC = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep patPackedGenParticles_packedGenParticles_*_*',
        'keep recoGenParticles_prunedGenParticles_*_*',
        'keep *_packedPFCandidateToGenAssociation_*_*',
        'keep *_lostTracksToGenAssociation_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_*_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep recoGenParticles_genPUProtons_*_*',
        'keep *_slimmedGenJetsFlavourInfos_*_*',
        'keep *_slimmedGenJets__*',
        'keep *_slimmedGenJetsAK8__*',
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*',
        'keep *_genMetTrue_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep *_genParticles_xyz0_*',
        'keep *_genParticles_t0_*',
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*',
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*'
    )
)

process.NANOAODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep nanoaodFlatTable_*Table_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep String_*_genModel_*',
        'keep nanoaodMergeableCounterTable_*Table_*_*',
        'keep nanoaodUniqueString_nanoMetadata_*_*'
    )
)

process.NANOAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep nanoaodFlatTable_*Table_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep String_*_genModel_*',
        'keep nanoaodMergeableCounterTable_*Table_*_*',
        'keep nanoaodUniqueString_nanoMetadata_*_*'
    )
)

process.NanoAODEDMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep nanoaodFlatTable_*Table_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep String_*_genModel_*',
        'keep nanoaodMergeableCounterTable_*Table_*_*',
        'keep nanoaodUniqueString_nanoMetadata_*_*'
    )
)

process.OnlineMetaDataContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*'
    )
)

process.PREMIXEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep *_simSiPixelDigis_*_*',
        'keep *_simSiStripDigis_ZeroSuppressed_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'keep *_mix_AffectedAPVList_*',
        'keep EBDigiCollection_simEcalDigis_*_*',
        'keep EEDigiCollection_simEcalDigis_*_*',
        'keep ESDigiCollection_simEcalUnsuppressedDigis_*_*',
        'keep *_simHcalDigis_*_*',
        'keep *_mix_g4SimHitsMuonDTHits_*',
        'keep *_mix_g4SimHitsMuonCSCHits_*',
        'keep *_mix_g4SimHitsMuonRPCHits_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.PREMIXRAWEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'drop CrossingFramePlaybackInfoNew_mix_*_*',
        'keep *_*_MergedTrackTruth_*',
        'keep *_*_StripDigiSimLink_*',
        'keep *_*_PixelDigiSimLink_*',
        'keep *_*_MuonCSCStripDigiSimLinks_*',
        'keep *_*_MuonCSCWireDigiSimLinks_*',
        'keep *_*_RPCDigiSimLink_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_*_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWAODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*'
     ) )
)

process.RAWAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep SimVertexs_g4SimHits_*_*'
     ) )
)

process.RAWDEBUGEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*',
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWDEBUGHLTEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*',
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWMINIAODEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*'
    )
)

process.RAWMINIAODSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJPTJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep *_slimmedDisplacedMuons_*_*',
        'keep recoTrackExtras_slimmedDisplacedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedDisplacedMuonTrackExtras_*_*',
        'keep patPackedGenParticles_packedGenParticles_*_*',
        'keep recoGenParticles_prunedGenParticles_*_*',
        'keep *_packedPFCandidateToGenAssociation_*_*',
        'keep *_lostTracksToGenAssociation_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_*_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep recoGenParticles_genPUProtons_*_*',
        'keep *_slimmedGenJetsFlavourInfos_*_*',
        'keep *_slimmedGenJets__*',
        'keep *_slimmedGenJetsAK8__*',
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*',
        'keep *_genMetTrue_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep *_genParticles_xyz0_*',
        'keep *_genParticles_t0_*',
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*',
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*',
        'keep SimVertexs_g4SimHits_*_*'
    )
)

process.RAWRECODEBUGHLTEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'drop *',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECOEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWRECOSIMHLTEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMEventContent = cms.PSet(
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RAWSIMHLTEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop *',
        'drop *',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*',
        'drop *_hlt*_*_*',
        'keep *_hltAK4CaloJetsCorrectedIDPassed_*_*',
        'keep *_hltAK4CaloJetsIDPassed_*_*',
        'keep *_hltAK4CaloJets_*_*',
        'keep *_hltAK4PFJetsCorrected_*_*',
        'keep *_hltAK4PFJetsForTaus_*_*',
        'keep *_hltAK4PFJets_*_*',
        'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
        'keep *_hltAlCaEtaEERechitsToDigis_*_*',
        'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
        'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
        'keep *_hltAlCaPi0EERechitsToDigis_*_*',
        'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
        'keep *_hltAlcaPixelClusterCounts_*_*',
        'keep *_hltBSoftMuonMu5L3_*_*',
        'keep *_hltCsc2DRecHits_*_*',
        'keep *_hltCscSegments_*_*',
        'keep *_hltCtfWithMaterialTracksP5_*_*',
        'keep *_hltDeepBLifetimeTagInfosPF_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsCalo_*_*',
        'keep *_hltDeepCombinedSecondaryVertexBJetTagsPF_*_*',
        'keep *_hltDeepSecondaryVertexTagInfosPF_*_*',
        'keep *_hltDisplacedhltIter4PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurityPPOnAA_*_*',
        'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
        'keep *_hltDt4DSegments_*_*',
        'keep *_hltEcalPhiSymFilter_*_*',
        'keep *_hltEcalRecHit_*_*',
        'keep *_hltEgammaCandidates_*_*',
        'keep *_hltEgammaGsfTracks_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltFastPVPixelTracksMerger_*_*',
        'keep *_hltFastPVPixelTracksRecover_*_*',
        'keep *_hltFastPVPixelTracks_*_*',
        'keep *_hltFastPVPixelVertices_*_*',
        'keep *_hltFastPixelBLifetimeL3Associator_*_*',
        'keep *_hltFastPrimaryVertex_*_*',
        'keep *_hltFullSiStripRawToClustersFacility_*_*',
        'keep *_hltGlbTrkMuonCandsNoVtx_*_*',
        'keep *_hltGtStage2Digis_*_*',
        'keep *_hltHITrackingSiStripRawToClustersFacilityFullZeroSuppression_*_*',
        'keep *_hltHbhereco_*_*',
        'keep *_hltHfreco_*_*',
        'keep *_hltHoreco_*_*',
        'keep *_hltImpactParameterTagInfos_*_*',
        'keep *_hltInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_hltIsolPixelTrackProdHB_*_*',
        'keep *_hltIsolPixelTrackProdHE_*_*',
        'keep *_hltIter0PFlowCtfWithMaterialTracks_*_*',
        'keep *_hltIter0PFlowTrackSelectionHighPurity_*_*',
        'keep *_hltIter2MergedForDisplaced_*_*',
        'keep *_hltIterL3GlbMuon_*_*',
        'keep *_hltIterL3MuonAndMuonFromL1Merged_*_*',
        'keep *_hltIterL3MuonMerged_*_*',
        'keep *_hltIterL3MuonsNoID_*_*',
        'keep *_hltIterL3Muons_*_*',
        'keep *_hltIterL3OIMuonTrackSelectionHighPurity_*_*',
        'keep *_hltL2MuonCandidatesNoVtx_*_*',
        'keep *_hltL2MuonCandidates_*_*',
        'keep *_hltL2MuonSeeds_*_*',
        'keep *_hltL2Muons_*_*',
        'keep *_hltL2TauJets_*_*',
        'keep *_hltL3MuonsIOHit_*_*',
        'keep *_hltL3MuonsLinksCombination_*_*',
        'keep *_hltL3MuonsOIHit_*_*',
        'keep *_hltL3MuonsOIState_*_*',
        'keep *_hltL3Muons_*_*',
        'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
        'keep *_hltL3NoFiltersNoVtxMuons_*_*',
        'keep *_hltL3TkFromL2OICombination_*_*',
        'keep *_hltL3TkTracksFromL2IOHit_*_*',
        'keep *_hltL3TkTracksFromL2OIHit_*_*',
        'keep *_hltL3TkTracksFromL2OIState_*_*',
        'keep *_hltL3TkTracksFromL2_*_*',
        'keep *_hltL3TrackCandidateFromL2IOHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIHit_*_*',
        'keep *_hltL3TrackCandidateFromL2OIState_*_*',
        'keep *_hltL3TrajSeedIOHit_*_*',
        'keep *_hltL3TrajSeedOIHit_*_*',
        'keep *_hltL3TrajSeedOIState_*_*',
        'keep *_hltL3TrajectorySeed_*_*',
        'keep *_hltMergedTracksForBTag_*_*',
        'keep *_hltMergedTracksPPOnAA_*_*',
        'keep *_hltMergedTracks_*_*',
        'keep *_hltMet_*_*',
        'keep *_hltMuonCSCDigis_*_*',
        'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
        'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
        'keep *_hltMuonDTDigis_*_*',
        'keep *_hltMuonRPCDigis_*_*',
        'keep *_hltOnlineBeamSpot_*_*',
        'keep *_hltPFJetForBtag_*_*',
        'keep *_hltPFJetForPNetAK8_*_*',
        'keep *_hltPFMETNoMuProducer_*_*',
        'keep *_hltPFMETProducer_*_*',
        'keep *_hltPFMETTypeOne_*_*',
        'keep *_hltPFMuonMerging_*_*',
        'keep *_hltPFTau35Track_*_*',
        'keep *_hltPFTau35_*_*',
        'keep *_hltPPSCalibrationRaw_*_*',
        'keep *_hltParticleFlowForTaus_*_*',
        'keep *_hltParticleFlow_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTagsAK8_*_*',
        'keep *_hltParticleNetDiscriminatorsJetTags_*_*',
        'keep *_hltParticleNetJetTagInfos_*_*',
        'keep *_hltPixelTracksPPOnAA_*_*',
        'keep *_hltPixelTracks_*_*',
        'keep *_hltPixelVerticesPPOnAA_*_*',
        'keep *_hltPixelVertices_*_*',
        'keep *_hltRpcRecHits_*_*',
        'keep *_hltSelector4CentralJetsL1FastJet_*_*',
        'keep *_hltSelectorJets20L1FastJet_*_*',
        'keep *_hltSiPixelClustersAfterSplittingPPOnAA_*_*',
        'keep *_hltSiPixelClustersCache_*_*',
        'keep *_hltSiPixelClusters_*_*',
        'keep *_hltSiStripClusterizerForRawPrime_*_*',
        'keep *_hltSiStripClusters2ApproxClusters_*_*',
        'keep *_hltSiStripRawToClustersFacility_*_*',
        'keep *_hltTowerMakerForAll_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep *_hltTriggerSummaryRAW_*_*',
        'keep *_hltTrimmedPixelVerticesPPOnAA_*_*',
        'keep *_hltTrimmedPixelVertices_*_*',
        'keep *_hltVerticesL3_*_*',
        'keep *_hltVerticesPFFilterPPOnAA_*_*',
        'keep *_hltVerticesPFFilter_*_*',
        'keep *_hltVerticesPFSelector_*_*',
        'keep DetIds_hltSiStripRawToDigi_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep L2MuonTrajectorySeeds_hltL2MuonSeeds_*_*',
        'keep L3MuonTrajectorySeeds_hltL3TrajSeedOIState_*_*',
        'keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*',
        'keep TrackingRecHitsOwned_hltL3Muons_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep recoCaloJets_*_*_*',
        'keep recoCaloMETs_*_*_*',
        'keep recoCaloMETs_hltMet_*_*',
        'keep recoCompositeCandidates_*_*_*',
        'keep recoElectrons_*_*_*',
        'keep recoIsolatedPixelTrackCandidates_*_*_*',
        'keep recoMETs_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoPFTaus_*_*_*',
        'keep recoRecoChargedCandidates_*_*_*',
        'keep recoRecoChargedCandidates_hltL2MuonCandidates_*_*',
        'keep recoRecoEcalCandidates_*_*_*',
        'keep triggerTriggerEventWithRefs_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep triggerTriggerFilterObjectWithRefs_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RECODEBUGEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'drop *',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECOEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.RECOSIMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring( (
        'drop *',
        'drop *',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*',
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*',
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_l1GtRecord_*_*',
        'keep *_l1GtTriggerMenuLite_*_*',
        'keep *_conditionsInEdm_*_*',
        'keep *_l1extraParticles_*_*',
        'keep *_l1L1GtObjectMap_*_*',
        'keep L1MuGMTReadoutCollection_gtDigis_*_*',
        'keep L1GctEmCand*_gctDigis_*_*',
        'keep L1GctJetCand*_gctDigis_*_*',
        'keep L1GctEtHad*_gctDigis_*_*',
        'keep L1GctEtMiss*_gctDigis_*_*',
        'keep L1GctEtTotal*_gctDigis_*_*',
        'keep L1GctHtMiss*_gctDigis_*_*',
        'keep L1GctJetCounts*_gctDigis_*_*',
        'keep L1GctHFRingEtSums*_gctDigis_*_*',
        'keep L1GctHFBitCounts*_gctDigis_*_*',
        'keep LumiDetails_lumiProducer_*_*',
        'keep LumiSummary_lumiProducer_*_*',
        'drop *_hlt*_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep DcsStatuss_hltScalersRawToDigi_*_*',
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*',
        'keep L1TriggerScalerss_scalersRawToDigi_*_*',
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep BeamSpotOnlines_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep CTPPSRecord_onlineMetaDataDigis_*_*',
        'keep DCSRecord_onlineMetaDataDigis_*_*',
        'keep OnlineLuminosityRecord_onlineMetaDataDigis_*_*',
        'keep recoBeamSpot_onlineMetaDataDigis_*_*',
        'keep *_tcdsDigis_*_*',
        'keep *_logErrorHarvester_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*'
     ) ),
    splitLevel = cms.untracked.int32(0)
)

process.REDIGIEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'drop *_randomEngineStateProducer_*_*'
    )
)

process.REGENEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_genParticles_*_*',
        'drop *_genParticlesForJets_*_*',
        'drop *_kt4GenJets_*_*',
        'drop *_kt6GenJets_*_*',
        'drop *_iterativeCone5GenJets_*_*',
        'drop *_ak4GenJets_*_*',
        'drop *_ak7GenJets_*_*',
        'drop *_ak8GenJets_*_*',
        'drop *_ak4GenJetsNoNu_*_*',
        'drop *_ak8GenJetsNoNu_*_*',
        'drop *_genCandidatesForMET_*_*',
        'drop *_genParticlesForMETAllVisible_*_*',
        'drop *_genMetCalo_*_*',
        'drop *_genMetCaloAndNonPrompt_*_*',
        'drop *_genMetTrue_*_*',
        'drop *_genMetIC5GenJs_*_*'
    )
)

process.REPACKRAWEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop FEDRawDataCollection_*_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*',
        'keep FEDRawDataCollection_rawDataReducedFormat_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'drop FEDRawDataCollection_source_*_*',
        'drop FEDRawDataCollection_rawDataCollector_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.REPACKRAWSIMEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'drop FEDRawDataCollection_*_*_*',
        'keep FEDRawDataCollection_rawDataRepacker_*_*',
        'keep FEDRawDataCollection_virginRawDataRepacker_*_*',
        'keep FEDRawDataCollection_rawDataReducedFormat_*_*',
        'keep  FEDRawDataCollection_rawDataCollector_*_*',
        'keep  FEDRawDataCollection_source_*_*',
        'drop *_hlt*_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep triggerTriggerEvent_*_*_*',
        'keep *_hltFEDSelectorL1_*_*',
        'keep *_hltScoutingEgammaPacker_*_*',
        'keep *_hltScoutingMuonPackerNoVtx_*_*',
        'keep *_hltScoutingMuonPackerVtx_*_*',
        'keep *_hltScoutingPFPacker_*_*',
        'keep *_hltScoutingPrimaryVertexPacker_*_*',
        'keep *_hltScoutingTrackPacker_*_*',
        'keep edmTriggerResults_*_*_*',
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*',
        'keep recoGenMETs_*_*_*',
        'keep FEDRawDataCollection_source_*_*',
        'keep FEDRawDataCollection_rawDataCollector_*_*',
        'keep *_MEtoEDMConverter_*_*',
        'keep *_randomEngineStateProducer_*_*',
        'keep *_logErrorHarvester_*_*',
        'drop FEDRawDataCollection_source_*_*',
        'drop FEDRawDataCollection_rawDataCollector_*_*'
    ),
    splitLevel = cms.untracked.int32(0)
)

process.RESIMEventContent = cms.PSet(
    inputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_randomEngineStateProducer_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenRunInfoProduct_generator_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_generator_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep edmHepMCProduct_generatorSmeared_*_*',
        'keep edmHepMCProduct_LHCTransport_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep *_genParticles_*_*'
    )
)

process.RecoBTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*'
    )
)

process.RecoBTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*'
    )
)

process.RecoBTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_softPFMuonsTagInfos_*_*',
        'keep *_softPFElectronsTagInfos_*_*',
        'keep *_pfImpactParameterTagInfos_*_*',
        'keep *_pfSecondaryVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*',
        'keep *_pfGhostTrackVertexTagInfos_*_*',
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*',
        'keep *_softPFElectronBJetTags_*_*',
        'keep *_softPFMuonBJetTags_*_*',
        'keep *_pfTrackCountingHighEffBJetTags_*_*',
        'keep *_pfJetProbabilityBJetTags_*_*',
        'keep *_pfJetBProbabilityBJetTags_*_*',
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*',
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*',
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*',
        'keep *_pfGhostTrackBJetTags_*_*',
        'keep *_pfCombinedMVAV2BJetTags_*_*',
        'keep *_inclusiveCandidateSecondaryVertices_*_*',
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*',
        'keep *_pfCombinedCvsLJetTags_*_*',
        'keep *_pfCombinedCvsBJetTags_*_*',
        'keep *_pfChargeBJetTags_*_*',
        'keep *_pfDeepCSVJetTags_*_*',
        'keep *_pfDeepCMVAJetTags_*_*',
        'keep *_pixelClusterTagInfos_*_*'
    )
)

process.RecoBTauAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoBTauFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoBTauRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoCTPPSAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*',
        'keep TotemFEDInfos_totemRPRawToDigi_*_*',
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*',
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*',
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*',
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*',
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*',
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*',
        'keep TotemFEDInfos_totemT2Digis_*_*',
        'keep TotemT2DigiedmNewDetSetVector_totemT2Digis_*_*',
        'keep TotemVFATStatusedmDetSetVector_totemT2Digis_*_*',
        'keep TotemFEDInfos_ctppsDiamondRawToDigi_*_*',
        'keep CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_*_*',
        'keep TotemVFATStatusedmDetSetVector_ctppsDiamondRawToDigi_*_*',
        'keep CTPPSDiamondRecHitedmDetSetVector_ctppsDiamondRecHits_*_*',
        'keep CTPPSDiamondLocalTrackedmDetSetVector_ctppsDiamondLocalTracks_*_*',
        'keep TotemTimingLocalTrackedmDetSetVector_diamondSampicLocalTracks_*_*',
        'keep TotemTimingDigiedmDetSetVector_totemTimingRawToDigi_*_*',
        'keep TotemTimingRecHitedmDetSetVector_totemTimingRecHits_*_*',
        'keep TotemTimingLocalTrackedmDetSetVector_totemTimingLocalTracks_*_*',
        'keep CTPPSPixelDigiedmDetSetVector_ctppsPixelDigis_*_*',
        'keep CTPPSPixelDataErroredmDetSetVector_ctppsPixelDigis_*_*',
        'keep CTPPSPixelClusteredmDetSetVector_ctppsPixelClusters_*_*',
        'keep CTPPSPixelRecHitedmDetSetVector_ctppsPixelRecHits_*_*',
        'keep CTPPSPixelLocalTrackedmDetSetVector_ctppsPixelLocalTracks_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*'
    )
)

process.RecoCTPPSFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*',
        'keep TotemFEDInfos_totemRPRawToDigi_*_*',
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*',
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*',
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*',
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*',
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*',
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*',
        'keep TotemFEDInfos_totemT2Digis_*_*',
        'keep TotemT2DigiedmNewDetSetVector_totemT2Digis_*_*',
        'keep TotemVFATStatusedmDetSetVector_totemT2Digis_*_*',
        'keep TotemFEDInfos_ctppsDiamondRawToDigi_*_*',
        'keep CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_*_*',
        'keep TotemVFATStatusedmDetSetVector_ctppsDiamondRawToDigi_*_*',
        'keep CTPPSDiamondRecHitedmDetSetVector_ctppsDiamondRecHits_*_*',
        'keep CTPPSDiamondLocalTrackedmDetSetVector_ctppsDiamondLocalTracks_*_*',
        'keep TotemTimingLocalTrackedmDetSetVector_diamondSampicLocalTracks_*_*',
        'keep TotemTimingDigiedmDetSetVector_totemTimingRawToDigi_*_*',
        'keep TotemTimingRecHitedmDetSetVector_totemTimingRecHits_*_*',
        'keep TotemTimingLocalTrackedmDetSetVector_totemTimingLocalTracks_*_*',
        'keep CTPPSPixelDigiedmDetSetVector_ctppsPixelDigis_*_*',
        'keep CTPPSPixelDataErroredmDetSetVector_ctppsPixelDigis_*_*',
        'keep CTPPSPixelClusteredmDetSetVector_ctppsPixelClusters_*_*',
        'keep CTPPSPixelRecHitedmDetSetVector_ctppsPixelRecHits_*_*',
        'keep CTPPSPixelLocalTrackedmDetSetVector_ctppsPixelLocalTracks_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*'
    )
)

process.RecoCTPPSRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*',
        'keep TotemFEDInfos_totemRPRawToDigi_*_*',
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*',
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*',
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*',
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*',
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*',
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*',
        'keep TotemFEDInfos_totemT2Digis_*_*',
        'keep TotemT2DigiedmNewDetSetVector_totemT2Digis_*_*',
        'keep TotemVFATStatusedmDetSetVector_totemT2Digis_*_*',
        'keep TotemFEDInfos_ctppsDiamondRawToDigi_*_*',
        'keep CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_*_*',
        'keep TotemVFATStatusedmDetSetVector_ctppsDiamondRawToDigi_*_*',
        'keep CTPPSDiamondRecHitedmDetSetVector_ctppsDiamondRecHits_*_*',
        'keep CTPPSDiamondLocalTrackedmDetSetVector_ctppsDiamondLocalTracks_*_*',
        'keep TotemTimingLocalTrackedmDetSetVector_diamondSampicLocalTracks_*_*',
        'keep TotemTimingDigiedmDetSetVector_totemTimingRawToDigi_*_*',
        'keep TotemTimingRecHitedmDetSetVector_totemTimingRecHits_*_*',
        'keep TotemTimingLocalTrackedmDetSetVector_totemTimingLocalTracks_*_*',
        'keep CTPPSPixelDigiedmDetSetVector_ctppsPixelDigis_*_*',
        'keep CTPPSPixelDataErroredmDetSetVector_ctppsPixelDigis_*_*',
        'keep CTPPSPixelClusteredmDetSetVector_ctppsPixelClusters_*_*',
        'keep CTPPSPixelRecHitedmDetSetVector_ctppsPixelRecHits_*_*',
        'keep CTPPSPixelLocalTrackedmDetSetVector_ctppsPixelLocalTracks_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*'
    )
)

process.RecoEcalAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*'
    )
)

process.RecoEcalFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_reducedEcalRecHitsEB_*_*',
        'keep *_reducedEcalRecHitsEE_*_*',
        'keep *_reducedEcalRecHitsES_*_*',
        'keep *_interestingEcalDetId*_*_*',
        'keep *_ecalWeightUncalibRecHit_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5*_*_*',
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*'
    )
)

process.RecoEcalRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_hybridSuperClusters_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep *_multi5x5SuperClusters_*_*',
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep *_particleFlowSuperClusterECAL_*_*',
        'keep *_particleFlowSuperClusterOOTECAL_*_*',
        'drop recoClusterShapes_*_*_*',
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*',
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*',
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*',
        'keep *_selectDigi_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*',
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*',
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*',
        'keep recoCaloClusters_hybridSuperClusters_*_*',
        'keep recoSuperClusters_hybridSuperClusters_uncleanOnlyHybridSuperClusters_*',
        'keep recoCaloClusters_multi5x5SuperClusters_multi5x5EndcapBasicClusters_*',
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*',
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterOOTECAL_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterOOTECAL_*_*'
    )
)

process.RecoEgammaAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*'
    )
)

process.RecoEgammaFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_gsfElectronCores_*_*',
        'keep *_gsfElectrons_*_*',
        'keep *_uncleanedOnlyGsfElectronCores_*_*',
        'keep *_uncleanedOnlyGsfElectrons_*_*',
        'keep *_eidRobustLoose_*_*',
        'keep *_eidRobustTight_*_*',
        'keep *_eidRobustHighEnergy_*_*',
        'keep *_eidLoose_*_*',
        'keep *_eidTight_*_*',
        'keep *_egmGedGsfElectronPFPileUpIsolation_*_*',
        'keep *_egmGedGsfElectronPFNoPileUpIsolation_*_*',
        'keep *_egmGsfElectronIDs_*_*',
        'keep *_egmPhotonIDs_*_*',
        'keep *_conversions_*_*',
        'drop *_conversions_uncleanedConversions_*',
        'keep *_mustacheConversions_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep *_photonCore_*_*',
        'keep *_photons_*_*',
        'keep *_mustachePhotonCore_*_*',
        'keep *_mustachePhotons_*_*',
        'keep *_ootPhotonCore_*_*',
        'keep *_ootPhotons_*_*',
        'keep *_allConversions_*_*',
        'keep *_allConversionsOldEG_*_*',
        'keep *_ckfOutInTracksFromConversions_*_*',
        'keep *_ckfInOutTracksFromConversions_*_*',
        'keep *_uncleanedOnlyAllConversions_*_*',
        'keep *_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep *_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*'
    )
)

process.RecoEgammaRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_gedPhotonCore_*_*',
        'keep *_gedPhotons_*_*',
        'keep recoPhotons_mustachePhotons_*_*',
        'keep recoPhotonCores_mustachePhotonCore_*_*',
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep recoGsfElectronCores_gsfElectronCores_*_*',
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*',
        'keep recoGsfElectrons_gsfElectrons_*_*',
        'keep recoGsfElectrons_gedGsfElectrons_*_*',
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*',
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*',
        'keep floatedmValueMap_eidRobustLoose_*_*',
        'keep floatedmValueMap_eidRobustTight_*_*',
        'keep floatedmValueMap_eidRobustHighEnergy_*_*',
        'keep floatedmValueMap_eidLoose_*_*',
        'keep floatedmValueMap_eidTight_*_*',
        'keep *_egmGedGsfElectronPFIsolation_*_*',
        'keep recoPhotonCores_gedPhotonCore_*_*',
        'keep recoPhotons_gedPhotons_*_*',
        'keep *_particleBasedIsolation_*_*',
        'keep recoPhotonCores_photonCore_*_*',
        'keep recoPhotons_photons_*_*',
        'keep recoPhotonCores_ootPhotonCore_*_*',
        'keep recoPhotons_ootPhotons_*_*',
        'keep recoConversions_conversions_*_*',
        'drop recoConversions_conversions_uncleanedConversions_*',
        'keep recoConversions_mustacheConversions_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep recoConversions_allConversions_*_*',
        'keep recoConversions_allConversionsOldEG_*_*',
        'keep recoTracks_ckfOutInTracksFromConversions_*_*',
        'keep recoTracks_ckfInOutTracksFromConversions_*_*',
        'keep recoConversions_uncleanedOnlyAllConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*',
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*',
        'keep *_PhotonIDProd_*_*',
        'keep *_PhotonIDProdGED_*_*',
        'keep *_hfRecoEcalCandidate_*_*',
        'keep *_hfEMClusters_*_*',
        'keep *_gedGsfElectronCores_*_*',
        'keep *_gedGsfElectrons_*_*',
        'keep recoCaloClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep recoGsfElectrons_lowPtGsfElectrons_*_*',
        'keep recoGsfElectronCores_lowPtGsfElectronCores_*_*',
        'keep recoGsfTracks_lowPtGsfEleGsfTracks_*_*',
        'keep *_lowPtGsfToTrackLinks_*_*',
        'keep recoSuperClusters_lowPtGsfElectronSuperClusters_*_*',
        'keep floatedmValueMap_lowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_rekeyLowPtGsfElectronSeedValueMaps_*_*',
        'keep floatedmValueMap_lowPtGsfElectronID_*_*'
    )
)

process.RecoGenJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*'
    )
)

process.RecoGenJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoGenJets_ak*_*_*',
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*'
    )
)

process.RecoGenJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ak4GenJets_*_*',
        'keep *_ak8GenJets_*_*',
        'keep *_ak4GenJetsNoNu_*_*',
        'keep *_ak8GenJetsNoNu_*_*',
        'keep *_genParticle_*_*'
    )
)

process.RecoGenMETAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoGenMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoGenMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring('keep recoGenMETs_*_*_*')
)

process.RecoHcalNoiseAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep HcalNoiseSummary_hcalnoise_*_*')
)

process.RecoHcalNoiseFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*'
    )
)

process.RecoHcalNoiseRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*'
    )
)

process.RecoJetsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*'
    )
)

process.RecoJetsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoCaloJets_*_*_*',
        'keep recoPFJets_*_*_*',
        'keep recoTrackJets_*_*_*',
        'keep recoJPTJets_*_*_*',
        'keep recoBasicJets_*_*_*',
        'keep *_kt4JetTracksAssociatorAtVertex_*_*',
        'keep *_kt4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_kt4JetExtender_*_*',
        'keep *_ak7JetTracksAssociatorAtVertex*_*_*',
        'keep *_ak7JetTracksAssociatorAtCaloFace*_*_*',
        'keep *_ak7JetExtender_*_*',
        'keep *_kt4CaloJets_*_*',
        'keep *_kt6CaloJets_*_*',
        'keep *_ak5CaloJets_*_*',
        'keep *_ak7CaloJets_*_*',
        'keep *_kt4PFJets_*_*',
        'keep *_kt6PFJets_*_*',
        'keep *_ak5PFJets_*_*',
        'keep *_ak7PFJets_*_*',
        'keep *_kt4TrackJets_*_*',
        'keep *_ca*Mass_*_*',
        'keep *_ak*Mass_*_*',
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*'
    )
)

process.RecoJetsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ak4CaloJets_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4TrackJets_*_*',
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*',
        'keep *_towerMaker_*_*',
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*',
        'keep *_ak5CastorJets_*_*',
        'keep *_ak7CastorJets_*_*',
        'keep recoCaloJets_ak4CaloJets_*_*',
        'keep *_ak4CaloJets_rho_*',
        'keep *_ak4CaloJets_sigma_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep floatedmValueMap_puppi_*_*',
        'keep *_ak4PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppi_*_*',
        'keep *_ak8PFJetsPuppiSoftDrop_*_*',
        'keep recoPFJets_ak4PFJets_*_*',
        'keep *_ak4PFJets_rho_*',
        'keep *_ak4PFJets_sigma_*',
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*',
        'keep *_caloTowers_*_*',
        'keep *_CastorTowerReco_*_*',
        'keep *_ak4JetTracksAssociatorAtVertex_*_*',
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*',
        'keep *_ak4JetTracksAssociatorExplicit_*_*',
        'keep *_ak4JetExtender_*_*',
        'keep *_ak4JetID_*_*',
        'keep recoBasicJets_ak5CastorJets_*_*',
        'keep *_ak5CastorJets_rho_*',
        'keep *_ak5CastorJets_sigma_*',
        'keep *_ak5CastorJetID_*_*',
        'keep recoBasicJets_ak7CastorJets_*_*',
        'keep *_ak7CastorJets_rho_*',
        'keep *_ak7CastorJets_sigma_*',
        'keep *_ak7CastorJetID_*_*',
        'keep *_fixedGridRhoAll_*_*',
        'keep *_fixedGridRhoFastjetAll_*_*',
        'keep *_fixedGridRhoFastjetAllTmp_*_*',
        'keep *_fixedGridRhoFastjetCentral_*_*',
        'keep *_fixedGridRhoFastjetAllCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralCalo_*_*',
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*',
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*',
        'keep *_ak8PFJetsPuppiSoftDropMass_*_*'
    )
)

process.RecoLocalCaloAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*'
    )
)

process.RecoLocalCaloFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep HBHERecHitsSorted_hbheprerecoMB_*_*',
        'keep ZDCDataFramesSorted_*Digis_*_*',
        'keep ZDCRecHitsSorted_*_*_*',
        'keep HcalUnpackerReport_*_*_*',
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*',
        'keep *_ecalMultiFitUncalibRecHit_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*'
    )
)

process.RecoLocalCaloRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_hbhereco_*_*',
        'keep *_hbheprereco_*_*',
        'keep *_hfprereco_*_*',
        'keep *_hfreco_*_*',
        'keep *_horeco_*_*',
        'keep HBHERecHitsSorted_hbherecoMB_*_*',
        'keep HORecHitsSorted_horecoMB_*_*',
        'keep HFRecHitsSorted_hfrecoMB_*_*',
        'keep ZDCDataFramesSorted_hcalDigis_*_*',
        'keep ZDCDataFramesSorted_castorDigis_*_*',
        'keep QIE10DataFrameHcalDataFrameContainer_hcalDigis_ZDC_*',
        'keep ZDCRecHitsSorted_zdcreco_*_*',
        'keep ZDCRecHitsSorted_zdcrecoRun3_*_*',
        'keep *_castorreco_*_*',
        'keep *_reducedHcalRecHits_*_*',
        'keep HcalUnpackerReport_castorDigis_*_*',
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*',
        'keep HcalUnpackerReport_hcalDigis_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*'
    )
)

process.RecoLocalFastTimeAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoLocalFastTimeFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_mtdUncalibratedRecHits_*_*',
        'keep *_mtdTrackingRecHits_*_*',
        'keep *_mtdRecHits_*_*',
        'keep *_mtdClusters_*_*'
    )
)

process.RecoLocalFastTimeRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_mtdRecHits_*_*',
        'keep *_mtdClusters_*_*'
    )
)

process.RecoLocalMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*'
    )
)

process.RecoLocalMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*'
    )
)

process.RecoLocalMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_dt1DRecHits_*_*',
        'keep *_dt1DCosmicRecHits_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_dt4DCosmicSegments_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_csc2DRecHits_*_*'
    )
)

process.RecoLocalTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep ClusterSummary_clusterSummaryProducer_*_*')
)

process.RecoLocalTrackerFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_clusterSummaryProducer_*_*',
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*'
    )
)

process.RecoLocalTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep DetIds_siStripDigis_*_*',
        'keep DetIdedmEDCollection_siPixelDigis_*_*',
        'keep PixelFEDChanneledmNewDetSetVector_siPixelDigis_*_*',
        'keep *_siPixelClusters_*_*',
        'keep *_siStripClusters_*_*',
        'keep ClusterSummary_clusterSummaryProducer_*_*'
    )
)

process.RecoMETAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*'
    )
)

process.RecoMETFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *HaloData_*_*_*',
        'keep *BeamHaloSummary_BeamHaloSummary_*_*',
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*'
    )
)

process.RecoMETRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoHcalNoiseRBXs_hcalnoise_*_*',
        'keep recoEcalHaloData_EcalHaloData_*_*',
        'keep recoHcalHaloData_HcalHaloData_*_*',
        'keep recoCaloMETs_caloMet_*_*',
        'keep recoCaloMETs_caloMetBE_*_*',
        'keep recoCaloMETs_caloMetBEFO_*_*',
        'keep recoCaloMETs_caloMetM_*_*',
        'keep recoPFMETs_pfMet_*_*',
        'keep recoPFMETs_pfChMet_*_*',
        'keep floatedmValueMap_puppiNoLep_*_*',
        'keep recoPFMETs_pfMetPuppi_*_*',
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoGlobalHaloData_GlobalHaloData_*_*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*'
    )
)

process.RecoMTDAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *edmValueMap_trackExtenderWithMTD_*_*',
        'keep *_mtdTrackQualityMVA_*_*'
    )
)

process.RecoMTDFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoTrack*_trackExtenderWithMTD_*_*',
        'keep TrackingRecHitsOwned_trackExtenderWithMTD_*_*',
        'keep *edmValueMap_trackExtenderWithMTD_*_*',
        'keep *_mtdTrackQualityMVA_*_*'
    )
)

process.RecoMTDRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoTrack*_trackExtenderWithMTD_*_*',
        'keep TrackingRecHitsOwned_trackExtenderWithMTD_*_*',
        'keep *edmValueMap_trackExtenderWithMTD_*_*',
        'keep *_mtdTrackQualityMVA_*_*'
    )
)

process.RecoMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*'
    )
)

process.RecoMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*'
    )
)

process.RecoMuonIsolationAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.RecoMuonIsolationFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*'
    )
)

process.RecoMuonIsolationParamGlobal = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_muParamGlobalIsoDepositGsTk_*_*',
        'keep *_muParamGlobalIsoDepositCalEcal_*_*',
        'keep *_muParamGlobalIsoDepositCalHcal_*_*',
        'keep *_muParamGlobalIsoDepositCtfTk_*_*',
        'keep *_muParamGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muParamGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muParamGlobalIsoDepositJets_*_*'
    )
)

process.RecoMuonIsolationRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*'
    )
)

process.RecoMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_MuonSeed_*_*',
        'keep *_ancientMuonSeed_*_*',
        'keep *_displacedMuonSeeds_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep TrackingRecHitsOwned_tevMuons_*_*',
        'keep *_CosmicMuonSeed_*_*',
        'keep recoTrackExtras_cosmicMuons_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons_*_*',
        'keep recoTrackExtras_cosmicMuons1Leg_*_*',
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*',
        'keep recoTracks_cosmicsVetoTracks_*_*',
        'keep recoMuons_muons_*_*',
        'keep booledmValueMap_muons_*_*',
        'keep doubleedmValueMap_muons_muPFMean*_*',
        'keep doubleedmValueMap_muons_muPFSum*_*',
        'keep *_muons_muonShowerInformation_*',
        'keep recoMuonTimeExtraedmValueMap_muons_*_*',
        'keep recoMuonCosmicCompatibilityedmValueMap_muons_*_*',
        'keep uintedmValueMap_muons_*_*',
        'keep *_particleFlow_muons_*',
        'keep recoMuons_displacedMuons_*_*',
        'keep booledmValueMap_displacedMuons_*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFMean*_*',
        'keep doubleedmValueMap_displacedMuons_dispMuPFSum*_*',
        'keep recoMuonTimeExtraedmValueMap_displacedMuons_*_*',
        'keep uintedmValueMap_displacedMuons_*_*',
        'keep *_particleFlow_displacedMuons_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_displacedTracks_*_*',
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*',
        'keep recoTracks_displacedGlobalMuons_*_*',
        'keep recoTrackExtras_displacedGlobalMuons_*_*',
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*',
        'keep recoTracks_cosmicMuons_*_*',
        'keep recoMuons_muonsFromCosmics_*_*',
        'keep recoTracks_cosmicMuons1Leg_*_*',
        'keep recoMuons_muonsFromCosmics1Leg_*_*',
        'keep recoTracks_refittedStandAloneMuons_*_*',
        'keep recoTrackExtras_refittedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTrackExtras_displacedStandAloneMuons_*_*',
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*',
        'keep *_muonReducedTrackExtras_*_*',
        'keep *_displacedMuonReducedTrackExtras_*_*',
        'keep *_muIsoDepositTk_*_*',
        'keep *_muIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muIsoDepositCalByAssociatorHits_*_*',
        'keep *_muIsoDepositJets_*_*',
        'keep *_muIsoDepositTkDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorTowersDisplaced_*_*',
        'keep *_muIsoDepositCalByAssociatorHitsDisplaced_*_*',
        'keep *_muIsoDepositJetsDisplaced_*_*',
        'keep *_muGlobalIsoDepositCtfTk_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*',
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*',
        'keep *_muGlobalIsoDepositJets_*_*'
    )
)

process.RecoParticleFlowAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*'
    )
)

process.RecoParticleFlowFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*'
    )
)

process.RecoParticleFlowRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoPFClusters_particleFlowClusterECAL_*_*',
        'keep recoPFClusters_particleFlowClusterHCAL_*_*',
        'keep recoPFClusters_particleFlowClusterHO_*_*',
        'keep recoPFClusters_particleFlowClusterHF_*_*',
        'keep recoPFClusters_particleFlowClusterPS_*_*',
        'keep recoPFBlocks_particleFlowBlock_*_*',
        'keep recoPFCandidates_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlowTmp_electrons_*',
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*',
        'keep *_pfElectronTranslator_*_*',
        'keep *_pfPhotonTranslator_*_*',
        'keep *_trackerDrivenElectronSeeds_preid_*',
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*',
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*',
        'keep recoCaloClusters_particleFlowEGamma_*_*',
        'keep recoSuperClusters_particleFlowEGamma_*_*',
        'keep recoCaloClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoSuperClusters_particleFlowSuperClusterECAL_*_*',
        'keep recoConversions_particleFlowEGamma_*_*',
        'keep recoPFCandidates_particleFlow_*_*',
        'keep recoPFCandidates_particleFlowTmp_AddedMuonsAndHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedCosmicsMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedFakeMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedHF_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughMuons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedPunchThroughNeutralHadrons_*',
        'keep recoPFCandidates_particleFlowTmp_CleanedTrackerAndGlobalMuons_*',
        'keep *_particleFlow_electrons_*',
        'keep *_particleFlow_photons_*',
        'keep *_particleFlow_muons_*',
        'keep recoCaloClusters_pfElectronTranslator_*_*',
        'keep recoPreshowerClusters_pfElectronTranslator_*_*',
        'keep recoSuperClusters_pfElectronTranslator_*_*',
        'keep recoCaloClusters_pfPhotonTranslator_*_*',
        'keep recoPreshowerClusters_pfPhotonTranslator_*_*',
        'keep recoSuperClusters_pfPhotonTranslator_*_*',
        'keep recoPhotons_pfPhotonTranslator_*_*',
        'keep recoPhotonCores_pfPhotonTranslator_*_*',
        'keep recoConversions_pfPhotonTranslator_*_*',
        'keep *_particleFlowPtrs_*_*',
        'keep *_particleFlowTmpPtrs_*_*',
        'keep *_chargedHadronPFTrackIsolation_*_*'
    )
)

process.RecoPixelVertexingFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*'
    )
)

process.RecoPixelVertexingRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_pixelTracks_*_*',
        'keep *_pixelVertices_*_*'
    )
)

process.RecoTauTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*'
    )
)

process.RecoTauTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ak4PFJetsRecoTauPiZeros_*_*',
        'keep *_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauDiscrimination*_*_*',
        'keep *_hpsPFTau*PtSum_*_*',
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*'
    )
)

process.RecoTauTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauBasicDiscriminators_*_*',
        'keep *_hpsPFTauBasicDiscriminatorsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByMuonRejection3_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*'
    )
)

process.RecoTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*'
    )
)

process.RecoTrackerFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*'
    )
)

process.RecoTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoTrackExtras_generalTracks_*_*',
        'keep TrackingRecHitsOwned_generalTracks_*_*',
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*',
        'keep uints_extraFromSeeds_*_*',
        'keep recoTrackExtras_beamhaloTracks_*_*',
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*',
        'keep recoTrackExtras_conversionStepTracks_*_*',
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*',
        'keep *_ctfPixelLess_*_*',
        'keep *_dedxTruncated40_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTracks_conversionStepTracks_*_*',
        'keep recoTracks_beamhaloTracks_*_*',
        'keep recoTracks_ctfPixelLess_*_*',
        'keep *_dedxHarmonic2_*_*',
        'keep *_dedxPixelHarmonic2_*_*',
        'keep *_dedxHitInfo_*_*',
        'keep *_trackExtrapolator_*_*',
        'keep *_generalTracks_MVAValues_*',
        'keep *_generalTracks_MVAVals_*'
    )
)

process.RecoVertexAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*'
    )
)

process.RecoVertexFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*'
    )
)

process.RecoVertexRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep  *_offlinePrimaryVertices__*',
        'keep *_offlinePrimaryVerticesWithBS_*_*',
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*',
        'keep *_nuclearInteractionMaker_*_*',
        'keep *_generalV0Candidates_*_*',
        'keep *_inclusiveSecondaryVertices_*_*'
    )
)

process.SimCalorimetryAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimCalorimetryFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_simEcalDigis_*_*',
        'keep *_simEcalPreshowerDigis_*_*',
        'keep *_simEcalTriggerPrimitiveDigis_*_*',
        'keep *_simEcalEBTriggerPrimitiveDigis_*_*',
        'keep *_simEcalEBTriggerPrimitivePhase2Digis_*_*',
        'keep *_simHcalDigis_*_*',
        'keep ZDCDataFramesSorted_simHcalUnsuppressedDigis_*_*',
        'drop ZDCDataFramesSorted_mix_simHcalUnsuppressedDigis*_*',
        'keep *_simHcalTriggerPrimitiveDigis_*_*',
        'keep *_mix_HcalSamples_*',
        'keep *_mixData_HcalSamples_*',
        'keep *_mix_HcalHits_*',
        'keep *_mixData_HcalHits_*',
        'keep *_DMHcalTriggerPrimitiveDigis_*_*'
    )
)

process.SimCalorimetryPREMIX = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep EBDigiCollection_simEcalDigis_*_*',
        'keep EEDigiCollection_simEcalDigis_*_*',
        'keep ESDigiCollection_simEcalUnsuppressedDigis_*_*',
        'keep *_simHcalDigis_*_*'
    )
)

process.SimCalorimetryRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep EBSrFlagsSorted_simEcalDigis_*_*',
        'keep EESrFlagsSorted_simEcalDigis_*_*'
    )
)

process.SimCalorimetryRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimFastTimingAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimFastTimingFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimFastTimingPREMIX = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimFastTimingRAW = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimFastTimingRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimG4CoreAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimG4CoreHLTAODSIM = cms.PSet(
    outputCommands = cms.untracked.vstring('keep SimVertexs_g4SimHits_*_*')
)

process.SimG4CoreRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_g4SimHits_*_*',
        'keep edmHepMCProduct_source_*_*'
    )
)

process.SimG4CoreRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep edmHepMCProduct_source_*_*',
        'keep SimTracks_g4SimHits_*_*',
        'keep SimVertexs_g4SimHits_*_*'
    )
)

process.SimGeneralAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*'
    )
)

process.SimGeneralFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *_trackingtruthprod_*_*',
        'drop *_electrontruth_*_*',
        'keep *_mix_MergedTrackTruth_*',
        'keep CrossingFramePlaybackInfoNew_*_*_*'
    )
)

process.SimGeneralPREMIX = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.SimGeneralRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep CrossingFramePlaybackInfoNew_*_*_*',
        'keep PileupSummaryInfos_*_*_*',
        'keep int6stdbitsetstdpairs_*_AffectedAPVList_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*',
        'keep *_mix_MergedTrackTruth_*'
    )
)

process.SimGeneralRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep PileupSummaryInfos_*_*_*',
        'keep int_*_bunchSpacing_*',
        'keep *_genPUProtons_*_*'
    )
)

process.SimMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_muonSimClassifier_*_*')
)

process.SimMuonFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_simMuonCSCDigis_*_*',
        'keep *_simMuonDTDigis_*_*',
        'keep *_simMuonRPCDigis_*_*'
    )
)

process.SimMuonPREMIX = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_mix_g4SimHitsMuonDTHits_*',
        'keep *_mix_g4SimHitsMuonCSCHits_*',
        'keep *_mix_g4SimHitsMuonRPCHits_*'
    )
)

process.SimMuonRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*'
    )
)

process.SimMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*',
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*',
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*',
        'keep *_muonSimClassifier_*_*'
    )
)

process.SimTrackerAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*'
    )
)

process.SimTrackerDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep PixelDigiSimLinkedmDetSetVector_simSiPixelDigis_*_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*'
    )
)

process.SimTrackerFEVTDEBUG = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_simSiPixelDigis_*_*',
        'keep *_simSiStripDigis_*_*',
        'drop *_mix_simSiPixelDigis*_*',
        'drop *_mix_simSiStripDigis*_*',
        'keep *_allTrackMCMatch_*_*',
        'keep *_trackingParticleRecoTrackAsssociation_*_*',
        'keep *_assoc2secStepTk_*_*',
        'keep *_assoc2thStepTk_*_*',
        'keep *_assoc2GsfTracks_*_*',
        'keep *_assocOutInConversionTracks_*_*',
        'keep *_assocInOutConversionTracks_*_*',
        'keep *_TTClusterAssociatorFromPixelDigis_*_*',
        'keep *_TTStubAssociatorFromPixelDigis_*_*',
        'keep *_simHitTPAssocProducer_*_*'
    )
)

process.SimTrackerPREMIX = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_simSiPixelDigis_*_*',
        'keep *_simSiStripDigis_ZeroSuppressed_*',
        'keep StripDigiSimLinkedmDetSetVector_simSiStripDigis_*_*',
        'keep *_mix_AffectedAPVList_*'
    )
)

process.SimTrackerRAW = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackingParticles_*_*',
        'keep *_prunedDigiSimLinks_*_*'
    )
)

process.SimTrackerRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_allTrackMCMatch_*_*',
        'keep *_prunedTrackMCMatch_*_*'
    )
)

process.TICL_AOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.TICL_FEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ticlSimTracksters_*_*',
        'keep *_ticlSimTICLCandidates_*_*',
        'keep *_ticlSimTrackstersFromCP_*_*',
        'keep *_SimTau*_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*',
        'keep *_ticlTrackstersCLUE3DHigh_*_*',
        'keep *_ticlTrackstersMerge_*_*',
        'keep *_ticlTrackstersHFNoseTrkEM_*_*',
        'keep *_ticlTrackstersHFNoseEM_*_*',
        'keep *_ticlTrackstersHFNoseTrk_*_*',
        'keep *_ticlTrackstersHFNoseMIP_*_*',
        'keep *_ticlTrackstersHFNoseHAD_*_*',
        'keep *_ticlTrackstersHFNoseMerge_*_*',
        'keep *_pfTICL_*_*',
        'keep CaloParticles_mix_*_*',
        'keep SimClusters_mix_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_layerClusterSimClusterAssociationProducer_*_*',
        'keep *_layerClusterCaloParticleAssociationProducer_*_*',
        'keep *_layerClusterSimTracksterAssociationProducer_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*'
    )
)

process.TICL_FEVTHLT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_hltPfTICL_*_*',
        'keep *_hltTiclTrackstersCLUE3D*_*_*',
        'keep *_hltTiclTracksterLinks_*_*',
        'keep *_hltTiclCandidate_*_*',
        'keep *_hltPfTICL_*_*',
        'keep *_ticlSimTracksters_*_*',
        'keep *_ticlSimTICLCandidates_*_*',
        'keep *_ticlSimTrackstersFromCP_*_*',
        'keep *_SimTau*_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*',
        'keep *_ticlTrackstersCLUE3DHigh_*_*',
        'keep *_ticlTrackstersMerge_*_*',
        'keep *_ticlTrackstersHFNoseTrkEM_*_*',
        'keep *_ticlTrackstersHFNoseEM_*_*',
        'keep *_ticlTrackstersHFNoseTrk_*_*',
        'keep *_ticlTrackstersHFNoseMIP_*_*',
        'keep *_ticlTrackstersHFNoseHAD_*_*',
        'keep *_ticlTrackstersHFNoseMerge_*_*',
        'keep *_pfTICL_*_*',
        'keep CaloParticles_mix_*_*',
        'keep SimClusters_mix_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_layerClusterSimClusterAssociationProducer_*_*',
        'keep *_layerClusterCaloParticleAssociationProducer_*_*',
        'keep *_layerClusterSimTracksterAssociationProducer_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*'
    )
)

process.TICL_RECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ticlTrackstersCLUE3DHigh_*_*',
        'keep *_ticlTrackstersMerge_*_*',
        'keep *_ticlTrackstersHFNoseTrkEM_*_*',
        'keep *_ticlTrackstersHFNoseEM_*_*',
        'keep *_ticlTrackstersHFNoseTrk_*_*',
        'keep *_ticlTrackstersHFNoseMIP_*_*',
        'keep *_ticlTrackstersHFNoseHAD_*_*',
        'keep *_ticlTrackstersHFNoseMerge_*_*',
        'keep *_pfTICL_*_*',
        'keep CaloParticles_mix_*_*',
        'keep SimClusters_mix_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_layerClusterSimClusterAssociationProducer_*_*',
        'keep *_layerClusterCaloParticleAssociationProducer_*_*',
        'keep *_layerClusterSimTracksterAssociationProducer_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*'
    )
)

process.TICLv5_FEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ticlSimTracksters_*_*',
        'keep *_ticlSimTICLCandidates_*_*',
        'keep *_ticlSimTrackstersFromCP_*_*',
        'keep CaloParticles_mix_*_*',
        'keep SimClusters_mix_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_layerClusterSimClusterAssociationProducer_*_*',
        'keep *_layerClusterCaloParticleAssociationProducer_*_*',
        'keep *_layerClusterSimTracksterAssociationProducer_*_*',
        'keep *_SimTau*_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*',
        'drop *_ticlTracksters*_*_*',
        'keep *_ticlTrackstersCLUE3DHigh_*_*',
        'keep *_ticlTracksterLinks*_*_*',
        'keep *_ticlTracksterLinksSuperclustering*_*_*',
        'keep *_ticlCandidate_*_*'
    )
)

process.TICLv5_FEVTHLT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *_hltTiclTracksters*_*_*',
        'keep *_hltTiclTrackstersCLUE3D*_*_*',
        'keep *_hltTiclTracksterLinks_*_*',
        'keep *_hltTiclCandidate_*_*',
        'keep *_hltPfTICL_*_*',
        'keep *_ticlSimTracksters_*_*',
        'keep *_ticlSimTICLCandidates_*_*',
        'keep *_ticlSimTrackstersFromCP_*_*',
        'keep CaloParticles_mix_*_*',
        'keep SimClusters_mix_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_SimClusterToCaloParticleAssociation*_*_*',
        'keep *_layerClusterSimClusterAssociationProducer_*_*',
        'keep *_layerClusterCaloParticleAssociationProducer_*_*',
        'keep *_layerClusterSimTracksterAssociationProducer_*_*',
        'keep *_SimTau*_*_*',
        'keep *_allTrackstersToSimTrackstersAssociations*_*_*',
        'drop *_ticlTracksters*_*_*',
        'keep *_ticlTrackstersCLUE3DHigh_*_*',
        'keep *_ticlTracksterLinks*_*_*',
        'keep *_ticlTracksterLinksSuperclustering*_*_*',
        'keep *_ticlCandidate_*_*'
    )
)

process.TICLv5_RECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *_ticlTracksters*_*_*',
        'keep *_ticlTrackstersCLUE3DHigh_*_*',
        'keep *_ticlTracksterLinks*_*_*',
        'keep *_ticlTracksterLinksSuperclustering*_*_*',
        'keep *_ticlCandidate_*_*'
    )
)

process.TcdsEventContent = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_tcdsDigis_*_*')
)

process.TrackingToolsAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*'
    )
)

process.TrackingToolsFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_electronGsfTracks_*_*',
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*'
    )
)

process.TrackingToolsRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_CkfElectronCandidates_*_*',
        'keep *_GsfGlobalElectronTest_*_*',
        'keep *_electronMergedSeeds_*_*',
        'keep recoGsfTrackExtras_electronGsfTracks_*_*',
        'keep recoTrackExtras_electronGsfTracks_*_*',
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*',
        'keep recoTracks_GsfGlobalElectronTest_*_*',
        'keep recoGsfTracks_electronGsfTracks_*_*'
    )
)

process.combinedSecondaryVertexCommon = cms.PSet(
    SoftLeptonFlip = cms.bool(False),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ecalLocalRecoAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)

process.ecalLocalRecoFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ecalMultiFitUncalibRecHit_*_*',
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*'
    )
)

process.ecalLocalRecoRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ecalPreshowerRecHit_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_ecalCompactTrigPrim_*_*',
        'keep *_ecalTPSkim_*_*',
        'keep EBSrFlagsSorted_ecalDigis__*',
        'keep EESrFlagsSorted_ecalDigis__*'
    )
)

process.j2tParametersCALO = cms.PSet(
    coneSize = cms.double(0.4),
    extrapolations = cms.InputTag("trackExtrapolator"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)

process.j2tParametersVX = cms.PSet(
    coneSize = cms.double(0.4),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.heavyIonCSV_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackSip3dSig_2'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackSip3dSig_3'),
        taggingVarName = cms.string('trackSip3dSig')
    ),
    cms.PSet(
        default = cms.double(-999),
        name = cms.string('TagVarCSV_trackSip3dSigAboveCharm'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackPtRel_2'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackPtRel_3'),
        taggingVarName = cms.string('trackPtRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackEtaRel_2'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackEtaRel_3'),
        taggingVarName = cms.string('trackEtaRel')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackDeltaR_2'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackDeltaR_3'),
        taggingVarName = cms.string('trackDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackPtRatio_2'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackPtRatio_3'),
        taggingVarName = cms.string('trackPtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackJetDist_2'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackJetDist_3'),
        taggingVarName = cms.string('trackJetDist')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackDecayLenVal_2'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackDecayLenVal_3'),
        taggingVarName = cms.string('trackDecayLenVal')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_vertexMass'),
        taggingVarName = cms.string('vertexMass')
    ),
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_vertexNTracks'),
        taggingVarName = cms.string('vertexNTracks')
    ),
    cms.PSet(
        default = cms.double(-10),
        name = cms.string('TagVarCSV_vertexEnergyRatio'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ),
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_vertexJetDeltaR'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ),
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('TagVarCSV_flightDistance2dSig'),
        taggingVarName = cms.string('flightDistance2dSig')
    ),
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ),
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_vertexCategory'),
        taggingVarName = cms.string('vertexCategory')
    )
)

process.PackedPFTowers = cms.EDProducer("PackedPFTowers",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("packedPFCandidates"),
    useHF = cms.bool(True)
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4HiGenJets = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJets"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak4HiGenJetsCleaned = cms.EDProducer("HiGenJetCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("ak4HiGenJetsNoNu")
)


process.ak4HiGenJetsNoNu = cms.EDProducer("SubEventGenJetProducer",
    Active_Area_Repeats = cms.int32(5),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(3.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("genParticlesForJetsNoNu"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True)
)


process.ak4HiSignalGenJets = cms.EDProducer("HiSignalGenJetProducer",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("ak4HiGenJetsNoNu")
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4L1JPTFastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1FastjetCorrector")
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsCHS = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("pfNoPileUpJME"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsForFlow = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(True),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(15.0),
    jetType = cms.string('BasicJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puPtMin = cms.double(25),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("hiPFCandCleanerforJets"),
    srcPVs = cms.InputTag(""),
    subtractorName = cms.string('MultipleAlgoIterator'),
    sumRecHits = cms.bool(False),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.ak5JetExtender = cms.EDProducer("JetExtender",
    coneSize = cms.double(0.5),
    jet2TracksAtCALO = cms.InputTag("ak5JetTracksAssociatorAtCaloFace"),
    jet2TracksAtVX = cms.InputTag("ak5JetTracksAssociatorAtVertex"),
    jets = cms.InputTag("ak5CaloJets")
)


process.ak5JetTracksAssociatorAtCaloFace = cms.EDProducer("JetTracksAssociatorAtCaloFace",
    coneSize = cms.double(0.5),
    extrapolations = cms.InputTag("trackExtrapolator"),
    jets = cms.InputTag("ak5CaloJets"),
    trackQuality = cms.string('goodIterative'),
    tracks = cms.InputTag("generalTracks")
)


process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5CaloJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak5JetTracksAssociatorExplicit = cms.EDProducer("JetTracksAssociatorExplicit",
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.akCs4PFJets = cms.EDProducer("CSJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.005),
    Ghost_EtaMax = cms.double(6.5),
    Rho_EtaMax = cms.double(4.5),
    applyWeight = cms.bool(False),
    csAlpha = cms.double(2.0),
    csRParam = cms.double(-1.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doFastJetNonUniform = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(True),
    etaMap = cms.InputTag("hiPuRho","mapEtaEdges"),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('pfParticlesCs'),
    jetPtMin = cms.double(0.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nExclude = cms.uint32(2),
    nSigmaPU = cms.double(1.0),
    puCenters = cms.vdouble(
        -5, -4, -3, -2, -1,
        0, 1, 2, 3, 4,
        5
    ),
    puWidth = cms.double(0.8),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    rho = cms.InputTag("hiPuRho","mapToRho"),
    rhoFlowFitParams = cms.InputTag("hiFJRhoFlowModulation","rhoFlowFitParams"),
    rhom = cms.InputTag("hiPuRho","mapToRhoM"),
    src = cms.InputTag("particleFlow"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useModulatedRho = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    writeJetsWithConst = cms.bool(True)
)


process.allPartons = cms.EDProducer("PartonSelector",
    src = cms.InputTag("hiSignalGenParticles"),
    withLeptons = cms.bool(False)
)


process.caloMetT1 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"))
)


process.caloMetT1T2 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"), cms.InputTag("corrCaloMetType2"))
)


process.cleanedPartons = cms.EDProducer("HiPartonCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("allPartons")
)


process.combinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('combinedSecondaryVertexV2Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"), cms.InputTag("secondaryVertexTagInfos"))
)


process.corrCaloMetType1 = cms.EDProducer("CaloJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4CaloL2L3Corrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    src = cms.InputTag("ak4CaloJets"),
    srcMET = cms.InputTag("caloMetM"),
    type1JetPtThreshold = cms.double(20.0)
)


process.corrCaloMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrCaloMetType1","type2"), cms.InputTag("muCaloMetCorr")),
    type2CorrFormula = cms.string('A + B*TMath::Exp(-C*x)'),
    type2CorrParameter = cms.PSet(
        A = cms.double(2.0),
        B = cms.double(1.3),
        C = cms.double(0.1)
    )
)


process.corrPfMetType1 = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsCHS"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1","type2"), cms.InputTag("corrPfMetType1","offset"), cms.InputTag("pfCandMETcorr")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.elPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons"),
    trackType = cms.string('candidate')
)


process.elPFIsoValueCharged03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04NoPFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFIsoDepositPUPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.electronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedGsfElectrons")
)


process.filteredDisplacedMuons = cms.EDProducer("DisplacedMuonFilterProducer",
    EcalIsoDeposits = cms.InputTag("displacedMuons","ecal"),
    FillDetectorBasedIsolation = cms.bool(False),
    FillTimingInfo = cms.bool(True),
    HcalIsoDeposits = cms.InputTag("displacedMuons","hcal"),
    HoIsoDeposits = cms.InputTag("displacedMuons","ho"),
    JetIsoDeposits = cms.InputTag("displacedMuons","jets"),
    TrackIsoDeposits = cms.InputTag("displacedMuons","tracker"),
    minMatches = cms.double(2),
    minPtSTA = cms.double(3.5),
    minPtTK = cms.double(3.5),
    srcMuons = cms.InputTag("displacedMuons")
)


process.genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    excludeResonances = cms.bool(False),
    ignoreParticleIDs = cms.vuint32(
        1000022, 1000012, 1000014, 1000016, 2000012,
        2000014, 2000016, 1000039, 5100039, 4000012,
        4000014, 4000016, 9900012, 9900014, 9900016,
        39, 12, 14, 16
    ),
    partonicFinalState = cms.bool(False),
    src = cms.InputTag("genParticles"),
    tausAsJets = cms.bool(False)
)


process.gtStage2Digis = cms.EDProducer("L1TRawToDigi",
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("hltFEDSelectorL1"),
    Setup = cms.string('stage2::GTSetup')
)


process.heavyIonCleanedGenJets = cms.EDProducer("HiGenJetCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("iterativeCone5HiGenJets")
)


process.hiFJRhoFlowModulation = cms.EDProducer("HiFJRhoFlowModulationProducer",
    EvtPlane = cms.InputTag("hiEvtPlane"),
    doEvtPlane = cms.bool(False),
    doFreePlaneFit = cms.bool(False),
    doJettyExclusion = cms.bool(False),
    evtPlaneLevel = cms.int32(0),
    exclusionRadius = cms.double(0.4),
    firstFittedVn = cms.int32(2),
    jetTag = cms.InputTag("ak4PFJetsForFlow"),
    lastFittedVn = cms.int32(3),
    mightGet = cms.optional.untracked.vstring,
    minPfCandidatesPerEvent = cms.int32(100),
    pfCandSource = cms.InputTag("packedPFCandidates"),
    pfCandidateEtaCut = cms.double(1),
    pfCandidateMaxPtCut = cms.double(3),
    pfCandidateMinPtCut = cms.double(0.3)
)


process.hiPartons = cms.EDProducer("HiPartonCleaner",
    createNewCollection = cms.untracked.bool(True),
    deltaR = cms.double(0.25),
    fillDummyEntries = cms.untracked.bool(True),
    ptCut = cms.double(20),
    src = cms.InputTag("genPartons")
)


process.hiPuRho = cms.EDProducer("HiPuRhoProducer",
    dropZeroTowers = cms.bool(True),
    medianWindowWidth = cms.int32(2),
    mightGet = cms.optional.untracked.vstring,
    minimumTowersFraction = cms.double(0.7),
    nSigmaPU = cms.double(1),
    puPtMin = cms.double(15),
    rParam = cms.double(0.3),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PFTowers"),
    towSigmaCut = cms.double(5)
)


process.hiSignalGenJetProducer = cms.EDProducer("HiSignalGenJetProducer",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("akHiGenJets")
)


process.hiSignalGenParticles = cms.EDProducer("HiSignalParticleProducer",
    mightGet = cms.optional.untracked.vstring,
    src = cms.InputTag("genParticles")
)


process.hpsPFTauBasicDiscriminators = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.impactParameterTagInfos = cms.EDProducer("TrackIPProducer",
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jetTracks = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(8),
    minimumNumberOfPixelHits = cms.int32(2),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlinePrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.jetBProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetBProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.jetProbabilityBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('jetProbabilityComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.lowPtElectronMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(11),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("lowPtGsfElectrons")
)


process.lowPtGsfElectronID = cms.EDProducer("LowPtGsfElectronIDProducer",
    MaxPtThreshold = cms.double(15),
    MinPtThreshold = cms.double(0.5),
    ModelNames = cms.vstring(''),
    ModelThresholds = cms.vdouble(-99),
    ModelWeights = cms.vstring('RecoEgamma/ElectronIdentification/data/LowPtElectrons/LowPtElectrons_ID_2020Nov28.root'),
    PassThrough = cms.bool(False),
    Version = cms.string('V1'),
    electrons = cms.InputTag("lowPtGsfElectrons"),
    gsfToTrack = cms.InputTag("lowPtGsfToTrackLinks"),
    mightGet = cms.optional.untracked.vstring,
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    unbiased = cms.InputTag("lowPtGsfElectronSeedValueMaps","unbiased"),
    useGsfToTrack = cms.bool(False),
    usePAT = cms.bool(False)
)


process.lowPtGsfElectrons = cms.EDProducer("LowPtGsfElectronFinalizer",
    mightGet = cms.optional.untracked.vstring,
    previousGsfElectronsTag = cms.InputTag("lowPtGsfElectronsPreRegression"),
    regressionConfig = cms.PSet(
        eleRegs = cms.PSet(
            ecalOnlyMean = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_mean"),
                ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_mean"),
                eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_mean"),
                eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_mean"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(20.0),
                rangeMaxHighEt = cms.double(3.0),
                rangeMaxLowEt = cms.double(2.0),
                rangeMinHighEt = cms.double(-1.0),
                rangeMinLowEt = cms.double(0.2)
            ),
            ecalOnlySigma = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_sigma"),
                ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalOnly_05To50_sigma"),
                eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_sigma"),
                eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalOnly_05To50_sigma"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(20.0),
                rangeMaxHighEt = cms.double(0.5),
                rangeMaxLowEt = cms.double(0.5),
                rangeMinHighEt = cms.double(0.0002),
                rangeMinLowEt = cms.double(0.0002)
            ),
            epComb = cms.PSet(
                ecalTrkRegressionConfig = cms.PSet(
                    ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_mean"),
                    ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_mean"),
                    eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_mean"),
                    eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_mean"),
                    forceHighEnergyTrainingIfSaturated = cms.bool(False),
                    lowEtHighEtBoundary = cms.double(20.0),
                    rangeMaxHighEt = cms.double(2.0),
                    rangeMaxLowEt = cms.double(2.0),
                    rangeMinHighEt = cms.double(0.2),
                    rangeMinLowEt = cms.double(0.2)
                ),
                ecalTrkRegressionUncertConfig = cms.PSet(
                    ebHighEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_sigma"),
                    ebLowEtForestName = cms.ESInputTag("","lowPtElectron_eb_ecalTrk_05To50_sigma"),
                    eeHighEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_sigma"),
                    eeLowEtForestName = cms.ESInputTag("","lowPtElectron_ee_ecalTrk_05To50_sigma"),
                    forceHighEnergyTrainingIfSaturated = cms.bool(False),
                    lowEtHighEtBoundary = cms.double(20.0),
                    rangeMaxHighEt = cms.double(0.5),
                    rangeMaxLowEt = cms.double(0.5),
                    rangeMinHighEt = cms.double(0.0002),
                    rangeMinLowEt = cms.double(0.0002)
                ),
                maxEPDiffInSigmaForComb = cms.double(15.0),
                maxEcalEnergyForComb = cms.double(200.0),
                maxRelTrkMomErrForComb = cms.double(10.0),
                minEOverPForComb = cms.double(0.025)
            )
        ),
        maxRawEnergyForLowPtEBSigma = cms.double(-1),
        maxRawEnergyForLowPtEESigma = cms.double(1200.0),
        modifierName = cms.string('EGRegressionModifierV3'),
        phoRegs = cms.PSet(
            ecalOnlyMean = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","photon_eb_ECALonly"),
                ebLowEtForestName = cms.ESInputTag("","photon_eb_ecalOnly_5To300_0p2To2_mean"),
                eeHighEtForestName = cms.ESInputTag("","photon_ee_ECALonly"),
                eeLowEtForestName = cms.ESInputTag("","photon_ee_ecalOnly_5To300_0p2To2_mean"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(999999.0),
                rangeMaxHighEt = cms.double(3.0),
                rangeMaxLowEt = cms.double(2.0),
                rangeMinHighEt = cms.double(-1.0),
                rangeMinLowEt = cms.double(0.2)
            ),
            ecalOnlySigma = cms.PSet(
                ebHighEtForestName = cms.ESInputTag("","photon_eb_ECALonly_var"),
                ebLowEtForestName = cms.ESInputTag("","photon_eb_ecalOnly_5To300_0p0002To0p5_sigma"),
                eeHighEtForestName = cms.ESInputTag("","photon_ee_ECALonly_var"),
                eeLowEtForestName = cms.ESInputTag("","photon_ee_ecalOnly_5To300_0p0002To0p5_sigma"),
                forceHighEnergyTrainingIfSaturated = cms.bool(True),
                lowEtHighEtBoundary = cms.double(999999.0),
                rangeMaxHighEt = cms.double(0.5),
                rangeMaxLowEt = cms.double(0.5),
                rangeMinHighEt = cms.double(0.0002),
                rangeMinLowEt = cms.double(0.0002)
            )
        ),
        rhoTag = cms.InputTag("fixedGridRhoFastjetAll"),
        useBuggedHOverE = cms.bool(False),
        useClosestToCentreSeedCrysDef = cms.bool(False)
    )
)


process.muCaloMetCorr = cms.EDProducer("MuonMETcorrInputProducer",
    src = cms.InputTag("muons"),
    srcMuonCorrections = cms.InputTag("muonMETValueMapProducer","muCorrData")
)


process.muPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("muons"),
    trackType = cms.string('candidate')
)


process.muPFIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMeanDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('meanDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueCharged04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueChargedAll04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(
            '0.0001',
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGamma04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueGammaHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositGammaPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutral04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValueNeutralHighThreshold04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(1.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU03PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.3),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFSumDRIsoValuePU04PAT = cms.EDProducer("CandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        deltaR = cms.double(0.4),
        mode = cms.string('sumDR'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFIsoDepositPUPAT"),
        vetos = cms.vstring(
            '0.01',
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(0.5),
    maxDeltaR = cms.double(0.5),
    mcPdgId = cms.vint32(13),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("muons")
)


process.ootPhotonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ootPhotons")
)


process.particleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.patDisplacedMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(False),
    addInverseBeta = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    addTriggerMatching = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    computeMiniIso = cms.bool(False),
    computeMuonIDMVA = cms.bool(False),
    computePuppiCombinedIso = cms.bool(False),
    computeSoftMuonMVA = cms.bool(False),
    effectiveAreaVec = cms.vdouble(0.0566, 0.0562, 0.0363, 0.0119, 0.0064),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(False),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(False),
    embedPfEcalEnergy = cms.bool(False),
    embedPickyMuon = cms.bool(False),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(False),
    embedTrack = cms.bool(True),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("displacedMuonMatch"),
    hltCollectionFilters = cms.vstring('*'),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(

    ),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001,
        0.01, 0.01, 0.01, 0.0
    ),
    muonSimInfo = cms.InputTag("displacedMuonSimClassifier"),
    muonSource = cms.InputTag("filteredDisplacedMuons"),
    mvaDrMax = cms.double(0.4),
    mvaIDTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mvaID.onnx'),
    mvaIDwpMedium = cms.double(0.08),
    mvaIDwpTight = cms.double(0.2),
    mvaJetTag = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    mvaL1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    mvaL1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    recomputeBasicSelectors = cms.bool(False),
    resolutions = cms.PSet(

    ),
    rho = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
    softMvaRun3Model = cms.string('RecoMuon/MuonIdentification/data/Run2022-20231030-1731-Event0'),
    softMvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/TMVA-muonid-bmm4-B-25.weights.xml'),
    sourceMuonTimeExtra = cms.InputTag("filteredDisplacedMuons","combined"),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    useJec = cms.bool(False),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(False),
    addGenMatch = cms.bool(True),
    addMVAVariables = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    computeMiniIso = cms.bool(False),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(False),
    embedHighLevelSelection = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPflowBasicClusters = cms.bool(True),
    embedPflowPreshowerClusters = cms.bool(True),
    embedPflowSuperCluster = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("electronMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("elPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04PFIdPAT")
    ),
    isolationValuesNoPFId = cms.PSet(
        pfChargedAll = cms.InputTag("elPFIsoValueChargedAll04NoPFIdPAT"),
        pfChargedHadrons = cms.InputTag("elPFIsoValueCharged04NoPFIdPAT"),
        pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral04NoPFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU04NoPFIdPAT"),
        pfPhotons = cms.InputTag("elPFIsoValueGamma04NoPFIdPAT")
    ),
    mightGet = cms.optional.untracked.vstring,
    miniIsoParamsB = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0
    ),
    miniIsoParamsE = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.015,
        0.015, 0.08, 0.0, 0.0
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    usePfCandidateMultiMap = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patJetCharge = cms.EDProducer("JetChargeProducer",
    exp = cms.double(1.0),
    src = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    var = cms.string('Pt')
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociation = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak4PFJetsCHS"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.4)
)


process.patJetFlavourAssociationLegacy = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacy")
)


process.patJetGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak4GenJets"),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartonAssociationLegacy = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak4PFJetsCHS"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5,
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak4PFJetsCHS")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    fullChainPhysPartons = cms.bool(True),
    particles = cms.InputTag("genParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("genParticles"),
    withLeptons = cms.bool(False)
)


process.patJets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(True),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        "pfJetBProbabilityBJetTags", "pfJetProbabilityBJetTags", "pfTrackCountingHighEffBJetTags", "pfSimpleSecondaryVertexHighEffBJetTags", "pfSimpleInclusiveSecondaryVertexHighEffBJetTags",
        "pfCombinedSecondaryVertexV2BJetTags", "pfCombinedInclusiveSecondaryVertexV2BJetTags", "softPFMuonBJetTags", "softPFElectronBJetTags", "pfCombinedMVAV2BJetTags",
        "pfCombinedCvsLJetTags", "pfCombinedCvsBJetTags", "pfDeepCSVJetTags:probb", "pfDeepCSVJetTags:probc", "pfDeepCSVJetTags:probudsg",
        "pfDeepCSVJetTags:probbb"
    ),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag("patJetCorrFactors"),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsCHS"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patLowPtElectrons = cms.EDProducer("PATElectronProducer",
    addEfficiencies = cms.bool(False),
    addElectronID = cms.bool(True),
    addGenMatch = cms.bool(True),
    addMVAVariables = cms.bool(False),
    addPFClusterIso = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    computeMiniIso = cms.bool(False),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronIDSources = cms.PSet(
        ID = cms.InputTag("lowPtGsfElectronID"),
        ptbiased = cms.InputTag("rekeyLowPtGsfElectronSeedValueMaps","ptbiased"),
        unbiased = cms.InputTag("rekeyLowPtGsfElectronSeedValueMaps","unbiased")
    ),
    electronSource = cms.InputTag("lowPtGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedGsfElectronCore = cms.bool(True),
    embedGsfTrack = cms.bool(True),
    embedHighLevelSelection = cms.bool(False),
    embedPFCandidate = cms.bool(False),
    embedPflowBasicClusters = cms.bool(False),
    embedPflowPreshowerClusters = cms.bool(False),
    embedPflowSuperCluster = cms.bool(False),
    embedPreshowerClusters = cms.bool(False),
    embedRecHits = cms.bool(False),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    embedTrack = cms.bool(True),
    genParticleMatch = cms.InputTag("lowPtElectronMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(

    ),
    isolationValuesNoPFId = cms.PSet(

    ),
    mightGet = cms.optional.untracked.vstring,
    miniIsoParamsB = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0
    ),
    miniIsoParamsE = cms.vdouble(
        0.05, 0.2, 10.0, 0.0, 0.015,
        0.015, 0.08, 0.0, 0.0
    ),
    pfCandidateMap = cms.InputTag("particleFlow","electrons"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfElectronSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    useParticleFlow = cms.bool(False),
    usePfCandidateMultiMap = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patMETs = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetT1"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.39, 1.26, 1.21, 1.23, 1.28),
        pjpar = cms.vdouble(-0.2586, 0.6173)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    srcWeights = cms.InputTag(""),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMuons = cms.EDProducer("PATMuonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addInverseBeta = cms.bool(True),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    addTriggerMatching = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    caloMETMuonCorrs = cms.InputTag("muonMETValueMapProducer","muCorrData"),
    computeMiniIso = cms.bool(False),
    computeMuonIDMVA = cms.bool(False),
    computePuppiCombinedIso = cms.bool(False),
    computeSoftMuonMVA = cms.bool(False),
    effectiveAreaVec = cms.vdouble(0.0566, 0.0562, 0.0363, 0.0119, 0.0064),
    efficiencies = cms.PSet(

    ),
    embedCaloMETMuonCorrs = cms.bool(True),
    embedCombinedMuon = cms.bool(True),
    embedDytMuon = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedHighLevelSelection = cms.bool(True),
    embedMuonBestTrack = cms.bool(True),
    embedPFCandidate = cms.bool(True),
    embedPfEcalEnergy = cms.bool(True),
    embedPickyMuon = cms.bool(True),
    embedStandAloneMuon = cms.bool(True),
    embedTcMETMuonCorrs = cms.bool(False),
    embedTpfmsMuon = cms.bool(True),
    embedTrack = cms.bool(False),
    embedTunePMuonBestTrack = cms.bool(True),
    forceBestTrackEmbedding = cms.bool(False),
    genParticleMatch = cms.InputTag("muonMatch"),
    hltCollectionFilters = cms.vstring('*'),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("muPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("muPFIsoValueChargedAll04PAT"),
        pfChargedHadrons = cms.InputTag("muPFIsoValueCharged04PAT"),
        pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral04PAT"),
        pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU04PAT"),
        pfPhotons = cms.InputTag("muPFIsoValueGamma04PAT")
    ),
    miniIsoParams = cms.vdouble(
        0.05, 0.2, 10.0, 0.5, 0.0001,
        0.01, 0.01, 0.01, 0.0
    ),
    muonSimInfo = cms.InputTag("muonSimClassifier"),
    muonSource = cms.InputTag("muons"),
    mvaDrMax = cms.double(0.4),
    mvaIDTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/mvaID.onnx'),
    mvaIDwpMedium = cms.double(0.08),
    mvaIDwpTight = cms.double(0.2),
    mvaJetTag = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    mvaL1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    mvaL1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    pfMuonSource = cms.InputTag("particleFlow"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    recomputeBasicSelectors = cms.bool(True),
    resolutions = cms.PSet(

    ),
    rho = cms.InputTag("fixedGridRhoFastjetCentralNeutral"),
    softMvaRun3Model = cms.string('RecoMuon/MuonIdentification/data/Run2022-20231030-1731-Event0'),
    softMvaTrainingFile = cms.FileInPath('RecoMuon/MuonIdentification/data/TMVA-muonid-bmm4-B-25.weights.xml'),
    sourceMuonTimeExtra = cms.InputTag("muons","combined"),
    tcMETMuonCorrs = cms.InputTag("muonTCMETValueMapProducer","muCorrData"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    triggerResults = cms.InputTag("TriggerResults","","HLT"),
    useJec = cms.bool(True),
    useParticleFlow = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patOOTPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    conversionSource = cms.InputTag("allConversions"),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(False),
    embedGenMatch = cms.bool(False),
    embedPreshowerClusters = cms.bool(False),
    embedRecHits = cms.bool(False),
    embedSeedCluster = cms.bool(False),
    embedSuperCluster = cms.bool(False),
    genParticleMatch = cms.InputTag("ootPhotonMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(

    ),
    isolationValues = cms.PSet(

    ),
    mightGet = cms.optional.untracked.vstring,
    photonIDSources = cms.PSet(

    ),
    photonSource = cms.InputTag("ootPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    saveRegressionData = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patPhotons = cms.EDProducer("PATPhotonProducer",
    addEfficiencies = cms.bool(False),
    addGenMatch = cms.bool(True),
    addPFClusterIso = cms.bool(False),
    addPhotonID = cms.bool(False),
    addPuppiIsolation = cms.bool(False),
    addResolutions = cms.bool(False),
    beamLineSrc = cms.InputTag("offlineBeamSpot"),
    conversionSource = cms.InputTag("allConversions"),
    ecalPFClusterIsoMap = cms.InputTag(""),
    efficiencies = cms.PSet(

    ),
    electronSource = cms.InputTag("gedGsfElectrons"),
    embedBasicClusters = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedPreshowerClusters = cms.bool(True),
    embedRecHits = cms.bool(True),
    embedSeedCluster = cms.bool(True),
    embedSuperCluster = cms.bool(True),
    genParticleMatch = cms.InputTag("photonMatch"),
    hcalPFClusterIsoMap = cms.InputTag(""),
    isoDeposits = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoDepositChargedPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoDepositNeutralPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoDepositPUPAT"),
        pfPhotons = cms.InputTag("phPFIsoDepositGammaPAT")
    ),
    isolationValues = cms.PSet(
        pfChargedAll = cms.InputTag("phPFIsoValueChargedAll04PFIdPAT"),
        pfChargedHadrons = cms.InputTag("phPFIsoValueCharged04PFIdPAT"),
        pfNeutralHadrons = cms.InputTag("phPFIsoValueNeutral04PFIdPAT"),
        pfPUChargedHadrons = cms.InputTag("phPFIsoValuePU04PFIdPAT"),
        pfPhotons = cms.InputTag("phPFIsoValueGamma04PFIdPAT")
    ),
    mightGet = cms.optional.untracked.vstring,
    photonIDSources = cms.PSet(

    ),
    photonSource = cms.InputTag("gedPhotons"),
    reducedBarrelRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    reducedEndcapRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    resolutions = cms.PSet(

    ),
    saveRegressionData = cms.bool(True),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTaus = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatch"),
    genParticleMatch = cms.InputTag("tauMatch"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejection"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLoose3 = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejection3'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejection3"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTight3 = cms.PSet(
            idLabel = cms.string('ByTightMuonRejection3'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejection3"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducer"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.pfCandMETcorr = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorr"),
    srcWeights = cms.InputTag("")
)


process.pfCandsNotInJetsForMetCorr = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsPtrForMetCorr = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(False),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorr")
)


process.pfJetsPtrForMetCorr = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfMetT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfNoPileUpIsoPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME")
)


process.pfNoPileUpPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpPFBRECO")
)


process.pfPileUpIsoPFBRECO = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(0),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(2),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpPFBRECO = cms.EDProducer("PFPileUp",
    DzCutForChargedFromPUVtxs = cms.double(0.2),
    NumOfPUVtxsForCharged = cms.uint32(0),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    enable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.phPFIsoDepositChargedAllPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositChargedPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositGammaPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(False),
        SCMatch_Veto = cms.bool(True),
        inputCandView = cms.InputTag("pfAllPhotonsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositNeutralPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadronsPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoDepositPUPAT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticlesPFBRECO")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("gedPhotons"),
    trackType = cms.string('candidate')
)


process.phPFIsoValueCharged03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueCharged04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueChargedAll04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositChargedAllPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueGamma04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositGammaPAT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.05)'),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValueNeutral04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositNeutralPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU03PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.3),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.phPFIsoValuePU04PFIdPAT = cms.EDProducer("PFCandIsolatorFromDeposits",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        deltaR = cms.double(0.4),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("phPFIsoDepositPUPAT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.photonMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(1.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(22),
    mcStatus = cms.vint32(1),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("gedPhotons")
)


process.primaryVertexAssociation = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(-1),
        NumOfPUVtxsForCharged = cms.uint32(0),
        OnlyUseFirstDz = cms.bool(False),
        PtMaxCharged = cms.double(-1),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(0.05),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.1),
        maxDzSigForPrimaryAssignment = cms.double(5),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("particleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("offlinePrimaryVertices")
)


process.primaryVertexAssociationJME = cms.EDProducer("PFCandidatePrimaryVertexSorter",
    assignment = cms.PSet(
        DzCutForChargedFromPUVtxs = cms.double(0.2),
        EtaMinUseDz = cms.double(2.4),
        NumOfPUVtxsForCharged = cms.uint32(2),
        OnlyUseFirstDz = cms.bool(True),
        PtMaxCharged = cms.double(20.0),
        maxDistanceToJetAxis = cms.double(0.07),
        maxDtSigForPrimaryAssignment = cms.double(3),
        maxDxyForJetAxisAssigment = cms.double(0.1),
        maxDxyForNotReconstructedPrimary = cms.double(0.01),
        maxDxySigForNotReconstructedPrimary = cms.double(2),
        maxDzErrorForPrimaryAssignment = cms.double(10000000000.0),
        maxDzForJetAxisAssigment = cms.double(0.1),
        maxDzForPrimaryAssignment = cms.double(0.3),
        maxDzSigForPrimaryAssignment = cms.double(10000000000.0),
        maxJetDeltaR = cms.double(0.5),
        minJetPt = cms.double(25),
        preferHighRanked = cms.bool(False),
        useTiming = cms.bool(False),
        useVertexFit = cms.bool(True)
    ),
    jets = cms.InputTag("ak4PFJets"),
    mightGet = cms.optional.untracked.vstring,
    particles = cms.InputTag("particleFlow"),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceNoPileUpCollection = cms.bool(False),
    producePileUpCollection = cms.bool(False),
    produceSortedVertices = cms.bool(False),
    qualityForPrimary = cms.int32(2),
    sorting = cms.PSet(

    ),
    usePVMET = cms.bool(True),
    vertices = cms.InputTag("goodOfflinePrimaryVertices")
)


process.rekeyLowPtGsfElectronSeedValueMaps = cms.EDProducer("LowPtGsfElectronSeedValueMapsProducer",
    ModelNames = cms.vstring(
        'unbiased',
        'ptbiased'
    ),
    floatValueMaps = cms.VInputTag("lowPtGsfElectronSeedValueMaps:unbiased", "lowPtGsfElectronSeedValueMaps:ptbiased"),
    gsfElectrons = cms.InputTag("lowPtGsfElectrons"),
    gsfTracks = cms.InputTag("lowPtGsfEleGsfTracks"),
    mightGet = cms.optional.untracked.vstring,
    preIdsValueMap = cms.InputTag("lowPtGsfElectronSeeds"),
    rekey = cms.bool(True)
)


process.secondaryVertexTagInfos = cms.EDProducer("SecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("impactParameterTagInfos"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(2),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(8),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.simpleSecondaryVertexHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex2TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.simpleSecondaryVertexHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('simpleSecondaryVertex3TrkComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
)


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("genParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("genParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.trackCountingHighEffBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D2ndComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.trackCountingHighPurBJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('trackCounting3D3rdComputer'),
    tagInfos = cms.VInputTag(cms.InputTag("impactParameterTagInfos"))
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.highPurityGeneralTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("generalTracks")
)


process.pfAllChargedHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfEmptyCollection = cms.EDFilter("GenericPFCandidateSelector",
    cut = cms.string('pt<0'),
    src = cms.InputTag("particleFlow")
)


process.pfPileUpAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJets")
)


process.dijetScouting = cms.EDAnalyzer("ScoutingTreeMakerRun3",
    NoiseFilterResultsTag = cms.InputTag("TriggerResults","","HLT"),
    ReadPrescalesFromFile = cms.bool(False),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    applyJEC = cms.bool(True),
    applyJECUncertainty = cms.bool(True),
    applyJetVetoMap = cms.bool(True),
    displacedVertices = cms.InputTag("hltScoutingMuonPackerNoVtx","displacedVtx"),
    doL1 = cms.bool(True),
    doTriggerObjects = cms.bool(True),
    electrons = cms.InputTag("hltScoutingEgammaPacker"),
    genJetsAK4 = cms.InputTag("slimmedGenJets"),
    genParticles = cms.InputTag("prunedGenParticlesDijet"),
    jecLevels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute',
        'L2L3Residual'
    ),
    jecMode = cms.string('txt'),
    jecPayload = cms.string('AK4PFHLT'),
    jecResidualByRun = cms.bool(False),
    jecResidualFallbackToTxt = cms.bool(True),
    jecResidualMap = cms.vstring(),
    jecResidualMapData = cms.vstring(),
    jecResidualMapMC = cms.vstring(),
    jecTxtFiles = cms.vstring(),
    jecTxtFilesData = cms.vstring(),
    jecTxtFilesMC = cms.vstring(),
    jecUncFallbackToTxt = cms.bool(True),
    jecUncTxtFile = cms.string(''),
    jecUncTxtFileData = cms.string(''),
    jecUncTxtFileMC = cms.string(''),
    jetVetoMapFiles = cms.vstring(),
    jetVetoMapFilesData = cms.vstring(),
    jetVetoMapFilesMC = cms.vstring(),
    l1GtSrc = cms.InputTag("gtStage2Digis","","HLT"),
    l1Seeds = cms.vstring(
        'L1_HTT120er',
        'L1_HTT160er',
        'L1_HTT200er',
        'L1_HTT255er',
        'L1_HTT280er',
        'L1_HTT320er',
        'L1_HTT400er',
        'L1_HTT450er',
        'L1_ZeroBias'
    ),
    l1tIgnoreMaskAndPrescale = cms.bool(False),
    l1tResults = cms.InputTag(""),
    muonsNoVtx = cms.InputTag("hltScoutingMuonPackerNoVtx"),
    muonsVtx = cms.InputTag("hltScoutingMuonPackerVtx"),
    pfMet = cms.InputTag("hltScoutingPFPacker","pfMetPt"),
    pfMetPhi = cms.InputTag("hltScoutingPFPacker","pfMetPhi"),
    pfcands = cms.InputTag("hltScoutingPFPacker"),
    pfjets = cms.InputTag("hltScoutingPFPacker"),
    photons = cms.InputTag("hltScoutingEgammaPacker"),
    primaryVertices = cms.InputTag("hltScoutingPrimaryVertexPacker","primaryVtx"),
    printJECFirstNJets = cms.uint32(6),
    printJECInfo = cms.bool(True),
    ptHat = cms.untracked.InputTag("generator"),
    ptMinPF = cms.double(15),
    pu = cms.untracked.InputTag("slimmedAddPileupInfo"),
    rho = cms.InputTag("hltScoutingPFPacker","rho"),
    throw = cms.bool(True),
    tracks = cms.InputTag("hltScoutingTrackPacker"),
    triggerSelection = cms.vstring(
        'DST_PFScouting_JetHT_v',
        'DST_PFScouting_SingleMuon_v',
        'HLT_Mu50_v',
        'HLT_Mu55_v',
        'HLT_IsoMu24_v',
        'HLT_IsoMu20_v',
        'HLT_IsoMu27_v',
        'HLT_PFHT180_v',
        'HLT_PFHT180_v',
        'HLT_PFHT350_v',
        'HLT_PFHT370_v',
        'HLT_PFHT430_v',
        'HLT_PFHT510_v',
        'HLT_PFHT590_v',
        'HLT_PFJet40_v',
        'HLT_PFJet60_v',
        'HLT_PFJet80_v',
        'HLT_PFJet140_v',
        'HLT_PFJet200_v',
        'HLT_PFJet260_v',
        'HLT_PFJet320_v',
        'HLT_PFJet400_v',
        'HLT_PFJet450_v',
        'HLT_PFJet500_v',
        'HLT_PFJet550_v',
        'DST_PFScouting_ZeroBias_v',
        'DST_PFScouting_AXOTight_v',
        'DST_PFScouting_AXOVLoose_v',
        'DST_PFScouting_AXOLoose_v',
        'DST_PFScouting_AXOVTight_v',
        'DST_PFScouting_SinglePhotonEB_v',
        'DST_PFScouting_CICADAVLoose_v',
        'DST_PFScouting_CICADALoose_v',
        'DST_PFScouting_CICADAMedium_v',
        'DST_PFScouting_CICADATight_v',
        'DST_PFScouting_CICADAVTight_v'
    ),
    usePathStatus = cms.bool(False)
)


process.patCandidateSummary = cms.EDAnalyzer("CandidateSummaryTable",
    candidates = cms.VInputTag(
        cms.InputTag("patElectrons"), cms.InputTag("patLowPtElectrons"), cms.InputTag("patMuons"), cms.InputTag("patDisplacedMuons"), cms.InputTag("patTaus"),
        cms.InputTag("patPhotons"), cms.InputTag("patOOTPhotons"), cms.InputTag("patJets"), cms.InputTag("patMETs")
    ),
    logName = cms.untracked.string('patCandidates|PATSummaryTables')
)


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(100000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(100000)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        JEC = cms.untracked.PSet(
            limit = cms.untracked.int32(1000000000)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(True),
    fileName = cms.string('ScoutingPFRun3__Run2024D-v1__HLTSCOUT.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'CASTOR',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string(''),
    dump = cms.untracked.vstring(),
    file = cms.untracked.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.SteppingHelixPropagatorAlong = cms.ESProducer("SteppingHelixPropagatorESProducer",
    ApplyRadX0Correction = cms.bool(True),
    AssumeNoMaterial = cms.bool(False),
    ComponentName = cms.string('SteppingHelixPropagatorAlong'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    SetVBFPointer = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    debug = cms.bool(False),
    endcapShiftInZNeg = cms.double(0.0),
    endcapShiftInZPos = cms.double(0.0),
    returnTangentPlane = cms.bool(True),
    sendLogWarning = cms.bool(False),
    useEndcapShiftsInZ = cms.bool(False),
    useInTeslaFromMagField = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    useMagVolumes = cms.bool(True),
    useMatVolumes = cms.bool(True),
    useTuningForL2Speed = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerAdditionalParametersPerDet = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder'),
    appendToDataLabel = cms.string('')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex',
        'CombinedSVIVFV2PseudoVertex',
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    opticsLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.heavyIonCSVComputer = cms.ESProducer("HeavyIonCSVESProducer",
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    sv_cfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVIVFV2RecoVertex',
            'CombinedSVIVFV2PseudoVertex',
            'CombinedSVIVFV2NoVertex'
        ),
        categoryVariableName = cms.string('vertexCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackSip3dSig_2'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackSip3dSig_3'),
            taggingVarName = cms.string('trackSip3dSig')
        ),
        cms.PSet(
            default = cms.double(-999),
            name = cms.string('TagVarCSV_trackSip3dSigAboveCharm'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackPtRel_2'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackPtRel_3'),
            taggingVarName = cms.string('trackPtRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackEtaRel_2'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackEtaRel_3'),
            taggingVarName = cms.string('trackEtaRel')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackDeltaR_2'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackDeltaR_3'),
            taggingVarName = cms.string('trackDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackPtRatio_2'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackPtRatio_3'),
            taggingVarName = cms.string('trackPtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackJetDist_2'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackJetDist_3'),
            taggingVarName = cms.string('trackJetDist')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackDecayLenVal_2'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackDecayLenVal_3'),
            taggingVarName = cms.string('trackDecayLenVal')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_vertexMass'),
            taggingVarName = cms.string('vertexMass')
        ),
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_vertexNTracks'),
            taggingVarName = cms.string('vertexNTracks')
        ),
        cms.PSet(
            default = cms.double(-10),
            name = cms.string('TagVarCSV_vertexEnergyRatio'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ),
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_vertexJetDeltaR'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ),
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('TagVarCSV_flightDistance2dSig'),
            taggingVarName = cms.string('flightDistance2dSig')
        ),
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ),
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_vertexCategory'),
            taggingVarName = cms.string('vertexCategory')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/TMVA_Btag_CsJets_PbPb2018_BDTG.weights.xml')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.multipleScatteringParametrisationMakerESProducer = cms.ESProducer("MultipleScatteringParametrisationMakerESProducer",
    appendToDataLabel = cms.string('')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    appendToDataLabel = cms.string(''),
    siPixelQualityFromDbLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.zdcTopologyEP = cms.ESProducer("ZdcTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        connectionTimeout = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    JsonDumpFileName = cms.untracked.string(''),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    appendToDataLabel = cms.string(''),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    frontierKey = cms.untracked.string(''),
    globaltag = cms.string('140X_dataRun3_HLT_v3'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    recordsToDebug = cms.untracked.vstring(),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        noiseThreshold = cms.double(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        seedThreshold = cms.double(0.1),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.ak4CaloL1FastL2L3CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL1FastL2L3L6CorrectorTask = cms.Task(process.ak4CaloL1FastL2L3L6Corrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak4CaloL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1FastL2L3ResidualCorrector, process.ak4CaloL1FastjetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4CaloL1L2L3CorrectorTask = cms.Task(process.ak4CaloL1L2L3Corrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL1L2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL1L2L3ResidualCorrector, process.ak4CaloL1OffsetCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4CaloL2L3CorrectorTask = cms.Task(process.ak4CaloL2L3Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector)


process.ak4CaloL2L3L6CorrectorTask = cms.Task(process.ak4CaloL2L3L6Corrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloL6SLBCorrector)


process.ak4CaloL2L3ResidualCorrectorTask = cms.Task(process.ak4CaloL2L3ResidualCorrector, process.ak4CaloL2RelativeCorrector, process.ak4CaloL3AbsoluteCorrector, process.ak4CaloResidualCorrector)


process.ak4L1JPTFastjetCorrectorTask = cms.Task(process.ak4CaloL1FastjetCorrector, process.ak4L1JPTFastjetCorrector)


process.ak4L1JPTOffsetCorrectorTask = cms.Task(process.ak4CaloL1OffsetCorrector, process.ak4L1JPTOffsetCorrector)


process.ak4PFCHSL1FastL2L3CorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3Corrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1FastL2L3ResidualCorrector, process.ak4PFCHSL1FastjetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFCHSL1L2L3CorrectorTask = cms.Task(process.ak4PFCHSL1L2L3Corrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL1L2L3ResidualCorrector, process.ak4PFCHSL1OffsetCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFCHSL2L3CorrectorTask = cms.Task(process.ak4PFCHSL2L3Corrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector)


process.ak4PFCHSL2L3ResidualCorrectorTask = cms.Task(process.ak4PFCHSL2L3ResidualCorrector, process.ak4PFCHSL2RelativeCorrector, process.ak4PFCHSL3AbsoluteCorrector, process.ak4PFCHSResidualCorrector)


process.ak4PFL1FastL2L3CorrectorTask = cms.Task(process.ak4PFL1FastL2L3Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL1FastL2L3L6CorrectorTask = cms.Task(process.ak4PFL1FastL2L3L6Corrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak4PFL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1FastL2L3ResidualCorrector, process.ak4PFL1FastjetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFL1L2L3CorrectorTask = cms.Task(process.ak4PFL1L2L3Corrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFL1L2L3ResidualCorrector, process.ak4PFL1OffsetCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFL2L3CorrectorTask = cms.Task(process.ak4PFL2L3Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector)


process.ak4PFL2L3L6CorrectorTask = cms.Task(process.ak4PFL2L3L6Corrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFL6SLBCorrector)


process.ak4PFL2L3ResidualCorrectorTask = cms.Task(process.ak4PFL2L3ResidualCorrector, process.ak4PFL2RelativeCorrector, process.ak4PFL3AbsoluteCorrector, process.ak4PFResidualCorrector)


process.ak4PFPuppiL1FastL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3Corrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1FastL2L3ResidualCorrector, process.ak4PFPuppiL1FastjetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL1L2L3CorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3Corrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL1L2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL1L2L3ResidualCorrector, process.ak4PFPuppiL1OffsetCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4PFPuppiL2L3CorrectorTask = cms.Task(process.ak4PFPuppiL2L3Corrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector)


process.ak4PFPuppiL2L3ResidualCorrectorTask = cms.Task(process.ak4PFPuppiL2L3ResidualCorrector, process.ak4PFPuppiL2RelativeCorrector, process.ak4PFPuppiL3AbsoluteCorrector, process.ak4PFPuppiResidualCorrector)


process.ak4TrackL2L3CorrectorTask = cms.Task(process.ak4TrackL2L3Corrector, process.ak4TrackL2RelativeCorrector, process.ak4TrackL3AbsoluteCorrector)


process.ak5JTAExplicitTask = cms.Task(process.ak5JetTracksAssociatorExplicit)


process.ak5JTATask = cms.Task(process.ak5JetExtender, process.ak5JetTracksAssociatorAtCaloFace, process.ak5JetTracksAssociatorAtVertex, process.ak5JetTracksAssociatorAtVertexPF)


process.correctionTermsCaloMetTask = cms.Task(process.ak4CaloL2L3CorrectorTask, process.ak4CaloL2L3ResidualCorrectorTask, process.corrCaloMetType1, process.corrCaloMetType2, process.muCaloMetCorr)


process.correctionTermsPfMetType1Type2Task = cms.Task(process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.corrPfMetType1, process.corrPfMetType2, process.particleFlowPtrs, process.pfCandMETcorr, process.pfCandsNotInJetsForMetCorr, process.pfCandsNotInJetsPtrForMetCorr, process.pfJetsPtrForMetCorr)


process.electronPFIsolationDepositsPATTask = cms.Task(process.elPFIsoDepositChargedAllPAT, process.elPFIsoDepositChargedPAT, process.elPFIsoDepositGammaPAT, process.elPFIsoDepositNeutralPAT, process.elPFIsoDepositPUPAT)


process.electronPFIsolationValuesPATTask = cms.Task(process.elPFIsoValueCharged03NoPFIdPAT, process.elPFIsoValueCharged03PFIdPAT, process.elPFIsoValueCharged04NoPFIdPAT, process.elPFIsoValueCharged04PFIdPAT, process.elPFIsoValueChargedAll03NoPFIdPAT, process.elPFIsoValueChargedAll03PFIdPAT, process.elPFIsoValueChargedAll04NoPFIdPAT, process.elPFIsoValueChargedAll04PFIdPAT, process.elPFIsoValueGamma03NoPFIdPAT, process.elPFIsoValueGamma03PFIdPAT, process.elPFIsoValueGamma04NoPFIdPAT, process.elPFIsoValueGamma04PFIdPAT, process.elPFIsoValueNeutral03NoPFIdPAT, process.elPFIsoValueNeutral03PFIdPAT, process.elPFIsoValueNeutral04NoPFIdPAT, process.elPFIsoValueNeutral04PFIdPAT, process.elPFIsoValuePU03NoPFIdPAT, process.elPFIsoValuePU03PFIdPAT, process.elPFIsoValuePU04NoPFIdPAT, process.elPFIsoValuePU04PFIdPAT)


process.filteredDisplacedMuonsTask = cms.Task(process.filteredDisplacedMuons)


process.hiCleanedGenJetsTask_ = cms.Task(process.ak4HiGenJetsCleaned, process.ak4HiGenJetsNoNu, process.allPartons, process.cleanedPartons, process.genParticlesForJetsNoNu)


process.hiGenJetsTask = cms.Task(process.ak4HiGenJetsNoNu, process.ak4HiSignalGenJets, process.allPartons, process.genParticlesForJetsNoNu, process.hiSignalGenParticles)


process.makePatDisplacedMuonsTask = cms.Task(process.filteredDisplacedMuonsTask, process.patDisplacedMuons)


process.makePatLowPtElectronsTask = cms.Task(process.lowPtElectronMatch, process.patLowPtElectrons)


process.makePatOOTPhotonsTask = cms.Task(process.ootPhotonMatch, process.patOOTPhotons)


process.muonPFIsolationDepositsPATTask = cms.Task(process.muPFIsoDepositChargedAllPAT, process.muPFIsoDepositChargedPAT, process.muPFIsoDepositGammaPAT, process.muPFIsoDepositNeutralPAT, process.muPFIsoDepositPUPAT)


process.muonPFIsolationValuesPATTask = cms.Task(process.muPFIsoValueCharged03PAT, process.muPFIsoValueCharged04PAT, process.muPFIsoValueChargedAll03PAT, process.muPFIsoValueChargedAll04PAT, process.muPFIsoValueGamma03PAT, process.muPFIsoValueGamma04PAT, process.muPFIsoValueGammaHighThreshold03PAT, process.muPFIsoValueGammaHighThreshold04PAT, process.muPFIsoValueNeutral03PAT, process.muPFIsoValueNeutral04PAT, process.muPFIsoValueNeutralHighThreshold03PAT, process.muPFIsoValueNeutralHighThreshold04PAT, process.muPFIsoValuePU03PAT, process.muPFIsoValuePU04PAT, process.muPFMeanDRIsoValueCharged03PAT, process.muPFMeanDRIsoValueCharged04PAT, process.muPFMeanDRIsoValueChargedAll03PAT, process.muPFMeanDRIsoValueChargedAll04PAT, process.muPFMeanDRIsoValueGamma03PAT, process.muPFMeanDRIsoValueGamma04PAT, process.muPFMeanDRIsoValueGammaHighThreshold03PAT, process.muPFMeanDRIsoValueGammaHighThreshold04PAT, process.muPFMeanDRIsoValueNeutral03PAT, process.muPFMeanDRIsoValueNeutral04PAT, process.muPFMeanDRIsoValueNeutralHighThreshold03PAT, process.muPFMeanDRIsoValueNeutralHighThreshold04PAT, process.muPFMeanDRIsoValuePU03PAT, process.muPFMeanDRIsoValuePU04PAT, process.muPFSumDRIsoValueCharged03PAT, process.muPFSumDRIsoValueCharged04PAT, process.muPFSumDRIsoValueChargedAll03PAT, process.muPFSumDRIsoValueChargedAll04PAT, process.muPFSumDRIsoValueGamma03PAT, process.muPFSumDRIsoValueGamma04PAT, process.muPFSumDRIsoValueGammaHighThreshold03PAT, process.muPFSumDRIsoValueGammaHighThreshold04PAT, process.muPFSumDRIsoValueNeutral03PAT, process.muPFSumDRIsoValueNeutral04PAT, process.muPFSumDRIsoValueNeutralHighThreshold03PAT, process.muPFSumDRIsoValueNeutralHighThreshold04PAT, process.muPFSumDRIsoValuePU03PAT, process.muPFSumDRIsoValuePU04PAT)


process.patJetCorrectionsTask = cms.Task(process.patJetCorrFactors)


process.patJetFlavourIdLegacyTask = cms.Task(process.patJetFlavourAssociationLegacy, process.patJetPartonAssociationLegacy, process.patJetPartonsLegacy)


process.patJetFlavourIdTask = cms.Task(process.patJetFlavourAssociation, process.patJetPartons)


process.patMETCorrectionsTask = cms.Task(process.caloMetT1, process.caloMetT1T2, process.correctionTermsCaloMetTask, process.correctionTermsPfMetType1Type2Task, process.pfMetT1, process.pfMetT1T2)


process.patPFTauIsolationTask = cms.Task(process.tauIsoDepositPFCandidates, process.tauIsoDepositPFChargedHadrons, process.tauIsoDepositPFGammas, process.tauIsoDepositPFNeutralHadrons)


process.pfElectronIsolationPATTask = cms.Task(process.electronPFIsolationDepositsPATTask, process.electronPFIsolationValuesPATTask)


process.pfNoPileUpIsoPFBRECOTask = cms.Task(process.pfNoPileUpIsoPFBRECO, process.pfPileUpIsoPFBRECO)


process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.pfNoPileUpPFBRECOTask = cms.Task(process.pfNoPileUpPFBRECO, process.pfPileUpPFBRECO)


process.pfSortByTypePFBRECOTask = cms.Task(process.pfAllChargedHadronsPFBRECO, process.pfAllChargedParticlesPFBRECO, process.pfAllNeutralHadronsAndPhotonsPFBRECO, process.pfAllNeutralHadronsPFBRECO, process.pfAllPhotonsPFBRECO, process.pfPileUpAllChargedParticlesPFBRECO)


process.photonPFIsolationDepositsPATTask = cms.Task(process.phPFIsoDepositChargedAllPAT, process.phPFIsoDepositChargedPAT, process.phPFIsoDepositGammaPAT, process.phPFIsoDepositNeutralPAT, process.phPFIsoDepositPUPAT)


process.photonPFIsolationValuesPATTask = cms.Task(process.phPFIsoValueCharged03PFIdPAT, process.phPFIsoValueCharged04PFIdPAT, process.phPFIsoValueChargedAll03PFIdPAT, process.phPFIsoValueChargedAll04PFIdPAT, process.phPFIsoValueGamma03PFIdPAT, process.phPFIsoValueGamma04PFIdPAT, process.phPFIsoValueNeutral03PFIdPAT, process.phPFIsoValueNeutral04PFIdPAT, process.phPFIsoValuePU03PFIdPAT, process.phPFIsoValuePU04PFIdPAT)


process.recoGenJetsHIpostAODTask = cms.Task(process.allPartons, process.hiGenJetsTask)


process.recoPFJetsHIpostAODTask = cms.Task(process.PackedPFTowers, process.ak4PFJetsForFlow, process.ak5JetTracksAssociatorAtVertex, process.akCs4PFJets, process.combinedSecondaryVertexV2BJetTags, process.hiFJRhoFlowModulation, process.hiPuRho, process.highPurityGeneralTracks, process.impactParameterTagInfos, process.jetBProbabilityBJetTags, process.jetProbabilityBJetTags, process.patJetCorrFactors, process.pfEmptyCollection, process.secondaryVertexTagInfos, process.simpleSecondaryVertexHighEffBJetTags, process.simpleSecondaryVertexHighPurBJetTags, process.trackCountingHighEffBJetTags, process.trackCountingHighPurBJetTags)


process.updateHPSPFTausTask = cms.Task(process.hpsPFTauBasicDiscriminators)


process.ak4JPTL1FastL2L3CorrectorTask = cms.Task(process.ak4JPTL1FastL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1FastL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTFastjetCorrectorTask)


process.ak4JPTL1L2L3CorrectorTask = cms.Task(process.ak4JPTL1L2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL1L2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL2L3CorrectorTask = cms.Task(process.ak4JPTL2L3Corrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.ak4JPTL2L3ResidualCorrectorTask = cms.Task(process.ak4JPTL2L3ResidualCorrector, process.ak4JPTL2RelativeCorrector, process.ak4JPTL3AbsoluteCorrector, process.ak4JPTResidualCorrector, process.ak4L1JPTOffsetCorrectorTask)


process.jetCorrectorsTask = cms.Task(process.ak4CaloL1FastL2L3CorrectorTask, process.ak4CaloL1FastL2L3L6CorrectorTask, process.ak4CaloL1FastL2L3ResidualCorrectorTask, process.ak4CaloL1L2L3CorrectorTask, process.ak4CaloL1L2L3ResidualCorrectorTask, process.ak4CaloL2L3CorrectorTask, process.ak4CaloL2L3L6CorrectorTask, process.ak4CaloL2L3ResidualCorrectorTask, process.ak4JPTL1FastL2L3CorrectorTask, process.ak4JPTL1FastL2L3ResidualCorrectorTask, process.ak4JPTL1L2L3CorrectorTask, process.ak4JPTL1L2L3ResidualCorrectorTask, process.ak4JPTL2L3CorrectorTask, process.ak4JPTL2L3ResidualCorrectorTask, process.ak4L1JPTFastjetCorrectorTask, process.ak4L1JPTOffsetCorrectorTask, process.ak4PFCHSL1FastL2L3CorrectorTask, process.ak4PFCHSL1FastL2L3ResidualCorrectorTask, process.ak4PFCHSL1L2L3CorrectorTask, process.ak4PFCHSL1L2L3ResidualCorrectorTask, process.ak4PFCHSL2L3CorrectorTask, process.ak4PFCHSL2L3ResidualCorrectorTask, process.ak4PFL1FastL2L3CorrectorTask, process.ak4PFL1FastL2L3L6CorrectorTask, process.ak4PFL1FastL2L3ResidualCorrectorTask, process.ak4PFL1L2L3CorrectorTask, process.ak4PFL1L2L3ResidualCorrectorTask, process.ak4PFL2L3CorrectorTask, process.ak4PFL2L3L6CorrectorTask, process.ak4PFL2L3ResidualCorrectorTask, process.ak4PFPuppiL1FastL2L3CorrectorTask, process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask, process.ak4PFPuppiL1L2L3CorrectorTask, process.ak4PFPuppiL1L2L3ResidualCorrectorTask, process.ak4PFPuppiL2L3CorrectorTask, process.ak4PFPuppiL2L3ResidualCorrectorTask, process.ak4TrackL2L3CorrectorTask)


process.makePatJetsTask = cms.Task(process.patJetCharge, process.patJetCorrectionsTask, process.patJetFlavourIdLegacyTask, process.patJetFlavourIdTask, process.patJetGenJetMatch, process.patJetPartonMatch, process.patJets)


process.makePatMETsTask = cms.Task(process.patMETCorrectionsTask, process.patMETs)


process.muonPFIsolationPATTask = cms.Task(process.muonPFIsolationDepositsPATTask, process.muonPFIsolationValuesPATTask)


process.patHPSPFTauDiscriminationTask = cms.Task(process.updateHPSPFTausTask)


process.patPFCandidateIsoDepositSelectionTask = cms.Task(process.pfNoPileUpIsoPFBRECOTask, process.pfSortByTypePFBRECOTask)


process.pfParticleSelectionPFBRECOTask = cms.Task(process.pfNoPileUpIsoPFBRECOTask, process.pfNoPileUpPFBRECOTask, process.pfSortByTypePFBRECOTask)


process.pfPhotonIsolationPATTask = cms.Task(process.photonPFIsolationDepositsPATTask, process.photonPFIsolationValuesPATTask)


process.makePatTausTask = cms.Task(process.patPFCandidateIsoDepositSelectionTask, process.patPFTauIsolationTask, process.patTaus, process.tauGenJetMatch, process.tauGenJets, process.tauGenJetsSelectorAllHadrons, process.tauMatch)


process.pfParticleSelectionForIsoTask = cms.Task(process.particleFlowPtrs, process.pfParticleSelectionPFBRECOTask)


process.makePatElectronsTask = cms.Task(process.electronMatch, process.patElectrons, process.pfElectronIsolationPATTask, process.pfParticleSelectionForIsoTask)


process.makePatMuonsTask = cms.Task(process.muonMatch, process.muonPFIsolationPATTask, process.patMuons, process.pfParticleSelectionForIsoTask)


process.makePatPhotonsTask = cms.Task(process.patPhotons, process.pfParticleSelectionForIsoTask, process.pfPhotonIsolationPATTask, process.photonMatch)


process.patCandidatesTask = cms.Task(process.makePatDisplacedMuonsTask, process.makePatElectronsTask, process.makePatJetsTask, process.makePatLowPtElectronsTask, process.makePatMETsTask, process.makePatMuonsTask, process.makePatOOTPhotonsTask, process.makePatPhotonsTask, process.makePatTausTask)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3CorrectorTask)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3L6CorrectorTask)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastL2L3ResidualCorrectorTask)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1L2L3CorrectorTask)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1L2L3ResidualCorrectorTask)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2L3CorrectorTask)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2L3L6CorrectorTask)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2L3ResidualCorrectorTask)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3CorrectorTask)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastL2L3ResidualCorrectorTask)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4JPTL1L2L3CorrectorTask)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1L2L3ResidualCorrectorTask)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4JPTL2L3CorrectorTask)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL2L3ResidualCorrectorTask)


process.ak4L1JPTFastjetCorrectorChain = cms.Sequence(process.ak4L1JPTFastjetCorrectorTask)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorTask)


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3CorrectorTask)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastL2L3ResidualCorrectorTask)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3CorrectorTask)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1L2L3ResidualCorrectorTask)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2L3CorrectorTask)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2L3ResidualCorrectorTask)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3CorrectorTask)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3L6CorrectorTask)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastL2L3ResidualCorrectorTask)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1L2L3CorrectorTask)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1L2L3ResidualCorrectorTask)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2L3CorrectorTask)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2L3L6CorrectorTask)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3CorrectorTask)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastL2L3ResidualCorrectorTask)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3CorrectorTask)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1L2L3ResidualCorrectorTask)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3CorrectorTask)


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2L3ResidualCorrectorTask)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2L3CorrectorTask)


process.ak5JTA = cms.Sequence(process.ak5JTATask)


process.ak5JTAExplicit = cms.Sequence(process.ak5JTAExplicitTask)


process.correctionTermsCaloMet = cms.Sequence(process.correctionTermsCaloMetTask)


process.correctionTermsPfMetType1Type2 = cms.Sequence(process.correctionTermsPfMetType1Type2Task)


process.electronPFIsolationDepositsPATSequence = cms.Sequence(process.electronPFIsolationDepositsPATTask)


process.electronPFIsolationValuesPATSequence = cms.Sequence(process.electronPFIsolationValuesPATTask)


process.makePatDisplacedMuons = cms.Sequence(process.makePatDisplacedMuonsTask)


process.makePatElectrons = cms.Sequence(process.makePatElectronsTask)


process.makePatJets = cms.Sequence(process.makePatJetsTask)


process.makePatLowPtElectrons = cms.Sequence(process.makePatLowPtElectronsTask)


process.makePatMETs = cms.Sequence(process.makePatMETsTask)


process.makePatMuons = cms.Sequence(process.makePatMuonsTask)


process.makePatOOTPhotons = cms.Sequence(process.makePatOOTPhotonsTask)


process.makePatPhotons = cms.Sequence(process.makePatPhotonsTask)


process.makePatTaus = cms.Sequence(process.makePatTausTask)


process.muonPFIsolationDepositsPATSequence = cms.Sequence(process.muonPFIsolationDepositsPATTask)


process.muonPFIsolationPATSequence = cms.Sequence(process.muonPFIsolationPATTask)


process.muonPFIsolationValuesPATSequence = cms.Sequence(process.muonPFIsolationValuesPATTask)


process.patCandidates = cms.Sequence(process.patCandidateSummary, process.patCandidatesTask)


process.patFixedConePFTauDiscrimination = cms.Sequence()


process.patHPSPFTauDiscrimination = cms.Sequence(process.patHPSPFTauDiscriminationTask)


process.patJetCorrections = cms.Sequence(process.patJetCorrectionsTask)


process.patJetFlavourId = cms.Sequence(process.patJetFlavourIdTask)


process.patJetFlavourIdLegacy = cms.Sequence(process.patJetFlavourIdLegacyTask)


process.patMETCorrections = cms.Sequence(process.patMETCorrectionsTask)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.patPFCandidateIsoDepositSelectionTask)


process.patPFTauIsolation = cms.Sequence(process.patPFTauIsolationTask)


process.patShrinkingConePFTauDiscrimination = cms.Sequence()


process.pfElectronIsolationPATSequence = cms.Sequence(process.pfElectronIsolationPATTask)


process.pfNoPileUpIsoPFBRECOSequence = cms.Sequence(process.pfNoPileUpIsoPFBRECOTask)


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.pfNoPileUpPFBRECOSequence = cms.Sequence(process.pfNoPileUpPFBRECOTask)


process.pfParticleSelectionForIsoSequence = cms.Sequence(process.pfParticleSelectionForIsoTask)


process.pfParticleSelectionPFBRECOSequence = cms.Sequence(process.pfParticleSelectionPFBRECOTask)


process.pfPhotonIsolationPATSequence = cms.Sequence(process.pfPhotonIsolationPATTask)


process.pfSortByTypePFBRECOSequence = cms.Sequence(process.pfSortByTypePFBRECOTask)


process.photonPFIsolationDepositsPATSequence = cms.Sequence(process.photonPFIsolationDepositsPATTask)


process.photonPFIsolationValuesPATSequence = cms.Sequence(process.photonPFIsolationValuesPATTask)


process.updateHPSPFTaus = cms.Sequence(process.updateHPSPFTausTask)


process.p = cms.Path(process.gtStage2Digis+process.dijetScouting)


