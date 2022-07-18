import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def enable_pin(pin):
    print("Enabling led: " + str(pin))
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)


def disable_pin(pin):
    print("Disabling led: " + str(pin))
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
