
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


### Run nTuple maker locally

> [!IMPORTANT]
> An active proxy is required to access and process CMS data.

```
voms-proxy-init --voms cms --valid 192:00
```


> [!WARNING]
> Please ensure that the correct era, globalTag, and input-root-file is used in the `ScoutingTreeMakerRun3/python/ScoutingTreeMakerRun3.py` script. <br>
> Also, ensure that the JEC paths are properly specified in the `data/cfg/data_jec_list.txt` (or `mc_jec_list`) file.


```
cmsRun ScoutingTreeMakerRun3/python/ScoutingTreeMakerRun3.py
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

| <sup><sub>QCD Samples (RunIII2024Summer24 AODSIM)</sub></sup>| <sup><sub>cross section (xsec)</sub></sup>|
|--|--|
| <sup><sub>/QCD_Bin-PT-50to80_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>16730000</sub></sup> |
| <sup><sub>/QCD_Bin-PT-80to120_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>2506000</sub></sup> |
| <sup><sub>/QCD_Bin-PT-120to170_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>439800</sub></sup> |
| <sup><sub>/QCD_Bin-PT-170to300_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>113300</sub></sup> |
| <sup><sub>/QCD_Bin-PT-300to470_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>7581</sub></sup> |
| <sup><sub>/QCD_Bin-PT-470to600_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>623.3</sub></sup> |
| <sup><sub>/QCD_Bin-PT-600to800_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>178.7</sub></sup> |
| <sup><sub>/QCD_Bin-PT-800to1000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>30.62</sub></sup> |
| <sup><sub>/QCD_Bin-PT-1000to1500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>9.306</sub></sup> |
| <sup><sub>/QCD_Bin-PT-1500to2000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>0.5015</sub></sup> |
| <sup><sub>/QCD_Bin-PT-2000to2500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>0.04264</sub></sup> |
| <sup><sub>/QCD_Bin-PT-2500to3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>0.004454</sub></sup> |
| <sup><sub>/QCD_Bin-PT-3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24DRPremix-140X_mcRun3_2024_realistic_v26-v2/AODSIM</sub></sup> | <sup><sub>0.0005539</sub></sup> |




> [!NOTE]
> Scouting content (eg.: `Run3ScoutingPFJet_hltScoutingPFPacker`) is not available in the `MINIAODSIM` format.


### CMS DAS Queries

> [!IMPORTANT]
> An active proxy is required to access and process CMS data.

```
voms-proxy-init --voms cms --valid 192:00
```

#### Run3 Scouting Datasets

```
./utils/dasgoclient --query='dataset dataset=/ScoutingPFRun3/Run2024*/HLTSCOUT'
```

```
./utils/dasgoclient --query='dataset dataset=/ScoutingPFRun3/Run2025*/HLTSCOUT'
```


#### Run3 Monitoring Datasets

```
./utils/dasgoclient --query='dataset dataset=/ScoutingPFMonitor/Run2024*/RAW'
```

```
./utils/dasgoclient --query='dataset dataset=/ScoutingPFMonitor/Run2025*/RAW'
```


#### Run3 QCD MC Samples

```
./utils/dasgoclient --query='dataset dataset=/QCD_*PT-*0_TuneCP5_13p6TeV_pythia8/Run*Summer*/AODSIM'
```



#### Run3 Signal Samples

```
./utils/dasgoclient --query='dataset dataset=/RSGravitonToQuarkQuark*kMpl*/Run*Summer2*/AODSIM'
```

```
./utils/dasgoclient --query='dataset dataset=/RSGravitonTo2G_kMpl-001*/Run*Summer2*/AODSIM'
./utils/dasgoclient --query='dataset dataset=/RSGravitonToGluonGluon_kMpl*_TuneCP5_13p6TeV_pythia8/Run*Summer2*/AODSIM'
```

```
./utils/dasgoclient --query='dataset dataset=/Qstarto2J*/Run*Summer2*/AODSIM'
```



## Extras

### 1) List all branches in the official root file

> [!NOTE]
> You need an active proxy (voms) (and a prefix `root://cms-xrd-global.cern.ch/` for the root paths if you're trying to access outside the CERN machines (lxplus), e.g.: LPC-machines) to be able to access root file and list the branches.


```
cmsenv
./utils/edmDumpEventFields root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root --tree Events --filter Run3ScoutingPFJets_hltScoutingPFPacker --what fields --show-types
```

> [!TIP]
> Auto-selects the largest tree if `--tree` is missing. <br>
> `--show-types` displays object types (float, vector, etc.) <br>
> `--summary` prints a compact per-branch table. <br>
> `--format {json|yaml|csv|raw}`


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
cmsRun ./utils/genXsec_cfg.py inputFiles="root://cms-xrd-global.cern.ch//store/mc/RunIII2024Summer24DRPremix/QCD_Bin-PT-50to80_TuneCP5_13p6TeV_pythia8/AODSIM/140X_mcRun3_2024_realistic_v26-v2/120000/005210b9-bf51-4f56-be43-814a093fc0af.root" maxEvents=-1
```

```
cmsRun ./utils/genXsec_cfg.py dataset="/QCD_Pt_2400to3200_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM" maxEvents=-1
```


> [!TIP]
> Wildcard dataset searches are allowed. Please use star (\*) character in the dataset query while using the `genXsec_cfg.py` tool. (e.g.: `/QCD_Pt_*0to*0_TuneCP5_13p6TeV_pythia8/Run3Winter22MiniAOD-122X_mcRun3_2021_realistic_v9-v2/MINIAODSIM'`).


> [!TIP]
> You can use comma separated dataset list to process multiple datasets at once without wildcard. (e.g.: dataset="/A/B/C, /X/Y/Z"`)

> [!TIP]
> If you want to combine multiple datasets to get one cross-section, use `combineSamples=True` along with the given command line.

> For more: https://cms-generators.docs.cern.ch/useful-tools-and-links/HowToGenXSecAnalyzer/#during-the-production-of-mc-samples


### 4) How to print available plugins within CMSSW

```
edmPluginDump | grep -i scouting
```


### 5) List all available edm tools in CMSSW

```
ls $CMSSW_RELEASE_BASE/bin/$SCRAM_ARCH/edm*
```


### 6) Check dataset availability on sites

```
./utils/check_dataset_completeness /QCD_PT-*0_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM --check-files
```

```
./utils/check_dataset_completeness /Qstarto2J_M-*_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM

```

> [!TIP]
> Input list is also supported with the `--input <yourList>` argument. <br>
> Only show sites where dataset presence is 100% (`--full_presence`). <br>
> Use `--include-tapes` to show **TAPE** information alongside **DISK** details.
> The use of wildcard (`*`) in the dataset argument is supported.



### 7) XRootD (XRD) Commands

#### XRDFS:: Root file size (if not availble on the given EOS path):

```
xrdfs root://cms-xrd-global.cern.ch stat /store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root | awk '/Size/{print $2}' | numfmt --to=iec
dasgoclient -query='file file=/store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root | grep file.size'
```

> [!TIP]
> The output of the `xrdfs` command provides the file size in bytes. <br>
> To convert into humand readable version, add ` | awk '/Size/{print $2}' | numfmt --to=iec` at the end of the `xrdfs` command.
> Only ` | numfmt --to=iec` enough for the `dasgoclient` command.


#### XRDCP:: Download Root with XRD Path (root://....)

```
xrdcp root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root .
```

> [!WARNING]
> You may need to install XRootD client: `brew install xrootd`
> If homebrew is not installed: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`



### 8) Find Global Tag info with edmProvDump

```
edmProvDump root://cms-xrd-global.cern.ch//store/data/Run2025C/ScoutingPFRun3/HLTSCOUT/v1/000/392/925/00000/b95d5cc9-62b2-4b3b-a0f9-d0d79b52a85d.root | grep 'globaltag'
```


## Useful Links

 + [Run3 Luminosity and uncertainty recommendations](https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun3)
 + [Golden JSON](https://cms-service-dqmdc.web.cern.ch/CAF/certification/)
 + [BrilCalc - Lumi Calculation](https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html)
 + [Run3 JERC](https://cms-jerc.web.cern.ch/)
 + [Run3 PdmV](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis)
 + [JES/JER for Run3 Scouting](https://twiki.cern.ch/twiki/bin/view/CMSPublic/)
 + [CMS Connect to submit jobs to CERN HTCondor (faster than the LPC condor)](https://uscms.org/uscms_at_work/computing/setup/batch_systems.shtml#CMSConnect)



