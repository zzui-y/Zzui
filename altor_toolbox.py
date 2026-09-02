import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

#==============TRIGGER WORDS==============#        
with open("make_folder_triggers.txt","r") as mft:
    makefolder = mft.read().splitlines()

with open("show_dir_triggers.txt","r") as sdt:
    showdir = sdt.read().splitlines()

with open("make_file_triggers.txt","r") as mflt:
    makefile = mflt.read().splitlines()

#==========================================#
#==============ACTION MODULE===============#
from action.make_folder import make_folder
from action.make_file import make_file
from action.show_dir import show_dir

#==========================================#
#===================CODE===================#

while True:
    action = input("\n")
    act = action.lower()
    if act in makefolder:
        make_folder()
    elif act in showdir:
        show_dir()
    elif act in makefile:
        make_file()
    elif act == "exit":
        break
    else:   
        print(Style.BRIGHT + Fore.RED + "\nNo work bruh.")

    
