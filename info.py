#
#   python header/module
#--------------------------
#   info.py
#   
#   project informations for shell.cmd("info")
#

import json
from colors import *

with open('info.json') as fi:
    ficnt = json.loads(fi.read())

pjnm = ficnt["name"]
pjver = ficnt["version"]
pjdesc = ficnt["desc"]
pjauth = ficnt["author"]
pjghurl = ficnt["ghurl"]

def showinfo(pjnm, pjver, pjdesc, pjauth, pjghurl):

    print(bold + green + "                       )/_           ")
    print(bold + green + "             _.--..---\"-,--c_       " + blue + "Name" + yellow + " : " + white + pjnm)
    print(bold + green + "        \L..'           ._O__)_     " + blue + "Version" + yellow + " : " + white + pjver)
    print(bold + green + ",-.     _.+  _  \..--( /            " + blue + "Description" + yellow + " : " + white + pjdesc)
    print(bold + green + "  `\.-''__.-' \ (     \_            " + blue + "Author" + yellow + " : " + white + pjauth)
    print(bold + green + "    `'''       `\__   /\\            " + blue + "Github Repo" + yellow + " : " + white + pjghurl)
    print(bold + green + "                ')                   ")