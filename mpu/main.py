from imu import MPU6050
from time import sleep
import time
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)
time_start = time.ticks_ms()
time_now = time.ticks_ms()

ax_avg = 0
ay_avg = 0
az_avg = 0
gx_avg = 0
gy_avg = 0
gz_avg = 0
avg_count = 0
print("Calibrating IMU...")
while time.ticks_diff(time_now, time_start) < 3000:
    time_now = time.ticks_ms()
    avg_count += 1
    ax_avg += imu.accel.x
    ay_avg += imu.accel.y
    az_avg += imu.accel.z
    gx_avg += imu.gyro.x
    gy_avg += imu.gyro.y
    gz_avg += imu.gyro.z
ax_avg = ax_avg / avg_count
ay_avg = ay_avg / avg_count
az_avg = az_avg / avg_count
gx_avg = gx_avg / avg_count
gy_avg = gy_avg / avg_count
gz_avg = gz_avg / avg_count
print("Calibration done!")
print("ax_avg",ax_avg,"\t","ay_avg",ay_avg,"\t","az_avg",az_avg,"\t","gx_avg",gx_avg,"\t","gy_avg",gy_avg,"\t","gz_avg",gz_avg,"\t") 
while True:
    ax=round(imu.accel.x - ax_avg,2)
    ay=round(imu.accel.y - ay_avg,2)
    az=round(imu.accel.z - az_avg,2)
    gx=round(imu.gyro.x - gx_avg)
    gy=round(imu.gyro.y - gy_avg)
    gz=round(imu.gyro.z - gz_avg)
    tem=round(imu.temperature,2)
    print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    sleep(0.2)