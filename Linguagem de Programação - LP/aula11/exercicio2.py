import pyautogui
import time

pyautogui.moveTo(960,1051,duration=2)
pyautogui.click(960,1051)
pyautogui.moveTo(510,64,duration=2)
pyautogui.click(510,64)
pyautogui.write("Wikipedia.com")
pyautogui.press("enter")

