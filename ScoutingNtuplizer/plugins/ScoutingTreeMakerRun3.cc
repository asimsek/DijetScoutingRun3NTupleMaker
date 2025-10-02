// -*- C++ -*-
//
/*

 Description: Ntuple maker for Run3 scouting dataset from the RAW/HLTSCOUT data-format

*/

#include "DijetScoutingRun3NTupleMaker/ScoutingNtuplizer/plugins/ScoutingTreeMakerRun3.h"
#include "DijetScoutingRun3NTupleMaker/ScoutingNtuplizer/plugins/JECUtils.h"
#include "DijetScoutingRun3NTupleMaker/ScoutingNtuplizer/plugins/JetVetoUtils.h"
#include "DijetScoutingRun3NTupleMaker/ScoutingNtuplizer/plugins/JECLog.h"



ScoutingTreeMakerRun3::ScoutingTreeMakerRun3(const edm::ParameterSet& iConfig)
{
  srcPFJets_             =  consumes<vector<Run3ScoutingPFJet> >          (iConfig.getParameter<InputTag>("pfjets"));
  srcPFCands_            =  consumes<vector<Run3ScoutingParticle> >       (iConfig.getParameter<InputTag>("pfcands"));
  srcRho_                =  consumes<double>                              (iConfig.getParameter<edm::InputTag>("rho"));
  srcMET_                =  consumes<double>                              (iConfig.getParameter<edm::InputTag>("pfMet"));
  srcMetPhi_             =  consumes<double>                              (iConfig.getParameter<edm::InputTag>("pfMetPhi"));
  srcVrtx_               =  consumes<vector<Run3ScoutingVertex>>          (iConfig.getParameter<edm::InputTag>("primaryVertices"));
  srcTriggerResultsTag_  =  consumes<edm::TriggerResults>                 (iConfig.getParameter<edm::InputTag>("TriggerResultsTag"));
  l1GtToken_             =  consumes<BXVector<GlobalAlgBlk> >             (iConfig.getParameter<edm::InputTag>("l1GtSrc"));
  ptMinPF_               =  iConfig.getParameter<double>("ptMinPF");
  vtriggerSelection_     =  iConfig.getParameter<vector<string> > ("triggerSelection");
  doL1_                  =  iConfig.getParameter<bool>("doL1");
  l1Seeds_               =  iConfig.getParameter<vector<string>>("l1Seeds");
  algTag_                =  iConfig.getParameter<edm::InputTag>("l1GtSrc");
  extTag_                =  iConfig.getParameter<edm::InputTag>("l1GtSrc");
  l1GtUtils_             =  new l1t::L1TGlobalUtil(iConfig, consumesCollector(), *this, algTag_, extTag_, l1t::UseEventSetupIn::Event);

  //----- JEC:: JEC config -------
  applyJEC_              =  iConfig.getParameter<bool>("applyJEC");
  jecMode_               =  iConfig.getParameter<std::string>("jecMode");
  jecPayload_            =  iConfig.getParameter<std::string>("jecPayload");
  jecLevels_             =  iConfig.getParameter<std::vector<std::string>>("jecLevels");
  jecTxtFiles_           =  iConfig.getParameter<std::vector<std::string>>("jecTxtFiles");

  //----- JEC:: TXT-mode: per-run residual override
  jecResidualByRun_      =  iConfig.getParameter<bool>("jecResidualByRun");
  jecResidualMap_        =  iConfig.getParameter<std::vector<std::string>>("jecResidualMap");
  jecResidualCurrent_.clear();

  //----- JEC:: JEC Uncertainty config -------
  applyJECUncertainty_   =  iConfig.getParameter<bool>("applyJECUncertainty");
  jecUncTxtFile_         =  iConfig.getParameter<std::string>("jecUncTxtFile");
  jecUncFallbackToTxt_   =  iConfig.getParameter<bool>("jecUncFallbackToTxt");

  //----- JEC:: Data/MC based on isData 
  jecTxtFilesData_       =  iConfig.getParameter<std::vector<std::string>>("jecTxtFilesData");
  jecTxtFilesMC_         =  iConfig.getParameter<std::vector<std::string>>("jecTxtFilesMC");

  jecResidualMapData_    =  iConfig.getParameter<std::vector<std::string>>("jecResidualMapData");
  jecResidualMapMC_      =  iConfig.getParameter<std::vector<std::string>>("jecResidualMapMC");

  jecUncTxtFileData_     =  iConfig.getParameter<std::string>("jecUncTxtFileData");
  jecUncTxtFileMC_       =  iConfig.getParameter<std::string>("jecUncTxtFileMC");

  jetVetoMapFilesData_   =  iConfig.getParameter<std::vector<std::string>>("jetVetoMapFilesData");
  jetVetoMapFilesMC_     =  iConfig.getParameter<std::vector<std::string>>("jetVetoMapFilesMC");

  //----- JEC:: ES-mode Residual TXT fallback toggle -------
  jecResidualFallbackToTxt_ = iConfig.getParameter<bool>("jecResidualFallbackToTxt");

  //----- JEC:: Jet Veto Map config -------
  applyJetVetoMap_       =  iConfig.getParameter<bool>("applyJetVetoMap");
  jetVetoMapFiles_       =  iConfig.getParameter<std::vector<std::string>>("jetVetoMapFiles");
  vetoMapCurrentKey_.clear();

  //----- JEC:: Printing controls
  printJECInfo_          =  iConfig.getParameter<bool>("printJECInfo");
  printJECFirstNJets_    =  iConfig.getParameter<unsigned>("printJECFirstNJets");

  //----- JEC:: Build TXT corrector (file mode, no per-run residual)
  if (applyJEC_ && jecMode_ == "txt" && !jecResidualByRun_ && jecTxtFilesData_.empty()
      && jecTxtFilesMC_.empty() && !jecTxtFiles_.empty()) {
    jecCorrector_ = jec::buildTxtCorrector(jecTxtFiles_, /*residual*/"");
  }

  //----- JEC:: Pretty banner for TXT mode
  if (applyJEC_ && jecMode_=="txt" && !jecResidualByRun_ && jecTxtFilesData_.empty()
      && jecTxtFilesMC_.empty() && !jecTxtFiles_.empty()) {
    jec::log::print(jec::log::TxtConfig{
      jecMode_, jecPayload_, /*residual*/"", jecUncTxtFile_, jecLevels_, jecTxtFiles_
    });
  }

  //----- JEC:: TXT-mode uncertainty
  if (applyJECUncertainty_ && jecMode_ == "txt" && jecTxtFilesData_.empty() 
      && jecTxtFilesMC_.empty() && !jecUncTxtFile_.empty()) {
    jecUnc_ = jec::buildUncertaintyFromTxt(jecUncTxtFile_);
  }

  //----- JEC:: Prepare ES token
  if (applyJEC_ && jecMode_ == "es") {
    jecESGetToken_ = esConsumes<JetCorrectorParametersCollection, JetCorrectionsRecord>(edm::ESInputTag("", jecPayload_));
  }

  //----- Allocate pointer members before use
  jecFactorAK4_     = new vector<float>();    jecRelUncAK4_     = new vector<float>();
  jecUpFactorAK4_   = new vector<float>();    jecDownFactorAK4_ = new vector<float>();
  chEmEAK4_         = new vector<float>();    chEmFAK4_         = new vector<float>();
  neEmEAK4_         = new vector<float>();    neEmFAK4_         = new vector<float>();
  rawPtAK4_         = new vector<float>();    jetRapidityAK4_   = new vector<float>();
  ptAK4_            = new vector<float>();    etaAK4_           = new vector<float>();
  phiAK4_           = new vector<float>();    massAK4_          = new vector<float>();
  energyAK4_        = new vector<float>();    areaAK4_          = new vector<float>();
  chfAK4_           = new vector<float>();    nhfAK4_           = new vector<float>();
  phfAK4_           = new vector<float>();    elfAK4_           = new vector<float>();
  mufAK4_           = new vector<float>();    hf_hfAK4_         = new vector<float>();
  hf_emfAK4_        = new vector<float>();    hofAK4_           = new vector<float>();

  idLAK4_           = new vector<int>();      idTAK4_           = new vector<int>();
  chHadMultAK4_     = new vector<int>();      neHadMultAK4_     = new vector<int>();
  phoMultAK4_       = new vector<int>();      elMultAK4_        = new vector<int>();
  muMultAK4_        = new vector<int>();      hfHadMultAK4_     = new vector<int>();
  hfEmMultAK4_      = new vector<int>();      jetVetoMapAK4_    = new vector<int>();
  triggerResult_    = new vector<bool>();     triggerName_      = new vector<string>();
  l1Result_         = new vector<bool>();     l1Name_           = new vector<string>();
  jecLoggedOnce_    = false;

} //----- Parameter Set End


void ScoutingTreeMakerRun3::beginJob() 
{

  triggerPassHisto_ = fs_->make<TH1F>("TriggerPass", "TriggerPass", 1, 0, 1);
  triggerPassHisto_->GetXaxis()->SetCanExtend(kTRUE);

  //----- Form tree branches -------
  outTree_ = fs_->make<TTree>("events","events");
  outTree_->SetAutoSave(0); //----- Stop ROOT from writing backup cycles
  outTree_->SetAutoFlush(-20*1024*1024);   // flush/optimize every ~20 MB

  outTree_->Branch("isData"                ,&isData_             ,"isData_/I"             );
  outTree_->Branch("runNo"                 ,&run_                ,"run_/I"                );
  outTree_->Branch("evtNo"                 ,&evt_                ,"evt_/L"                );
  outTree_->Branch("lumi"                  ,&lumi_               ,"lumi_/I"               );
  outTree_->Branch("nvtx"                  ,&nVtx_               ,"nVtx_/I"               );
  outTree_->Branch("rho"                   ,&rho_                ,"rho_/F"                );
  outTree_->Branch("met"                   ,&met_                ,"met_/F"                );
  outTree_->Branch("metphi"                ,&metphi_             ,"metphi_/F"             );

  //----- Experimental MET Significance Branches
  outTree_->Branch("sumEt"                 ,&sumEt_              ,"sumEt_/F"              );
  outTree_->Branch("metSig"                ,&metSig_             ,"metSig_/F"             );
  outTree_->Branch("metOverSumEt"          ,&metOverSumEt_       ,"metOverSumEt_/F"       );
  outTree_->Branch("unclusteredEnFrac"     ,&unclusteredEnFrac_  ,"unclusteredEnFrac_/F"  );
  outTree_->Branch("minDPhiMetJet2"        ,&minDPhiMetJet2_     ,"minDPhiMetJet2_/F"     );
  outTree_->Branch("minDPhiMetJet4"        ,&minDPhiMetJet4_     ,"minDPhiMetJet4_/F"     );
  //-------------------------------

  outTree_->Branch("nPFJets"               ,&nPFJets_            ,"nPFJets_/I"            );
  outTree_->Branch("htAK4"                 ,&htAK4_              ,"htAK4_/F"              );
  outTree_->Branch("mjjAK4"                ,&mjjAK4_             ,"mjjAK4_/F"             );
  outTree_->Branch("dEtajjAK4"             ,&dEtajjAK4_          ,"dEtajjAK4_/F"          );
  outTree_->Branch("dPhijjAK4"             ,&dPhijjAK4_          ,"dPhijjAK4_/F"          );
  outTree_->Branch("jetPtAK4"              ,"vector<float>"      ,&ptAK4_                 );
  outTree_->Branch("jetRawPtAK4"           ,"vector<float>"      ,&rawPtAK4_              );
  outTree_->Branch("jetEtaAK4"             ,"vector<float>"      ,&etaAK4_                );
  outTree_->Branch("jetPhiAK4"             ,"vector<float>"      ,&phiAK4_                );
  outTree_->Branch("jetMassAK4"            ,"vector<float>"      ,&massAK4_               );
  outTree_->Branch("jetEnergyAK4"          ,"vector<float>"      ,&energyAK4_             );
  outTree_->Branch("jetAreaAK4"            ,"vector<float>"      ,&areaAK4_               );
  outTree_->Branch("jetChfAK4"             ,"vector<float>"      ,&chfAK4_                );
  outTree_->Branch("jetNhfAK4"             ,"vector<float>"      ,&nhfAK4_                );
  outTree_->Branch("jetPhfAK4"             ,"vector<float>"      ,&phfAK4_                );
  outTree_->Branch("jetMufAK4"             ,"vector<float>"      ,&mufAK4_                );
  outTree_->Branch("jetElfAK4"             ,"vector<float>"      ,&elfAK4_                );
  outTree_->Branch("jetHf_hfAK4"           ,"vector<float>"      ,&hf_hfAK4_              );
  outTree_->Branch("jetHf_emfAK4"          ,"vector<float>"      ,&hf_emfAK4_             );
  outTree_->Branch("jetHofAK4"             ,"vector<float>"      ,&hofAK4_                );
  outTree_->Branch("idTAK4"                ,"vector<int>"        ,&idTAK4_                );
  outTree_->Branch("idLAK4"                ,"vector<int>"        ,&idLAK4_                );
  outTree_->Branch("chHadMultAK4"          ,"vector<int>"        ,&chHadMultAK4_          );
  outTree_->Branch("neHadMultAK4"          ,"vector<int>"        ,&neHadMultAK4_          );
  outTree_->Branch("phoMultAK4"            ,"vector<int>"        ,&phoMultAK4_            );
  outTree_->Branch("elMultAK4"             ,"vector<int>"        ,&elMultAK4_             );
  outTree_->Branch("muMultAK4"             ,"vector<int>"        ,&muMultAK4_             );
  outTree_->Branch("hfHadMultAK4"          ,"vector<int>"        ,&hfHadMultAK4_          );
  outTree_->Branch("hfEmMultAK4"           ,"vector<int>"        ,&hfEmMultAK4_           );
  outTree_->Branch("jetJECFactorAK4"       ,"vector<float>"      ,&jecFactorAK4_          );
  outTree_->Branch("jetJECUncRelAK4"       ,"vector<float>"      ,&jecRelUncAK4_          );
  outTree_->Branch("jetJECUpFactorAK4"     ,"vector<float>"      ,&jecUpFactorAK4_        );
  outTree_->Branch("jetJECDownFactorAK4"   ,"vector<float>"      ,&jecDownFactorAK4_      );
  outTree_->Branch("jetRapidityAK4"        ,"vector<float>"      ,&jetRapidityAK4_        );

  //----- Jet veto map products (no event filtering is applied)
  outTree_->Branch("jetVetoMapAK4"         ,"vector<int>"        ,&jetVetoMapAK4_         );
  outTree_->Branch("nJetInVetoMap"         ,&nJetInVetoMap_      ,"nJetInVetoMap_/I"      );

  //----- Calculated Charged and Neutral EM Energies and Fractions
  outTree_->Branch("jetChEmEAK4"           ,"vector<float>"      ,&chEmEAK4_              );
  outTree_->Branch("jetNeEmEAK4"           ,"vector<float>"      ,&neEmEAK4_              );
  outTree_->Branch("jetChEmFAK4"           ,"vector<float>"      ,&chEmFAK4_              );
  outTree_->Branch("jetNeEmFAK4"           ,"vector<float>"      ,&neEmFAK4_              );

  //----- Trigger
  outTree_->Branch("triggerResult"         ,"vector<bool>"       ,&triggerResult_         );
  outTree_->Branch("triggerName"           ,"vector<string>"     ,&triggerName_           );

  //----- L1 branches
  outTree_->Branch("l1Result"              ,"vector<bool>"       ,&l1Result_              );
  outTree_->Branch("l1Name"                ,"vector<string>"     ,&l1Name_                );

} //----- beginJob End



void ScoutingTreeMakerRun3::analyze(const Event& iEvent, const EventSetup& iSetup)
{

  initialize();

  Handle<vector<Run3ScoutingPFJet>>   PFJets;
  iEvent.getByToken(srcPFJets_,       PFJets);
  if (!PFJets.isValid()) { outTree_->Fill(); return; } // If the PFJets product were ever absent, this avoids a hard crash.

  edm::Handle<vector<Run3ScoutingParticle>> pfcandsH;
  iEvent.getByToken(srcPFCands_, pfcandsH);

  Handle<double> rhoHandle, metHandle, metPhiHandle;
  iEvent.getByToken(srcRho_,    rhoHandle);
  iEvent.getByToken(srcMET_,    metHandle);
  iEvent.getByToken(srcMetPhi_, metPhiHandle);

  Handle<vector<Run3ScoutingVertex>> recVtxs;
  iEvent.getByToken(srcVrtx_, recVtxs);

  //-------------- Event Info -----------------------------------
  rho_      =   rhoHandle.isValid()     ?  static_cast<float>(*rhoHandle)    : -999.f;
  met_      =   metHandle.isValid()     ?  static_cast<float>(*metHandle)    : -999.f;
  metphi_   =   metPhiHandle.isValid()  ?  static_cast<float>(*metPhiHandle) : -999.f;
  nVtx_     =   recVtxs.isValid()       ?  static_cast<int>(recVtxs->size()) : 0;
  run_      =   iEvent.id().run();
  evt_      =   iEvent.id().event();
  lumi_     =   iEvent.id().luminosityBlock();
  isData_   =   int(iEvent.isRealData());


  //----- Pick once by isData and ensure TXT no-residual is prebuilt (affects FIRST event)
  if (!jecPickedByIsData_ && ( !jecTxtFilesData_.empty() || !jecTxtFilesMC_.empty() )) {
    const bool wantData = (isData_ == 1);
    const auto sel = jec::pickInputsByIsDataAndMaybePrebuildTxt(wantData, jecMode_, jecLevels_, jecTxtFilesData_, 
      jecTxtFilesMC_, jecResidualMapData_, jecResidualMapMC_, jecUncTxtFileData_, jecUncTxtFileMC_, jetVetoMapFilesData_, 
      jetVetoMapFilesMC_, applyJEC_, applyJECUncertainty_, jecCorrector_, jecUnc_, jecBannerKey_);

    jecTxtFiles_          =  sel.txtFiles;
    jecResidualMap_       =  sel.residualMap;
    jecUncTxtFile_        =  sel.uncTxtFile;
    jetVetoMapFiles_      =  sel.vetoMapFiles;
    jecResidualByRun_     =  sel.residualByRun;

    jecPickedByIsData_    =  true;

    //----- If TXT mode with no residuals
    if (applyJEC_ && jecMode_ == "txt" && !jecResidualByRun_) {
      jec::log::maybePrintTxtBanner(jecBannerKey_, jecMode_, jecPayload_, /*residual*/"", jecUncTxtFile_, jecLevels_, jecTxtFiles_);
    }
  }

  //----- Build JEC: separate JEC input-files based on 'isData'
  if (applyJEC_) {
    if (jecMode_ == "txt") {
      if (jecResidualByRun_) {
        //----- TXT mode WITH residuals
        std::string residualKey;
        const bool haveResidual = jec::pickResidualForRun(jecResidualMap_, run_, residualKey);
        const std::string cacheKey = haveResidual ? residualKey : std::string();
        const bool mustBuild = (!jecCorrector_) || (jecResidualCurrent_ != cacheKey);

        if (mustBuild) {
          jecCorrector_ = jec::buildTxtCorrector(jecTxtFiles_, residualKey);
          if (!jecCorrector_) {
            throw cms::Exception("JEC")
              << "TXT JEC build failed (run " << run_ << "). Check jecTxtFiles/jecResidualMap.";
          }
          jecResidualCurrent_ = haveResidual ? residualKey : std::string();
          jec::log::maybePrintTxtBanner(jecBannerKey_, jecMode_, jecPayload_, (haveResidual ? residualKey : ""), jecUncTxtFile_, jecLevels_, jecTxtFiles_);
          if (applyJECUncertainty_ && !jecUnc_) {
            jecUnc_ = jec::buildUncertaintyFromTxt(jecUncTxtFile_);
            if (!jecUnc_) {
              edm::LogWarning("JEC") << "[JEC] Uncertainty TXT not found or empty: " << jecUncTxtFile_;
            }
          }
        }
      }
    }
    else if (jecMode_ == "es") {
      //----- ES mode: build after dropping L2L3Residual for MC (if MC)
      const auto& coll = iSetup.getData(jecESGetToken_);

      //----- Only allow a TXT residual fallback when configured and (for DATA)
      std::string residualKey;
      const bool haveResidualTxt = jecResidualByRun_ && jec::pickResidualForRun(jecResidualMap_, run_, residualKey);
      const std::string cacheKey = haveResidualTxt ? residualKey : std::string();

      const bool mustBuild = (!jecCorrector_) || (jecResidualFallbackToTxt_ && (jecResidualCurrent_ != cacheKey));
      if (mustBuild) {
        bool usedTxtRes = false;
        jecCorrector_ = jec::buildEsCorrectorWithOptionalTxtResidual(coll, jecLevels_, haveResidualTxt ? residualKey : std::string(), 
            jecResidualFallbackToTxt_, usedTxtRes);
        if (!jecCorrector_) {
          throw cms::Exception("JEC") << "ES JEC build failed (payload=" << jecPayload_ << ").";
        }
        jecResidualCurrent_ = cacheKey;
      }

      //----- ES banner (post-pick, post-build)
      const bool wantsResidual =
          (std::find(jecLevels_.begin(), jecLevels_.end(), std::string("L2L3Residual")) != jecLevels_.end());
      bool esHasResidual = false;
      if (wantsResidual) {
        try { (void)coll["L2L3Residual"]; esHasResidual = true; } catch (...) { esHasResidual = false; }
      }

      //----- Build unc if still missing
      static bool esUncUsedTxt = false;
      if (applyJECUncertainty_ && !jecUnc_) {
        bool usedTxt = false;
        jecUnc_ = jec::buildUncertaintyEsWithOptionalTxtFallback(coll, jecUncTxtFile_, jecUncFallbackToTxt_, usedTxt);
        esUncUsedTxt = usedTxt;
        if (!jecUnc_) {
          edm::LogWarning("JEC") << "[JEC] Not found any unc in es or in txt file.";
        }
      }

      const std::string resSrc = wantsResidual
        ? (esHasResidual ? "es" : (jecResidualFallbackToTxt_ && !jecResidualCurrent_.empty() ? "txt" : "none"))
        : "n/a";

      jec::log::maybePrintEsBanner(jecBannerKey_, jecPayload_, jecLevels_, bool(jecUnc_), esUncUsedTxt, resSrc);
    }
  }

  //----- JetVeto: load/cycle map per run (no-op if 'disabled or no files')
  jetveto::ensureVetoMapReady(applyJetVetoMap_, jetVetoMapFiles_, run_, vetoMapCurrentKey_, jetVetoMap_);

  //----- SumET from PF-candidate pt (scouting has no stored sumEt)
  //----- MET Significance = MET / std::sqrt(SumET)
  //----- source: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsDP23010
  //----- source: https://github.com/cms-sw/cmssw/blob/master/DataFormats/METReco/interface/MET.h#L57
  double sumEt_val = -1.0;
  if (pfcandsH.isValid()) {
    double s = 0.0;
    for (const auto& c : *pfcandsH) {
      const float pt = c.pt();
      if (pt > 0.f) s += pt;
    }
    sumEt_val = s;
  }

  sumEt_             =  (sumEt_val >= 0.0              )  ?  static_cast<float>(sumEt_val)                       : -1.0f;
  metSig_            =  (sumEt_val > 0.0 && met_ >= 0.0)  ?  static_cast<float>(met_ / std::sqrt(sumEt_val))     : -1.0f;
  metOverSumEt_      =  (sumEt_val > 0.0 && met_ >= 0.0)  ?  static_cast<float>(met_ / sumEt_val)                : -1.0f;

  //-------------- Trigger Info -----------------------------------
  triggerPassHisto_->Fill("totalEvents", 1);

  edm::Handle<edm::TriggerResults> hltresults = iEvent.getHandle(srcTriggerResultsTag_);
  if (hltresults.isValid()) {
    const edm::TriggerNames &triggerNames_ = iEvent.triggerNames(*hltresults);
    int ntrigs = hltresults->size();
    triggerName_    ->reserve(ntrigs);
    triggerResult_  ->reserve(ntrigs);

    for (int itrig = 0; itrig != ntrigs; ++itrig) {
      const string &trigName = triggerNames_.triggerName(itrig);
      bool accept = hltresults->accept(itrig); 

      for(unsigned i=0;i<vtriggerSelection_.size();i++) {
        if(trigName.compare(0,vtriggerSelection_[i].length(),vtriggerSelection_[i])==0){
          triggerName_    ->push_back( trigName );
          triggerResult_  ->push_back( accept   );

          if(accept){ triggerPassHisto_->Fill(trigName.c_str(), 1); }

        } //----- 
      } //----- Selected trigger loop
    } //----- All HLT loop
  } //----- if hltresults valid

  //-------------- L1T (Global) --------------
  if (doL1_) {
    l1Name_->reserve(l1Seeds_.size());
    l1Result_->reserve(l1Seeds_.size());

    // Pull decisions for this event
    l1GtUtils_->retrieveL1(iEvent, iSetup, l1GtToken_);
    for (const auto& seed : l1Seeds_) {
      bool accept = false;
      l1GtUtils_->getFinalDecisionByName(seed, accept);
      l1Name_->push_back(seed);
      l1Result_->push_back(accept);
    }
  }

  //----- At least one good vertex requirement
  //if (recVtxs->size() > 0) {

  //----- Proper sorting according to the PFJet pT values.
  //----- Sort by *corrected* pT (so jet[0], jet[1] are leading/subleading after JEC)
  std::vector<float> jecCache(PFJets->size(), 1.f);
  std::vector<float> corrPt(PFJets->size(), 0.f);

  for (size_t i = 0; i < PFJets->size(); ++i) {
    const auto& j = PFJets->at(i);
    TLorentzVector vRaw; vRaw.SetPtEtaPhiM(j.pt(), j.eta(), j.phi(), j.m());

    const auto ev = jec::evaluate((applyJEC_ ? jecCorrector_.get() : nullptr), nullptr, 
      jec::CorrInput{rho_, j.jetArea(), j.pt(), j.eta(), j.phi(), float(vRaw.Energy()), nVtx_});

    jecCache[i] = ev.jec;
    corrPt[i]   = ev.pt_corr;
  }

  //----- Sort by corrected pT
  std::vector<unsigned> sortedPFJetIdx(PFJets->size());
  std::iota(sortedPFJetIdx.begin(), sortedPFJetIdx.end(), 0u);
  std::sort(sortedPFJetIdx.begin(), sortedPFJetIdx.end(),
            [&](unsigned a, unsigned b){ return corrPt[a] > corrPt[b]; });

  //----- Build the list of jets that actually pass the corrected pT cut
  std::vector<unsigned> passIdx;
  passIdx.reserve(sortedPFJetIdx.size());
  for (auto i : sortedPFJetIdx) {
    if (corrPt[i] > ptMinPF_) passIdx.push_back(i);
  }

  //----- Reserve capacity for all jet vectors once per event
  const size_t nPass = passIdx.size();
  ptAK4_          ->reserve(nPass);   etaAK4_            ->reserve(nPass);    phiAK4_    ->reserve(nPass);
  massAK4_        ->reserve(nPass);   energyAK4_         ->reserve(nPass);    areaAK4_   ->reserve(nPass);
  chfAK4_         ->reserve(nPass);   nhfAK4_            ->reserve(nPass);    phfAK4_    ->reserve(nPass);
  elfAK4_         ->reserve(nPass);   mufAK4_            ->reserve(nPass);    hf_hfAK4_  ->reserve(nPass);
  hf_emfAK4_      ->reserve(nPass);   hofAK4_            ->reserve(nPass);    rawPtAK4_  ->reserve(nPass);
  chEmEAK4_       ->reserve(nPass);   neEmEAK4_          ->reserve(nPass);
  chEmFAK4_       ->reserve(nPass);   neEmFAK4_          ->reserve(nPass);
  idLAK4_         ->reserve(nPass);   idTAK4_            ->reserve(nPass);
  chHadMultAK4_   ->reserve(nPass);   neHadMultAK4_      ->reserve(nPass);
  phoMultAK4_     ->reserve(nPass);   elMultAK4_         ->reserve(nPass);
  muMultAK4_      ->reserve(nPass);   hfHadMultAK4_      ->reserve(nPass);
  hfEmMultAK4_    ->reserve(nPass);   jecRelUncAK4_      ->reserve(nPass);
  jetVetoMapAK4_  ->reserve(nPass);   jecUpFactorAK4_    ->reserve(nPass);
  jecFactorAK4_   ->reserve(nPass);   jecDownFactorAK4_  ->reserve(nPass);

  nPFJets_ = 0;
  int vetoCount = 0;
  float htAK4 = 0.0;
  TLorentzVector vP4AK4;
  for (unsigned idx : passIdx) {
    const auto& ijet    =   PFJets->at(idx);
    float eta           =   ijet.eta(); 
    float pt_raw        =   ijet.pt();
    float phi           =   ijet.phi();
    float mass_raw      =   ijet.m();

    //----- Raw 4-vector (for fractions)
    TLorentzVector vP4Raw;
    vP4Raw.SetPtEtaPhiM(pt_raw, eta, phi, mass_raw);
    const double jet_energy_raw = vP4Raw.Energy();
    //double jet_energy_raw = ijet->photonEnergy() + ijet->electronEnergy() + ijet->muonEnergy()
    //                        + ijet->neutralHadronEnergy() + ijet->chargedHadronEnergy();

    //----- JEC factor
    float jec = jecCache[idx];  // idx is the original PFJets index

    //----- Corrected 4-vector for kinematics
    const float pt_corr   =  corrPt[idx];
    const float mass_corr =  mass_raw * jec;
    vP4AK4.SetPtEtaPhiM(pt_corr, eta, phi, mass_corr);
    const double jet_energy = vP4AK4.Energy();

    // True jet rapidity from the 4-vector: y = 0.5*ln((E + pz)/(E - pz))
    const double jet_rapidity = vP4AK4.Rapidity();

    //----- JES Uncertainty (use corrected pT for the evaluation)
    float jes_unc_rel = 0.f;
    if (applyJECUncertainty_ && jecUnc_) {
      jecUnc_->setJetEta(eta);
      jecUnc_->setJetPt(pt_corr);
      jes_unc_rel = jecUnc_->getUncertainty(true); // absolute relative uncertainty
    }

    //----- Debug: Print of what we actually applied
    const auto ev = jec::evaluate(
      (applyJEC_ ? jecCorrector_.get() : nullptr),
      (applyJECUncertainty_ ? jecUnc_.get() : nullptr),
      jec::CorrInput{rho_, ijet.jetArea(), pt_raw, eta, phi, float(jet_energy), nVtx_}
    );

    if (printJECInfo_ && printedJets_ < printJECFirstNJets_) {
      jec::log::printJet(++printedJets_, run_, lumi_, evt_,
                         eta, pt_raw, ijet.jetArea(), rho_,
                         ev.jec, ev.pt_corr, ev.jes_rel);
    }

    //----- JETID

    //----- EM energies from jet components 
    //----- Source for method: https://github.com/cms-sw/cmssw/blob/master/RecoJets/JetProducers/src/JetSpecific.cc#L277
    //----- chargedEmEnergy := electronEnergy (abs(pdgId)==11)
    //----- neutralEmEnergy := photonEnergy (pdgId==22) + eGamma (hfEmEnergy) (pdgId==2)
    double chEmE      =   ijet.electronEnergy();
    double neEmE      =   ijet.photonEnergy() + ijet.HFEMEnergy();

    //----- Fractions
    double chEF       =   ijet.chargedHadronEnergy() / jet_energy_raw;
    double nhEF       =   ijet.neutralHadronEnergy() / jet_energy_raw;
    double phoEF      =   ijet.photonEnergy()        / jet_energy_raw;
    double elEF       =   ijet.electronEnergy()      / jet_energy_raw;
    double muEF       =   ijet.muonEnergy()          / jet_energy_raw;
    double hfHadEF    =   ijet.HFHadronEnergy()      / jet_energy_raw;
    double hfEmEF     =   ijet.HFEMEnergy()          / jet_energy_raw;
    double hoEF       =   ijet.HOEnergy()            / jet_energy_raw;  
    double chEmF      =   chEmE                      / jet_energy_raw;
    double neEmF      =   neEmE                      / jet_energy_raw;

    //----- Multiplicity
    int chHadMult     =   ijet.chargedHadronMultiplicity();
    int neHadMult     =   ijet.neutralHadronMultiplicity();
    int npr           =   chHadMult + neHadMult;
    int phoMult       =   ijet.photonMultiplicity();
    int elMult        =   ijet.electronMultiplicity();
    int muMult        =   ijet.muonMultiplicity();
    int hfHadMult     =   ijet.HFHadronMultiplicity();
    int hfEmMult      =   ijet.HFEMMultiplicity();

    //----- https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID
    int idL = (chEF>0.01 && chHadMult>1 && nhEF<0.99 && npr>1 && muEF<0.80 && (neEmF+chEmF) < 0.90);
    int idT = (chEF>0.01 && chHadMult>1 && nhEF<0.90 && npr>1 && muEF<0.80 && neEmF < 0.90 && chEmF < 0.80);

    //----- Flag eta–phi in veto map (1=vetoed, 0=ok). No filtering here; only store flags.
    int inVeto = jetveto::flagFromMap(jetVetoMap_.get(), eta, phi);

    htAK4 += pt_corr;
    if (inVeto) ++vetoCount;

    ptAK4_             ->push_back(pt_corr);
    rawPtAK4_          ->push_back(pt_raw);
    phiAK4_            ->push_back(phi);
    etaAK4_            ->push_back(eta);
    massAK4_           ->push_back(mass_corr);
    energyAK4_         ->push_back(jet_energy);
    jecFactorAK4_      ->push_back(jec);
    jecRelUncAK4_      ->push_back(jes_unc_rel);
    jecUpFactorAK4_    ->push_back(1.f + jes_unc_rel);
    jecDownFactorAK4_  ->push_back(std::max(0.f, 1.f - jes_unc_rel));
    idLAK4_            ->push_back(idL);
    idTAK4_            ->push_back(idT);
    chfAK4_            ->push_back(chEF);
    nhfAK4_            ->push_back(nhEF);
    phfAK4_            ->push_back(phoEF);
    elfAK4_            ->push_back(elEF);
    mufAK4_            ->push_back(muEF);
    chHadMultAK4_      ->push_back(chHadMult);
    neHadMultAK4_      ->push_back(neHadMult);
    areaAK4_           ->push_back(ijet.jetArea());
    hf_hfAK4_          ->push_back(hfHadEF);
    hf_emfAK4_         ->push_back(hfEmEF);
    hofAK4_            ->push_back(hoEF);
    chEmEAK4_          ->push_back(chEmE);
    neEmEAK4_          ->push_back(neEmE);
    chEmFAK4_          ->push_back(chEmF);
    neEmFAK4_          ->push_back(neEmF);
    phoMultAK4_        ->push_back(phoMult);
    elMultAK4_         ->push_back(elMult);
    muMultAK4_         ->push_back(muMult);
    hfHadMultAK4_      ->push_back(hfHadMult);
    hfEmMultAK4_       ->push_back(hfEmMult);
    jetVetoMapAK4_     ->push_back(inVeto);
    jetRapidityAK4_    ->push_back(jet_rapidity);

  } //----- Jet loop

  nJetInVetoMap_     =  vetoCount;
  nPFJets_           =  static_cast<int>(ptAK4_->size());
  htAK4_             =  htAK4;
  unclusteredEnFrac_ =  (sumEt_>0.f)  ?  ((sumEt_ - htAK4_) / sumEt_) : -1.0f;

  //----- Fake-MET detection:
  //----- Compute min DeltaPhi between MET and the leading (up to N=2 and N=4) jets.
  //----- Small minDeltaPhi => MET aligned with a hard jet => likely mis-measurement/noise rather than genuine MET.
  //----- N=4 to catch ISR/FSR; N=2 for a stricter pure-dijet selection.
  //----- Sets -1 if undefined (e.g. no jets or invalid MET).
  float v2 = std::numeric_limits<float>::infinity();
  float v4 = std::numeric_limits<float>::infinity();

  if (met_ >= 0.f && !phiAK4_->empty()) {
    const size_t upto = std::min<size_t>(4, phiAK4_->size()); // already sorted by corr pT
    for (size_t i = 0; i < upto; ++i) {
      const float dphi = std::fabs(reco::deltaPhi(metphi_, (*phiAK4_)[i]));
      if (dphi < v4) v4 = dphi;
      if (i < 2 && dphi < v2) v2 = dphi;
    }
  }

  //----- If no valid jets/MET 'minDPhi = -1'
  minDPhiMetJet2_ = std::isfinite(v2) ? v2 : -1.f;
  minDPhiMetJet4_ = std::isfinite(v4) ? v4 : -1.f;

  if (ptAK4_->size() > 1) {
    //----- Find indices of the top-2 jets by *corrected* pT
    TLorentzVector j1, j2;
    j1.SetPtEtaPhiM((*ptAK4_)[0], (*etaAK4_)[0], (*phiAK4_)[0], (*massAK4_)[0]);
    j2.SetPtEtaPhiM((*ptAK4_)[1], (*etaAK4_)[1], (*phiAK4_)[1], (*massAK4_)[1]);

    mjjAK4_    = (j1 + j2).M();
    dEtajjAK4_ = std::fabs(j1.Eta() - j2.Eta());
    dPhijjAK4_ = std::fabs(j1.DeltaPhi(j2));
  }

  // } //----- vtx requirement end
  
  //----- Fill Tree ---
  outTree_->Fill();     
  //------------------

} //----- analyze End - Event Loop


void ScoutingTreeMakerRun3::initialize()
{
  isData_             = -999;
  run_                = -999;
  evt_                = -999;
  lumi_               = -999;
  nVtx_               = -999;
  rho_                = -999;
  nPFJets_            = -999;
  met_                = -999.f;
  metphi_             = -999.f;
  htAK4_              = -999.f;
  mjjAK4_             = -999.f; 
  dEtajjAK4_          = -999.f; 
  dPhijjAK4_          = -999.f;
  sumEt_              = -999.f;
  metSig_             = -999.f;
  metOverSumEt_       = -999.f;
  minDPhiMetJet2_     = -999.f;
  minDPhiMetJet4_     = -999.f;
  nJetInVetoMap_      = -999;
  ptAK4_              ->clear();
  rawPtAK4_           ->clear();
  etaAK4_             ->clear();
  phiAK4_             ->clear();
  massAK4_            ->clear();
  energyAK4_          ->clear();
  areaAK4_            ->clear();
  chfAK4_             ->clear();
  nhfAK4_             ->clear();
  phfAK4_             ->clear();
  elfAK4_             ->clear();
  mufAK4_             ->clear();
  hf_hfAK4_           ->clear();
  hf_emfAK4_          ->clear();
  hofAK4_             ->clear();
  chEmEAK4_           ->clear();
  neEmEAK4_           ->clear();
  chEmFAK4_           ->clear();
  neEmFAK4_           ->clear();
  idLAK4_             ->clear();
  idTAK4_             ->clear();
  chHadMultAK4_       ->clear();
  neHadMultAK4_       ->clear();
  phoMultAK4_         ->clear();
  triggerName_        ->clear();
  triggerResult_      ->clear();
  l1Name_             ->clear();
  l1Result_           ->clear();
  elMultAK4_          ->clear();
  muMultAK4_          ->clear();
  hfHadMultAK4_       ->clear();
  hfEmMultAK4_        ->clear();
  jecFactorAK4_       ->clear();
  jecRelUncAK4_       ->clear();
  jecUpFactorAK4_     ->clear();
  jecDownFactorAK4_   ->clear();
  jetVetoMapAK4_      ->clear();
  jetRapidityAK4_     ->clear();
  
}


void ScoutingTreeMakerRun3::endJob() 
{
  delete ptAK4_;
  delete rawPtAK4_;
  delete etaAK4_;
  delete phiAK4_;
  delete massAK4_;
  delete energyAK4_;
  delete areaAK4_;
  delete chfAK4_;
  delete nhfAK4_;
  delete phfAK4_;
  delete mufAK4_;
  delete elfAK4_;
  delete hf_hfAK4_;
  delete hf_emfAK4_;
  delete hofAK4_;
  delete chEmEAK4_;
  delete neEmEAK4_;
  delete chEmFAK4_;
  delete neEmFAK4_;
  delete idLAK4_;
  delete idTAK4_;
  delete chHadMultAK4_;
  delete neHadMultAK4_;
  delete phoMultAK4_;
  delete elMultAK4_;
  delete muMultAK4_;
  delete hfHadMultAK4_;
  delete hfEmMultAK4_;
  delete jecFactorAK4_;
  delete jecRelUncAK4_;
  delete jecUpFactorAK4_;
  delete jecDownFactorAK4_;
  delete jetVetoMapAK4_;
  delete jetRapidityAK4_;
  delete triggerResult_;
  delete triggerName_;
  delete l1Result_;
  delete l1Name_;
}


ScoutingTreeMakerRun3::~ScoutingTreeMakerRun3() 
{
}

DEFINE_FWK_MODULE(ScoutingTreeMakerRun3);



