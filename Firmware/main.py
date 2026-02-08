import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# IMPORTANT : Vérifie tes pins sur ton schéma KiCad (ici D0, D1, D2 par défaut)
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3,)
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
