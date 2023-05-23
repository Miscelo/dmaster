import os
import goodies
import logging.handlers


# Check if config file exist in program folder and if not, it will be created.
def createConfigFile():
    configFile='dmaster.conf'
    if not os.path.isfile(configFile):
        with open(configFile, "w") as fobj:
            fobj.write("# Directorys that dmaster control the disk usage.\n"
                        "directories=/home/,/,/boot,/var\n"
                        "# Set the critical limit of disk usage in % to throw alerts, send reports and create log.\n"
                        "disk_usage_critical=98\n"
                        "# Set the warning limit o disk usage in % to throw alerts, send reports and create log.\n"
                        "disk_usage_warning=90\n"
                        "# Set path to logfile. Example: logfile=/var/log/dmaster.log\n"
                        "logFile=dmaster.log\n"
                        "# Set logging level. Recommend INFO [CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET]\n"
                        "logLevel=INFO)\n")


# returns a dictionary with all config data from dmaster.conf inside.
def getConfigData():
    createConfigFile()
    configs = {}
    try:
        with open("dmaster.conf", "r") as fobj:
            for line in fobj:
                # empty line in file and lines starting with # will be ingored.
                if not len(line.strip()) == 0 and not line.startswith('#'):
                    key = line.split('=')[0].rstrip('\n')
                    value = line.split('=')[1].rstrip('\n')
                    # if there a more values seperated with coma, then value in dictionary will be a list
                    if key == 'directories':
                        value = value.split(',')
                    configs[key] = value
        return configs
    except Exception:
        goodies.log("dmaster.goodies","ERROR", "Config file could not be read.")




# catch logs and printed them in dmaster.log.
def log(loggername='dmaster', loglevel='INFO', message='dmaster fails.'):
    #get path from config file where logs will be stored
    configs = getConfigData()
    logfile = configs['logFile']
    loglevel = configs['logLevel']
    logger = logging.getLogger(loggername)
    level = logging.getLevelName(loglevel)
    logger.setLevel(level)
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(name)s\t['+str(os.getpid())+']: %(levelname)s\t %(message)s')
    fh.setFormatter(formatter)
    sh = logging.StreamHandler()
    logger.addHandler(fh)
    logger.addHandler(sh)
    if loglevel == 'debug':
        logger.debug(message)
    elif loglevel == 'INFO':
        logger.info(message)
    elif loglevel == 'WARNING':
        logger.warning(message)
    elif loglevel == 'ERROR':
        logger.error(message)
    elif loglevel == 'CRITICAL':
        logger.critical(message)
    else:
        pass

