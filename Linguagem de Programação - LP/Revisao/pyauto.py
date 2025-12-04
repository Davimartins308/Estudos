# usamos varias vezes para tarefas de automaçao 
import pyautogui
# mover
#pyautogui.moveTo(600,500,duration=2)

# clicar
#pyautogui.click()

#digitar
#pyautogui.write("Ola mundo! ",interval=0.1)

#pressiona tecla
#pyautogui.press("enter")


# exemplos de automaçao
import time

pyautogui.PAUSE = 0.5
pyautogui.hotkey('win','r')
time.sleep(1)

pyautogui.write("notepad")
pyautogui.press("enter")

time.sleep(1)
pyautogui.write("ola, este texto foi digitado automaticamente", interval = 0.07)

