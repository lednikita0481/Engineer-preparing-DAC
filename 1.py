import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
for i in dac:
    GPIO.setup(i, GPIO.OUT)

try:
    while True:
        n = input("Введите числовое целое значение:")
        if n == 'q':
            break

        try:
            n = int(n)
        except ValueError:
            print("Пользователь, ты дурачок, сказано же, числовое значение")
            continue
        if n < 0:
            print("Число должно быть не отрицательным!")
            continue
        if n > 255:
            print("Число превышает возможности ЦАП")
            continue
        
        m = decimal2binary(n)
        v = 0
        for i in range(len(dac)):
            v += m[i]/(2**(8-i))
        v *= 3.3
        print("v =", v)

        GPIO.output(dac, m)

finally:
    for i in dac:
        GPIO.output(i, 0)
    GPIO.cleanup()