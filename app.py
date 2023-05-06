import pyautogui
import webbrowser
from time import sleep

# 1) Navegaremos até o site https://cursoautomacao.netlify.app/
# 2) Encontrará campo "Exemplo Alertas" e digitaremos um Nome
# 3) Clicará em "alerta", para gerar a alerta
# 4) Fechará a mensagem de alerta
# 5) Retornando para o topo da página
''' 6) Descerá até a seção que contém os arquivos para o quais irá fazer o download,
   então fará o click no botão de download para realizar o downlaod dos arquivos excel e pdf.'''
# 7) Depois de ter feito isso, criará uma alerta que diz "VOCÊ TERMINOU"

# 1
webbrowser.open_new('https://cursoautomacao.netlify.app/')
sleep(2)


# 2
pyautogui.click(1909,172,duration=0.5)
sleep(0.5)
pyautogui.scroll(-1000)
pyautogui.click(1533,260,duration=0.5)
pyautogui.typewrite('Lucas Lemes')


# 3
pyautogui.click(1469,301,duration=0.5)


# 4
sleep(0.5)
pyautogui.press('enter')


# 5 
sleep(0.5)
pyautogui.scroll(1000)


# 6
sleep(0.5)
pyautogui.scroll(-1000)
sleep(0.5)
pyautogui.scroll(-500)
sleep(0.5)
pyautogui.click(703,721,duration=0.5)
sleep(1)
pyautogui.click(474,718,duration=0.8)


# 7
pyautogui.alert('VOCÊ TERMINOU SUA AUTOMAÇÃO!!')