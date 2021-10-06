import time
from adafruit_magtag.magtag import MagTag

magtag = MagTag()
graphics = magtag.graphics
peripherals = magtag.peripherals


mid_x = magtag.graphics.display.width // 2 - 1
magtag.add_text(
    text_font="opensans-36.bdf",
    text_position=(mid_x, 20),
    text_anchor_point=(0.5, 0),
    is_data=False,)
magtag.set_text("Amy Moretti")

magtag.add_text(
    text_font="opensans-18.bdf",
    text_wrap=30,
    text_maxlen=160,
    text_position=(
        5,
        (magtag.graphics.display.height // 2) + 20,
    ),
    line_spacing=0.75
)

magtag.set_text("Hello!", index=1)

while True:
    if magtag.peripherals.button_a_pressed:
        magtag.set_text("Please knock", index=1)
    elif magtag.peripherals.button_b_pressed:
        magtag.set_text("In a meeting, slack me", index=1)
    elif magtag.peripherals.button_c_pressed:
        magtag.set_text("Remote today", index=1)
    elif magtag.peripherals.button_d_pressed:
        magtag.set_text("Go bother Amanda", index=1)

    else:
        magtag.peripherals.neopixel_disable = True
    time.sleep(0.01)
