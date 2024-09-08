import RPi.GPIO as GPIO
import time
import speech

speech = speech.Speech()

GPIO.setmode(GPIO.BCM)

TRIG_PINS = [23, 24, 25, 26]  
ECHO_PINS = [27, 28, 29, 30] 

DISTANCE_THRESHOLD = 30 

for trig_pin, echo_pin in zip(TRIG_PINS, ECHO_PINS):
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

def measure_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(echo_pin) == 0:
        start_time = time.time()

    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

try:
    while True:
        for i, (trig_pin, echo_pin) in enumerate(zip(TRIG_PINS, ECHO_PINS)):
            distance = measure_distance(trig_pin, echo_pin)
            direction = ["North", "South", "East", "West"][i]
            
            if distance < DISTANCE_THRESHOLD:
                speech.speak(f"Obstacle detected {direction}: {distance:.1f} cm away!")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
