
import shutil
import sys

""" FunctionReturn True, if there is enough disk space"""
def disk_usage(path, min_absolute, min_percent):
    # Size, Used , Available, Used %
    total, used, free = shutil.disk_usage(path)
    #Cambiamos de Bytes a GB
    totalGB = total / 2**30
    usedGB = used / 2**30
    freeGB = free / 2**30
    free_percent = 100 * usedGB / totalGB


    print("{} GB free , used {} GB of {} GB".format(round(freeGB,2), round(usedGB, 2), round(totalGB,2)))
    print("{}% free".format(round(free_percent, 2)))

    # return value panic=0, critical=1, alert=3, ...
    if free_percent < min_percent or freeGB < min_absolute:
        return False
    return True

path = "/var/"

if not disk_usage(path, 2, 10):
    print("Error, not enough disk space.")
else:
    print("enough")

a = 109272832 / 1024    #KB
b = a /1024             #MB
c = b/1024              #GB
print(c)
