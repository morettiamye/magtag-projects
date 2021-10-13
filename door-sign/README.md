# Office Door Sign Using Adafruit Magtag

With the return to the office in the midst of the COVID-19 pandemic, rules were implemented that if you wanted to work with no mask on, you would need to close your door.  This presented a problem in that because our doors are solid wood, it was impossible to know if someone was in their office, in a meeting, busy, or otherwise wished to not be bothered.  My solution to this was to build a small e-ink sign that can be updated at the press of a button.  It then hibernates into a deep sleep, conserving battery power so that the sign does not need to be charged often.

## Supplies
- [Adafruit Magtag Starter Kit - ADABOX017 Essentials](https://www.adafruit.com/product/4819)
- Small phillips head screwdriver
- Usb-C cable capable of data-sync (a cable meant for just charging will not work).  I used the cable that came included with my iPad Mini 6.

## Getting Started
The first step is to install Circuit Python onto the board.  Download the .bin of latest release [here](https://circuitpython.org/board/adafruit_magtag_2.9_grayscale/), then connect the Magtag to your computer. You should see it as an external drive named **MAGTAGBOOT**.  You can now drag and drop Circuit Python into the main directory of the board.  It will restart and now appear as an external drive named CIRCUITPY.  Now you will need to download the package of [Circuit Python Libraries](https://circuitpython.org/libraries) to install on the board.  Because the board cannot hold much data, you will only want to install the libraries that you need.  In this case you want to install:
- adafruit_bitmap_font
- adafruit_display_text
- adafruit_fakerequests
- adafruit_io
- adafruit_magtag
- adafruit_portalbase
- adafruit_requests
- neopixel.mpy
- simpleio.mpy

The next step is to create your Secrets.py file.  While internet connectivity is not a requirement for this project, the file is a requirement for the board to run. Simply create a Secrets.py file with the following information:

```
  #This file is where you keep secret settings, passwords, and tokens!
  #If you put them in the code you risk committing that info or sharing it

  secrets = {
      'ssid' : ,
      'username' : ,
      'password' : ,
      'timezone' : , #Find your timezone name here: http://worldtimeapi.org/timezones
    }
```
