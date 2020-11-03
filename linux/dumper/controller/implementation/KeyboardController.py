
from getkey import getkey, keys

from linux.dumper.controller.Controller import UP, DOWN, LEFT, RIGHT, SELECT, Controller


def handle_key(key):
    if key == keys.UP: return UP
    if key == keys.DOWN: return DOWN
    if key == keys.LEFT: return LEFT
    if key == keys.RIGHT: return RIGHT
    if key == keys.SPACE or key == keys.ENTER: return SELECT


class KeyboardController(Controller):

    def get_input(self):
        key = getkey
        return handle_key(key)
