import os
import sys

import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

def p():
    print(Style.BRIGHT + Fore.YELLOW + "Processing action ", end = "", flush = True)
    for _ in range(3): time.sleep(0.3); print(Fore.YELLOW + "-", end = " ", flush = True)
    time.sleep(0.3)
