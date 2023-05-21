
import shutil
import os.path
import logging
from datetime import datetime

now = datetime.now()




""" FunctionReturn True, if there is enough disk space"""
def disk_usage(path, min_emergency, min_critical, now, statsfile):
    # Size, Used , Available, Used %
    total, used, free = shutil.disk_usage(path)
    #Cambiamos de Bytes a GB
    totalGB = round(total / 2**30, 2)
    usedGB = round(used / 2**30, 2)
    freeGB = round(free / 2**30, 2)
    used_percent = round(100 * (used / 2**30) / (total / 2**30), 2)
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    stats = timestamp+","+path+","+str(totalGB)+","+str(usedGB)+","+str(freeGB)+","+str(used_percent)
    writeDiskStats(statsfile, stats)

    if (100 - used_percent) < min_emergency:
        print("Emergency alert! Diskspace {}% full.".format(path, used_percent))
        return False
    elif (100 - used_percent) < min_critical:
        print("Emergency alert! Diskspace {}% full.".format(path, used_percent))
        return False
    return True


def writeDiskStats(statsfile, stats):
    if not os.path.isfile(statsfile):
        try:
            with open(statsfile, "w") as fobj:
                fobj.write("Date & Time, Size, Used, Available, Used in %\n")
        except Exception:
            print("Error to access to file {}. Please check permissions.".format(statsfile))
            logging.warning("ERROR dmaster: diskspace - can not create file for stats.")
    else:
        try:
            with open(statsfile, "a+") as fobj:
                fobj.write(stats)
        except Exception:
            print("Error to access to file {}. Please check permissions.".format(statsfile))
            logging.warning("ERROR dmaster: diskspace - can not write stats to file.")




path = "/boot/"
min_emerg = 2
min_critical = 10
a = disk_usage(path, min_emerg, min_critical, now, "diskspace.dat")

