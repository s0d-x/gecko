#
#   python header/module
#--------------------------
#   shell.py
#   
#   shell environment for gecko (gecko-sh)
#

#---
#   COMMANDS -
#       exit, help, clear/cls, info
#

from os import system, name
import info
from info import *
from colors import *

def clear(): 
  
    # windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # posix 
    else: 
        _ = system('clear')

def execute_commands(cmd):
    try:
        subprocess.run(cmd.split())
    except Exception:
        print("gecko-sh: command not found: {}".format(cmd))

#------------------
#   Shell Prompt
#------------------
#   Variable = prompt
#
prompt = bold + blue + info.ficnt["name"] + yellow + " >" + reset + " "
#------------------

#------------------
#   CMD "help" 
#------------------
#   Message for the "help" cmd
#
def helpmsg():
    print(info.ficnt["name"] + "-sh: This is a shell environment for " + info.ficnt["name2"])
    print("   - [exit]")
    print("   - [help]")
    print("   - [clear/cls]")
    print("   - [info]")
#------------------

while True:
    cmd = input(prompt)

    # exit
    if cmd == "exit":
        break

    # help
    elif cmd == "help":
        helpmsg()

    # clear screen
    elif cmd == "cls" or cmd == "clear":
        clear()

    # info
    elif cmd == "info":
        info.showinfo(pjnm, pjver, pjdesc, pjauth, pjghurl)

    else:
        execute_commands(cmd)