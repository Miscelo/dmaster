
import shutil
import sys

with open("/etc/fstab", "r") as fobj:
    for line in fobj:
        if line[:4] == 'UUID' or line[:5] == 'LABEL':
            print(line)

""" FunctionReturn True, if there is enough disk space"""
def disk_usage(path, min_emergency, min_critical):
    # Size, Used , Available, Used %
    total, used, free = shutil.disk_usage(path)
    #Cambiamos de Bytes a GB
    totalGB = round(total / 2**30, 2)
    usedGB = round(used / 2**30, 2)
    freeGB = round(free / 2**30, 2)
    used_percent = round(100 * (used / 2**30) / (total / 2**30), 2)

    print("Total: {}GB, Used: {}GB, Available: {}GB, Used: {}%".format(totalGB, usedGB, freeGB, used_percent))


    if (100 - used_percent) < min_emergency:
        print("Emergency alert! Diskspace {}% full.".format(path, used_percent))
        return False
    elif (100 - used_percent) < min_critical:
        print("Emergency alert! Diskspace {}% full.".format(path, used_percent))
        return False
    return True

path = "/boot/"

if not disk_usage(path, 2, 10):
    print("Error, not enough disk space.")
else:
    print("enough")

