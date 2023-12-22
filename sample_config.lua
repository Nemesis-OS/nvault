-- nvault: backup files securely
drive = "your_drive" -- replace your_drive by the drive where nvault will store your files
mountpoint = "mountpoint" -- replace mountpoint by the location where your nvault partition will be mounted

backup = {
    home = true, -- backup /home.. usually true or false
    config = true,
    cache = false,
    snapshots = true,
    pkgdir = true,
    buildcache = false
}

directories = {
    include = {
        "dox",
        "mail",
        "git"
    },
    exclude = {}
}
