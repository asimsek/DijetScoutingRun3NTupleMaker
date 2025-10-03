from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = '/uscms_data/d3/asimsek/Dijet_Run3/treeMaker/CMSSW_15_0_6/src/DijetScoutingRun3NTupleMaker/submitCrab3Jobs/Output_ScoutingPFRun3/ScoutingPFRun3_Run2024C-v1_03October2025_20251003_1500/workdir'
config.General.requestName = 'ScoutingPFRun3__Run2024C-v1__HLTSCOUT'

config.section_('JobType')
config.JobType.psetName = '/uscms_data/d3/asimsek/Dijet_Run3/treeMaker/CMSSW_15_0_6/src/DijetScoutingRun3NTupleMaker/submitCrab3Jobs/Output_ScoutingPFRun3/ScoutingPFRun3_Run2024C-v1_03October2025_20251003_1500/cfg/ScoutingPFRun3_cmssw.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ScoutingPFRun3__Run2024C-v1__HLTSCOUT.root']

config.section_('Data')
config.Data.inputDataset = '/ScoutingPFRun3/Run2024C-v1/HLTSCOUT'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 20 #without '' since it must be an int
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.publication = False
#config.Data.lumiMask = '../data/json/Cert_Collisions2024_378981_386951_Golden.json'
config.Data.outLFNDirBase = '/store/group/lpcjj/CaloScouting/Run3PFScouting/rootTrees_big/2024/ScoutingPFRun3/'
#config.Data.ignoreLocality = True

config.section_('User')

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
