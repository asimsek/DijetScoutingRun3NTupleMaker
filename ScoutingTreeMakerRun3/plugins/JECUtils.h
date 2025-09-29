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
}

#endif


