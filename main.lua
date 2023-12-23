#!/usr/bin/env csto

local mount_point = "/nemesis-backup" -- mountpoint location
local drive = "" -- drive for nvault backup
local config_path = "/etc/nvault/config.lua" -- default config path

config = {}

-- if check_mountpoint().. see if mountpoint exists
local function check_mountpoint(point)
  if not fs.exists(point) then
    print("=> \x1b[1m\x1b[33mwarning:\x1b[0m mountpoint was not found so made it")
    fs.mkdir(point)
  else
    print("=> \x1b[32m\x1b[1msucess:\x1b[0m mountpoint found in system")
  end
end

local function mount_drive(drive)
  -- In Linux drives are usually a file like /dev/sda1 is a file.. if it gets a file which exists
  -- then it will mount it to verify rather it works or not and return true or nil
  print(drive)

  if not fs.exists(drive) then
    return nil -- drive exists
  end

  local mount_cmd = "mount %s /mnt"
  if os.execute(mount_cmd:format(mount_cmd, drive)) then
    return true -- drive has been mounted
  end

  return nil -- drive failed to mount
end

local function parse_config()
  if fs.exists(config_path) then
    print("=> \x1b[1m\x1b[34mnote:\x1b[0m config found.. using config")
    loadfile(config_path, "t", config)()
  end

  print("=> \x1b[34m\x1b[1mnote:\x1b[0m checking mountpoint")

  if config.mountpoint ~= nil then
    check_mountpoint(config.mountpoint)
  else
    print("=> \x1b[31m\x1b[1merror:\x1b[0m mountpoint is undefined")
  end
end

-- check if user is root
if environ["USER"] ~= "root" then
  print("=> \x1b[1m\x1b[31merror:\x1b[0m nvault requires root to run")
  os.exit(1)
end
parse_config()
