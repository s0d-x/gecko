#
#   python header/module (exec)
#--------------------------
#   shell.py
#   
#   shell environment for gecko (gecko-sh)
#

#---
#   COMMANDS -
#       exit, help, clear/cls, info
#

import info
import cmds
from info import *
from colors import *

def execute_commands(cmd):
    try:
        subprocess.run(cmd.split())
    except Exception:
        print(bold + red + cmds.shname + reset + white + ": command not found:" + bold + " {}".format(cmd))

#------------------
#   Shell Prompt
#------------------
#   Variable = prompt
#
prompt = bold + pjclr + info.ficnt["name"] + yellow + " >" + reset + " "
#------------------

cmds.welcomemsg()

while True:
    cmd = input(prompt)

    # exit
    if cmd == "exit":
        break

    # help
    elif cmd == "help":
        cmds.helpmsg()

    # clear screen
    elif cmd == "cls" or cmd == "clear":
        cmds.clear()

    # info
    elif cmd == "info":
        info.showinfo(pjnm, pjver, pjdesc, pjauth, pjghurl)

    else:
        execute_commands(cmd)