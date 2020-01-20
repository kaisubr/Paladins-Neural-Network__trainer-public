import win32api,win32con
import time
import math

while True:
    x = 0#int(500+math.sin(math.pi*i/100)*500)
    y = 0#int(500+math.cos(i)*100)
    #win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    time.sleep(10)
