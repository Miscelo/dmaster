
import shutil
import os.path
import goodies
from datetime import datetime


# Function creates a file for diskusage statistics. The first line have column-info.
def writeDiskStats(statsfile, stats):
    # First time executed, in statsfile will be added first line with infos.
    if not os.path.isfile(statsfile):
        try:
            with open(statsfile, "w") as fobj:
                fobj.write("# Date & Time, Size, Used, Available, Used in %\n")
                fobj.write(stats)
        except FileNotFoundError:
            goodies.log("dmaster.diskspace", "ERROR", "File for stats not created.")
        except Exception:
            goodies.log("dmaster.diskspace", "ERROR", "File for stats not created.")
    else:
        try:
            with open(statsfile, "a+") as fobj:
                fobj.write(stats)
        except Exception:
            goodies.log("dmaster.diskspace", "ERROR", "Can not write stats to file diskspace.dat.")



# Function check usage of disk and passed it to a statistic file. If the limits of diskusage are broken, given by
# dmaster.conf file, there will be a log and later soon an email alert.
def disk_usage():
    statsfile = "diskusage.dat"
    now = datetime.now()
    configs = goodies.getConfigData()
    max_critical = float(configs['disk_usage_critical'])
    max_warning = float(configs['disk_usage_warning'])
    pathlist = configs['directories']
    for dir in pathlist:
        # Size, Used , Available, Used %
        total, used, free = shutil.disk_usage(dir)
        #Cambiamos de Bytes a GB
        totalGB = round(total / 2**30, 2)
        usedGB = round(used / 2**30, 2)
        freeGB = round(free / 2**30, 2)
        used_percent = round(100 * (used / 2**30) / (total / 2**30), 2)
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        stats = f'{timestamp},{dir},{totalGB},{usedGB},{freeGB},{used_percent}\n'
        # Pass stats to a file
        writeDiskStats(statsfile, stats)
        message = f"Diskspace on {dir} to {used_percent}% full."
        if (100 - used_percent) < (100 - max_critical):
            goodies.log("dmaster.diskspace", "CRITICAL", message)
            # send mail with 50
        if (100 - max_critical) < (100 - used_percent) and (100 - used_percent) < (100 - max_warning):
            goodies.log("dmaster.diskspace", "WARNING", message)
            # send mail with 30



