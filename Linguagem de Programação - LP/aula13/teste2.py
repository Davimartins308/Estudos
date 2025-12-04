import pyautogui
import time

time.sleep(5)
# (x,y,largura e altura)
im1= pyautogui.screenshot(region=(109,194,314,530)) 
im1.save("imagem2.png")