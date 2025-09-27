// -*- C++ -*-
//
/*

 Description: Ntuple maker for Run3 scouting data set from the RAW/HLTSCOUT data-format

*/

#include "DijetScoutingRun3NTupleMaker/ScoutingTreeMakerRun3/plugins/ScoutingTreeMakerRun3.h"
#include "DijetScoutingRun3NTupleMaker/ScoutingTreeMakerRun3/plugins/JECUtils.h"


ScoutingTreeMakerRun3::ScoutingTreeMakerRun3(const edm::ParameterSet& iConfig)
{
  srcPFJets_                = consumes<vector<Run3ScoutingPFJet> >          (iConfig.getParameter<InputTag>("pfcands"));
  srcPFCands_               = consumes<vector<Run3ScoutingParticle> >       (iConfig.getParameter<InputTag>("pfcands"));
  srcRho_                   = consumes<double>                              (iConfig.getParameter<edm::InputTag>("rho"));
  srcMET_                   = consumes<double>                              (iConfig.getParameter<edm::InputTag>("pfMet"));
  srcMetPhi_                = consumes<double>                              (iConfig.getParameter<edm::InputTag>("pfMetPhi"));
  srcVrtx_                  = consumes<vector<Run3ScoutingVertex>>          (iConfig.getParameter<edm::InputTag>("primaryVertices"));
  srcTriggerResultsTag_     = consumes<edm::TriggerResults>                 (iConfig.getParameter<edm::InputTag>("TriggerResultsTag"));
  l1GtToken_                = consumes<BXVector<GlobalAlgBlk> >             (iConfig.getParameter<edm::InputTag>("l1GtSrc"));
  ptMinPF_                  = iConfig.getParameter<double>("ptMinPF");
  vtriggerSelection_        = iConfig.getParameter<vector<string> > ("triggerSelection");
  algTag_                   = iConfig.getParameter<edm::InputTag>("l1GtSrc");
  extTag_                   = iConfig.getParameter<edm::InputTag>("l1GtSrc");
  l1GtUtils_                = new l1t::L1TGlobalUtil(iConfig, consumesCollector(), *this, algTag_, extTag_, l1t::UseEventSetupIn::Event);
  isData_                   = iConfig.getParameter<bool>("isData");


  //------- JEC config -------
  applyJEC_            =   iConfig.getParameter<bool>("applyJEC");
  jecMode_             =   iConfig.getParameter<std::string>("jecMode");
  jecPayload_          =   iConfig.getParameter<std::string>("jecPayload");
  jecLevels_           =   iConfig.getParameter<std::vector<std::string>>("jecLevels");
  jecTxtFiles_         =   iConfig.getParameter<std::vector<std::string>>("jecTxtFiles");

  // TXT-mode: per-run residual override
  jecResidualByRun_    =   iConfig.getParameter<bool>("jecResidualByRun");
  jecResidualMap_      =   iConfig.getParameter<std::vector<std::string>>("jecResidualMap");
  jecResidualCurrent_.clear();


  //------- JEC Uncertainty config -------
  applyJECUncertainty_ =   iConfig.getParameter<bool>("applyJECUncertainty");
  jecUncTxtFile_       =   iConfig.getParameter<std::string>("jecUncTxtFile");

  //------- Printing controls
  printJECInfo_        =   iConfig.getParameter<bool>("printJECInfo");
  printJECFirstNJets_  =   iConfig.getParameter<unsigned>("printJECFirstNJets");

  //------- Build TXT corrector (file mode, no per-run residual)
  if (applyJEC_ && jecMode_ == "txt" && !jecResidualByRun_) {
    jecCorrector_ = jec::buildTxtCorrector(jecTxtFiles_, /*residual*/"");
  }

  //------- TXT-mode uncertainty (independent of per-run residual)
  if (applyJECUncertainty_ && jecMode_ == "txt") {
    jecUnc_ = jec::buildUncertaintyFromTxt(jecUncTxtFile_);
  }


  //------- Prepare ES token
  if (applyJEC_ && jecMode_ == "es") {
    jecESGetToken_ = esConsumes<JetCorrectorParametersCollection, JetCorrectionsRecord>(edm::ESInputTag("", jecPayload_));
  }

  
  //------- Allocate the JEC factor vector
  jecFactorAK4_ = new std::vector<float>();
  jecRelUncAK4_     = new std::vector<float>();
  jecUpFactorAK4_   = new std::vector<float>();
  jecDownFactorAK4_ = new std::vector<float>();

  //------- Allocate pointer members before use
  triggerResult_  = new vector<bool>();
  triggerName_    = new vector<string>();

  ptAK4_          = new vector<float>();    etaAK4_        =  new vector<float>();
  phiAK4_         = new vector<float>();    massAK4_       =  new vector<float>();
  energyAK4_      = new vector<float>();    areaAK4_       =  new vector<float>();
  chfAK4_         = new vector<float>();    nhfAK4_        =  new vector<float>();
  phfAK4_         = new vector<float>();    elfAK4_        =  new vector<float>();
  mufAK4_         = new vector<float>();    hf_hfAK4_      =  new vector<float>();
  hf_emfAK4_      = new vector<float>();    hofAK4_        =  new vector<float>();

  idLAK4_         = new vector<int>();      idTAK4_        =  new vector<int>();
  chHadMultAK4_   = new vector<int>();      neHadMultAK4_  =  new vector<int>();
  phoMultAK4_     = new vector<int>();      elMultAK4_     =  new vector<int>();
  muMultAK4_      = new vector<int>();      hfHadMultAK4_  =  new vector<int>();
  hfEmMultAK4_    = new vector<int>();
  jecLoggedOnce_  = false;

} //------- Parameter Set End


void ScoutingTreeMakerRun3::beginJob() 
{

  triggerPassHisto_ = fs_->make<TH1F>("TriggerPass", "TriggerPass", 1, 0, 1);
  triggerPassHisto_->GetXaxis()->SetCanExtend(kTRUE);

  //------- Form tree branches -------
  outTree_ = fs_->make<TTree>("events","events");
  outTree_->SetAutoSave(0); //------- Stop ROOT from writing backup cycles
  outTree_->SetAutoFlush(50000); //------- flush/optimize every ~50k events

  outTree_->Branch("runNo"                 ,&run_                ,"run_/I"                );
  outTree_->Branch("evtNo"                 ,&evt_                ,"evt_/L"                );
  outTree_->Branch("lumi"                  ,&lumi_               ,"lumi_/I"               );
  outTree_->Branch("nvtx"                  ,&nVtx_               ,"nVtx_/I"               );
  outTree_->Branch("rho"                   ,&rho_                ,"rho_/F"                );
  outTree_->Branch("met"                   ,&met_                ,"met_/F"                );
  outTree_->Branch("metphi"                ,&metphi_             ,"metphi_/F"             );

  //------- Experimental MET Significance Branches
  outTree_->Branch("sumEt"                 ,&sumEt_              ,"sumEt_/F"              );
  outTree_->Branch("metSig"                ,&metSig_             ,"metSig_/F"             );
  outTree_->Branch("metOverSumEt"          ,&metOverSumEt_       ,"metOverSumEt_/F"       );
  outTree_->Branch("unclusteredEnFrac"     ,&unclusteredEnFrac_  ,"unclusteredEnFrac_/F"  );
  outTree_->Branch("minDPhiMetJet2"        ,&minDPhiMetJet2_     , "minDPhiMetJet2_/F"    );
  outTree_->Branch("minDPhiMetJet4"        ,&minDPhiMetJet4_     , "minDPhiMetJet4_/F"    );
  //-------

  outTree_->Branch("nPFJets"               ,&nPFJets_            ,"nPFJets_/I"            );
  outTree_->Branch("htAK4"                 ,&htAK4_              ,"htAK4_/F"              );
  outTree_->Branch("mjjAK4"                ,&mjjAK4_             ,"mjjAK4_/F"             );
  outTree_->Branch("dEtajjAK4"             ,&dEtajjAK4_          ,"dEtajjAK4_/F"          );
  outTree_->Branch("dPhijjAK4"             ,&dPhijjAK4_          ,"dPhijjAK4_/F"          );
  outTree_->Branch("jetPtAK4"              ,"vector<float>"      ,&ptAK4_                 );
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

  //------- Trigger
  outTree_->Branch("triggerResult"         ,"vector<bool>"       ,&triggerResult_         );
  outTree_->Branch("triggerName"           ,"vector<string>"     ,&triggerName_           );

} //------- beginJob End


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

  //------- TXT-mode: (re)build corrector with per-run Residual override
  if (applyJEC_ && jecMode_ == "txt" && jecResidualByRun_) {
    std::string residualKey;
    const bool haveResidual = jec::pickResidualForRun(jecResidualMap_, iEvent.id().run(), residualKey);
    const std::string cacheKey = haveResidual ? residualKey : std::string();
    const bool mustBuild = (!jecCorrector_) || (jecResidualCurrent_ != cacheKey);

    if (mustBuild) {
      jecCorrector_ = jec::buildTxtCorrector(jecTxtFiles_, residualKey);
      if (!jecCorrector_) {
        throw cms::Exception("JEC")
          << "TXT JEC build: no parameters after applying per-run residual logic "
          << "(run " << iEvent.id().run() << "). Check jecTxtFiles/jecResidualMap.";
      }
      jecResidualCurrent_ = cacheKey;

      if (!jecLoggedOnce_) {
        jecLoggedOnce_ = true;
        edm::LogInfo("JEC") << "TXT JEC loaded with levels: "
                            << jec::joinLevels(jecLevels_)
                            << (haveResidual ? (std::string(" | Residual(TXT): ") + residualKey)
                                             : " | Residual: (none)");
      }
    }
  }
  
  //------- Build the ES-corrector (jecMode_ == "es")
  if (applyJEC_ && jecMode_ == "es" && !jecCorrector_) {
    const auto& coll = iSetup.getData(jecESGetToken_);
    jecCorrector_ = jec::buildEsCorrector(coll, jecLevels_);
  }

  if (!jecLoggedOnce_ && jecCorrector_) {
    jecLoggedOnce_ = true;
    edm::LogInfo("JEC") << "ES JEC loaded for payload: " << jecPayload_
                        << " with levels: " << jec::joinLevels(jecLevels_);
  }

  //------- Build JES uncertainty from ES (if available)
  if (applyJECUncertainty_ && jecMode_ == "es" && !jecUnc_) {
    const auto& coll = iSetup.getData(jecESGetToken_);
    jecUnc_ = jec::buildUncertaintyFromEs(coll);
    static bool warned = false;
    if (!jecUnc_ && !warned) {
      warned = true;
      edm::LogInfo("JEC") << "No ES 'Uncertainty' payload for " << jecPayload_
                          << ". Provide jecUncTxtFile or switch jecMode='txt'.";
    }
  }

  //------- Reserve capacity for all jet vectors once per event
  const size_t nj = PFJets->size();
  ptAK4_          ->reserve(nj);   etaAK4_        ->reserve(nj);    phiAK4_    ->reserve(nj);
  massAK4_        ->reserve(nj);   energyAK4_     ->reserve(nj);    areaAK4_   ->reserve(nj);
  chfAK4_         ->reserve(nj);   nhfAK4_        ->reserve(nj);    phfAK4_    ->reserve(nj);
  elfAK4_         ->reserve(nj);   mufAK4_        ->reserve(nj);    hf_hfAK4_  ->reserve(nj);
  hf_emfAK4_      ->reserve(nj);   hofAK4_        ->reserve(nj);
  idLAK4_         ->reserve(nj);   idTAK4_        ->reserve(nj);
  chHadMultAK4_   ->reserve(nj);   neHadMultAK4_  ->reserve(nj);
  phoMultAK4_     ->reserve(nj);   elMultAK4_     ->reserve(nj);
  muMultAK4_      ->reserve(nj);   hfHadMultAK4_  ->reserve(nj);
  hfEmMultAK4_    ->reserve(nj);

  //-------------- Event Info -----------------------------------
  rho_      =   rhoHandle.isValid()     ?  static_cast<float>(*rhoHandle)    : -999.f;
  met_      =   metHandle.isValid()     ?  static_cast<float>(*metHandle)    : -999.f;
  metphi_   =   metPhiHandle.isValid()  ?  static_cast<float>(*metPhiHandle) : -999.f;
  nVtx_     =   recVtxs.isValid()       ?  static_cast<int>(recVtxs->size()) : 0;
  run_      =   iEvent.id().run();
  evt_      =   iEvent.id().event();
  lumi_     =   iEvent.id().luminosityBlock();

  //------- SumET from PF-candidate pt (scouting has no stored sumEt)
  //------- MET Significance = MET / std::sqrt(SumET)
  //------- source: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsDP23010
  //------- source: https://github.com/cms-sw/cmssw/blob/master/DataFormats/METReco/interface/MET.h#L57
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

        } //------- 
      } //------- Selected trigger loop
    } //------- All HLT loop
  } //------- if hltresults valid

  //----- At least one good vertex requirement
  //if (recVtxs->size() > 0) {

  //------- Proper sorting according to the PFJet pT values.
  vector<unsigned> sortedPFJetIdx(PFJets->size());
  iota(sortedPFJetIdx.begin(), sortedPFJetIdx.end(), 0u);  // 0,1,2,...,N-1
  sort(sortedPFJetIdx.begin(), sortedPFJetIdx.end(),
            [&](unsigned a, unsigned b){
              return PFJets->at(a).pt() > PFJets->at(b).pt();  // sort by pT (desc)
            });

  nPFJets_ = 0;
  float htAK4 = 0.0;
  TLorentzVector vP4AK4;
  for (unsigned idx : sortedPFJetIdx) { 
    const auto& ijet    =   PFJets->at(idx);
    float eta           =   ijet.eta(); 
    float pt_raw        =   ijet.pt();
    float phi           =   ijet.phi();
    float mass_raw      =   ijet.m();

    //----- Raw 4-vector (for fractions)
    TLorentzVector vP4Raw;
    vP4Raw.SetPtEtaPhiM(pt_raw, eta, phi, mass_raw);
    const double jet_energy_raw = vP4Raw.Energy();

    //----- JEC factor
    double jec = 1.0;
    if (applyJEC_ && jecCorrector_) {
      jecCorrector_->setRho(std::max(0.f, rho_));
      jecCorrector_->setJetA(ijet.jetArea());
      jecCorrector_->setJetPt(pt_raw);
      jecCorrector_->setJetEta(eta);
      jecCorrector_->setJetPhi(phi);
      jecCorrector_->setJetE(vP4Raw.Energy());
      if (nVtx_ >= 0) jecCorrector_->setNPV(nVtx_);
      jec = jecCorrector_->getCorrection();
    }

    //----- Corrected 4-vector for kinematics
    const float pt_corr   =  pt_raw   * jec;
    const float mass_corr =  mass_raw * jec;
    vP4AK4.SetPtEtaPhiM(pt_corr, eta, phi, mass_corr);
    const double jet_energy = vP4AK4.Energy();


    //----- JES Uncertainty (use corrected pT for the evaluation)
    float jes_unc_rel = 0.f;
    if (applyJECUncertainty_ && jecUnc_) {
      jecUnc_->setJetEta(eta);
      jecUnc_->setJetPt(pt_corr);
      jes_unc_rel = jecUnc_->getUncertainty(true); // absolute relative uncertainty
    }

    //----- Debug: Print of what we actually applied
    static unsigned jecPrintedJets = 0;
    if (printJECInfo_ && jecPrintedJets < printJECFirstNJets_) {
      ++jecPrintedJets;
      edm::LogVerbatim("JEC")
        << "run:lumi:evt " << run_ << ":" << lumi_ << ":" << evt_
        << " | jet#" << jecPrintedJets
        << " | eta=" << eta
        << " pt_raw=" << pt_raw
        << " area=" << ijet.jetArea()
        << " rho=" << std::max(0.f, rho_)
        << " | JEC=" << jec
        << " pt_corr=" << pt_corr
        << " | JES_rel=" << jes_unc_rel
        << " upFactor=" << (1.f + jes_unc_rel)
        << " downFactor=" << std::max(0.f, 1.f - jes_unc_rel);
    }

    //----- JETID
    double chE_frac     =   ijet.chargedHadronEnergy() / jet_energy_raw;
    double nhE_frac     =   ijet.neutralHadronEnergy() / jet_energy_raw;
    double phoE_frac    =   ijet.photonEnergy()        / jet_energy_raw;
    double elE_frac     =   ijet.electronEnergy()      / jet_energy_raw;
    double muE_frac     =   ijet.muonEnergy()          / jet_energy_raw;

    double hfHadE_frac  =   ijet.HFHadronEnergy()      / jet_energy_raw;
    double hfEmE_frac   =   ijet.HFEMEnergy()          / jet_energy_raw;
    double hoE_frac     =   ijet.HOEnergy()            / jet_energy_raw;


    int chHadMult       =   ijet.chargedHadronMultiplicity();
    int neHadMult       =   ijet.neutralHadronMultiplicity();
    int npr             =   chHadMult + neHadMult;
    int phoMult         =   ijet.photonMultiplicity();
    int elMult          =   ijet.electronMultiplicity();
    int muMult          =   ijet.muonMultiplicity();
    int hfHadMult       =   ijet.HFHadronMultiplicity();
    int hfEmMult        =   ijet.HFEMMultiplicity();
    

    //------- https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID
    int idL = (chE_frac<0.99 && nhE_frac<0.99 && npr>1 && muE_frac<0.99);
    int idT = (chE_frac<0.99 && nhE_frac<0.90 && npr>1 && muE_frac<0.99);

    if (pt_corr > ptMinPF_) {
      htAK4 += pt_corr;

      ptAK4_                 ->push_back(pt_corr);
      phiAK4_                ->push_back(phi);
      etaAK4_                ->push_back(eta);
      massAK4_               ->push_back(mass_corr);
      energyAK4_             ->push_back(jet_energy);
      jecFactorAK4_          ->push_back(static_cast<float>(jec));
      jecRelUncAK4_          ->push_back(jes_unc_rel);
      jecUpFactorAK4_        ->push_back(1.f + jes_unc_rel);
      jecDownFactorAK4_      ->push_back(std::max(0.f, 1.f - jes_unc_rel));
      idLAK4_                ->push_back(idL);
      idTAK4_                ->push_back(idT);
      chfAK4_                ->push_back(chE_frac);
      nhfAK4_                ->push_back(nhE_frac);
      phfAK4_                ->push_back(phoE_frac);
      elfAK4_                ->push_back(elE_frac);
      mufAK4_                ->push_back(muE_frac);
      chHadMultAK4_          ->push_back(chHadMult);
      neHadMultAK4_          ->push_back(neHadMult);
      areaAK4_               ->push_back(ijet.jetArea());
      hf_hfAK4_              ->push_back(hfHadE_frac);
      hf_emfAK4_             ->push_back(hfEmE_frac);
      hofAK4_                ->push_back(hoE_frac);
      phoMultAK4_            ->push_back(phoMult);
      elMultAK4_             ->push_back(elMult);
      muMultAK4_             ->push_back(muMult);
      hfHadMultAK4_          ->push_back(hfHadMult);
      hfEmMultAK4_           ->push_back(hfEmMult);

    }

  } //------- Jet loop

  nPFJets_           =  static_cast<int>(ptAK4_->size());
  htAK4_             =  htAK4;
  unclusteredEnFrac_ =  (sumEt_>0.f)  ?  static_cast<float>((sumEt_ - htAK4_) / sumEt_) : -1.0f;

  //------- Fake-MET detection:
  //------- Compute min DeltaPhi between MET and the leading (up to N=2 and N=4) jets.
  //------- Small minDeltaPhi => MET aligned with a hard jet => likely mis-measurement/noise rather than genuine MET.
  //------- N=4 to catch ISR/FSR; N=2 for a stricter pure-dijet selection.
  //------- Sets -1 if undefined (e.g. no jets or invalid MET).
  float v2 = std::numeric_limits<float>::infinity();
  float v4 = std::numeric_limits<float>::infinity();

  if (met_ >= 0.f && !phiAK4_->empty()) {
    // build indices 0..N-1 sorted by corrected pT (desc)
    std::vector<size_t> idx(ptAK4_->size());
    std::iota(idx.begin(), idx.end(), 0u);
    std::sort(idx.begin(), idx.end(), [&](size_t a, size_t b){ return (*ptAK4_)[a] > (*ptAK4_)[b]; });

    const size_t upto = std::min<size_t>(4, idx.size());
    for (size_t r = 0; r < upto; ++r) {
      const size_t i = idx[r];
      const float dphi = std::fabs(reco::deltaPhi(metphi_, (*phiAK4_)[i]));
      if (dphi < v4) v4 = dphi;
      if (r < 2 && dphi < v2) v2 = dphi;
    }
  }

  //------- If no valid jets/MET 'minDPhi = -1'
  minDPhiMetJet2_ = std::isfinite(v2) ? v2 : -1.f;
  minDPhiMetJet4_ = std::isfinite(v4) ? v4 : -1.f;

  if (ptAK4_->size() > 1) {
    // find indices of the top-2 jets by *corrected* pT
    size_t i1 = 0, i2 = 1;
    if ((*ptAK4_)[i2] > (*ptAK4_)[i1]) std::swap(i1, i2);
    for (size_t i = 2; i < ptAK4_->size(); ++i) {
      if ((*ptAK4_)[i] > (*ptAK4_)[i1]) { i2 = i1; i1 = i; }
      else if ((*ptAK4_)[i] > (*ptAK4_)[i2]) { i2 = i; }
    }

    TLorentzVector j1, j2;
    j1.SetPtEtaPhiM((*ptAK4_)[i1], (*etaAK4_)[i1], (*phiAK4_)[i1], (*massAK4_)[i1]);
    j2.SetPtEtaPhiM((*ptAK4_)[i2], (*etaAK4_)[i2], (*phiAK4_)[i2], (*massAK4_)[i2]);
    mjjAK4_    = (j1 + j2).M();
    dEtajjAK4_ = std::fabs(j1.Eta() - j2.Eta());
    dPhijjAK4_ = std::fabs(j1.DeltaPhi(j2));
  }

  // } //------- vtx requirement end
  
  //---- Fill Tree ---
  outTree_->Fill();     
  //------------------

} // analyze End - Event Loop


void ScoutingTreeMakerRun3::initialize()
{
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
  ptAK4_              ->clear();
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
  idLAK4_             ->clear();
  idTAK4_             ->clear();
  chHadMultAK4_       ->clear();
  neHadMultAK4_       ->clear();
  phoMultAK4_         ->clear();
  triggerName_        ->clear();
  triggerResult_      ->clear();
  elMultAK4_          ->clear();
  muMultAK4_          ->clear();
  hfHadMultAK4_       ->clear();
  hfEmMultAK4_        ->clear();
  jecFactorAK4_       ->clear();
  jecRelUncAK4_       ->clear();
  jecUpFactorAK4_     ->clear();
  jecDownFactorAK4_   ->clear();
  
}


void ScoutingTreeMakerRun3::endJob() 
{  
  delete triggerResult_;
  delete triggerName_;
  delete ptAK4_;
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

}


ScoutingTreeMakerRun3::~ScoutingTreeMakerRun3() 
{
}

DEFINE_FWK_MODULE(ScoutingTreeMakerRun3);

