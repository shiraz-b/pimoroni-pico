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
STRIPE_LENGTH = 10

def random_rgb():
    return random.randint(30,200), random.randint(30,200), random.randint(30,200)

def random_rgb_max(max_r, max_g, max_b):
    return random.randint(30,max_r), random.randint(30,max_g), random.randint(30,max_b)

def random_rgb_strong_colour(colour):
    if (colour == 0):
        return random_rgb_max(255 ,50, 50)
    elif (colour == 1):
        return random_rgb_max(50 ,255, 50)
    else:
        return random_rgb_max(50 ,50, 255)

def shiraz_walk():
    print('SHIRAZ WALK!')

    while True:
        # light up the LEDs in order in the random colour
        for start_i in range(STRIPE_LENGTH):
            r, g, b = random_rgb_strong_colour(random.randint(0,2))
            for i in range(start_i,NUM_LEDS, STRIPE_LENGTH):
                led_strip.set_rgb(i, r, g, b)
                time.sleep(0.05)
        for start_i in range(STRIPE_LENGTH):
            # now walk back in a different colour
            r, g, b = random_rgb_strong_colour(random.randint(0,2))
            for i in range(NUM_LEDS-start_i, -1, -STRIPE_LENGTH):
                led_strip.set_rgb(i, r, g, b)
                time.sleep(0.05)

# set up the Pico W's onboard LED
pico_led = Pin('LED', Pin.OUT)

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# start updating the LED strip
led_strip.start()

shiraz_walk()

