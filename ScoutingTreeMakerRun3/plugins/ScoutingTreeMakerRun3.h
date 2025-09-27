#ifndef ScoutingTreeMakerRun3_h
#define ScoutingTreeMakerRun3_h


#include <numeric>
#include <string>
#include <cmath>
#include <vector>
#include <limits>
#include <cstdint>
#include <TTree.h>
#include <algorithm>
#include <TLorentzVector.h>
//#include <memory>
//#include <iostream>
//#include <sstream>
//#include <istream>
//#include <fstream>
//#include <iomanip>
//#include <functional>
//#include <cassert>
//#include "TFile.h"
//#include "TH1D.h"
//#include "TH1F.h"
//#include "TMath.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
//#include "DataFormats/Math/interface/deltaR.h"
//#include "DataFormats/JetReco/interface/JetCollection.h"
//#include "DataFormats/METReco/interface/MET.h"
//#include "DataFormats/VertexReco/interface/Vertex.h"
//#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "L1Trigger/L1TGlobal/interface/L1TGlobalUtil.h"
//#include "DataFormats/JetReco/interface/Jet.h"
//#include "DataFormats/PatCandidates/interface/Jet.h"
//#include "HLTrigger/HLTcore/interface/TriggerExpressionData.h"
//#include "HLTrigger/HLTcore/interface/TriggerExpressionEvaluator.h"
//#include "HLTrigger/HLTcore/interface/TriggerExpressionParser.h"


// PFMET
//#include "DataFormats/METReco/interface/PFMET.h"
//#include "DataFormats/METReco/interface/PFMETFwd.h"
//#include "DataFormats/PatCandidates/interface/MET.h"

// JEC
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

// Trigger 
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h"
#include "DataFormats/L1Trigger/interface/BXVector.h"
//#include "DataFormats/HLTReco/interface/TriggerEvent.h"

// Scouting
#include "DataFormats/Scouting/interface/Run3ScoutingPFJet.h"
#include "DataFormats/Scouting/interface/Run3ScoutingVertex.h"
#include "DataFormats/Scouting/interface/Run3ScoutingParticle.h"
//#include "DataFormats/Scouting/interface/Run3ScoutingElectron.h"
//#include "DataFormats/Scouting/interface/Run3ScoutingPhoton.h"
//#include "DataFormats/Scouting/interface/Run3ScoutingTrack.h"
//#include "DataFormats/Scouting/interface/Run3ScoutingMuon.h"




//#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
//#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
//#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
//#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

//#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"


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


    // --- JEC config/state ---
    bool applyJEC_;
    std::string jecMode_;                  // "es" | "txt" | "none"
    std::string jecPayload_;               // e.g. "AK4PF", "AK4PFchs", "AK4PFPuppi"
    std::vector<std::string> jecLevels_;   // e.g. {"L1FastJet","L2Relative","L3Absolute",["L2L3Residual"]}
    std::vector<std::string> jecTxtFiles_; // txt paths when jecMode_ == "txt"

    // --- TXT-mode: optional per-run override for L2L3Residual
    bool jecResidualByRun_;                      // if true, choose Residual TXT by run
    std::vector<std::string> jecResidualMap_;    // entries "min:max:file" (min inclusive, max exclusive; -1 = open)
    std::string jecResidualCurrent_;             // cache last applied residual file (FileInPath key)


    // --- JEC uncertainty (JES) config/state ---
    bool applyJECUncertainty_;             // enable JES uncertainty
    std::string jecUncTxtFile_;            // used if jecMode_ == "txt"
    std::unique_ptr<JetCorrectionUncertainty> jecUnc_;  // built from ES or TXT

    // --- Debug/printing controls ---
    bool     printJECInfo_;          // print ES/JEC info and a few per-jet lines
    unsigned printJECFirstNJets_;    // print at most this many jets across the job

    // Corrector built either from ES params (on first event) or from txt files (in ctor)
    std::unique_ptr<FactorizedJetCorrector> jecCorrector_;

    // ES token (only used if jecMode_ == "es")
    edm::ESGetToken<JetCorrectorParametersCollection, JetCorrectionsRecord> jecESGetToken_;


    edm::EDGetTokenT<vector<Run3ScoutingPFJet>> srcPFJets_;
    edm::EDGetTokenT<vector<Run3ScoutingParticle>> srcPFCands_;

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
    float rho_, met_, metphi_, minDPhiMetJet2_, minDPhiMetJet4_;
    float sumEt_, metSig_, metOverSumEt_, unclusteredEnFrac_;
    float htAK4_, mjjAK4_, dEtajjAK4_, dPhijjAK4_;
    std::vector<bool> *triggerResult_;
    std::vector<std::string> *triggerName_;

    //---- jet and genJet variables --------------
    std::vector<float> *ptAK4_, *etaAK4_, *phiAK4_, *massAK4_, *energyAK4_, *areaAK4_, *chfAK4_, *nhfAK4_, *phfAK4_, *elfAK4_, *mufAK4_;
    std::vector<int> *idLAK4_, *idTAK4_, *chHadMultAK4_, *neHadMultAK4_, *phoMultAK4_;
    std::vector<int> *elMultAK4_, *muMultAK4_, *hfHadMultAK4_, *hfEmMultAK4_;
    std::vector<float> *hf_hfAK4_, *hf_emfAK4_, *hofAK4_;
    std::vector<float> *jecFactorAK4_;   // correction factor applied to each jet p4

    // --- JES uncertainty outputs ---
    std::vector<float> *jecRelUncAK4_;      // relative JES uncertainty per jet
    std::vector<float> *jecUpFactorAK4_;    // 1 + unc
    std::vector<float> *jecDownFactorAK4_;  // 1 - unc
    bool jecLoggedOnce_;

};



#endif

