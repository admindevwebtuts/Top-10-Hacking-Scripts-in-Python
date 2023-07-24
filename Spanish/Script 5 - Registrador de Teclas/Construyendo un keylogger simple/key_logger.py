from pynput.keyboard import Key, Listener

def on_press(tecla):
  print(f"{tecla} presionada")

with Listener(on_press=on_press) as listener:
  listener.join()



