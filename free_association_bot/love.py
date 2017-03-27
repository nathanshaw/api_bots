import os
import threading
import time
from sys import executable
from subprocess import Popen

threads = []

def ralphLove():
    os.system("python free_association_bot.py love Ralph")

def vickiLove():
    os.system("python free_association_bot.py love Vicki")


Popen([executable, "free_association_bot.py love"], shell=True)
input('Enter to exit from this launcher script...')

"""
try:
    r = threading.Thread(target=ralphLove)
    threads.append(r)
    v = threading.Thread(target=vickiLove)
    threads.append(v)
    r.start()
    print("started Ralph")
    v.start()
    print("started Vicki")

except Exception as e:
    print("error unable to start thread :", e)
"""
