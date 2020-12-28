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
        print(bold + red + "gecko-sh" + reset + white + ": command not found:" + bold + " {}".format(cmd))

#------------------
#   Shell Prompt
#------------------
#   Variable = prompt
#
prompt = bold + pjclr + info.ficnt["name"] + yellow + " >" + reset + " "
#------------------

#------------------
#   CMD "help" 
#------------------
#   Message for the "help" cmd
#
def helpmsg():
    print(bold + green + info.ficnt["name"] + "-sh!" + white + " : A shell environment for " + green + info.ficnt["name2"] + reset)
    print("   " + bold + "- " + white + "[" + violet + "exit" + white + "]")
    print("   " + bold + "- " + white + "[" + violet + "help" + white + "]")
    print("   " + bold + "- " + white + "[" + violet + "clear/cls" + white + "]")
    print("   " + bold + "- " + white + "[" + violet + "info" + white + "]")
#------------------

#------------------
#   Welcome MSG
#------------------
#   Welcome msg when Shell is started
#
def welcomemsg():
    print("Welcome to " + bold + green + info.ficnt["name"] + "-sh!" + white + " : A shell environment for " + green + info.ficnt["name2"] + reset)
#------------------

welcomemsg()

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