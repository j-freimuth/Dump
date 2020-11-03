
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

from linux.dumper.controller.Controller import UP, DOWN, LEFT, RIGHT, SELECT, Controller


def init_lcd():
    """
        Params: lcd_columns - number of columns the LCD Screen has (int)
                lcd_rows    - number of rows the LCD Screen has (int)
                i2c         - calling i2c program
                lcd         - setting lcd screen
        Returns: lcd
    """

    import board
    lcd_columns = 16
    lcd_rows = 2
    i2c = busio.I2C(board.SCL, board.SDA)
    lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

    return lcd


def handle_key(lcd):
    if lcd.up_button: return UP
    if lcd.down_button: return DOWN
    if lcd.left_button: return LEFT
    if lcd.right_button: return RIGHT
    if lcd.select_button: return SELECT
    return None


class LcdController(Controller):

    def __init__(self):
        lcd = init_lcd()

    def get_input(self):
        while True:
            command = handle_key(self.lcd)
            if command is not None:
                return command
