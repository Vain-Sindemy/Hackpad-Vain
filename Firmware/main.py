import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Configuration selon ta photo : pins 11, 10, 9 pour les touches
# et pin 13 pour le retour commun
keyboard.col_pins = (board.GP11, board.GP10, board.GP9)
keyboard.row_pins = (board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.LALT(KC.TAB),            # Switch 1 : Alt + Tab
        KC.LALT(KC.LSFT(KC.TAB)),   # Switch 2 : Alt + Shift + Tab
        KC.LGUI(KC.D)               # Switch 3 : Windows + D (Bureau)
    ]
]

if __name__ == '__main__':
    keyboard.go()
