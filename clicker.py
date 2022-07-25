import time
import threading
import random
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import os
import sys
import colorama
from colorama import init, Fore
import cursor

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

clickrange = (0.062, 0.073, 0.087, 0.093,)

clicking = False
mouse = Controller()

print(Fore.GREEN + '''
            --------------------------------------------
             To use the clicker press F on you keyboard
            --------------------------------------------
''')

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(random.choice(clickrange))

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        print('F key pressed\n')

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
