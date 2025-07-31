import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

col_0  = board.GP00
col_1  = board.GP07
col_2  = board.GP08
col_3  = board.GP09
col_4  = board.GP10
col_5  = board.GP11
col_6  = board.GP12
col_7  = board.GP13
col_8  = board.GP14
col_9  = board.GP15
col_10 = board.GP16

row_0 = board.GP01
row_1 = board.GP02
row_2 = board.GP03
row_3 = board.GP04
row_4 = board.GP05
row_5 = board.GP06
row_6 = board.GP22
row_7 = board.GP21
row_8 = board.GP20
row_9 = board.GP19

keyboard.keymap = [
    [
        KC.ESC,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
        KC.PSCR, KC.SLCK, KC.PAUS,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
        KC.INS, KC.HOME, KC.PGUP,
        KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
        KC.DEL, KC.END, KC.PGDN,
        KC.P7, KC.P8, KC.P9, KC.PPLS,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,
        KC.P4, KC.P5, KC.P6,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.UP,
        KC.P1, KC.P2, KC.P3, KC.PENT,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL,
        KC.LEFT, KC.DOWN, KC.RIGHT,
        KC.P0, KC.PDOT
    ]
]


if __name__ == '__main__':
    keyboard.go()