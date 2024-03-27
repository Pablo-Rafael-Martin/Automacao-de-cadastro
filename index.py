import pyautogui as auto
import time
import pandas
import numpy

link = 'https:/dlp.hashtagtreinamentos.com/python/intensivao/login'
auto.PAUSE = 0.3
tabela = pandas.read_csv('C:/Users/rafae/Programas/Intensivão de Python/produtos.csv')

# Entrar no sistema
auto.press('win')
auto.write('chrome')
auto.press('enter')
time.sleep(4)
auto.hotkey('ctrl', 't', interval=0.2)
auto.write(link)
auto.press('enter')
time.sleep(3)

# Fazer login
auto.click(918, 1524)
auto.write('email_teste@gmail.com')
auto.click(991, 1642)
auto.write('senha123')
auto.press('enter')
time.sleep(2)

# Cadastrar um produto. Repetir para todos os produtos
auto.PAUSE = 0.3    

for i in tabela.index:
    j = 0
    auto.click(946, 1401)
    print(f'i = {i}')

    for k in range (0, 7):
        # condição para não escrever a observação se não tiver        
        if (k == 6):
            if (not pandas.isna(tabela.iloc[i, j])):
                auto.write(str(tabela.iloc[i, j]))
            else:
                break
        auto.write(str(tabela.iloc[i, j]))
        j = j + 1
        k = k + 1
        auto.press('tab')
    
    auto.press('enter')
    auto.scroll(5000)
    