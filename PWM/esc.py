from machine import Pin, PWM
FULL_DUTY = 65535
p0 = Pin(0, Pin.OUT)
p1 = Pin(1, Pin.OUT)
p2 = Pin(2, Pin.OUT)
p3 = Pin(3, Pin.OUT)
pwm0 = PWM(p0, freq=5000, duty_u16= 0)
pwm1 = PWM(p0, freq=5000, duty_u16= 0)
pwm2 = PWM(p0, freq=5000, duty_u16= 0)
pwm3 = PWM(p0, freq=5000, duty_u16= 0)


# while True:
#     i = int(input("Enter a value between 0 and 100: "))
#     pwm0.duty_u16(int((i/100)*FULL_DUTY))
