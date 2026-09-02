import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from action.processing import p

def make_file():
    name = input("Enter File Name : ").strip()
    content = input("Enter contents (optional): ")
    d = os.path.join("..", name)
    try:
        with open(d,"w") as f:
            f.write(content)
        p()
        print(Style.BRIGHT + Fore.GREEN + "File created.")
    except FileExistsError:
        print(Style.BRIGHT + Fore.RED + f"Error: '{name}' already exists")
    except:
        print(Style.BRIGHT + Fore.RED + f"Error : {e}")
