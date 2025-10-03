#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
import py_compile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# =============== Pretty colors & tiny logger ===============
class C:
    R = "\033[91m"   # bright red
    G = "\033[92m"   # bright green
    Y = "\033[93m"   # bright yellow
    B = "\033[94m"   # bright blue
    M = "\033[95m"   # bright magenta
    C = "\033[96m"   # bright cyan
    BOLD = "\033[1m"
    RESET = "\033[0m"

def _use_color() -> bool:
    return sys.stdout.isatty()

def _c(msg: str, code: str) -> str:
    return f"{code}{msg}{C.RESET}" if _use_color() else msg

def info(msg: str) -> None:
    print(_c(f"ℹ {msg}", C.C))

def ok(msg: str) -> None:
    print(_c(f"✔ {msg}", C.G))

def warn(msg: str) -> None:
    print(_c(f"▲ {msg}", C.Y))

def err(msg: str) -> None:
    print(_c(f"✖ {msg}", C.R))

# ====================== Helpers ============================
def timestamp_label(now: Optional[dt.datetime] = None) -> str:
    now = now or dt.datetime.now()
    return f"{now.year:04d}{now.month:02d}{now.day:02d}_{now.hour:02d}00"

def sanitize_request_name(s: str, maxlen: int = 100) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", s)[:maxlen]

def ensure_dirs(paths: List[Path]) -> None:
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)

def read_input_lines(path: Path) -> List[str]:
    with path.open() as f:
        return [ln.strip() for ln in f if ln.strip() and not ln.lstrip().startswith('#')]

def parse_dataset_line(line: str) -> Dict[str, str]:
    parts = line.split()
    if len(parts) < 4:
        raise ValueError(
            "Malformed line (need >=4 columns)\n"
            "Format: <dataset> <processedEvents> <lumisPerJob> <globalTag> [secondaryDataset] <era>"
        )
    dataset, processedEvents, lumisPerJob, globalTag = parts[0], parts[1], parts[2], parts[3]
    secondaryDataset: Optional[str] = None
    era: Optional[str] = None
    if len(parts) >= 5:
        era = parts[-1]
        if len(parts) >= 6:
            secondaryDataset = parts[4]
    out = {
        "dataset": dataset,
        "processedEvents": processedEvents,
        "lumisPerJob": lumisPerJob,
        "globalTag": globalTag,
    }
    if secondaryDataset is not None:
        out["secondaryDataset"] = secondaryDataset
    if era is not None:
        out["era"] = era
    return out

def build_tokens(dataset: str,
                 processed_events: str,
                 lumis_per_job: str,
                 global_tag: str,
                 cfg_path: Path,
                 working_area: Path,
                 namedir: str,
                 lumi_mask: Optional[Path] = None,
                 secondary_dataset: Optional[str] = None) -> Dict[str, str]:
    try:
        sample = dataset.split('/')[1]
        processing = dataset.split('/')[2]
        tier = dataset.split('/')[3]
    except Exception as exc:
        raise ValueError(f"Dataset must look like /Primary/Processing/Tier, got: {dataset}") from exc

    request_name = sanitize_request_name(f"{sample}__{processing}__{tier}")
    root_name = f"{request_name}.root"

    tokens: Dict[str, str] = {
        "THISROOTFILE": root_name,
        "THISGLOBALTAG": global_tag,
        "LUMISPERJOB": lumis_per_job,
        "OUTPUTFOLDER": namedir,
        "WORKINGAREA": str(working_area),
        "WORKINGDIR": request_name,
        "CMSSWCFG": str(cfg_path),
        "OUTFILENAME": root_name,
        "INPUTDATASET": dataset,
    }
    if secondary_dataset:
        tokens["SECONDARYDATASET"] = secondary_dataset
    if lumi_mask:
        tokens["LUMIMASK"] = str(lumi_mask)
    return tokens

# ----- Template rendering -----
def render_template_text(text: str, tokens: Dict[str, str]) -> str:
    patterns = {k: re.compile(rf"\b{re.escape(k)}\b") for k in tokens}
    out: List[str] = []
    for raw in text.splitlines(keepends=True):
        line = raw
        for k, pat in patterns.items():
            line = pat.sub(tokens[k], line)
        out.append(line)
    return "".join(out)

# ----- CMSSW cfg patching (era + tokens + maxEvents) -----
def _comment(line: str) -> str:
    return line if line.lstrip().startswith('#') else re.sub(r"^(\s*)", r"\1#", line)

def _uncomment(line: str) -> str:
    return re.sub(r"^(\s*)#\s*", r"\1", line)

def _ensure_maxevents_minus1(text: str) -> str:
    """
    Force process.maxEvents input to -1.
    Balanced replacement so we don't leave a dangling ')'.
    """
    canon = (
        "process.maxEvents = cms.untracked.PSet(\n"
        "    input = cms.untracked.int32(-1)\n"
        ")\n"
    )
    m = re.search(r"process\.maxEvents\s*=\s*cms\.untracked\.PSet\(", text)
    if not m:
        ins_after = re.search(r"process\.MessageLogger[\s\S]*?\n", text)
        idx = ins_after.end() if ins_after else 0
        return text[:idx] + canon + text[idx:]

    start_pset = m.start()
    i = m.end()   # after '('
    depth = 1
    j = i
    while j < len(text) and depth > 0:
        c = text[j]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        j += 1
    if depth == 0:
        return text[:start_pset] + canon + text[j:]
    return text[:start_pset] + canon + text[start_pset:]

def patch_cmssw_cfg_text(text: str, era: Optional[str]) -> Tuple[str, Dict[str, bool]]:
    lines = text.splitlines(keepends=False)
    has_token_globaltag = False
    has_token_rootfile = False
    new_lines: List[str] = []
    re_era = re.compile(r"^\s*era_\s*=\s*['\"][^'\"]*['\"]")

    for ln in lines:
        if era and re_era.match(ln):
            ln = re.sub(re_era, f"era_     = '{era}'", ln)

        if 'THISGLOBALTAG' in ln:
            ln = _uncomment(ln); has_token_globaltag = True
        elif 'process.GlobalTag' in ln and 'GlobalTag(' in ln and "'" in ln and 'THISGLOBALTAG' not in ln:
            ln = _comment(ln)

        if 'THISROOTFILE' in ln:
            ln = _uncomment(ln); has_token_rootfile = True
        elif 'fileName' in ln and 'THISROOTFILE' not in ln and re.search(r"cms\.string\(\s*'[^']+'\s*\)", ln):
            ln = _comment(ln)

        new_lines.append(ln)

    new_text = "\n".join(new_lines) + "\n"
    new_text = _ensure_maxevents_minus1(new_text)

    return new_text, {
        'has_token_globaltag': has_token_globaltag,
        'has_token_rootfile': has_token_rootfile,
    }

# ========================= Main ===========================
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create CMSSW+CRAB cfgs (era/tokens/maxEvents), optionally submit."
    )
    parser.add_argument('-i', '--inputList', required=True, help='Input dataset list file.')
    parser.add_argument('-d', '--storageDir', dest='storage_dir', required=True, help='Output base dir.')
    parser.add_argument('-t', dest='template_crab', required=True, help='CRAB3 template cfg.')
    parser.add_argument('-c', dest='template_cmssw', required=True, help='CMSSW template cfg.')
    parser.add_argument('-v', dest='tagname', required=True, help='Tag prefix for output folder.')
    parser.add_argument('--lumi-mask', dest='lumi_mask', default=None,
                        help="Optional lumiMask JSON path (requires LUMIMASK token in template).")
    parser.add_argument('--submit', action='store_true', default=False, help='Submit with CRAB.')
    args = parser.parse_args()

    input_list = Path(args.inputList).resolve()
    template_crab = Path(args.template_crab).resolve()
    template_cmssw = Path(args.template_cmssw).resolve()
    storage_base = Path(args.storage_dir).resolve()
    tagname = args.tagname

    for pth, msg in [
        (input_list, "Input list not found"),
        (template_crab, "CRAB template not found"),
        (template_cmssw, "CMSSW template not found"),
    ]:
        if not pth.exists():
            err(f"{msg}: {pth}")
            sys.exit(1)

    lumi_mask_path: Optional[Path] = None
    if args.lumi_mask:
        p = Path(args.lumi_mask).expanduser().resolve()
        if not p.exists():
            err(f"--lumi-mask not found: {p}")
            sys.exit(1)
        lumi_mask_path = p

    stamp = timestamp_label()
    namedir = f"{tagname}_{stamp}"
    out_root = storage_base / namedir
    cfg_dir = out_root / 'cfg'
    work_dir = out_root / 'workdir'
    ensure_dirs([out_root, cfg_dir, work_dir])

    lines = read_input_lines(input_list)
    if not lines:
        err(f"No valid dataset lines in {input_list}")
        sys.exit(1)
    if len(lines) > 1:
        warn(f"Multiple dataset lines ({len(lines)}); using the first.")

    spec = parse_dataset_line(lines[0])
    dataset = spec['dataset']
    processed = spec['processedEvents']  # currently unused
    lumis_per_job = spec['lumisPerJob']
    global_tag = spec['globalTag']
    secondary = spec.get('secondaryDataset')
    era = spec.get('era')

    try:
        sample = dataset.split('/')[1]
        processing = dataset.split('/')[2]
        tier = dataset.split('/')[3]
    except Exception:
        err(f"Bad dataset (expect /Primary/Processing/Tier): {dataset}")
        sys.exit(1)

    request_name = sanitize_request_name(f"{sample}__{processing}__{tier}")
    cmssw_cfg_path = cfg_dir / f"{sample}_cmssw.py"
    crab_cfg_path = cfg_dir / f"{sample}_crab.py"

    tokens = build_tokens(
        dataset=dataset,
        processed_events=processed,
        lumis_per_job=lumis_per_job,
        global_tag=global_tag,
        cfg_path=cmssw_cfg_path,
        working_area=work_dir,
        namedir=namedir,
        lumi_mask=lumi_mask_path,
        secondary_dataset=secondary,
    )

    cmssw_template_text = template_cmssw.read_text()
    tokens_cmssw = dict(tokens)

    if ("THISGLOBALTAG" in cmssw_template_text
            and "'THISGLOBALTAG'" not in cmssw_template_text
            and '"THISGLOBALTAG"' not in cmssw_template_text):
        tokens_cmssw["THISGLOBALTAG"] = f"'{tokens_cmssw['THISGLOBALTAG']}'"

    if ("THISROOTFILE" in cmssw_template_text
            and "'THISROOTFILE'" not in cmssw_template_text
            and '"THISROOTFILE"' not in cmssw_template_text):
        tokens_cmssw["THISROOTFILE"] = f"'{tokens_cmssw['THISROOTFILE']}'"

    # Patch & write CMSSW cfg
    patched_text, checks = patch_cmssw_cfg_text(cmssw_template_text, era)
    if not checks.get('has_token_globaltag', False):
        err("Template must have active THISGLOBALTAG line.")
        sys.exit(1)
    if not checks.get('has_token_rootfile', False):
        err("Template must have active THISROOTFILE line.")
        sys.exit(1)

    final_cmssw = render_template_text(patched_text, tokens_cmssw)
    cmssw_cfg_path.write_text(final_cmssw)

    # Syntax check (catch issues early)
    try:
        py_compile.compile(str(cmssw_cfg_path), doraise=True)
    except py_compile.PyCompileError as e:
        err("CMSSW cfg syntax error.")
        print(e.msg)
        sys.exit(1)

    # Render & write CRAB cfg
    crab_text = Path(template_crab).read_text()
    final_crab = render_template_text(crab_text, tokens)
    crab_cfg_path.write_text(final_crab)

    # Minimal, bright, and crisp output
    ok(f"Prepared: {dataset}")
    print(f"      \033[91mEra:\033[0m {era if era else '(template)'}")
    print(f"      \033[91mCMSSW:\033[0m {cmssw_cfg_path}")
    print(f"      \033[91mCRAB:\033[0m {crab_cfg_path}")

    # Optional submission
    if args.submit:
        if shutil.which('crab') is None:
            err("'crab' not found in PATH.")
            sys.exit(1)

        info("Submitting...")
        try:
            # Capture output to extract essentials
            cp = subprocess.run(
                ['crab', 'submit', '-c', str(crab_cfg_path)],
                text=True, capture_output=True, check=True
            )
            out_all = (cp.stdout or "") + (cp.stderr or "")
            # Extract essentials
            task_name = re.search(r"Task name:\s*(.+)", out_all)
            project_dir = re.search(r"Project dir:\s*(.+)", out_all)
            log_file = re.search(r"Log file is\s*(.+)", out_all)

            ok("Delivered to CRAB3.")
            if task_name:
                print(f"      \033[91mTask:\033[0m {task_name.group(1).strip()}")
            if project_dir:
                print(f"      \033[91mWorkdir:\033[0m {project_dir.group(1).strip()}")
            if log_file:
                print(f"      \033[91mLog:\033[0m {log_file.group(1).strip()}")
        except subprocess.CalledProcessError as e:
            out_all = (e.stdout or "") + (e.stderr or "")
            err(f"CRAB submission failed (exit {e.returncode}).")
            # Try to surface the CRAB workdir/log if present
            m_proj = re.search(r"Project dir:\s*(.+)", out_all)
            m_log = re.search(r"Log file is\s*(.+)", out_all)
            if m_proj:
                print(f"      \033[91mWorkdir:\033[0m {m_proj.group(1).strip()}")
            if m_log:
                print(f"      \033[91mLog:\033[0m {m_log.group(1).strip()}")
            # Show a short tail of the output to help
            tail = "\n".join(out_all.strip().splitlines()[-20:])
            if tail:
                print(_c("  --- crab output (tail) ---", C.Y))
                print(tail)
            sys.exit(e.returncode)

    ok(f"Done: {out_root}")

if __name__ == '__main__':
    main()

