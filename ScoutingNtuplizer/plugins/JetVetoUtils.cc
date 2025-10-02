#include "DijetScoutingRun3NTupleMaker/ScoutingNtuplizer/plugins/JetVetoUtils.h"
#include <TFile.h>
#include <TKey.h>
#include "FWCore/MessageLogger/interface/MessageLogger.h"

namespace jetveto {

std::string pickFileForRun(const std::vector<std::string>& entries,
                           unsigned run,
                           std::string& keyOut)
{
  auto trim = [](std::string s) {
    const char* ws = " \t\n\r";
    const auto b = s.find_first_not_of(ws);
    const auto e = s.find_last_not_of(ws);
    if (b == std::string::npos) return std::string();
    return s.substr(b, e - b + 1);
  };

  auto safe_stoll = [&trim](const std::string& s, bool& ok)->long long {
    ok = false;
    std::string t = s;
    // tolerate trailing commas/brackets if present
    while (!t.empty() && (t.back()==',' || t.back()==']' || t.back()==')')) t.pop_back();
    t = trim(t);
    if (t.empty()) return 0;
    // valid pattern: optional '-', then digits
    size_t i = 0;
    if (t[0]=='-') i = 1;
    for (; i < t.size(); ++i) if (!std::isdigit(static_cast<unsigned char>(t[i]))) return 0;
    try { long long v = std::stoll(t); ok = true; return v; } catch(...) { return 0; }
  };

  for (const auto& raw : entries) {
    // ignore empty strings
    std::string entry = trim(raw);
    if (entry.empty()) continue;

    const auto pos1 = entry.find(':');
    const auto pos2 = (pos1==std::string::npos) ? std::string::npos : entry.find(':', pos1+1);

    // Not a run-ranged form -> treat as plain file
    if (pos1==std::string::npos || pos2==std::string::npos) {
      keyOut = entry; 
      return entry; // plain file
    }

    const std::string minS = trim(entry.substr(0, pos1));
    const std::string maxS = trim(entry.substr(pos1+1, pos2-pos1-1));
    const std::string file = trim(entry.substr(pos2+1));

    bool ok1=false, ok2=false;
    const long long minRun = safe_stoll(minS, ok1);
    const long long maxRun = safe_stoll(maxS, ok2);

    // If numbers are not parseable, fall back to plain file path (no crash)
    if (!ok1 || !ok2 || file.empty()) {
      keyOut = entry;
      return entry; // behave as a plain file
    }

    const bool okMin = (minRun < 0) || (static_cast<long long>(run) >= minRun);
    const bool okMax = (maxRun < 0) || (static_cast<long long>(run) <  maxRun);
    if (okMin && okMax) { keyOut = entry; return file; }
  }

  keyOut.clear();
  return std::string();
}

std::unique_ptr<TH2> loadTH2FromRoot(const std::string& path)
{
  std::unique_ptr<TFile> f(TFile::Open(path.c_str(), "READ"));
  if (!f || f->IsZombie()) { edm::LogWarning("JetVeto") << "Cannot open veto file: " << path; return nullptr; }

  // 1) Prefer the JERC-recommended name
  if (auto* h = dynamic_cast<TH2*>(f->Get("jetvetomap"))) {
    std::unique_ptr<TH2> out((TH2*)h->Clone("jetVetoMap_mem"));
    out->SetDirectory(nullptr);
    return out;
  }

  // 2) Fallbacks (other flavors present in the file)
  for (const char* name : {
        "jetvetomap_all", "jetvetomap_hotandcold",
        "jetvetomap_hot", "jetvetomap_cold",
        "jetvetomap_bpix","jetvetomap_fpix",
        "vetoMap","h2","hJetVeto"
      }) {
    if (auto* h = dynamic_cast<TH2*>(f->Get(name))) {
      std::unique_ptr<TH2> out((TH2*)h->Clone("jetVetoMap_mem"));
      out->SetDirectory(nullptr);
      edm::LogInfo("JetVeto") << "Falling back to TH2 named '" << name << "' in " << path;
      return out;
    }
  }

  // 3) Last resort: first TH2 in file
  TH2* picked = nullptr;
  TIter nextKey(f->GetListOfKeys());
  while (TKey* key = (TKey*)nextKey()) {
    if (auto* h = dynamic_cast<TH2*>(key->ReadObj())) { picked = h; break; }
  }
  if (!picked) { edm::LogWarning("JetVeto") << "No TH2 found in " << path; return nullptr; }

  std::unique_ptr<TH2> out((TH2*)picked->Clone("jetVetoMap_mem"));
  out->SetDirectory(nullptr);
  edm::LogInfo("JetVeto") << "Using first TH2 found: '" << picked->GetName() << "'";
  return out;
}

void ensureVetoMapReady(bool enabled,
                        const std::vector<std::string>& entries,
                        unsigned run,
                        std::string& cacheKey,
                        std::unique_ptr<TH2>& mapOut)
{
  if (!enabled || entries.empty()) return;

  std::string key, file = pickFileForRun(entries, run, key);
  if (file.empty()) { mapOut.reset(); cacheKey.clear(); return; }

  if (key != cacheKey) {
    mapOut.reset();
    if (file.size()>=5 && file.substr(file.size()-5)==".root") {
      mapOut = loadTH2FromRoot(file);
    } else {
      // JSON (correctionlib) can be added here if needed.
      edm::LogInfo("JetVeto") << "JSON veto map given (" << file << "); JSON evaluation not enabled.";
    }
    cacheKey = key;
    edm::LogInfo("JetVeto") << "Loaded veto map from: " << file;
  }
}

} // namespace jetveto


