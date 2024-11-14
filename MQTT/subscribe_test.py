from machine import Pin
from time import sleep
import network
from umqtt.simple import MQTTClient
import config

# Initialize Wi-Fi Interface
def initialize_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    sleep(5)  # 等待幾秒鐘以連接
    if wlan.isconnected():
        print('Wi-Fi connected:', wlan.ifconfig())
        return True
    else:
        print('Failed to connect to Wi-Fi')
        return False

# Connect to MQTT Broker
def connect_mqtt():
    try:
        client = MQTTClient(client_id='raspberrypi_picow',
                            server=config.mqtt_server,
                            port=1883,
                            keepalive=60,
                            ssl=False)
        client.connect()
        print('Connected to MQTT broker')
        return client
    except Exception as e:
        print('Failed to connect to MQTT broker:', e)
        return None

import socket

def test_mqtt_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((config.mqtt_server, 1883))
        print("Successfully connected to MQTT broker")
    except OSError as e:
        print("Failed to connect to MQTT broker:", e)
    finally:
        sock.close()




# Main loop
if __name__ == '__main__':
    if initialize_wifi(config.wifi_ssid, config.wifi_password):
        test_mqtt_connection()
        client = connect_mqtt()
