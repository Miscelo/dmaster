
import shutil
import sys

""" FunctionReturn True, if there is enough disk space"""
def disk_usage(disk, min_absolute, min_percent):
    diskusage = shutil.disk_usage(disk)
    free_percent = (100 * diskusage.free / diskusage.total)
    print(free_percent)
    return True

path = "/var/"
if not disk_usage(path, 2, 10):
    print("Error, not enough disk space.")
    sys.exit(1)
else:
    print("enough")

