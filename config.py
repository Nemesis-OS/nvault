#|================================|
#|nvault: NemesisOS Backup Utility|
#|================================|

DRIVE = ""
MOUNTPOINT = "/nemesis-backup" # the folder where it will be mounted
BACKUP_HOME = True # this option backs up /home
BACKUP_CONFIGS = True # this option backs up  /home/$currentuser/.config.. it needs BACKUP_HOME to be enabled
BACKUP_CACHE = True # this option backs up /home/$currentuser/.cache
BACKUP_NEMESIS_HIST_SNAPSHOTS = True # you can backup your old nemesis-pkg snapshots
BACKUP_NEMESIS_PKG_DIR = True # your IPKGLIST, PKGLIST and config.py will be backed up
BACKUP_BUILD_CACHE = True # your build cache or compiled programs will be saved so in reinstall you dont need to spent hours for compiling 
