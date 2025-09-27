import os, re

__all__ = [
    "infer_era_from_filenames",
    "parse_residual_list",
    "load_jec_config_text",
    "normalize_era_key",
    "get_era_block",
]

def infer_era_from_filenames(file_names):
    """
    Pull 'Run20XX[A-I]' from input LFNs, e.g. /store/data/Run2024G/...
    Returns '' if not found.
    """
    pat = re.compile(r"/store/(?:data|mc)/(Run20\d{2}[A-I])/")
    for s in file_names:
        m = pat.search(s)
        if m:
            return m.group(1)
    return ""

def normalize_era_key(raw):
    """
    Accept '2024F' or 'Run2024F' and return 'Run2024F'.
    """
    raw = raw.strip()
    if not raw:
        return ""
    return raw if raw.startswith("Run") else ("Run" + raw)

def parse_residual_list(s):
    """
    Accept a one-line or multi-line list:
      [ -1:-1:/path.txt, 382298:383247:/path2.txt, ... ]
    Returns list of strings 'min:max:path' ready for cms.vstring().
    """
    s = s.strip()
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1]
    out = []
    for item in s.split(','):
        item = item.strip().strip('()')
        if not item:
            continue
        # allow colons inside path: split only first 2
        a, b, rest = item.split(':', 2)
        out.append(":".join([a.strip(), b.strip(), rest.strip()]))
    return out

def load_jec_config_text(path):
    """
    Parse your free-form JEC text file into:
      { 'Run2024F': {'L1FastJet':..., 'L2Relative':..., 'L3Absolute':...,
                     'L2L3Residual':[ 'min:max:file', ... ],
                     'Unc': ... }, ... }
    Header lines may be like:
      #---- Year: 2024F:
      #---- year: 2024G:
      #---- era:  2025C:
    """
    db = {}
    if not os.path.isfile(path):
        return db

    cur = None
    in_list = False
    buf = []

    hdr = re.compile(r"#-+\s*(?:Year|year|era)\s*:\s*([A-Za-z0-9_]+)\s*:?\s*$")

    with open(path, "r") as f:
        for raw in f:
            line = raw.strip()

            # skip empty or comment-only lines (except section headers)
            if not line:
                continue
            m = hdr.match(line)
            if m:
                key = normalize_era_key(m.group(1))
                cur = key
                db[cur] = {
                    "L1FastJet": "",
                    "L2Relative": "",
                    "L3Absolute": "",
                    "L2L3Residual": [],
                    "Unc": "",
                }
                in_list = False
                buf = []
                continue

            if cur is None:
                # ignore lines before first section header
                continue

            if line.startswith("L2L3Residual:"):
                rhs = line.split(":", 1)[1].strip()
                if "[" in rhs and "]" in rhs:
                    db[cur]["L2L3Residual"] = parse_residual_list(rhs)
                else:
                    # start multi-line list
                    in_list = True
                    buf = [rhs]
                continue

            if in_list:
                buf.append(line)
                if "]" in line:
                    in_list = False
                    db[cur]["L2L3Residual"] = parse_residual_list(" ".join(buf))
                    buf = []
                continue

            # simple key: value
            if ":" in line:
                k, v = line.split(":", 1)
                db[cur][k.strip()] = v.strip().rstrip(",").strip()

    return db

def get_era_block(db, era_hint):
    """
    Resolve the block for 'era_hint' (normalize to Run20XX?).
    Return {} if not found.
    """
    key = normalize_era_key(era_hint) if era_hint else ""
    if key and key in db:
        return db[key]
    return {}

