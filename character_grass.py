from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character =load_image('character.png')

r = 210
angle = 270

while(True):
    x = 0
    y = 100
    while x <= 790:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    if x >= 790:
        while y <= 570:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y + 2
            delay(0.01)

    if y >= 570:
        while x >= 0:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x = x - 2
            delay(0.01)

    if x <= 0:
        while y >= 90:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y = y - 2
            delay(0.01)

    if y <= 90:
        while angle <= 630:
            clear_canvas_now()
            grass.draw_now(400, 30)
            x = r * math.cos(math.radians(angle)) + 400
            y = r * math.sin(math.radians(angle)) + 300
            character.draw_now(x, y)
            angle = angle + 1
            delay(0.01)

    if angle > 630:
        angle = 270

close_canvas()
