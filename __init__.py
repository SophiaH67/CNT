import display
import time


class State:
    name = "Marnix"
    x = 0
    y = 0
    x_motion = 2
    y_motion = 2
    x_scale = 2
    y_scale = 2
    fps = 30
    color_index = 0

    delay_per_frame = 1 / fps


colors = [
    0xFF0000,
    0x00FF00,
    0x0000FF,
    0xFFFF00,
    0x00FFFF,
    0xFF00FF,
    0x000000,
    0xFFA500,
    0xAA00FF,
    0xAA0000,
]


def cycle_color():
    State.color_index += 1
    if State.color_index >= len(colors):
        State.color_index = 0


def draw_text():
    display.drawText(
        State.x,
        State.y,
        State.name,
        colors[State.color_index],
        "PermanentMarker22",
        State.x_scale,
        State.y_scale,
    )
    display.flush()


def movetick():
    # Move the text
    State.x += State.x_motion
    State.y += State.y_motion

    x_upperbound = display.width() - (
        display.getTextWidth(State.name, "PermanentMarker22") * State.x_scale
    )
    y_upperbound = display.height() - (
        display.getTextHeight("PermanentMarker22") * State.y_scale * 2
    )
    # Check for collisions
    if State.x < 0 or State.x > x_upperbound:
        State.x_motion = -State.x_motion
        State.x += State.x_motion
        cycle_color()
    if State.y < 0 or State.y > y_upperbound:
        State.y_motion = -State.y_motion
        State.y += State.y_motion
        cycle_color()


while True:
    performance_start = time.time()
    display.drawFill(0xFFFFFF)
    movetick()
    draw_text()
    display.flush()
    performance_end = time.time()
    performance_time = performance_end - performance_start
    # if performance_time < State.delay_per_frame:
    #     time.sleep(State.delay_per_frame - performance_time)
