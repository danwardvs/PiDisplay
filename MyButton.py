
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


def setup(pins,handle_press):
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

    for pin in pins:

        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin,GPIO.RISING,callback=handle_press,bouncetime=300)
 
def cleanup():
    GPIO.cleanup() # Clean up