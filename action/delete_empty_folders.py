import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from action.processing import p

def delete_empty_folders():
    d = ".."
    count = 0
    p()
    print("\n")
    for item in os.listdir(d): #scanning the desktop
        if item in (".",".."):
            continue #skipping parent dir and current dir

        target_path = os.path.join(d, item) #building full relative path

        if os.path.isdir(target_path): #to target only directories
            try:
                os.rmdir(target_path)
                print(Style.BRIGHT + Fore.RED + f" [x] Deleted detected folder: {item}")
                count += 1
            except OSError:
                pass
        
    if count == 0:
        print(Fore.YELLOW + "No empty folders found to remove.")
    else:
        print(Style.BRIGHT + Fore.CYAN + f"Cleaned up {count} empty folder(s).\n")
        print(Style.BRIGHT + Fore.GREEN + "Empty Folder removed.")
        
        
