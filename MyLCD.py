from i2c_lcd import I2cLcd
import time

lcd = None

def setup():
    global lcd
    # The PCF8574 has a jumper selectable address: 0x20 - 0x27
    DEFAULT_I2C_ADDR = 0x27
    lcd = I2cLcd(1, DEFAULT_I2C_ADDR, 2, 16)
    lcd.blink_cursor_off()
    lcd.hide_cursor()
    lcd.putstr("   Welcome to\n     DannyPC")
    time.sleep(1)
    lcd.clear()

def write(string):
    if lcd is None:
        print("Error: LCD not initalized")
    else:
        valid = True
        sp = string.split("\n")
        for i in sp:
            if len(i) > 16:
                valid = False
        if valid:
            lcd.clear()
            lcd.putstr(string)
        else:
            print("Error: Too large of text")

def flash(off_time,on_time,n):
    if lcd is None:
        print("Error: LCD not initalized")
    else:
        for _ in range(n):
            lcd.backlight_off()
            time.sleep(off_time)
            lcd.backlight_on()
            time.sleep(on_time)

