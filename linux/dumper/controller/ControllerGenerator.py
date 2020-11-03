from linux.dumper.controller import Controller
from linux.dumper.controller.exception.ControllerException import ControllerException
from linux.dumper.output.OutputGenerator import LCD, MONITOR, DISPLAY_TYPES


# todo instead of using a command line parameter, we should use inject config

def get(display: str) -> Controller:
    if display not in DISPLAY_TYPES: raise ControllerException("Undefined controller type")
    if display == MONITOR:
        from linux.dumper.controller.implementation.KeyboardController import KeyboardController
        return KeyboardController()
    if display == LCD:
        from linux.dumper.controller.implementation.LcdController import LcdController
        return LcdController()
