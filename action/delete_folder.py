import os
import sys
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from action.processing import p

def delete_empty_folders():
    try:
        p()
        os.rmdir("..")
    except:
        
        
