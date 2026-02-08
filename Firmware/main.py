import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# On utilise tes numéros de pins (GP9, GP10, GP11)
# La pin 13 (GP13) sert de ligne commune
keyboard.col_pins = (board.GP11, board.GP10, board.GP9)
keyboard.row_pins = (board.GP13,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.LALT(KC.TAB),            # Switch 1 (Pin 11) : Alt + Tab
        KC.LALT(KC.LSFT(KC.TAB)),   # Switch 2 (Pin 10) : Alt + Shift + Tab
        KC.LGUI(KC.D)               # Switch 3 (Pin 9) : Windows + D
    ]
]

if __name__ == '__main__':
    keyboard.go()
