from adafruit_magtag.magtag import MagTag
import alarm
import board
import digitalio
import neopixel
import time

magtag = MagTag()
graphics = magtag.graphics
peripherals = magtag.peripherals

magtag.peripherals.neopixel_disable = True

mid_x = magtag.graphics.display.width // 2 - 1
magtag.add_text(
    text_font="cousinebold-36.bdf",
    text_position=(mid_x, 20),
    text_anchor_point=(0.5, 0),
    is_data=False,)
magtag.set_text("Amy Moretti")

#wakeup = magtag.peripherals.button_a_pressed

def wakeup():

    time_span = 0.01;
    total_sleep_time = 15;
    time_elapsed = 0;

    while time_elapsed < total_sleep_time:
        if magtag.peripherals.button_a_pressed:
            magtag.set_text("BRB!")
        elif magtag.peripherals.button_b_pressed:
            magtag.set_text("Please knock")
        elif magtag.peripherals.button_c_pressed:
            magtag.set_text("In a meeting,\n slack me")
        elif magtag.peripherals.button_d_pressed:
            magtag.set_text("Remote today")

    time_elapsed = time_elapsed + time_span
    time.sleep(time_span)

magtag.exit_and_deep_sleep(wakeup())


