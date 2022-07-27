from itertools import count
from multiprocessing.spawn import is_forking
from sre_compile import isstring
import time
import threading
import random
from turtle import speed
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import os
import sys
import colorama
from colorama import init, Fore
import cursor
import pyautogui

os.system('mode con: cols=75 lines=25')
os.system('title Python Clicker')

colorama.init(autoreset = True)

print(Fore.RED + '''
         Welcome to the most basic python clicker in existence!
''')

startclicker = input('Are you ready to start clicking? [y/n] \n> ')

if startclicker == 'y':
    os.system('cls')
    cursor.hide()
else:
    print(Fore.RED + "\nClosing...")
    sys.exit(0)

TOGGLE_KEY = KeyCode(char="f")
HUMAN_KEY = KeyCode(char="h")
MANUAL_KEY = KeyCode(char="m")
INTERVAL_KEY = KeyCode(char="i")


global human, clicking, manual, interval, speed_

clickrange = (0.062, 0.073, 0.087, 0.093,)
ranges = ([0.14,0.25], [0.1,0,125], [0.09,0.071])

clicking = False
human = False
manual = False
interval = False
mouse = Controller()
speed_ = 0
total_time = 0
random_time = 0
counter = 0


print(Fore.GREEN + '''
            ------------------------------------------------
             To use the clicker press F on your keyboard
             To use the humanized cps use H on your keyboard
            ------------------------------------------------
''')

def clicker():
    

    global counter,random_time,speed_,total_time
    
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            

        if human: 
            random_time = round(random.uniform(ranges[counter][0], ranges[counter][1]), 3)
            time.sleep(random_time)
            total_time = total_time + random_time

            if total_time >= 2:
                counter = random.randint(0,(len(ranges)-1))
        elif manual:
            time.sleep(speed_)
        else:
            time.sleep(random.choice(clickrange))


def toggle_event(key):
    global human, clicking, counter, total_time, random_time, manual, interval, speed_

    # Clicker mode
    if key == TOGGLE_KEY:
        clicking = not clicking

        if clicking:
            print(Fore.GREEN + 'Started Clicker\n')
        elif not clicking:
            print(Fore.RED + 'Stopped Clicker\n')

    # Human mode
    elif key == HUMAN_KEY:
        if manual:
            print(Fore.RED + 'Stopped Manual Mode\n')
            manual = False
        human = not human
        if human:
            print(Fore.GREEN + 'Started Human Mode\n')
        elif not human:
            print(Fore.RED + 'Stopped Human Mode\n')

    # Manual mode
    elif key == MANUAL_KEY:

        if human:
            print(Fore.RED + 'Stopped human Mode\n')
            human = False

        if clicking:
            clicking = False
            print(Fore.RED + 'Stopped clicker\n')

        manual = not manual
        if not manual:
            print(Fore.RED + 'Stopped Manual Mode\n')
            
        elif manual:
            
            print(Fore.GREEN + 'Started Manual Mode\n')
        
            cps = int(input(Fore.WHITE + "Enter CPS: \n"))
            speed_ = 1/cps
            print(Fore.WHITE + "\nStart clicker to proceed \n")

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
