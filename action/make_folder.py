import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from action.processing import p

def make_folder():
    raw = input("Enter Folder Name(s) : ").strip()
    count = 0
    p()
    print("\n")
    if not raw:
        print(Style.BRIGHT + Fore.YELLOW + "No folder(s) name given...")
        time.sleep(0.3)
        print(Style.BRIGHT + Fore.YELLOW + "Exiting action.")
        return

    names = [n.strip() for n in raw.split(",") if n.strip()]

    for name in names:
        d = os.path.join("..", name)
        try:
            os.makedirs(d, exist_ok = True)
            print(Style.BRIGHT + Fore.GREEN + f" [+] Created: {name}")
            count += 1
        except Exception as e:
            print(Style.BRIGHT + Fore.RED + f"Failed : {name} ({e})")
    
    if count == 1:
        print("Done.")
    else:
        print(Style.BRIGHT + Fore.CYAN + f"Created {count} new folders(s).")
    
