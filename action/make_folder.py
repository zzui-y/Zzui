import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from action.processing import p

def make_folder():
    
    name = input("Enter Folder Name : ")
    d = os.path.join("..",name)
    try:
        os.makedirs(d, exist_ok=True)
        p()
        print(Style.BRIGHT + Fore.GREEN + "Folder created.")
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"Error : {e}")
    
