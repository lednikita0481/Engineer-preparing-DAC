import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

p1 = GPIO.PWM(23, 1000)
p1.start(0)

p2 = GPIO.PWM(26, 1000)
p2.start(0)

try:
    while True:
        dc = input("Введите dc от 0 до 100:")
        if dc == 'q':
            break

        try:
            dc = int(dc)
        except ValueError:
            print("Пользователь, ты дурачок, сказано же, числовое значение")
            continue
        
        if dc > 100 or dc < 0:
            print("пользователь накринжил")
            continue

        p1.ChangeDutyCycle(dc)
        p2.ChangeDutyCycle(dc)

finally:
    GPIO.output(23, 0)
    GPIO.cleanup()