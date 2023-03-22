import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
for i in dac:
    GPIO.setup(i, GPIO.OUT)

try:
    check = True
    t = input("Введите числовое значение периода:")
    if t == 'q':
        check = False

    try:
        t = float(t)
        t_sleep = t / 2**9
    except ValueError:
        print("Пользователь, ты дурачок, сказано же, числовое значение")
        check = False
    while True:
        for i in range(256):
            m = decimal2binary(i)
            GPIO.output(dac, m)
            time.sleep(t_sleep)
        for i in range(254, -1, -1):
            m = decimal2binary(i)
            GPIO.output(dac, m)
            time.sleep(t_sleep)

finally:
    for i in dac:
        GPIO.output(i, 0)
    GPIO.cleanup()