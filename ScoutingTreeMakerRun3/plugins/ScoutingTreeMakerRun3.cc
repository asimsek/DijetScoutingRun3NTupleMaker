// -*- C++ -*-
//
/*

 Description: Ntuple maker for Run3 scouting data set from the RAW/HLTSCOUT data-format

*/

#include "DijetScoutingRun3NTupleMaker/ScoutingTreeMakerRun3/plugins/ScoutingTreeMakerRun3.h"


ScoutingTreeMakerRun3::ScoutingTreeMakerRun3(const edm::ParameterSet& iConfig)
{
  srcPFJets_                = consumes<vector<Run3ScoutingPFJet> >          (iConfig.getParameter<InputTag>("pfjets"));
  srcRho_                   = consumes<double>                              (iConfig.getParameter<edm::InputTag>("rho"));
  srcMET_                   = consumes<double>                              (iConfig.getParameter<edm::InputTag>("pfMet"));
  srcMetPhi_                = consumes<double>                              (iConfig.getParameter<edm::InputTag>("pfMetPhi"));
  srcVrtx_                  = consumes<vector<Run3ScoutingVertex>>          (iConfig.getParameter<edm::InputTag>("primaryVertices"));
  srcTriggerResultsTag_     = consumes<edm::TriggerResults>                 (iConfig.getParameter<edm::InputTag>("TriggerResultsTag"));
  l1GtToken_                = consumes<BXVector<GlobalAlgBlk> >             (iConfig.getParameter<edm::InputTag>("l1GtSrc"));
  ptMinPF_                  = iConfig.getParameter<double>("ptMinPF");
  vtriggerSelection_        = iConfig.getParameter<std::vector<std::string> > ("triggerSelection");
  algTag_                   = iConfig.getParameter<edm::InputTag>("l1GtSrc");
  extTag_                   = iConfig.getParameter<edm::InputTag>("l1GtSrc");
  l1GtUtils_                = new l1t::L1TGlobalUtil(iConfig, consumesCollector(), *this, algTag_, extTag_, l1t::UseEventSetupIn::Event);
  isData_                   = iConfig.getParameter<bool>("isData");

  // Allocate pointer members before use
  triggerResult_  = new std::vector<bool>();
  triggerName_    = new std::vector<std::string>();

  ptAK4_          = new std::vector<float>();  etaAK4_ = new std::vector<float>();
  phiAK4_         = new std::vector<float>();  massAK4_ = new std::vector<float>();
  energyAK4_      = new std::vector<float>();  areaAK4_ = new std::vector<float>();
  chfAK4_         = new std::vector<float>();  nhfAK4_ = new std::vector<float>();
  phfAK4_         = new std::vector<float>();  elfAK4_ = new std::vector<float>();
  mufAK4_         = new std::vector<float>();  hf_hfAK4_ = new std::vector<float>();
  hf_emfAK4_      = new std::vector<float>();  hofAK4_ = new std::vector<float>();

  idLAK4_         = new std::vector<int>();    idTAK4_ = new std::vector<int>();
  chHadMultAK4_   = new std::vector<int>();    neHadMultAK4_ = new std::vector<int>();
  phoMultAK4_     = new std::vector<int>();    elMultAK4_ = new std::vector<int>();
  muMultAK4_      = new std::vector<int>();    hfHadMultAK4_ = new std::vector<int>();
  hfEmMultAK4_    = new std::vector<int>();


} //------- Parameter Set End



void ScoutingTreeMakerRun3::beginJob() 
{
  triggerPassHisto_ = fs_->make<TH1F>("TriggerPass", "TriggerPass", 1, 0, 1);
  
  //------- form tree branches -----------------------
  outTree_ = fs_->make<TTree>("events","events");
  outTree_->SetAutoSave(0); // Stop ROOT from writing backup cycles
  //outTree_->SetAutoFlush(2000); // flush/optimize every ~2000 events
  outTree_->Branch("runNo"                    ,&run_               ,"run_/I"               );
  outTree_->Branch("evtNo"                    ,&evt_               ,"evt_/L"               );
  outTree_->Branch("lumi"                     ,&lumi_              ,"lumi_/I"              );
  outTree_->Branch("nvtx"                     ,&nVtx_              ,"nVtx_/I"              );
  outTree_->Branch("rho"                      ,&rho_               ,"rho_/F"               );
  outTree_->Branch("met"                      ,&met_               ,"met_/F"               );
  outTree_->Branch("metphi"                   ,&metphi_            ,"metphi_/F"            );
  outTree_->Branch("nPFJets"                  ,&nPFJets_           ,"nPFJets_/I"           );
  outTree_->Branch("htAK4"                    ,&htAK4_             ,"htAK4_/F"             );
  outTree_->Branch("mjjAK4"                   ,&mjjAK4_            ,"mjjAK4_/F"            );
  outTree_->Branch("dEtajjAK4"                ,&dEtajjAK4_         ,"dEtajjAK4_/F"         );
  outTree_->Branch("dPhijjAK4"                ,&dPhijjAK4_         ,"dPhijjAK4_/F"         );
  outTree_->Branch("jetPtAK4"                 ,"vector<float>"     ,&ptAK4_                );
  outTree_->Branch("jetEtaAK4"                ,"vector<float>"     ,&etaAK4_               );
  outTree_->Branch("jetPhiAK4"                ,"vector<float>"     ,&phiAK4_               );
  outTree_->Branch("jetMassAK4"               ,"vector<float>"     ,&massAK4_              );
  outTree_->Branch("jetEnergyAK4"             ,"vector<float>"     ,&energyAK4_            );
  outTree_->Branch("jetAreaAK4"               ,"vector<float>"     ,&areaAK4_              );
  outTree_->Branch("jetChfAK4"                ,"vector<float>"     ,&chfAK4_               );
  outTree_->Branch("jetNhfAK4"                ,"vector<float>"     ,&nhfAK4_               );
  outTree_->Branch("jetPhfAK4"                ,"vector<float>"     ,&phfAK4_               );
  outTree_->Branch("jetMufAK4"                ,"vector<float>"     ,&mufAK4_               );
  outTree_->Branch("jetElfAK4"                ,"vector<float>"     ,&elfAK4_               );
  outTree_->Branch("jetHf_hfAK4"              ,"vector<float>"     ,&hf_hfAK4_             );
  outTree_->Branch("jetHf_emfAK4"             ,"vector<float>"     ,&hf_emfAK4_            );
  outTree_->Branch("jetHofAK4"                ,"vector<float>"     ,&hofAK4_               );
  outTree_->Branch("idTAK4"                   ,"vector<int>"       ,&idTAK4_               );
  outTree_->Branch("idLAK4"                   ,"vector<int>"       ,&idLAK4_               );
  outTree_->Branch("chHadMultAK4"             ,"vector<int>"       ,&chHadMultAK4_         );
  outTree_->Branch("neHadMultAK4"             ,"vector<int>"       ,&neHadMultAK4_         );
  outTree_->Branch("phoMultAK4"               ,"vector<int>"       ,&phoMultAK4_           );
  outTree_->Branch("elMultAK4"                ,"vector<int>"       ,&elMultAK4_            );
  outTree_->Branch("muMultAK4"                ,"vector<int>"       ,&muMultAK4_            );
  outTree_->Branch("hfHadMultAK4"             ,"vector<int>"       ,&hfHadMultAK4_         );
  outTree_->Branch("hfEmMultAK4"              ,"vector<int>"       ,&hfEmMultAK4_          );


  //------------------------------------------------------------------
  outTree_->Branch("triggerResult"            ,"vector<bool>"      ,&triggerResult_        );
  outTree_->Branch("triggerName"              ,"vector<string>"    ,&triggerName_          );


} //------- beginJob End


void ScoutingTreeMakerRun3::analyze(const Event& iEvent, const EventSetup& iSetup)
{

  initialize();

  Handle<vector<Run3ScoutingPFJet>>   PFJets;
  iEvent.getByToken(srcPFJets_,       PFJets);

  Handle<double> rhoHandle, metHandle, metPhiHandle;
  iEvent.getByToken(srcRho_,    rhoHandle);
  iEvent.getByToken(srcMET_,    metHandle);
  iEvent.getByToken(srcMetPhi_, metPhiHandle);

  Handle<vector<Run3ScoutingVertex>> recVtxs;
  iEvent.getByToken(srcVrtx_, recVtxs);

  //-------------- Event Info -----------------------------------
  rho_      =   rhoHandle.isValid()    ? static_cast<float>(*rhoHandle)    : -999.f;
  met_      =   metHandle.isValid()    ? static_cast<float>(*metHandle)    : -999.f;
  metphi_   =   metPhiHandle.isValid() ? static_cast<float>(*metPhiHandle) : -999.f;
  nVtx_     =   recVtxs.isValid()      ?  static_cast<int>(recVtxs->size()): 0;
  run_      =   iEvent.id().run();
  evt_      =   iEvent.id().event();
  lumi_     =   iEvent.id().luminosityBlock();

  //-------------- Trigger Info -----------------------------------
  triggerPassHisto_->Fill("totalEvents", 1);

  edm::Handle<edm::TriggerResults> hltresults = iEvent.getHandle(srcTriggerResultsTag_);
  if (hltresults.isValid()) {
    const edm::TriggerNames &triggerNames_ = iEvent.triggerNames(*hltresults);
    int ntrigs = hltresults->size();

    for (int itrig = 0; itrig != ntrigs; ++itrig) {
      const string &trigName = triggerNames_.triggerName(itrig);
      bool accept = hltresults->accept(itrig); 
      //cout << trigName << endl;

      for(unsigned i=0;i<vtriggerSelection_.size();i++) {
        if(trigName.compare(0,vtriggerSelection_[i].length(),vtriggerSelection_[i])==0){
          //cout << "trig = " << trigName << ", pass = " << accept << endl;
          triggerName_    ->push_back( trigName );
          triggerResult_  ->push_back( accept   );

          if(accept){ triggerPassHisto_->Fill(trigName.c_str(), 1); }

        } //------- 
      } //------- Selected trigger loop
    } //------- All HLT loop
  } //------- if hltresults valid

  //----- At least one good vertex requirement
  //if (recVtxs->size() > 0) {

  std::vector<unsigned> sortedAK4JetIdx;
  for(auto ijet = PFJets->begin();ijet != PFJets->end(); ++ijet)
  {
    sortedAK4JetIdx.push_back(ijet - PFJets->begin());
  }

  nPFJets_ = 0;
  float htAK4 = 0.0;
  TLorentzVector vP4AK4;
  for(auto i = sortedAK4JetIdx.begin(); i != sortedAK4JetIdx.end(); ++i) {

    auto ijet           =   (PFJets->begin() + *i);
    float eta           =   ijet->eta(); 
    float pt            =   ijet->pt();
    float phi           =   ijet->phi();
    float mass          =   ijet->m();
    
    vP4AK4.SetPtEtaPhiM(pt, eta, phi, mass);
    double jet_energy   =  vP4AK4.Energy();
    //double jet_energy   =   ijet->HOEnergy() + ijet->HFHadronEnergy() + ijet->HFEMEnergy(); // No "EE, EB, HE" information in the scouting stream
    //---- just testing an idea: https://pdg.lbl.gov/2018/reviews/rpp2018-rev-kinematics.pdf (E^2=p^2+m^2)
    //double p = pt * cosh(eta);
    //double jet_energy = std::sqrt(p*p + mass*mass);

    //----- JETID
    double chE_frac     =   ijet->chargedHadronEnergy() / jet_energy;
    double nhE_frac     =   ijet->neutralHadronEnergy() / jet_energy;
    double phoE_frac    =   ijet->photonEnergy()        / jet_energy;
    double elE_frac     =   ijet->electronEnergy()      / jet_energy;
    double muE_frac     =   ijet->muonEnergy()          / jet_energy;

    double hfHadE_frac  =   ijet->HFHadronEnergy()      / jet_energy;
    double hfEmE_frac   =   ijet->HFEMEnergy()          / jet_energy;
    double hoE_frac     =   ijet->HOEnergy()            / jet_energy;

    int chHadMult       =   ijet->chargedHadronMultiplicity();
    int neHadMult       =   ijet->neutralHadronMultiplicity();
    int npr             =   chHadMult + neHadMult;
    int phoMult         =   ijet->photonMultiplicity();
    int elMult          =   ijet->electronMultiplicity();
    int muMult          =   ijet->muonMultiplicity();
    int hfHadMult       =   ijet->HFHadronMultiplicity();
    int hfEmMult        =   ijet->HFEMMultiplicity();
    

    //------- https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID
    int idL = (chE_frac<0.99 && nhE_frac<0.99 && npr>1 && muE_frac<0.99);
    int idT = (chE_frac<0.99 && nhE_frac<0.90 && npr>1 && muE_frac<0.99);

    if(pt > ptMinPF_) {
      htAK4 += pt;
      nPFJets_++;

      ptAK4_                 ->push_back(pt);
      phiAK4_                ->push_back(phi);
      etaAK4_                ->push_back(eta);
      massAK4_               ->push_back(mass);
      energyAK4_             ->push_back(jet_energy);
      idLAK4_                ->push_back(idL);
      idTAK4_                ->push_back(idT);
      chfAK4_                ->push_back(chE_frac);
      nhfAK4_                ->push_back(nhE_frac);
      phfAK4_                ->push_back(phoE_frac);
      elfAK4_                ->push_back(elE_frac);
      mufAK4_                ->push_back(muE_frac);
      chHadMultAK4_          ->push_back(chHadMult);
      neHadMultAK4_          ->push_back(neHadMult);
      areaAK4_               ->push_back(ijet->jetArea());
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

  htAK4_       =   htAK4;

  if (nPFJets_ > 1) { //------- Assuming jets are ordered by pt in the collection

    mjjAK4_    =   fabs((*massAK4_)[0] + (*massAK4_)[1]);
    dEtajjAK4_ =   fabs((*etaAK4_)[0]  - (*etaAK4_)[1]); 
    dPhijjAK4_ =   fabs(deltaPhi((*phiAK4_)[0], (*phiAK4_)[1]));

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
  met_                = -999;
  metphi_             = -999;
  nPFJets_            = -999;
  htAK4_              = -999;
  mjjAK4_             = -999; 
  dEtajjAK4_          = -999; 
  dPhijjAK4_          = -999;
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
}


ScoutingTreeMakerRun3::~ScoutingTreeMakerRun3() 
{
}

DEFINE_FWK_MODULE(ScoutingTreeMakerRun3);

