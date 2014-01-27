#!/usr/bin/python

import time
import random

#pins on the rpi for each led
LEDS = {"RED":17,"GREEN":21,"BLUE":22}

def off(led):
    pwm = open("/dev/pi-blaster","w")

    if led == 'ALL':
        for pin in LEDS.values():
            pwm.write("%s=%f\n" % (pin,0))
    else:
        pwm.write("%s=%f\n" % (LEDS[led],0))

    pwm.close()

def on(led,intensity=1):
    pwm = open("/dev/pi-blaster","w")

    if led == 'ALL':
        for pin in LEDS.values():
            pwm.write("%s=%f\n" % (pin,intensity))
    else:
        pwm.write("%s=%f\n" % (LEDS[led],intensity))

    pwm.close()


def ramp(led, t, steps = 10):
    sleep_time = 1.0 * t / steps
    for x in range(steps)
        on(led, 1.0 * x / steps)
        time.sleep(sleep_time)
    for x in range(steps)
        on(led, 1.0 * (steps - x) / steps)
        time.sleep(sleep_time)
    off(randled)    
        
        
def random_blink():
    """blink random time between white, red, green, blue for 5 seconds"""
                                                                                        
    workseconds = time.time() + 5                                                       
    while time.time() < workseconds:
        randsleep = random.randrange(0,100)/1000
        randled = random.choice(["ALL","RED","GREEN","BLUE"])
        ramp(randled, randsleep)
        

if __name__=="__main__":
    random_blink()
    off("ALL")


