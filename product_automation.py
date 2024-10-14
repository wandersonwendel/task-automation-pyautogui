import pyautogui
import time

# Configuração de pausa para cada operação
pyautogui.PAUSE = 1

# -----------------------------------------
# Etapa 1: Abrir o navegador Chrome
# -----------------------------------------
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Pausa para permitir que o navegador abra
time.sleep(1)

# Clicar na conta do Google escolhida (coordenadas do mouse)
pyautogui.click(x=862, y=616)
