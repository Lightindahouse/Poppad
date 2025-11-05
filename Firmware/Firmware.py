#temp ai code ( faq said i can, i will do this myself when i get the pcb so i can test )
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

kb = KMKKeyboard()

# SW1, SW2, SW3, SW4, ENC_CLICK
pins = [board.D3, board.D4, board.D2, board.D1, board.D0]
kb.matrix = KeysScanner(pins=pins, value_when_pressed=False)

enc = EncoderHandler()
enc.pins = ((board.D5, board.D6, None),)   # A, B, (click handled above)
enc.map = ((KC.VOLD, KC.VOLU),)
kb.modules.append(enc)

# K1=Play, K2=Pause/Stop, K3=Next, K4=Prev, Click=Mute
kb.keymap = [[KC.MPLY, KC.MSTP, KC.MNXT, KC.MPRV, KC.MUTE]]

if __name__ == "__main__":
    kb.go()

