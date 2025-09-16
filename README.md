# Dijet Scouting Run3 NTuple Maker


### Setup environment

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



