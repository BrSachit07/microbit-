from microbit import *
import random

player_x = 2  # start in middle

while True:
    dot_x = random.randint(0, 4)
    for y in range(5):
        display.clear()
        display.set_pixel(dot_x, y, 9)
        display.set_pixel(player_x, 4, 5)
        sleep(300)

        # Move player left
        if input.button_is_pressed(Button.A) and player_x > 0:
            player_x -= 1
        # Move player right
        if input.button_is_pressed(Button.B) and player_x < 4:
            player_x += 1

        # Check if player caught the dot
        if y == 4:
            if player_x == dot_x:
                display.show(Image.HAPPY)
            else:
                display.show(Image.SAD)
            sleep(1000)
            display.clear()
