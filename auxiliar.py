from math import nan
import pyautogui as pa
import time 

time.sleep(4)

print(f'Posição do mouse: {pa.position()[0]}x, {pa.position()[1]}y')

print(f'Resolução da tela: {pa.size()[0]}x, {pa.size()[1]}y')
