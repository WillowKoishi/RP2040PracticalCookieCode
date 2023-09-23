import board
import time
from rainbowio import colorwheel
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner

_KEY_CFG = [board.GP14,board.GP23,board.GP22,board.GP21,board.GP20,
            board.GP15,board.GP17,board.GP19,board.GP18,]
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.0001,
            max_events=128)
keyboard = MyKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
Venti = KC.LWIN(KC.D)
keymap1 = [[KC.ESC,   KC.R,   KC.A,   KC.D,   Venti,
           KC.LSHIFT,         KC.Z,   KC.X,   KC.C,]]

keymap2 = [[KC.Z,     KC.X,   KC.A,   KC.UP,   Venti,
            KC.LSHIFT,        KC.LEFT,KC.DOWN,KC.RIGHT,]]

keyboard.keymap = keymap1
                  
print("test0")
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.RGB import RGB
rgb_ext = RGB(pixel_pin=board.GP7,num_pixels=10,val_limit=100,hue_default=1,sat_default=225,rgb_order=(1, 0, 2), val_default=100,hue_step=10,sat_step=10,val_step=10,animation_speed=10,breathe_center=1,knight_effect_length=3,
              animation_mode=AnimationModes.BREATHING,
              reverse_animation=False,refresh_rate=60,)
keyboard.extensions.append(rgb_ext)
if __name__ == '__main__':
    keyboard.go()
    while True:
        keyboard.goLoop()