import threading
import time
from RPLCD.i2c import CharLCD

I2C_BUS = 1
I2C_ADDRESS = 0x26
LCD_COLUMNS = 16
LCD_ROWS = 2
lcd_lock = threading.Lock()

lcd = None  # LCD 객체

def initialize_lcd():
    global lcd
    try:
        lcd = CharLCD(i2c_expander='PCF8574', address=I2C_ADDRESS, port=I2C_BUS,
                      cols=LCD_COLUMNS, rows=LCD_ROWS, dotsize=8,
                      charmap='A00', auto_linebreaks=True, backlight_enabled=True)
        lcd.clear()
    except Exception as e:
        print(f"LCD 초기화 오류: {e}")

def update_lcd_static(curtain_status, led_status):
    with lcd_lock:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Blind".ljust(6))
        lcd.cursor_pos = (0, 6)
        lcd.write_string("Led".ljust(4))
        lcd.cursor_pos = (1, 0)
        lcd.write_string(curtain_status.ljust(6))
        lcd.cursor_pos = (1, 6)
        lcd.write_string(led_status.ljust(4))
