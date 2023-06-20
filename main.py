from os import system
from sys import argv, path
from subprocess import check_output

ANSI_CODES = [
    "\x1b[31m",
    "\x1b[32m",
    "\x1b[33m",
    "\x1b[34m",
    "\x1b[0m"
]

if __name__ == "__main__":
    if check_output('whoami') == b'root\n':
        pass
    else:
        print("{}error{}: nvault needs root to run properly".format(ANSI_CODES[0],ANSI_CODES[4]))
        exit(1)
