
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import MyLCD

def setup(pins,handle_press):
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

    for pin in pins:

        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin,GPIO.RISING,callback=handle_press,bouncetime=300)
def setup_light(pin):
    def handle_press(e):
        print("Light Status Change")
        MyLCD.toggle_backlight_enabled()

    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin,GPIO.RISING,callback=handle_press,bouncetime=300)


def is_light_on(pin):
    return not GPIO.input(pin)

def cleanup():
    GPIO.cleanup() # Clean up