import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from action.processing import p
def show_dir():
    try:
        p()
        print("\n")
        for item in os.listdir('..'): time.sleep(0.02); print(f"- {item}")
        print(Style.BRIGHT + Fore.GREEN + "\nDir retrieved.")
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f"Error : {e}")
