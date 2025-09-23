
# Dijet Scouting Run3 NTuple Maker

## Table of Content:

- [Setup Analysis Environment](#setup-analysis-environment)
- [Datasets](#datasets)
   + [Run3 Scouting Datasets](#run3-scouting-datasets)
   + [Run3 Monitoring Datasets](#run3-monitoring-datasets)
   + [Run3 QCD MC Samples](#run3-qcd-mc-samples)
   + [CMS DAS Queries](#cms-das-queries)
- [Extras](#extras)
- [Useful Links](#useful-links)

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

> [!IMPORTANT]
> An active proxy is required to access and process CMS data.

```
voms-proxy-init --voms cms --valid 192:00
```


## Datasets

### Run3 Scouting Datasets

|<sup><sub>2024 Datasets</sub></sup>|<sup><sub>2025 Datasets</sub></sup>|
|--|--|
|<sup><sub>/ScoutingPFRun3/Run2024C-v1/HLTSCOUT</sub></sup>|<sup><sub>/ScoutingPFRun3/Run2025B-v1/HLTSCOUT</sub></sup>|
|<sup><sub>/ScoutingPFRun3/Run2024D-v1/HLTSCOUT</sub></sup>|<sup><sub>/ScoutingPFRun3/Run2025C-v1/HLTSCOUT</sub></sup>|
|<sup><sub>/ScoutingPFRun3/Run2024E-v1/HLTSCOUT</sub></sup>|<sup><sub>/ScoutingPFRun3/Run2025D-v1/HLTSCOUT</sub></sup>|
|<sup><sub>/ScoutingPFRun3/Run2024F-v1/HLTSCOUT</sub></sup>|<sup><sub>/ScoutingPF[0,1]/Run2025E-v1/HLTSCOUT</sub></sup>|
|<sup><sub>/ScoutingPFRun3/Run2024G-v1/HLTSCOUT</sub></sup>|<sup><sub>/ScoutingPF[0,1]/Run2025F-v1/HLTSCOUT</sub></sup>|
|<sup><sub>/ScoutingPFRun3/Run2024H-v1/HLTSCOUT</sub></sup>||
|<sup><sub>/ScoutingPFRun3/Run2024I-v1/HLTSCOUT</sub></sup>||


### Run3 Monitoring Datasets

|<sup><sub>2024 Datasets</sub></sup>|<sup><sub>2025 Datasets</sub></sup>|
|--|--|
|<sup><sub>/ScoutingPFMonitor/Run2024C-v1/RAW</sub></sup>|<sup><sub>/ScoutingPFMonitor/Run2024B-v1/RAW</sub></sup>|
|<sup><sub>/ScoutingPFMonitor/Run2024D-v1/RAW</sub></sup>|<sup><sub>/ScoutingPFMonitor/Run2025C-v1/RAW</sub></sup>|
|<sup><sub>/ScoutingPFMonitor/Run2024E-v1/RAW</sub></sup>|<sup><sub>/ScoutingPFMonitor/Run2025D-v1/RAW</sub></sup>|
|<sup><sub>/ScoutingPFMonitor/Run2024F-v1/RAW</sub></sup>|<sup><sub>/ScoutingPFMonitor/Run2025E-v1/RAW</sub></sup>|
|<sup><sub>/ScoutingPFMonitor/Run2024G-v1/RAW</sub></sup>|<sup><sub>/ScoutingPFMonitor/Run2025F-v1/RAW</sub></sup>|
|<sup><sub>/ScoutingPFMonitor/Run2024H-v1/RAW</sub></sup>||
|<sup><sub>/ScoutingPFMonitor/Run2024I-v1/RAW</sub></sup>||


### Run3 QCD MC Samples

| <sup><sub>QCD Samples (Run3Winter22 MiniAOD)</sub></sup>| <sup><sub>cross section (xsec)</sub></sup>|
|--|--|
| <sup><sub>/QCD_Pt_50to80_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>16740000</sub></sup> |
| <sup><sub>/QCD_Pt_80to120_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>2511000</sub></sup> |
| <sup><sub>/QCD_Pt_120to170_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>442000</sub></sup> |
| <sup><sub>/QCD_Pt_170to300_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>113700</sub></sup> |
| <sup><sub>/QCD_Pt_300to470_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>7621</sub></sup> |
| <sup><sub>/QCD_Pt_470to600_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>626</sub></sup> |
| <sup><sub>/QCD_Pt_600to800_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>179.7</sub></sup> |
| <sup><sub>/QCD_Pt_800to1000_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>30.7</sub></sup> |
| <sup><sub>/QCD_Pt_1000to1400_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>8.946</sub></sup> |
| <sup><sub>/QCD_Pt_1400to1800_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>0.8098</sub></sup> |
| <sup><sub>/QCD_Pt_1800to2400_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>0.1152</sub></sup> |
| <sup><sub>/QCD_Pt_2400to3200_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>0.007591</sub></sup> |
| <sup><sub>/QCD_Pt_3200toInf_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM</sub></sup> | <sup><sub>0.0002303</sub></sup> |



### CMS DAS Queries

> [!IMPORTANT]
> An active proxy is required to access and process CMS data.

```
voms-proxy-init --voms cms --valid 192:00
```

#### Run3 Scouting Datasets

```
./utils/dasgoclient --query='dataset status=* dataset=/ScoutingPFRun3/Run2024*/HLTSCOUT'`
```

```
./utils/dasgoclient --query='dataset status=* dataset=/ScoutingPFRun3/Run2025*/HLTSCOUT'`
```


#### Run3 Monitoring Datasets

```
./utils/dasgoclient --query='dataset status=* dataset=/ScoutingPFMonitor/Run2024*/RAW'`
```

```
./utils/dasgoclient --query='dataset status=* dataset=/ScoutingPFMonitor/Run2025*/RAW'`
```


#### Run3 QCD MC Samples

```
./utils/dasgoclient --query='dataset status=* dataset=/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM'`
```

```
./utils/dasgoclient --query='dataset status=* dataset=/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22DRPremix-122X_mcRun3_2021_realistic_v9-v2/AODSIM'`
```

> [!NOTE]
> Please note that we also used the `QCD_Pt_3200toInf_TuneCP5_13p6TeV_pythia8` sample in addition to these queries.





## Extras

### 1) List all branches in the official root file

```
TObjArray* branches = Events->GetListOfBranches();
for (int i=0; i<branches->GetEntries(); i++) { cout << branches->At(i)->GetName() << endl; }
```

### 2) Check the status of your lxplus/cmslpc tasks using a web-based GUI

> [!WARNING]
> Don't forget to change XXX with the machine that you're conencted for LPC machines.

```
ssh -L localhost:8787:localhost:8787 asimsek@cmslpcXXX.fnal.gov
```

Navigate to `http://localhost:8787` on your browser.


### 3) How to compute MC cross-sections with GenXSecAnalyzer

This tool allows you to use existing cmssw library ([GenXSecAnalyzer.cc](https://github.com/cms-sw/cmssw/blob/master/GeneratorInterface/Core/plugins/GenXSecAnalyzer.cc)) to compute MC cross sections in a more accurate way. This is useful when there is no xsec information given on the [XSDB](https://xsecdb-xsdb-official.app.cern.ch/xsdb/).

> [!WARNING]
> Please provide the dataset as an input to facilitate more precise cross-section calculations, as relying on a single file will yield only a rough estimate.


```
cmsRun utils/genXsec_cfg.py inputFiles="/store/mc/Run3Winter22DRPremix/QCD_Pt_50to80_TuneCP5_13p6TeV_pythia8/AODSIM/122X_mcRun3_2021_realistic_v9-v2/60000/00013e73-2f84-4d54-a6f5-cfdfafb08614.root" maxEvents=-1
```

```
cmsRun utils/genXsec_cfg.py dataset="/QCD_Pt_2400to3200_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM" maxEvents=-1
```


> [!TIP]
> Wildcard dataset searches are allowed. Please use star (\*) character in the dataset query while using the `genXsec_cfg.py` script. (e.g.: `/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM'`).


> [!TIP]
> You can use comma separated dataset list to process multiple datasets at once without wildcard. (e.g.: dataset="/A/B/C, /X/Y/Z"`)

> [!TIP]
> If you want to combine multiple datasets to get one cross-section, use `combineSamples=True` along with the given command line.

> For more: https://cms-generators.docs.cern.ch/useful-tools-and-links/HowToGenXSecAnalyzer/#during-the-production-of-mc-samples



## Useful Links

 + [Run3 Luminosity and uncertainty recommendations](https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun3)
 + [Golden JSON](https://cms-service-dqmdc.web.cern.ch/CAF/certification/)
 + [BrilCalc - Lumi Calculation](https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html)
 + [Run3 JERC](https://cms-jerc.web.cern.ch/)
 + [Run3 PdmV](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis)
 + [JES/JER for Run3 Scouting](https://twiki.cern.ch/twiki/bin/view/CMSPublic/)



