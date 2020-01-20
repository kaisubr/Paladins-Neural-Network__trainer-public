from mss import mss
import mss.tools
import keyboard
import threading
import sys 
import os
import random
import time

# Requires installation of keyboard and mss as follows
#   pip -V # should be v3, otherwise use pip3 or upgrade as necessary
#   pip install keyboard
#   pip install mss

print("*** Ready ***")

i = 0
version = 4.1

def takeshot() :
    global i # or send as parameter.
    
    cwd = os.getcwd()
    fname = cwd + '\j_' + str(i) + '-' + str(version) + '.png'
    # print("Save as " + fname)
    i += 1

    s = mss().shot(output=fname)
    # print(s)

def takeshot_center() :
    # The screen part to capture
    global i
    cwd = os.getcwd()
    monitor = {"top": 210, "left": 490, "width": 300, "height": 300}
    fname = cwd + '\j_' + str(i) + '-' + str(version) + '.png'
    img = mss.mss().grab(monitor)
    mss.tools.to_png(img.rgb, img.size, output=fname)   

    i+= 1

def run() : 
    takeshot_center()
    threading.Timer(random.randint(1,7), run).start() #or import threading.Timer as timer

def burstshot(event) :
    if (event.name == 'r' or event.name == 'shift'):
        print("click!")
        for i in range(0, 5):
                takeshot_center()
                time.sleep(0.75)

print("waiting!")
keyboard.on_press(burstshot)

t = input("Input anything to start on interval, r or shift to burst shot, x to exit, ^C to interrupt: ")
if (t == 'x') :
    sys.exit(0)
else :
    run()