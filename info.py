#
#   python header/module
#--------------------------
#   info.py
#   
#   project informations for shell.cmd("info")
#

import json

with open('info.json') as fi:
    ficnt = json.loads(fi.read())

pjnm = ficnt["name"]
pjver = ficnt["version"]
pjdesc = ficnt["desc"]
pjauth = ficnt["author"]
pjghurl = ficnt["ghurl"]

def showinfo(pjnm, pjver, pjdesc, pjauth, pjghurl):

    print("                       )/_           ")
    print("             _.--..---\"-,--c_       " + "Name : " + pjnm)
    print("        \L..'           ._O__)_     " + "Version : " + pjver)
    print(",-.     _.+  _  \..--( /            " + "Description : " + pjdesc)
    print("  `\.-''__.-' \ (     \_            " + "Author : " + pjauth)
    print("    `'''       `\__   /\\            " + "Github Repo : " + pjghurl)
    print("                ')                   ")