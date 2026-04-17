import WIFI_CONFIG
from network_manager import NetworkManager
import uasyncio
import urequests
import time
import plasma
import random
from plasma import plasma_stick
from machine import Pin

# Set how many LEDs you have
NUM_LEDS = 50
DADO_START = 3
DADO_END = 20
BOX_START = 21
BOX_END = 50

def random_rgb():
    return random.randint(30,250), random.randint(30,250), random.randint(30,250)

def shiraz_walk():
    print('SHIRAZ WALK!')

    while True:
        # light up the LEDs in order in the random colour
        r, g, b = random_rgb()
        for i in range(NUM_LEDS):
            # DADO
            if ( i+DADO_START < DADO_END):
                led_strip.set_rgb(i+DADO_START, r, g, b)
            if ( i+BOX_START < BOX_END):
                led_strip.set_rgb(i+BOX_START, r, g, b)
            time.sleep(0.1)
            if ( i+DADO_START < DADO_END):
                led_strip.set_rgb(i+DADO_START, 0, 0, 0)
            if ( i+BOX_START < BOX_END):
                led_strip.set_rgb(i+BOX_START, 0, 0, 0)


        # now walk back in a different colour
        r, g, b = random_rgb()
        for i in reversed(range(NUM_LEDS)):
            if ( i+DADO_START < DADO_END):
                led_strip.set_rgb(i+DADO_START, r, g, b)
            if ( i+BOX_START < BOX_END):
                led_strip.set_rgb(i+BOX_START, r, g, b)
            time.sleep(0.1)
            if ( i+DADO_START < DADO_END):
                led_strip.set_rgb(i+DADO_START, 0, 0, 0)
            if ( i+BOX_START < BOX_END):
                led_strip.set_rgb(i+BOX_START, 0, 0, 0)

# set up the Pico W's onboard LED
pico_led = Pin('LED', Pin.OUT)

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# start updating the LED strip
led_strip.start()

shiraz_walk()

