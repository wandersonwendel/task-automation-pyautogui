import pyautogui
import time
import pandas as pd

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

# Abrir uma nova aba no Chrome (estava com uma aberta para exemplo)
pyautogui.click(x=368, y=22)


# -----------------------------------------
# Etapa 2: Acessar o sistema da empresa
# -----------------------------------------

# Digitar o endereço do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pausa para permitir que o site carregue
time.sleep(2)

# Clicar no campo de entrada de E-Mail (coordenadas do mouse)
# pyautogui.click(x=615, y=521)  # Tela maximizada
pyautogui.click(x=366, y=474)  # Tela dividida

# Inserir um e-mail para testes
pyautogui.write("email.email@gmail.com")

# Usar a tecla TAB para pular para o campo de senha
pyautogui.press("TAB")

# Inserir uma senha para testes
pyautogui.write("senhasenhasenha")

# Pausa breve antes de ir para o botão
time.sleep(0.3)

# Clicar no botão de Login
pyautogui.press("TAB")
pyautogui.press("enter")


# -----------------------------------------
# Etapa 3: Ler a base de dados
# -----------------------------------------

# Ler o arquivo CSV com os dados dos produtos
base_de_dados = pd.read_csv("data/products.csv")