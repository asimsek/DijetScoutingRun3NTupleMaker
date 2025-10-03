from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = 'WORKINGAREA'
config.General.requestName = 'WORKINGDIR'

config.section_('JobType')
config.JobType.psetName = 'CMSSWCFG'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['OUTFILENAME']

config.section_('Data')
config.Data.inputDataset = 'INPUTDATASET'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = LUMISPERJOB #without '' since it must be an int
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.publication = False
#config.Data.lumiMask = '../data/json/Cert_Collisions2024_378981_386951_Golden.json'
config.Data.outLFNDirBase = '/store/group/lpcjj/Run3PFScouting/rootTrees_big/2024/'
#config.Data.ignoreLocality = True

config.section_('User')

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
