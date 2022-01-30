#CP Nano Q (Python 3.6 or compatible)
#Nano Version 1.0, CP version 0.9-5
#Compatible with PROPERLY CPT2-compliant modules
#TODO:
#
version = "CP Nano Q\nVersion 1.0"

#For some reason this won't work when placed in the comms dict.
def echo(cargs):
 ui.say(" ".join(cargs))

comms = {"ver":"ui.say(version)",
"echo":"echo(cargs)",
"merge":"Utils.Impor(cargs[0])",
"help":"ui.say(list(comms))"}

cargs = ["cargs initialization error"]

class UI:
 def say(self, msg):
  print(msg)
 def ask(self, msg=""):
  return input(msg+":")
 def debug(self, msg):
  f.write(f"\n{msg}")
  self.say(msg)

class Utils:
 @staticmethod
 def Impor(mod):
  thing = __import__(mod)
  globals().update(thing.__dict__)
  comms.update(newcomms)

class CP:
 def start(self):
  while True:
   try:
    user = ui.ask()
    user = shlex.split(user)
    command = user[0]
    global cargs
    cargs = user[1:len(user)]
    if command != "":
     if command in list(comms):
      exec(comms[command])
     else:
      ui.say(eval(command))
   except Exception as x:
    ui.say("Couldn't process command.")
    ui.debug(x)
     
     
#Provide same built-in modules as CP
import os
import sys
import time
import shlex
from pathlib import Path
from random import randint
from argparse import ArgumentParser
CP = CP()
f = open("cplog.txt", "w")
ui = UI()
CP.start()