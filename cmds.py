#
#   python header/module
#--------------------------
#   cmds.py
#   
#   Commands for the Shell
#

from os import system, name
import info
from info import *
from colors import *

shname=ficnt["name"] + "-sh"

#------------------
#   CMD "clear/cls" 
#------------------
#   Clear terminal screen
#
def clear(): 
  
    # windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # posix 
    else: 
        _ = system('clear')
#------------------

#------------------
#   CMD "help" 
#------------------
#   Message for the "help" cmd
#
def helpmsg():
    print(bold + green + shname + "!" + white + " : A shell environment for " + green + info.ficnt["name2"] + reset)
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