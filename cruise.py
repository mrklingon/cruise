from adafruit_circuitplayground import cp
import time
import random
from bach import *

from blinknum import *

def loc(pos):
    pos = pos +10
    return (pos%10)

if cp.switch:
    cp.play_file("trek/proximityalert_ep.wav")
while True:
    ship = 0
    dir = 1
    klingon = 5
    life = 5
    duration = 0
    while life > 0:
        duration = duration + .1
        cp.pixels[ship] = blue
        cp.pixels[klingon] = green
        if ship == klingon:
            blinknum(life,red)
            life = life - 1
            if cp.switch:
                cp.play_file("trek/smallexplosion1.wav")
                klingon = loc(klingon+1)
                ship = loc(ship - 1)
        time.sleep(.2)
        cp.pixels[ship] = blank
        cp.pixels[klingon] = blank

        ship = loc(ship + dir)
        cmd = 0
        if cp.button_a:
            cmd = cmd +1
        if cp.button_b:
            cmd = cmd +2
        
        if  cmd == 1:
            dir = 1
        if cmd == 2:
            dir = -1
        
        if (random.randrange(100)>49):
            klingon = loc(klingon + (2 - random.randrange(3)))
    if cp.switch:
        cp.play_file("trek/largeexplosion1.wav")
    shownum(duration)
    time.sleep(3)

        
