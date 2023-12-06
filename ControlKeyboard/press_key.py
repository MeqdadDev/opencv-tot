from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)
# Press and release ESC key for 1 second using pynput
keyboard.press('A')
time.sleep(1)

# ESC example:
# keyboard.press(Key.esc)
# keyboard.release(Key.esc)

