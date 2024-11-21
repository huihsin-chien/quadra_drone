from machine import Pin, PWM

import config


p0 = Pin(0, Pin.OUT)
p1 = Pin(1, Pin.OUT)
p2 = Pin(2, Pin.OUT)
p3 = Pin(3, Pin.OUT)


esc_speed0 = 0
esc_speed1 = 0
esc_speed2 = 0
esc_speed3 = 0

pwm0 = PWM(p0, freq=config.FREQ, duty_u16= esc_speed0)
pwm1 = PWM(p1, freq=config.FREQ, duty_u16= esc_speed1)
pwm2 = PWM(p2, freq=config.FREQ, duty_u16= esc_speed2)
pwm3 = PWM(p3, freq=config.FREQ, duty_u16= esc_speed3)

def UpateSetpoints():
    global esc_speed0, esc_speed1, esc_speed2, esc_speed3
    user_input = input("ws for throttle, ad for yaw, jl for pitch, ik for roll: ")
    if user_input == "w": # ws for throttle, ad for yaw, jl for pitch, ik for roll
        esc_speed0 +=1 if esc_speed0 < 100 else 100
        esc_speed1 +=1 if esc_speed1 < 100 else 100
        esc_speed2 +=1 if esc_speed2 < 100 else 100
        esc_speed3 +=1 if esc_speed3 < 100 else 100
    elif user_input == "s":
        esc_speed0 -=1 if esc_speed0 > 0 else 0
        esc_speed1 -=1 if esc_speed1 > 0 else 0
        esc_speed2 -=1 if esc_speed2 > 0 else 0
        esc_speed3 -=1 if esc_speed3 > 0 else 0
    elif user_input == "a": #ad for yaw,
        esc_speed0 +=1 if esc_speed0 < 100 else 100
        esc_speed1 -=1 if esc_speed1 > 0 else 0
        esc_speed2 +=1 if esc_speed2 < 100 else 100
        esc_speed3 -=1 if esc_speed3 > 0 else 0
    elif user_input == "d":
        esc_speed0 -=1 if esc_speed2 > 0 else 0
        esc_speed1 +=1 if esc_speed1 < 100 else 100
        esc_speed2 -=1 if esc_speed2 > 0 else 0
        esc_speed3 +=1 if esc_speed1 < 100 else 100
    elif user_input == "j": #jl for pitch
        esc_speed0 +=1 if esc_speed0 < 100 else 100
        esc_speed1 -=1 if esc_speed1 > 0 else 0
        esc_speed2 -=1 if esc_speed2 > 0 else 0
        esc_speed3 +=1 if esc_speed3 < 100 else 100
    elif user_input == "l":  
        esc_speed0 -=1 if esc_speed1 > 0 else 0
        esc_speed1 +=1 if esc_speed3 < 100 else 100
        esc_speed2 +=1 if esc_speed3 < 100 else 100
        esc_speed3 -=1 if esc_speed1 > 0 else 0
    elif user_input == "i": #ik for roll
        esc_speed0 +=1 if esc_speed0 < 100 else 100
        esc_speed1 +=1 if esc_speed1 < 100 else 100
        esc_speed2 -=1 if esc_speed2 > 0 else 0
        esc_speed3 -=1 if esc_speed3 > 0 else 0
    elif user_input == "k":
        esc_speed0 -=1 if esc_speed0 > 0 else 0
        esc_speed1 -=1 if esc_speed1 > 0 else 0
        esc_speed2 +=1 if esc_speed2 < 100 else 100
        esc_speed3 +=1 if esc_speed3 < 100 else 100

def esc_speed_to_pwm():
    # pwm0.duty_u16(int((esc_speed0/2000 +config.esc_thre_low)*config.FULL_DUTY)) #for esc
    # pwm1.duty_u16(int(((esc_speed1/2000 + config.esc_thre_low))*config.FULL_DUTY))
    # pwm2.duty_u16(int((esc_speed2/2000 + config.esc_thre_low)*config.FULL_DUTY))
    # pwm3.duty_u16(int((esc_speed3/2000 + config.esc_thre_low)*config.FULL_DUTY))
    pwm0.duty_u16(int((esc_speed0/100 +config.esc_thre_low)*config.FULL_DUTY)) #for led testing
    pwm1.duty_u16(int(((esc_speed1/100 + config.esc_thre_low))*config.FULL_DUTY))
    pwm2.duty_u16(int((esc_speed2/100 + config.esc_thre_low)*config.FULL_DUTY))
    pwm3.duty_u16(int((esc_speed3/100 + config.esc_thre_low)*config.FULL_DUTY))

while True:
    UpateSetpoints()
    esc_speed_to_pwm()
