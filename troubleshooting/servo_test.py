from gpiozero import AngularServo, Device
import time

import RPi.GPIO as GPIO

from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

TRIG = 21
ECHO = 20

thumb_servo = AngularServo(27, min_pulse_width=0.0006, max_pulse_width=0.0023)
index_servo = AngularServo(23, min_pulse_width=0.0006, max_pulse_width=0.0023 )
middle_servo = AngularServo(22, min_pulse_width=0.0006, max_pulse_width=0.0023)
ring_servo = AngularServo(24, min_pulse_width=0.0006, max_pulse_width=0.0023)
pinkie_servo = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance, 2)
    return distance

def get_angle(distance):
    if distance > 15:
        angle = -90
    elif distance < 4:
        angle = 30
    else:
        angle = 30 - distance*8
    return angle

try:
    GPIO.output(TRIG, False)    
    while (True):
        time.sleep(0.2)
        distance = get_distance()
        angle = get_angle(distance)
        thumb_servo.angle = angle
        index_servo.angle = angle
        middle_servo.angle = angle
        ring_servo.angle = angle + 25
        pinkie_servo.angle = angle
        
        print(f"distance: {distance} cm")
        print(angle)
    
finally:
    thumb_servo.angle = 50
    index_servo.angle = 50
    middle_servo.angle = 50
    ring_servo.angle = 50
    pinkie_servo.angle = 50
    print("clean up")
    GPIO.cleanup()