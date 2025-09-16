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






# Extra:

### List all branches in the root file:

```
TObjArray* branches = Events->GetListOfBranches();
for (int i=0; i<branches->GetEntries(); i++) { cout << branches->At(i)->GetName() << endl; }
```


### Check the status of your lxplus/cmslpc tasks using a web-based GUI:

> Don't forget to change XXX with the machine that you're conencted for LPC machines. 

```
ssh -L localhost:8787:localhost:8787 asimsek@cmslpcXXX.fnal.gov
```

Navigate to `http://localhost:8787` on your browser.




