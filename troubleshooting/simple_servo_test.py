from gpiozero import AngularServo, Device
import time

import RPi.GPIO as GPIO

from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

ANGLE1 = 40
ANGLE2 = -90

DELAY1 = 0.15

thumb_servo = AngularServo(27, min_pulse_width=0.0006, max_pulse_width=0.0023)
index_servo = AngularServo(23, min_pulse_width=0.0006, max_pulse_width=0.0023 )
middle_servo = AngularServo(22, min_pulse_width=0.0006, max_pulse_width=0.0023)
ring_servo = AngularServo(24, min_pulse_width=0.0006, max_pulse_width=0.0023)
pinkie_servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)

try:
    while (True):
        thumb_servo.angle = ANGLE1 + 50
        time.sleep(DELAY1)
        index_servo.angle = ANGLE1
        time.sleep(DELAY1)
        middle_servo.angle = ANGLE1 + 30
        time.sleep(DELAY1)
        ring_servo.angle = ANGLE1 + 25
        time.sleep(DELAY1)
        pinkie_servo.angle = ANGLE1
        time.sleep(2)
        thumb_servo.angle = ANGLE2 + 50
        time.sleep(DELAY1)
        index_servo.angle = ANGLE2
        time.sleep(DELAY1)
        middle_servo.angle = ANGLE2 + 20
        time.sleep(DELAY1)
        ring_servo.angle = ANGLE2 + 25
        time.sleep(DELAY1)
        pinkie_servo.angle = ANGLE2
        time.sleep(2)
        
finally:
    thumb_servo.angle = ANGLE1
    index_servo.angle = ANGLE1
    middle_servo.angle = ANGLE1
    ring_servo.angle = ANGLE1
    pinkie_servo.angle = ANGLE1
    print("clean up")
    GPIO.cleanup()
