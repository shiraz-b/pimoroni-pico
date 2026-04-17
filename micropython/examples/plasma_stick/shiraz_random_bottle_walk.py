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
BRIGHTNESS = 150

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

def rgb_christmas_colour(colour):
    if (colour == 0):
        return (int(BRIGHTNESS*6/8) ,0, BRIGHTNESS)
    elif (colour == 1):
        return (0 ,BRIGHTNESS, 0)
    elif (colour == 2):
        return (BRIGHTNESS, int(BRIGHTNESS/2), 0)
    else:
        return (BRIGHTNESS ,BRIGHTNESS, BRIGHTNESS)

def translate_column(start_i):
    if (start_i == 0):
        col_i = 0
    if (start_i == 1):
        col_i = 7
    if (start_i == 2):
        col_i = 4
    if (start_i == 3):
        col_i = 1
    if (start_i == 4):
        col_i = 8
    if (start_i == 5):
        col_i = 5
    if (start_i == 6):
        col_i = 2
    if (start_i == 7):
        col_i = 9
    if (start_i == 8):
        col_i = 6
    if (start_i == 9):
        col_i = 3
    return col_i

def shiraz_walk():
    print('SHIRAZ WALK!')

    ccol = 0
    
    while True:
        # light up the LEDs in order in the random colour
        r, g, b = rgb_christmas_colour(ccol % 3)
        for start_i in range(STRIPE_LENGTH):
            col_i = translate_column(start_i)
            for i in range(col_i,NUM_LEDS, STRIPE_LENGTH):
                led_strip.set_rgb(i, r, g, b)
            #col_i = translate_column((start_i-1) % STRIPE_LENGTH)
            #for i in range(col_i,NUM_LEDS, STRIPE_LENGTH):
            #    led_strip.set_rgb(i, 0, 0, 0)
            time.sleep(0.4)
        ccol=ccol+1
'''
for start_i in range(STRIPE_LENGTH):
            # now walk back in a different colour
            col_i = translate_column(start_i)
            r, g, b = random_rgb()
            for i in range(NUM_LEDS-col_i, -1, -STRIPE_LENGTH):
                led_strip.set_rgb(i, r, g, b)
                time.sleep(0.05)
'''
# set up the Pico W's onboard LED
pico_led = Pin('LED', Pin.OUT)

# set up the WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

# start updating the LED strip
led_strip.start()

shiraz_walk()

