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


# -----------------------------------------
# Etapa 2: Acessar o sistema da empresa
# -----------------------------------------
# Digitar o endereço do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pausa para permitir que o site carregue
time.sleep(2)

# Clicar no campo de entrada de E-Mail (coordenadas do mouse)
pyautogui.click(x=615, y=521)

# Inserir um e-mail para testes
pyautogui.write("email.email@gmail.com")

# Usar a tecla TAB para pular para o campo de senha
pyautogui.press("TAB")

# Inserir uma senha para testes
pyautogui.write("senhasenhasenha")

# Pausa breve antes de ir para o botão
time.sleep(0.3)

# Pula para o botão e pressiona enter
pyautogui.press("TAB")
pyautogui.press("enter")


# -----------------------------------------
# Etapa 3: Ler a base de dados
# -----------------------------------------
# Ler o arquivo CSV com os dados dos produtos
base_de_dados = pd.read_csv("data/products.csv")

for row in base_de_dados.index:
    # Coordenada do primeiro campo de cadastro de produto
    pyautogui.click(x=614, y=365)

    # Preencher campo: CÓDIGO
    code = base_de_dados.loc[row, "codigo"]
    pyautogui.write(str(code))
    pyautogui.press("TAB") # Ir pulando para os demais campos

    # Preencher campo: MARCA
    brand = base_de_dados.loc[row, "marca"]
    pyautogui.write(str(brand))
    pyautogui.press("TAB")

    # Preencher campo: TIPO
    type = base_de_dados.loc[row, "tipo"]
    pyautogui.write(str(type))
    pyautogui.press("TAB")

    # Preencher campo: CATEGORIA
    category = base_de_dados.loc[row, "categoria"]
    pyautogui.write(str(category))
    pyautogui.press("TAB")

    # Preencher campo: PREÇO UNITÁRIO
    unit_price = base_de_dados.loc[row, "preco_unitario"]
    pyautogui.write(str(unit_price))
    pyautogui.press("TAB")

    # Preencher campo: CUSTO
    cost = base_de_dados.loc[row, "custo"]
    pyautogui.write(str(cost))
    pyautogui.press("TAB")

    # Preencher campo: OBSERVAÇÕES (se não for NaN)
    obs = base_de_dados.loc[row, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("TAB")

    pyautogui.press("enter")

    # Rolar a tela para cima, repetindo o loop de cadastrar novo produto
    pyautogui.scroll(5000)
