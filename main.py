from os import system
from os.path import isfile, isdir
from sys import argv, path
from subprocess import check_output

ANSI_CODES = [
    "\x1b[31m",
    "\x1b[32m",
    "\x1b[33m",
    "\x1b[34m",
    "\x1b[0m"
]

DRIVE = ''
MOUNTPOINT = '/nemesis-backup'
BACKUP_HOME = True
BACKUP_CONFIGS = True
BACKUP_CACHE = True
BACKUP_NEMESIS_HIST_SNAPSHOTS = True
BACKUP_NEMESIS_PKG_DIR = True
BACKUP_BUILD_CACHE = True

def parse_config():
    global DRIVE, MOUNTPOINT, BACKUP_HOME, BACKUP_CACHE, BACKUP_NEMESIS_HIST_SNAPSHOTS, BACKUP_BUILD_CACHE, BACKUP_NEMESIS_PKG_DIR
    print("{}note{}: checking if config file is found or not".format(ANSI_CODES[3], ANSI_CODES[4]))
    if isfile("/etc/nvault/config.py") == True:
        pass
    else:
        print("{}warning{}: config file is not on path so using the fallback config".format(ANSI_CODES[2], ANSI_CODES[4]))
        DRIVE = str(input("{}note{}: the fallback config does not have any drives defined so please enter the target drive: ".format(ANSI_CODES[3], ANSI_CODES[4])))
        return "UseFallBack"

    print("{}sucess{}: config found so setting the variables..".format(ANSI_CODES[1] , ANSI_CODES[4]))
    path.append("/etc/nvault")
    

try:
    if __name__ == "__main__":
        if check_output('whoami') == b'root\n':
            pass
        else:
            print("{}error{}: nvault needs root to run properly".format(ANSI_CODES[0],ANSI_CODES[4]))
            exit(1)

        parse_config()
except KeyboardInterrupt:
    print("{} error{}: user pressed ctrl-c so exiting".format(ANSI_CODES[0], ANSI_CODES[4]))
    exit(1)

