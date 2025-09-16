#ifndef ScoutingTreeMakerRun3_h
#define ScoutingTreeMakerRun3_h


#include <memory>
#include <iostream>
#include <sstream>
#include <istream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
#include <functional>
#include <vector>
#include <cassert>
#include <TTree.h>
#include <TLorentzVector.h>
#include "TFile.h"
#include "TH1D.h"
#include "TH1F.h"
#include "TMath.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionData.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionEvaluator.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionParser.h"
#include "L1Trigger/L1TGlobal/interface/L1TGlobalUtil.h"
#include "DataFormats/JetReco/interface/Jet.h"

// JEC
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"

// Trigger 
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"

// Scouting
#include "DataFormats/Scouting/interface/Run3ScoutingElectron.h"
#include "DataFormats/Scouting/interface/Run3ScoutingPhoton.h"
#include "DataFormats/Scouting/interface/Run3ScoutingPFJet.h"
#include "DataFormats/Scouting/interface/Run3ScoutingVertex.h"
#include "DataFormats/Scouting/interface/Run3ScoutingTrack.h"
#include "DataFormats/Scouting/interface/Run3ScoutingMuon.h"
#include "DataFormats/Scouting/interface/Run3ScoutingParticle.h"


#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "DataFormats/L1Trigger/interface/BXVector.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"


using namespace std;
using namespace reco;
using namespace pat;
using namespace edm;


class ScoutingTreeMakerRun3 : public edm::one::EDAnalyzer<>
{
  public:
    typedef reco::Particle::LorentzVector LorentzVector;
    explicit ScoutingTreeMakerRun3(edm::ParameterSet const& iConfig);
    virtual void beginJob();
    virtual void analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup);
    virtual void endJob();
    virtual ~ScoutingTreeMakerRun3();

  private:
    void initialize();
    //---- configurable parameters --------   
    double ptMinPF_;
    bool isData_;

    edm::EDGetTokenT<vector<Run3ScoutingPFJet>> srcPFJets_;

    edm::EDGetTokenT<double> srcRho_;
    edm::EDGetTokenT<double> srcMET_;
    edm::EDGetTokenT<double> srcMetPhi_;
    edm::EDGetTokenT<vector<Run3ScoutingVertex> > srcVrtx_;
    
    edm::EDGetTokenT<edm::TriggerResults> srcTriggerResultsTag_;
    edm::EDGetTokenT<BXVector<GlobalAlgBlk>> l1GtToken_;

    l1t::L1TGlobalUtil* l1GtUtils_;
    edm::InputTag  algTag_, extTag_;

    edm::Service<TFileService> fs_;
    TTree *outTree_;

    //---- TRIGGER -------------------------
    std::vector<std::string> vtriggerSelection_;
    TH1F *triggerPassHisto_, *triggerNamesHisto_;
    //---- output TREE variables ------
    //---- global event variables -----
    int   run_,nVtx_,lumi_;
    long int evt_;
    int   nPFJets_;
    float rho_, met_, metphi_;
    float htAK4_, mjjAK4_, dEtajjAK4_, dPhijjAK4_;
    std::vector<bool> *triggerResult_;
    std::vector<std::string> *triggerName_;


    //---- jet and genJet variables --------------
    std::vector<float> *ptAK4_, *etaAK4_, *phiAK4_, *massAK4_, *energyAK4_, *areaAK4_, *chfAK4_, *nhfAK4_, *phfAK4_, *elfAK4_, *mufAK4_;
    std::vector<int> *idLAK4_, *idTAK4_, *chHadMultAK4_, *neHadMultAK4_, *phoMultAK4_;
    std::vector<int> *elMultAK4_, *muMultAK4_, *hfHadMultAK4_, *hfEmMultAK4_;
    std::vector<float> *hf_hfAK4_, *hf_emfAK4_, *hofAK4_;

};



#endif

