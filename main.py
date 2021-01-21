import MyLCD
import MyButton
import MyScreen
import MyRequest
import requests
import time
from datetime import datetime
from enum import Enum

class Button(Enum):
    DOWN = 10
    UP = 8
    REFRESH = 11
    ENTER = 12

def handle_press(channel):
 
    print("Button " + str(channel) + " pressed.")

    if channel == Button.DOWN.value:
        MyScreen.scroll("Down")
    if channel == Button.UP.value:
        MyScreen.scroll("Up")
    if channel == Button.REFRESH.value:
        MyLCD.write("Force update...")
        fetch_data()

MyLCD.setup()
MyButton.setup([8,10,11,12],handle_press)
MyScreen.screen = [ "Loading..."]

def fetch_data():
    new_screen = []
    new_screen+=MyRequest.fetch_stock("FLT.V",1815)[1]
    new_screen+=MyRequest.fetch_stock("TSLA",0)[1]
    new_screen+=MyRequest.fetch_vaccine()[1]
    new_screen+=MyRequest.fetch_weather()[1]

    MyScreen.screen = new_screen
    print(new_screen)
    MyScreen.update()

    
    MyLCD.flash(0.5,0.5, 1)            

while True:
    
    fetch_data()
    time.sleep(60*3)

MyButton.cleanup()