import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('MSI 6218', 'abcd0113')

while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

print(wlan.ifconfig())