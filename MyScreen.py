import MyLCD

screen_location = 0
screen = ["Screen contents"]

def scroll(direction):
    global screen
    global screen_location

    if direction == "Up":
        if screen_location < len(screen)-1:
            screen_location += 1
            update()
    if direction == "Down":
        if screen_location > 0:
            screen_location -= 1
            update()

def update():
    global screen_location
    global screen

    if screen_location > len(screen):
        screen_location = 0

    line_1 = screen[screen_location]
    line_2 = "" if screen_location==len(screen)-1 else screen[screen_location+1]
    MyLCD.write(line_1 + "\n" + line_2)