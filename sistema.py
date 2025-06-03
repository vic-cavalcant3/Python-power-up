# importando o pyautogui -> automatização de sistemas
import pyautogui
import time
import pandas

pyautogui.PAUSE = 1.5
# Abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrando no site
pyautogui.write("https://cadastrodalunos.netlify.app/")
pyautogui.press("enter")
time.sleep(2)

# Fazendo o login no site
pyautogui.click(x=604, y=400)
pyautogui.write("victorrocha0223@gmail.com")
pyautogui.click(x=400, y=495)
pyautogui.write("12345")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.press("enter")

# Cadastrando os dados usando o pandas

tabela = pandas.read_csv("./src/alunos_30.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=190, y=275)

    nome = tabela.loc[linha, "nome"]
    pyautogui.write(nome)
    pyautogui.press("tab")

    email = tabela.loc[linha, "email"]
    pyautogui.write(email)
    pyautogui.press("tab")

    nome_mae = tabela.loc[linha, "nome_mae"]
    pyautogui.write(nome_mae)
    pyautogui.press("tab")

    cpf = str(tabela.loc[linha, "cpf"])
    pyautogui.write(cpf)
    pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("enter")

    pyautogui.scroll(-10000)
    time.sleep(0.3)
    pyautogui.scroll(10000)

pyautogui.scroll(-10000)
