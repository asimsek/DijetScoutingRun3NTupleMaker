# utils/genXsec_cfg.py
import os, re, shlex, subprocess, sys
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

# -------------------------------
# ANSI color helpers (red prefix only)
# -------------------------------
def _supports_color():
    return sys.stdout.isatty() and os.environ.get("NO_COLOR", "") == ""

ANSI_RED   = "\033[31m" if _supports_color() else ""
ANSI_RESET = "\033[0m"  if _supports_color() else ""

def red_prefix(i, n):
    return f"{ANSI_RED}[genXsec] [{i}/{n}]{ANSI_RESET}"

# -------------------------------
# Shell helpers
# -------------------------------
def _run(cmd, check=True):
    proc = subprocess.run(
        cmd if isinstance(cmd, list) else shlex.split(cmd),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"Command failed ({proc.returncode}): {cmd}\n{proc.stderr}")
    return proc.returncode, proc.stdout, proc.stderr

# -------------------------------
# XRootD helpers
# -------------------------------
def _redirector():
    return os.environ.get("XRD_DEFAULT_REDIRECTOR", "root://cms-xrd-global.cern.ch/")

def _to_xrootd(path, redir):
    if path.startswith(("root://", "file:")):
        return path
    if path.startswith("/store/"):
        sep = "" if redir.endswith("/") else "/"
        return f"{redir}{sep}{path}"
    return path

# Extract canonical /store/... path (so different endpoints still match)
_STORE_RE = re.compile(r"(/store/.*\.root)")

def _store_path(s):
    m = _STORE_RE.search(s)
    return m.group(1) if m else s

# -------------------------------
# DAS wrappers (portable flags)
# -------------------------------
def das_datasets(pattern):
    # -limit 0 removes the 250-cap
    cmd = ["dasgoclient", "-limit", "0", "-query", f"dataset={pattern}"]
    _, out, _ = _run(cmd)
    return [l.strip() for l in out.splitlines() if l.strip()]

def das_files(dataset):
    cmd = ["dasgoclient", "-limit", "0", "-query", f"file dataset={dataset}"]
    _, out, _ = _run(cmd)
    return [l.strip() for l in out.splitlines() if l.strip()]

# -------------------------------
# Dataset argument parsing/expansion
# -------------------------------
def parse_dataset_arg(ds_arg):
    if not ds_arg:
        return []
    return [tok.strip() for tok in ds_arg.split(",") if tok.strip()]

def expand_datasets(tokens):
    out = []
    for t in tokens:
        if "*" in t:
            out.extend(das_datasets(t))
        else:
            out.append(t)
    # preserve order, drop dups
    seen, uniq = set(), []
    for ds in out:
        if ds not in seen:
            seen.add(ds)
            uniq.append(ds)
    return uniq

# -------------------------------
# GenXsec parsing from logs
# -------------------------------
_XSEC_RE1 = re.compile(
    r"final\s+cross\s+section\s*=\s*([0-9.+\-Ee]+)\s*(?:\+\-|\u00b1)\s*([0-9.+\-Ee]+)\s*pb",
    re.IGNORECASE)
_XSEC_RE2 = re.compile(
    r"GenX(?:sec|Sec)Analyzer.*?(?:cross\s*section\s*=?\s*)([0-9.+\-Ee]+)\s*pb",
    re.IGNORECASE)

def parse_xsec_from_log(text):
    m = _XSEC_RE1.search(text)
    if m:
        return float(m.group(1)), float(m.group(2))
    m = _XSEC_RE2.search(text)
    if m:
        return float(m.group(1)), None
    return None, None

# -------------------------------
# Child-runner (for multi-dataset summary path)
# -------------------------------
def run_one_dataset_with_cmsrun(cfg_path, dataset, maxEvents, redirector):
    args = [
        "cmsRun", cfg_path,
        f"dataset={dataset}",
        f"maxEvents={maxEvents}",
        f"redirector={redirector}",
        "childMode=True",   # ensures the child actually runs the CMSSW Process
    ]
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    x, dx = parse_xsec_from_log(proc.stdout)
    return proc.returncode, x, dx, proc.stdout

# -------------------------------
# Stream a child cmsRun and reformat fileAction messages with [i/N]
# -------------------------------
_INIT_RE  = re.compile(r"Initiating request to open file\s+(root://\S+)")
_OPEN_RE  = re.compile(r"Successfully opened file\s+(root://\S+)")
_CLOSE_RE = re.compile(r"Closed file\s+(root://\S+)")

def stream_child_with_counter(child_args, nfiles):
    """Run cmsRun as a child, pretty-print file open/close with [i/N], and
       collect full log for later xsec parsing."""
    proc = subprocess.Popen(child_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, bufsize=1, universal_newlines=True)
    i = 0
    full = []
    try:
        for line in proc.stdout:
            full.append(line)

            # Match and pretty-print
            m_init = _INIT_RE.search(line)
            if m_init:
                i += 1
                url = m_init.group(1)
                print(f"{red_prefix(i, nfiles)}  Initiating request to open file: {url}")
                continue

            if _OPEN_RE.search(line):
                print("  Successfully opened the root file.")
                continue

            if _CLOSE_RE.search(line):
                print("  Closed the root file.")
                continue

            # Pass through only important lines to keep output clean
            if ("GenXsecAnalyzer" in line) or ("cross section" in line and "pb" in line):
                print(line.rstrip())
                continue
            if ("Fatal Exception" in line) or ("ERROR" in line) or ("Exception of category" in line):
                print(line.rstrip())
                continue
            # else: suppress noisy lines
        proc.wait()
    finally:
        try:
            proc.stdout.close()
        except Exception:
            pass
    return proc.returncode, "".join(full)

# -------------------------------
# Options
# -------------------------------
options = VarParsing('analysis')
options.register('dataset', '', VarParsing.multiplicity.singleton, VarParsing.varType.string,
                 "DAS dataset path, wildcard pattern, or comma-separated list")
options.register('combineSamples', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "When multiple datasets/patterns are given, combine all matches into a single run")
options.register('redirector', _redirector(), VarParsing.multiplicity.singleton, VarParsing.varType.string,
                 "XRootD redirector used for /store paths")
# internal flag: parent orchestrates, child actually runs the Process
options.register('childMode', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "INTERNAL: run the CMSSW Process (do not orchestrate)")

options.parseArguments()
cfg_abspath = os.path.abspath(__file__)

# -------------------------------
# Multi-dataset orchestration (separate runs, summary table)
# -------------------------------
if options.dataset and not options.combineSamples and not options.childMode:
    tokens = parse_dataset_arg(options.dataset)
    needs_expand = any(("*" in t) for t in tokens)
    ds_list = expand_datasets(tokens) if (needs_expand or len(tokens) > 1) else None

    if ds_list and len(ds_list) > 1:
        print(f"[genXsec] Found {len(ds_list)} dataset(s). Running GenXsecAnalyzer per dataset...\n")
        rows = []
        for i, ds in enumerate(ds_list, 1):
            print(f"{red_prefix(i, len(ds_list))} {ds}")
            # Optional: count files quickly
            try:
                nf = len(das_files(ds))
                print(f"  -> {nf} file(s) in this dataset")
            except Exception:
                pass

            # Run a child job (non-streaming here; could be upgraded to streaming per dataset if you like)
            rc, x, dx, logtxt = run_one_dataset_with_cmsrun(
                cfg_abspath, ds, options.maxEvents, options.redirector
            )
            if rc != 0:
                print(f"  -> cmsRun failed for {ds} (rc={rc}). Skipping.\n")
                continue
            if x is None:
                print("  -> Could not parse cross section from log. Tail follows:\n")
                print("\n".join(logtxt.splitlines()[-30:]), "\n")
                continue
            rows.append((ds, x, dx))

        if rows:
            print("\n=== GenXsec per dataset ===")
            w = max(len(r[0]) for r in rows)
            print(f"{'Dataset'.ljust(w)}  {'xsec [pb]':>14}  {'stat err [pb]':>14}")
            print("-" * (w + 32))
            for ds, x, dx in rows:
                dxs = f"{dx:.6g}" if dx is not None else "-"
                print(f"{ds.ljust(w)}  {x:>14.6g}  {dxs:>14}")
            print("-" * (w + 32))
            print("\n[genXsec] To combine all matched samples in a single run, add combineSamples=True.\n")
        sys.exit(0)

# -------------------------------
# Resolve to file list (single or combined)
# -------------------------------
file_names = list(options.inputFiles)

if (not file_names) and options.dataset:
    tokens = parse_dataset_arg(options.dataset)
    if options.combineSamples and (len(tokens) > 1 or any("*" in t for t in tokens)):
        ds_list = expand_datasets(tokens)
        if not ds_list:
            raise RuntimeError(f"No datasets matched any token in: {options.dataset}")
        files = []
        for ds in ds_list:
            files.extend(das_files(ds))
        file_names = files
        print(f"[genXsec] Combining {len(ds_list)} datasets, total files: {len(file_names)}")
    else:
        if len(tokens) == 1 and "*" in tokens[0]:
            ds_list = expand_datasets(tokens)
            if not ds_list:
                raise RuntimeError(f"No datasets matched pattern: {tokens[0]}")
            if len(ds_list) != 1:
                raise RuntimeError(f"Pattern expanded to {len(ds_list)} datasets; set combineSamples=True or use comma-separated list.")
            file_names = das_files(ds_list[0])
        else:
            file_names = das_files(tokens[0])

if not file_names:
    raise RuntimeError("No input files were provided or found via DAS.")

# Normalize to XRootD
redir = options.redirector
file_names = [_to_xrootd(f, redir) for f in file_names]

# -------------------------------
# Orchestrate pretty progress for single/combined run (parent)
# -------------------------------
if not options.childMode:
    nfiles = len(file_names)
    print(f"{ANSI_RED}[genXsec]{ANSI_RESET} Total input files: {nfiles}")

    # Launch child that actually runs the CMSSW Process; parent reformats output
    child_args = [
        "cmsRun", cfg_abspath,
        f"dataset={options.dataset}",
        f"maxEvents={options.maxEvents}",
        f"redirector={options.redirector}",
        f"combineSamples={str(bool(options.combineSamples))}",
        "childMode=True",
    ]
    rc, full_log = stream_child_with_counter(child_args, nfiles)

    # Parse and print xsec summary (leave exact analyzer lines as-is if they appeared)
    x, dx = parse_xsec_from_log(full_log)
    if x is not None:
        dxs = f" ± {dx:.6g}" if dx is not None else ""
        print(f"[genXsec] Final cross section = {x:.6g}{dxs} pb")
    sys.exit(rc)

# -------------------------------
# CHILD MODE: define and run the CMSSW Process (emit fileAction lines)
# -------------------------------
process = cms.Process('XSec')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100000
# Keep default logger behavior so fileAction lines appear naturally

secFiles = cms.untracked.vstring()
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*file_names),
    secondaryFileNames = secFiles
)

process.xsec = cms.EDAnalyzer("GenXSecAnalyzer")
process.ana = cms.Path(process.xsec)
process.schedule = cms.Schedule(process.ana)

