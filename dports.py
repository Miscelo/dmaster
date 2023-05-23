#!/usr/bin/env python3

import goodies
import socket
import time

# Function return local IP to use it in openports() function.
def getIP():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        local_ip = sock.getsockname()[0]
        sock.close()
    except Exception:
        goodies.log("dmaster.dports", "ERROR", "Can not establish socket connection to find local IP Address.")
    return local_ip



# Function check open ports in the whole range.
def openports(target=getIP()):
    target_IP = socket.gethostbyname(target)
    portlist = []
    try:
        for port in range(1, 65534):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((target_IP, port))
            if res == 0:
                # create a list with open ports
                portlist.append(port)
            sock.close()
    except Exception:
        goodies.log("dmaster.dports", "ERROR", "Can not scan ports on local machine. Socket Problem")
    return portlist
