
# Dijet Scouting Run3 NTuple Maker

## Table of Content:

- [Dijet Scouting Run3 NTuple Maker](#dijet-scouting-run3-ntuple-maker)
   * [Setup Analysis Environment](#setup-analysis-environment)
   * [Datasets](#datasets)
      + [QCD MC Samples](#qcd-mc-samples)
      + [CMS DAS Queries](#cms-das-queries)
         - [QCD MC Samples](#qcd-mc-samples-1)
   * [Extra:](#extra)
      + [List all branches in the root file](#list-all-branches-in-the-root-file)
      + [Check the status of your lxplus/cmslpc tasks using a web-based GUI](#check-the-status-of-your-lxpluscmslpc-tasks-using-a-web-based-gui)
      + [How to compute MC cross-sections with GenXSecAnalyzer](#how-to-compute-mc-cross-sections-with-genxsecanalyzer)

## Setup Analysis Environment

Load cmssw libraries:
> Use `.csh` if you're a **csh** user. Check with `echo $0` on your terminal (lxplus/cmslpc).

```
source /cvmfs/cms.cern.ch/cmsset_default.sh
```

Setup CMSSW & Pull nTuple maker framework:

```
cmsrel CMSSW_15_0_6
cd CMSSW_15_0_6/src
cmsenv
git cms-init
git clone git@github.com:asimsek/DijetScoutingRun3NTupleMaker.git
cd DijetScoutingRun3
scram b clean; scram b -j 8
```

[!IMPORTANT]
An active proxy is required to access and process CMS data.

```
voms-proxy-init --voms cms --valid 192:00
```


## Datasets


### QCD MC Samples
|QCD Samples (Run3Winter22 MiniAOD):| xsec |
|--|--|
| /QCD_Pt_50to80_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 16740000 |
| /QCD_Pt_80to120_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 2511000 |
| /QCD_Pt_120to170_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 442000 |
| /QCD_Pt_170to300_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 113700 |
| /QCD_Pt_300to470_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 7621 |
| /QCD_Pt_470to600_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 626 |
| /QCD_Pt_600to800_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 179.7 |
| /QCD_Pt_800to1000_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 30.7 |
| /QCD_Pt_1000to1400_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 8.946 |
| /QCD_Pt_1400to1800_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 0.8098 |
| /QCD_Pt_1800to2400_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 0.1152 |
| /QCD_Pt_2400to3200_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 0.005241 |
| /QCD_Pt_3200toInf_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM | 0.0002303 |



### CMS DAS Queries

#### QCD MC Samples

Require an active proxy with `voms-proxy-init --voms cms --valid 192:00`

`./utils/dasgoclient --query='dataset status=* dataset=/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM'`

`./utils/dasgoclient --query='dataset status=* dataset=/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22DRPremix-122X_mcRun3_2021_realistic_v9-v2/AODSIM'`

[!NOTE]
Please note that we also used the `QCD_Pt_3200toInf_TuneCP5_13p6TeV_pythia8` sample in addition to these queries.





## Extra:

### List all branches in the root file

```
TObjArray* branches = Events->GetListOfBranches();
for (int i=0; i<branches->GetEntries(); i++) { cout << branches->At(i)->GetName() << endl; }
```

### Check the status of your lxplus/cmslpc tasks using a web-based GUI

[!WARNING]
Don't forget to change XXX with the machine that you're conencted for LPC machines.

```
ssh -L localhost:8787:localhost:8787 asimsek@cmslpcXXX.fnal.gov
```

Navigate to `http://localhost:8787` on your browser.


### How to compute MC cross-sections with GenXSecAnalyzer

This tool allows you to use existing cmssw library ([GenXSecAnalyzer.cc](https://github.com/cms-sw/cmssw/blob/master/GeneratorInterface/Core/plugins/GenXSecAnalyzer.cc)) to compute MC cross sections in a more accurate way. This is useful when there is no xsec information given on the [XSDB](https://xsecdb-xsdb-official.app.cern.ch/xsdb/).

[!TIP]
To process multiple datasets at the same time (wildcard), use star (*) character in the dataset query while using the `genXsec_cfg.py` script. (e.g.: `/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM'`).

[!TIP]
If you want to combine multiple datasets to get one cross-section, use `combineSamples=True` along with the given command line.

[!TIP]
You can use comma separated dataset list to process multiple datasets at once without wildcard. (e.g.: dataset="/A/B/C, /X/Y/Z"`)


```
cmsRun utils/genXsec_cfg.py dataset="/QCD_Pt_2400to3200_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM" maxEvents=-1
```

> For more: https://cms-generators.docs.cern.ch/useful-tools-and-links/HowToGenXSecAnalyzer/#during-the-production-of-mc-samples


