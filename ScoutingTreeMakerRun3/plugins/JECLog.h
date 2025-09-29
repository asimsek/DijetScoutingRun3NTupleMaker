#pragma once
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DijetScoutingRun3NTupleMaker/ScoutingTreeMakerRun3/plugins/JECUtils.h"

namespace jec { namespace log {

inline std::string pickByHint(const std::vector<std::string>& files, const char* hint){
  for (const auto& f : files) if (f.find(hint)!=std::string::npos) return f;
  return {};
}
inline const std::string& safe(const std::string& s){
  static const std::string kNone{"(none)"}; return s.empty()?kNone:s;
}

struct TxtConfig {
  std::string mode, payload, residual, uncFile;
  std::vector<std::string> levels, txtFiles;
};
struct EsConfig {
  std::string payload;
  std::vector<std::string> levels;
  bool hasUnc{false};
  bool usedTxtFallback{false}; // ES mode: Unc came from TXT fallback
};


inline void print(const TxtConfig& c){
  std::ostringstream oss;
  oss << "\n**************************************************\n"
      << "TXT JEC configuration\n"
      << "  Mode       : " << c.mode << "\n"
      << "  Payload    : " << c.payload << "\n"
      << "  Levels     : " << jec::joinLevels(c.levels) << "\n"
      << "  Files:\n"
      << "    - L1FastJet   : " << safe(pickByHint(c.txtFiles, "L1FastJet"))   << "\n"
      << "    - L2Relative  : " << safe(pickByHint(c.txtFiles, "L2Relative"))  << "\n"
      << "    - L3Absolute  : " << safe(pickByHint(c.txtFiles, "L3Absolute"))  << "\n"
      << "    - L2L3Residual: " << (c.residual.empty()? "(none)" : c.residual) << "\n"
      << "  Uncertainty     : " << safe(c.uncFile) << "\n"
      << "**************************************************";
  edm::LogVerbatim("JEC") << oss.str();
}

inline void print(const EsConfig& c){
  std::ostringstream oss;
  oss << "\n##################################################\n"
      << "ES JEC configuration\n"
      << "  Record     : JetCorrectionsRecord\n"
      << "  Payload    : " << c.payload << "\n"
      << "  Levels     : " << jec::joinLevels(c.levels) << "\n"
      << "  Uncertainty: "
      << (c.hasUnc
            ? (c.usedTxtFallback ? "Loaded from txt fallback!" : "present in ES")
            : "NOT found in ES")
      << "\n"
      << "  Note       : ES mode reads from the GlobalTag payload (no local TXT files)\n"
      << "##################################################";
  edm::LogVerbatim("JEC") << oss.str();
}

inline void printJet(unsigned printedIdx, int run, int lumi, long long evt,
                     float eta, float pt_raw, float area, float rho,
                     float jec, float pt_corr, float jes_rel){
  std::ostringstream oss;
  oss << "run:lumi:evt " << run << ":" << lumi << ":" << evt
      << " | jet#" << printedIdx
      << std::fixed << std::setprecision(6)
      << " | eta=" << eta
      << " pt_raw=" << pt_raw
      << " area=" << area
      << " rho=" << std::max(0.f, rho)
      << " | JEC=" << jec
      << " pt_corr=" << pt_corr
      << " | JES_rel=" << jes_rel
      << " upFactor=" << (1.f + jes_rel)
      << " downFactor=" << std::max(0.f, 1.f - jes_rel)
      << std::defaultfloat;
  edm::LogVerbatim("JEC") << oss.str();
}

}} // namespace jec::log


