import os
import logging.handlers


# Check if config file exist in program folder and if not, it will be created.
def createConfigFile():
    configFile='dmaster.conf'
    if not os.path.isfile(configFile):
        with open(configFile, "w") as fobj:
            fobj.write("# Directorys that dmaster control the disk usage.\n"
                        "directories=/,/home/,/var,/boot\n"
                        "# Set path to logfile. Example: logfile=/var/log/dmaster.log\n"
                        "logFile=dmaster.log\n"
                        "# Set logging level. Recommend INFO [CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET]\n"
                        "logLevel=INFO\n")


# Get path and file where to store the logging file get from dmaster.conf file.
# Preconfiguration is main program folder 'logfile=dmaster.conf'
def getLogFilefromConfig():
    createConfigFile()
    logfile=""
    try:
        with open("dmaster.conf", "r") as flog:
            for line in flog:
                if line.startswith('logFile'):
                    logfile = line.split("=")[1].rstrip('\n')
        return logfile
    except Exception:
        log("dmaster.goodies", "WARNING", "Could not read dmaster.conf file")
    finally:
        # Precase, if dmaster.conf is not readable
        return 'dmaster.log'



# Get loglevel for logging file from dmaster.conf file.
# [CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0]
def getLogLevel():
    createConfigFile()
    level=""
    try:
        with open("dmaster.conf", "r") as flog:
            for line in flog:
                if line.startswith('logLevel'):
                    level=line.split("=")[1].rstrip('\n')
        return level
    except Exception:
        log("dmaster.goodies", "WARNING", "Could not read dmaster.conf file.")
    finally:
        return 'INFO'


# catch logs and printed them in dmaster.log.
def log(loggername='dmaster', loglevel=getLogLevel(), message='dmaster fails.'):
    logger = logging.getLogger(loggername)
    level = logging.getLevelName(loglevel)
    logger.setLevel(level)
    logfile = getLogFilefromConfig()
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(name)s\t['+str(os.getpid())+']: %(levelname)s\t %(message)s')
    fh.setFormatter(formatter)
    sh = logging.StreamHandler()
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.debug(message)
    logger.info(message)
    logger.warning(message)
    logger.error(message)
    logger.critical(message)

