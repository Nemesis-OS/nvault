from os import system, chdir, mkdir
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
    chdir("/etc/nvault")
    path.append("/etc/nvault")
    import config

    if config.DRIVE != '':
        print("{}note{}: checking if {} exists..".format(ANSI_CODES[3], ANSI_CODES[4], config.DRIVE))
        drive_exists = False
        drives = check_output('blkid').decode('utf-8').splitlines()
        for i in range(0, len(drives)):
            if config.DRIVE in drives[i]:
                drive_exists = True
                break
            else:
                continue

        if drive_exists == True:
            print("{}sucess{}: {} found".format(ANSI_CODES[1], ANSI_CODES[4], config.DRIVE))
            pass
        else:
            print("{}error{}: {} is not found.. either select a different partition or create a seperate partition".format(ANSI_CODES[0], ANSI_CODES[4], config.DRIVE))
            exit(1)
    else:
        print("{}error{}: drive is not defined so exiting".format(ANSI_CODES[0], ANSI_CODES[4]))
        exit(1)

    if config.MOUNTPOINT != '':
        print("{}note{}: checking if {} exists..".format(ANSI_CODES[3], ANSI_CODES[4] , config.MOUNTPOINT))
        if isdir(config.MOUNTPOINT) == False:
            print("{}warning{}: the mountpoint does not exist on the filesystem so creating it.".format(ANSI_CODES[2], ANSI_CODES[4]))
            mkdir(config.MOUNTPOINT)
        else:
            print("{}sucess{}: the mountpoint exists on the filesystem so continuing".format(ANSI_CODES[1], ANSI_CODES[4]))
    else:
        print("{}error{} no mountpoint is specified.. please specify a mountpoint".format(ANSI_CODES[0], ANSI_CODES[4]))

    if config.BACKUP_HOME == True or config.BACKUP_HOME == False and config.BACKUP_CACHE == True or config.BACKUP_CACHE == False and config.BACKUP_NEMESIS_PKG_DIR == True or BACKUP_NEMESIS_PKG_DIR == False and BACKUP_BUILD_CACHE == True or BACKUP_BUILD_CACHE == False and BACKUP_NEMESIS_HIST_SNAPSHOTS == True or BACKUP_NEMESIS_HIST_SNAPSHOTS == False:
        print("{}note{}: configuring the other variables to determine somethibgs..".format(ANSI_CODES[3], ANSI_CODES[4]))
        BACKUP_HOME = config.BACKUP_HOME
        BACKUP_CACHE = config.BACKUP_CACHE
        BACKUP_NEMESIS_HIST_SNAPSHOTS = config.BACKUP_NEMESIS_HIST_SNAPSHOTS
        BACKUP_NEMESIS_PKG_DIR = config.BACKUP_NEMESIS_PKG_DIR
        BACKUP_CONFIGS = config.BACKUP_CACHE
        BACKUP_BUILD_CACHE = config.BACKUP_BUILD_CACHE
        print("{}sucess{}: the variables were configured succesfully and configuration applied".format(ANSI_CODES[1], ANSI_CODES[4]))
    else:
        print("{}error{}: the rest other variables need to be either True or False.".format(ANSI_CODES[0], ANSI_CODES[4]))
        exit(1)
        
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
except NameError:
    print("{}error{}: something went wrong!.. please check you config file for any errors/misspells".format(ANSI_CODES[0], ANSI_CODES[4]))
