#ifndef JECUtils_h
#define JECUtils_h

#include <memory>
#include <string>
#include <vector>
#include <limits>
#include <numeric>
#include <algorithm>
#include <cctype>

#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"


namespace jec {

  /// Select "Residual" TXT for a run from entries "min:max:file" (min inclusive, max exclusive; -1=open)
  bool pickResidualForRun(const std::vector<std::string>& residualMap,
                          unsigned int run, std::string& outFile);

  /// Build a TXT-based corrector from base files (L1/L2/L3) and optional residual file.
  std::unique_ptr<FactorizedJetCorrector>
  buildTxtCorrector(const std::vector<std::string>& baseTxtFiles,
                    const std::string& residualTxtIfAny);

  /// Build an ES-based corrector from a payload collection and JEC level list.
  /// ES-mode helper: build from ES; if "L2L3Residual" is requested but missing in ES,
  /// optionally append it from a TXT file. Sets usedTxtResidual=true iff TXT residual is used.
  std::unique_ptr<FactorizedJetCorrector>
  buildEsCorrectorWithOptionalTxtResidual(const JetCorrectorParametersCollection& coll,
                                          const std::vector<std::string>& levels,
                                          const std::string& residualTxtFile,
                                          bool allowFallback,
                                          bool& usedTxtResidual);

  /// Make a JetCorrectionUncertainty from ES (if present).
  std::unique_ptr<JetCorrectionUncertainty>
  buildUncertaintyFromEs(const JetCorrectorParametersCollection& coll);

  /// Make a JetCorrectionUncertainty from a TXT file.
  std::unique_ptr<JetCorrectionUncertainty>
  buildUncertaintyFromTxt(const std::string& uncTxtFile);

  /// ES-mode helper: try ES first; optionally fall back to TXT if ES is missing.
  /// Returns nullptr if neither is available. Sets usedTxtFallback=true if TXT was used.
  std::unique_ptr<JetCorrectionUncertainty>
  buildUncertaintyEsWithOptionalTxtFallback(const JetCorrectorParametersCollection& coll,
                                            const std::string& uncTxtFile,
                                            bool allowFallback,
                                            bool& usedTxtFallback);


  /// Pretty join of level names for logging.
  std::string joinLevels(const std::vector<std::string>& levels);

struct CorrInput {
  float rho, area, pt_raw, eta, phi, energy;
  int   npv;
};

struct CorrOutput {
  float jec = 1.f;
  float pt_corr = 0.f;
  float jes_rel = 0.f;
};

inline CorrOutput evaluate(FactorizedJetCorrector* corr,
                           JetCorrectionUncertainty* unc,
                           const CorrInput& in)
{
  CorrOutput out;

  // correction
  if (corr) {
    corr->setRho(std::max(0.f, in.rho));
    corr->setJetA(in.area);
    corr->setJetPt(in.pt_raw);
    corr->setJetEta(in.eta);
    corr->setJetPhi(in.phi);
    corr->setJetE(in.energy);
    if (in.npv >= 0) corr->setNPV(in.npv);
    out.jec = corr->getCorrection();
  }
  out.pt_corr = in.pt_raw * out.jec;

  // JES uncertainty (relative)
  if (unc) {
    unc->setJetEta(in.eta);
    unc->setJetPt(std::max(1.f, out.pt_corr));
    out.jes_rel = std::max(0.f, float(unc->getUncertainty(true)));
  }
  return out;
}

// --- first-event picker + prebuild for TXT no-residual ----------------------
struct FirstEventSelection {
  // chosen “single” members
  std::vector<std::string> txtFiles;
  std::vector<std::string> residualMap;
  std::string              uncTxtFile;
  std::vector<std::string> vetoMapFiles;
  bool                     residualByRun = false;
};

FirstEventSelection pickInputsByIsDataAndMaybePrebuildTxt(bool wantData,
                                                          const std::string& jecMode,
                                                          std::vector<std::string>& levels /*in/out*/,
                                                          const std::vector<std::string>& dataTxt,
                                                          const std::vector<std::string>& mcTxt,
                                                          const std::vector<std::string>& dataRes,
                                                          const std::vector<std::string>& mcRes,
                                                          const std::string& dataUnc,
                                                          const std::string& mcUnc,
                                                          const std::vector<std::string>& dataVeto,
                                                          const std::vector<std::string>& mcVeto,
                                                          bool applyJEC, bool applyJECUnc,
                                                          std::unique_ptr<FactorizedJetCorrector>& corr,
                                                          std::unique_ptr<JetCorrectionUncertainty>& unc,
                                                          std::string& bannerKey);
} // namespace jec


#endif


