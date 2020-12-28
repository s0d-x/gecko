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

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def execute_commands(cmd):
    try:
        subprocess.run(cmd.split())
    except Exception:
        print("gecko-sh: command not found: {}".format(cmd))

#
#   Shell Prompt
#------------------
#   Variable = prompt
#

prompt = info.ficnt["name"] + " > "

while True:
    cmd = input(prompt)

    if cmd == "exit":
        break

    elif cmd == "help":
        print("gecko-sh: This is a shell environment for Gecko [exit, help, clear/cls, info]")

    elif cmd == "cls" or cmd == "clear":
        clear()

    elif cmd == "info":
        
        info.showinfo(pjnm, pjver, pjdesc, pjauth, pjghurl)

    else:
        execute_commands(cmd)