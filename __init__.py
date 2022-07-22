import display
from time import sleep

colors = [
    0xFF0000,
    0x00FF00,
    0x0000FF,
    0xFF00FF,
    0xFFFF00,
    0x00FFFF
]

class State:
    name = "Marnix"
    color_index = 0
    x = 0
    y = 0
    x_motion = 2
    y_motion = 2
    x_scale = 2
    y_scale = 2

def cycle_color():
    # Increment the color index
    State.color_index = (State.color_index + 1) % len(colors)


def draw_text():
    display.drawText(State.x, State.y, State.name ,colors[State.color_index], "PermanentMarker22", State.x_scale, State.y_scale)
    display.flush()

def movetick():
    # Move the text
    State.x += State.x_motion
    State.y += State.y_motion

    x_upperbound = display.width() - (display.getTextWidth(State.name, "PermanentMarker22") * State.x_scale)
    y_upperbound = display.height() - (display.getTextHeight("PermanentMarker22") * State.y_scale * 2)
    # Check for collisions
    if State.x < 0 or State.x > x_upperbound:
        State.x_motion = -State.x_motion
        State.x += State.x_motion
    if State.y < 0 or State.y > y_upperbound:
        State.y_motion = -State.y_motion
        State.y += State.y_motion

while True:
    display.drawFill(0xFFFFFF)
    movetick()
    cycle_color()
    draw_text()
    display.flush()
    sleep(0.1)
