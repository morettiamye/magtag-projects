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

button = (board.BUTTON_A)  # pick any two
wakeup = [alarm.pin.PinAlarm(pin=button, value=False, pull=True)]

time_span = 0.01;
total_sleep_time = 15;
time_elapsed = 0;

while time_elapsed < total_sleep_time:
    if magtag.peripherals.button_b_pressed:
        magtag.set_text("Please knock", index=1)
    elif magtag.peripherals.button_c_pressed:
        magtag.set_text("In a meeting, slack me", index=1)
    elif magtag.peripherals.button_d_pressed:
        magtag.set_text("Remote today", index=1)

    time_elapsed = time_elapsed + time_span
    time.sleep(time_span)

alarm.exit_and_deep_sleep_until_alarms(wakeup)


