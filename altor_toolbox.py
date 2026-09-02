import colorama
from colorama import Fore, Style
colorama.init(autoreset = True)

#==============TRIGGER WORDS==============#        
with open("make_folder_triggers.txt","r") as mft:
    makefolder = mft.read().splitlines()

with open("show_dir_triggers.txt","r") as sdt:
    showdir = sdt.read().splitlines()

with open("make_file_triggers.txt","r") as mflt:
    makefile = mflt.read().splitlines()

with open("delete_empty_folders_triggers.txt","r") as defl:
    deleteEfolders = defl.read().splitlines()

#==========================================#
#==============ACTION MODULE===============#
from action.make_folder import make_folder
from action.make_file import make_file
from action.show_dir import show_dir
from action.delete_empty_folders import delete_empty_folders

#==========================================#
#===================CODE===================#

print(Style.BRIGHT + Fore.CYAN + r"""
      ___                                       ___           ___     
     /\  \                                     /\  \         /\  \        
    /::\  \                       ___         /::\  \       /::\  \   
   /:/\:\  \                     /\__\       /:/\:\  \     /:/\:\__\  
  /:/ /::\  \   ___     ___     /:/  /      /:/  \:\  \   /:/ /:/  /  
 /:/_/:/\:\__\ /\  \   /\__\   /:/__/      /:/__/ \:\__\ /:/_/:/__/___
 \:\/:/  \/__/ \:\  \ /:/  /  /::\  \      \:\  \ /:/  / \:\/:::::/  /
  \::/__/       \:\  /:/  /  /:/\:\  \      \:\  /:/  /   \::/~~/~~~~ 
   \:\  \        \:\/:/  /   \/__\:\  \      \:\/:/  /     \:\~~\     
    \:\__\        \::/  /         \:\__\      \::/  /       \:\__\    
     \/__/         \/__/           \/__/       \/__/         \/__/    
""")
print(Fore.CYAN + "\n  c o r e ")

while True:
    action = input("\n exe: ")
    act = action.lower()
    if act in makefolder:
        make_folder()
    elif act in showdir:
        show_dir()
    elif act in makefile:
        make_file()
    elif act in deleteEfolders:
        delete_empty_folders()
    elif act == "exit":
        break
    else:   
        print(Style.BRIGHT + Fore.RED + "\nNo work bruh.")

    
