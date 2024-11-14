from machine import PWM, Pin
import time
FULL_DUTY = 65535

p0 = Pin(0, Pin.OUT)
pwm = PWM(p0, duty_ns = 5000, duty_u16=FULL_DUTY)
# pwm.deinit()
# pwm.init(freq=5000, duty_u16=FULL_DUTY, duty_ns=5000) 

while True:
    for i in range (0,int(FULL_DUTY/1.5), 1):
        pwm.duty_u16(i)
    for i in range (int(FULL_DUTY/1.5),0,-1):
        pwm.duty_u16(i)

