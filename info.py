#
#   python header/module
#--------------------------
#   info.py
#   
#   project informations for shell.cmd("info")
#

import json
import colors
from colors import *

with open('info.json') as fi:
    ficnt = json.loads(fi.read())

pjclr = green
pjnm = ficnt["name"]
pjver = ficnt["version"]
pjdesc = ficnt["desc"]
pjauth = ficnt["author"]
pjghurl = ficnt["ghurl"]

def showinfo(pjnm, pjver, pjdesc, pjauth, pjghurl):

    print(bold + pjclr + "                       )/_           ")
    print(bold + pjclr + "             _.--..---\"-,--c_       " + blue + "Name" + yellow + " : " + pjclr + pjnm)
    print(bold + pjclr + "        \L..'           ._O__)_     " + blue + "Version" + yellow + " : " + white + pjver)
    print(bold + pjclr + ",-.     _.+  _  \..--( /            " + blue + "Description" + yellow + " : " + white + pjdesc)
    print(bold + pjclr + "  `\.-''__.-' \ (     \_            " + blue + "Author" + yellow + " : " + white + pjauth)
    print(bold + pjclr + "    `'''       `\__   /\\            " + blue + "Github Repo" + yellow + " : " + white + pjghurl)
    print(bold + pjclr + "                ')                   ")