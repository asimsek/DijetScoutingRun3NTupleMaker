#ifndef JetVetoUtils_h
#define JetVetoUtils_h

#include <string>
#include <vector>
#include <memory>
#include <TH2.h>
#include <cctype>

namespace jetveto {

  // Choose file path for this run. Returns "" if no match. keyOut=matched entry (for caching).
  std::string pickFileForRun(const std::vector<std::string>& entries,
                             unsigned run,
                             std::string& keyOut);

  // Load a TH2 from a ROOT file; prefers JERC's "jetvetomap" by name.
  std::unique_ptr<TH2> loadTH2FromRoot(const std::string& path);

  // Ensure proper veto map is loaded for this run (no-op if disabled or no files).
  void ensureVetoMapReady(bool enabled,
                          const std::vector<std::string>& entries,
                          unsigned run,
                          std::string& cacheKey,
                          std::unique_ptr<TH2>& mapOut);

  // JERC 'jetvetomap': 1 = GOOD, 0 = BAD (veto). Return 1 if in veto (BAD), else 0.
  // Auto-detect axis roles (eta vs phi) from ranges, and wrap phi if the map uses [0, 2pi].
  inline int flagFromMap(const TH2* h, float eta, float phi) {
    if (!h) return 0;

    const auto xMin = h->GetXaxis()->GetXmin();
    const auto xMax = h->GetXaxis()->GetXmax();
    const auto yMin = h->GetYaxis()->GetXmin();
    const auto yMax = h->GetYaxis()->GetXmax();

    // Heuristics: eta spans roughly [-6, +6]; phi spans either [-pi, +pi] or [0, 2pi].
    auto isEtaRange = [](double a, double b) {
      return (a < -4.0 && b > 4.0); // generous for eta coverage
    };
    auto isPhiRange = [](double a, double b) {
      // Allow some slack for bin edges (e.g. -3.2..3.2 or 0..6.4)
      const bool pmPi  = (a <= -3.3 && b >= 3.0);     // ~[-pi, +pi]
      const bool zTo2Pi = (a >= -0.2 && b > 5.8 && b < 6.6); // ~[0, 2pi]
      return pmPi || zTo2Pi;
    };


    const bool yLooksEta = isEtaRange(yMin, yMax);
    const bool xLooksPhi = isPhiRange(xMin, xMax);

    // Decide mapping (default: X=eta, Y=phi). Swap if X looks like phi and Y looks like eta.
    bool xIsEta = true;
    if (xLooksPhi && yLooksEta) xIsEta = false; // swap: X=phi, Y=eta


    // Prepare query coordinates in the map's phi convention
    const double PI  = 3.14159265358979323846;
    const double TPI = 2.0*PI;
    auto wrapPhiTo = [&](double p, double a, double b) {
      // If axis looks like [0,2pi], convert negative phi to [0,2pi]
      if (a >= -0.2 && b > 5.8) {
        if (p < 0) p += TPI;
        // keep within range if slightly beyond due to fp rounding
        if (p < a) p = a;
        if (p > b) p = b - 1e-6;
      }
      return p;
    };

    double xq = 0, yq = 0;
    if (xIsEta) {
      xq = eta;
      yq = wrapPhiTo(phi, yMin, yMax);
    } else {
      xq = wrapPhiTo(phi, xMin, xMax);
      yq = eta;
    }

    const int bx = h->GetXaxis()->FindBin(xq);
    const int by = h->GetYaxis()->FindBin(yq);
    if (bx < 1 || bx > h->GetNbinsX() || by < 1 || by > h->GetNbinsY()) return 0;

    const double v = h->GetBinContent(bx, by);
    // Map semantics: 1 = GOOD, 0 = BAD -> return 1 if BAD (veto)
    return (v < 0.5) ? 1 : 0;
  }



} // namespace jetveto

#endif


