#include "DijetScoutingRun3NTupleMaker/ScoutingTreeMakerRun3/plugins/JECUtils.h"
#include <limits>
#include <numeric>

namespace jec {

  bool pickResidualForRun(const std::vector<std::string>& residualMap,
                          unsigned int run, std::string& outFile) {
    for (const auto& entry : residualMap) {
      // "min:max:file"
      const auto p1 = entry.find(':');
      if (p1 == std::string::npos) continue;
      const auto p2 = entry.find(':', p1 + 1);
      if (p2 == std::string::npos) continue;

      auto trim = [](std::string s) {
      auto wsfront = std::find_if_not(s.begin(), s.end(), ::isspace);
      auto wsback  = std::find_if_not(s.rbegin(), s.rend(), ::isspace).base();
      return (wsfront < wsback ? std::string(wsfront, wsback) : std::string());
    };

    std::string sMin = trim(entry.substr(0, p1));
    std::string sMax = trim(entry.substr(p1 + 1, p2 - (p1 + 1)));
    std::string sFile= trim(entry.substr(p2 + 1));

    long long minRun = 0;
    long long maxRun = std::numeric_limits<long long>::max();

    try {
      if (!(sMin.empty() || sMin == "-1")) minRun = std::stoll(sMin);
      if (!(sMax.empty() || sMax == "-1")) maxRun = std::stoll(sMax);
    } catch (const std::exception& e) {
      // Skip malformed entry rather than crash
      continue;
    }

      if (static_cast<long long>(run) >= minRun &&
          static_cast<long long>(run) <  maxRun) {
        outFile = sFile;
        return true;
      }
    }
    return false;
  }

  std::unique_ptr<FactorizedJetCorrector>
  buildTxtCorrector(const std::vector<std::string>& baseTxtFiles,
                    const std::string& residualTxtIfAny) {
    std::vector<JetCorrectorParameters> pars;
    pars.reserve(baseTxtFiles.size() + (residualTxtIfAny.empty() ? 0 : 1));

    for (const auto& f : baseTxtFiles) {
      edm::FileInPath fp(f);
      pars.emplace_back(fp.fullPath());
    }
    if (!residualTxtIfAny.empty()) {
      edm::FileInPath fp(residualTxtIfAny);
      pars.emplace_back(fp.fullPath());
    }
    if (pars.empty()) {
      return nullptr;
    }
    return std::make_unique<FactorizedJetCorrector>(pars);
  }

  std::unique_ptr<FactorizedJetCorrector>
  buildEsCorrector(const JetCorrectorParametersCollection& coll,
                   const std::vector<std::string>& levels) {
    std::vector<JetCorrectorParameters> pars;
    pars.reserve(levels.size());
    for (const auto& lvl : levels) {
      pars.push_back(coll[lvl]);  // will throw if missing; matches prior behavior
    }
    if (pars.empty()) {
      return nullptr;
    }
    return std::make_unique<FactorizedJetCorrector>(pars);
  }

  std::unique_ptr<JetCorrectionUncertainty>
  buildUncertaintyFromEs(const JetCorrectorParametersCollection& coll) {
    try {
      JetCorrectorParameters up = coll["Uncertainty"];
      return std::make_unique<JetCorrectionUncertainty>(up);
    } catch (...) {
      return nullptr;
    }
  }

  std::unique_ptr<JetCorrectionUncertainty>
  buildUncertaintyEsWithOptionalTxtFallback(const JetCorrectorParametersCollection& coll,
                                            const std::string& uncTxtFile,
                                            bool allowFallback,
                                            bool& usedTxtFallback)
  {
    usedTxtFallback = false;

    // Try ES first
    if (auto es = buildUncertaintyFromEs(coll)) {
      return es;
    }

    // Optionally fall back to TXT
    if (allowFallback && !uncTxtFile.empty()) {
      if (auto txt = buildUncertaintyFromTxt(uncTxtFile)) {
        usedTxtFallback = true;
        return txt;
      }
    }

    return nullptr;
  }


  std::unique_ptr<JetCorrectionUncertainty>
  buildUncertaintyFromTxt(const std::string& uncTxtFile) {
    if (uncTxtFile.empty()) return nullptr;
    try {
      edm::FileInPath f(uncTxtFile);
      JetCorrectorParameters up(f.fullPath());
      return std::make_unique<JetCorrectionUncertainty>(up);
    } catch (...) {
      return nullptr;
    }
  }

  std::string joinLevels(const std::vector<std::string>& levels) {
    if (levels.empty()) return "(none)";
    return std::accumulate(std::next(levels.begin()), levels.end(), levels.front(),
                           [](std::string a, const std::string& b) {
                             return std::move(a) + ", " + b;
                           });
  }

} // namespace jec



