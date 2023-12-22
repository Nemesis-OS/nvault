#!/usr/bin/env csto

local mount_point = "/nemesis-backup" -- mountpoint location

-- if check_mountpoint().. see if mountpoint exists
function check_mountpoint()
  if not fs.exists(mount_point) then
    print("=> \x1b[1m\x1b[33mwarning:\x1b[0m mountpoint was not found so made it")
    fs.mkdir(mount_point)
  end
end

-- check if user is root
if environ["USER"] ~= "root" then
  print("=> \x1b[1m\x1b[31merror:\x1b[0m nvault requires root to run")
end

check_mountpoint()
