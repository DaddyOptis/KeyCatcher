import subprocess
import sys

# Function to install the pynput library
def install_pynput():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])

try:
    from pynput import keyboard
except ImportError:
    print("pynput library not found. Installing...")
    install_pynput()
    from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
