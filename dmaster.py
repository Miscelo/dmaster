#!/usr/bin/env python3
import diskspace
import dports
import goodies


'''
Main program that will handle a menu.
'''

def main():
    print("************* DMASTER ***************")
    diskspace.disk_usage()
    openports = dports.openports()
    print(openports)



if __name__ == "__main__":
    main()
