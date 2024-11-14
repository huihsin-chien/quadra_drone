from machine import Pin, PWM
import time
FULL_DUTY = 65535
FREQ = 50
DUTY_CLYCLE = 0.06

p0 = Pin(0, Pin.OUT)
start_time = time.ticks_ms()
now_time = time.ticks_ms()

while time.ticks_diff(now_time, start_time) < 2000:
    now_time = time.ticks_ms()


pwm = PWM(p0, freq=FREQ, duty_u16= 0)

# while True:
#     # i = int(input("Enter a value between 0 and 100: "))
#     pwm.duty_u16(int((i/100)*FULL_DUTY))
try:
    while True:
        for i in range (0,int(FULL_DUTY*DUTY_CLYCLE), 1):
            pwm.duty_u16(i)
            print(i)
            time.sleep_ms(10)
        for i in range (int(FULL_DUTY*DUTY_CLYCLE),0,-1):
            pwm.duty_u16(i)
            print(i)
            time.sleep_ms(10)

except KeyboardInterrupt:
    pwm.deinit()
    print("PWM stopped")
    pass
except Exception as e:
    print("Error: ", e)
    pass
finally:
    pwm.deinit()
    print("PWM stopped")
    pass