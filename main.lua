#!/usr/bin/env csto

local mount_point = "/nemesis-backup" -- mountpoint location
local drive = "" -- drive for nvault backup
local config_path = "/etc/nvault/config.lua" -- default config path

config = {}

-- if check_mountpoint().. see if mountpoint exists
local function check_mountpoint(point)
  if not fs.exists(point) then
    print("=> \x1b[1m\x1b[33mWARNING:\x1b[0m mountpoint was not found so made it")
    fs.mkdir(point)
  else
    print("=> \x1b[32m\x1b[1mSUCESS:\x1b[0m mountpoint found in system")
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
    print("=> \x1b[1m\x1b[34mNOTE:\x1b[0m config found.. using config")
    loadfile(config_path, "t", config)()
  end

  print("=> \x1b[34m\x1b[1mNOTE:\x1b[0m checking mountpoint")

  if config.mountpoint ~= nil then
    check_mountpoint(config.mountpoint)
  else
    print("=> \x1b[31m\x1b[1mCONFIG ERROR:\x1b[0m mountpoint is undefined")
  end

  if config.backup.home then
      if type(config.backup.home) ~= "boolean" then
	  print("=> \x1b[1m\x1b[31mCONFIG ERROR:\x1b[0m\x1b[1m \x1b[33mbackup.home\x1b[0m expected to be a boolean.")
	  os.exit(1)
      else
	  print("=> \x1b[1m\x1b[34mNOTE:\x1b[0m\x1b[1m\x1b[33m /home\x1b[0m will be backed up.")
      end
  end

  if config.directories then
      if type(config.directories) ~= "table" then
	  print("=> \x1b[1m\x1b[31mCONFIG ERROR: \x1b[33mconfig.directories\x1b[0m expected to be a table")
	  os.exit(1)
      end
  else
      print("=> \x1b[31m\x1b[1mCONFIG ERROR: \x1b[33mconfig.directories\x1b[0m not found in config")
      os.exit(1)
  end

  if config.directories.include and type(config.directories.include) == "table" then
      print("=> \x1b[34m\x1b[1mNOTE:\x1b[0m verifying the availability of optional backup directories")
      for k, v in pairs(config.directories.include) do
	  if not fs.isdirectory(v) then
	      str = " -> looking for \x1b[33m\x1b[1m%s\x1b[0m.. \x1b[31m\x1b[1mNOT FOUND\x1b[0m"
	      print(str.format(str, v))
	  else
	      str = " -> looking for \x1b[33m\x1b[1m%s\x1b[0m.. \x1b[32m\x1b[1mFOUND\x1b[0m"
	      print(str.format(str, v))
	  end
      end
  else
      print("=> \x1b[31m\x1b[1mCONFIG ERROR:\x1b[0m \x1b[33m\x1b[1mconfig.directories\x1b[0m is expected to be a table")
  end
end

-- check if user is root
if environ["USER"] ~= "root" then
  print("=> \x1b[1m\x1b[31mERROR:\x1b[0m nvault requires root to run")
  os.exit(1)
end

parse_config()
