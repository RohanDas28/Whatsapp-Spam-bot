import pyautogui
import webbrowser
import time 
webbrowser.open("web.whatsapp.com")
time.sleep(30)
while True:
    pyautogui.press("R")
    pyautogui.press("enter")
