from machine import Pin
from time import sleep
import network
import config
from simple import MQTTClient


# Define LED
led = Pin(0, Pin.OUT)

# Constants for MQTT Topics
MQTT_TOPIC_LED = 'pico/led'

MQTT_KEEPALIVE = 1111000 #7200
MQTT_SSL = False   # set to False if using local Mosquitto MQTT broker
MQTT_SSL_PARAMS = {'server_hostname': config.mqtt_server}

# Init Wi-Fi Interface
def initialize_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Connect to the network
    wlan.connect(ssid, password)

    # Wait for Wi-Fi connection
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        sleep(1)

    # Check if connection is successful
    if wlan.status() != 3:
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        print('mqtt server\'s address:',config.mqtt_server )
        return True

# Connect to MQTT Broker
def connect_mqtt():
    try:
        client = MQTTClient(client_id=b'raspberrypi_picow',
                    server=config.mqtt_server,
                    port=config.mqtt_port,
                    keepalive=MQTT_KEEPALIVE,
                    ssl=MQTT_SSL,
                    ssl_params=MQTT_SSL_PARAMS if MQTT_SSL else None)

        client.connect()
        print('Connected to MQTT broker')
        return client
    except OSError as e:
        print('OS error:', e)
    except Exception as e:
        print('General error:', e)
    return None


# Subcribe to MQTT topics
def subscribe(client, topic):
    client.subscribe(topic)
    print('Subscribe to topic:', topic)

def publish(client, topic, message):
    client.publish(topic, message)
    print('Published to topic:', topic, 'Message:', message)

# Callback function that runs when you receive a message on subscribed topic
def my_callback(topic, message):
    # Perform desired actions based on the subscribed topic and response
    print('Received message on topic:', topic)
    print('Response:', message)
    # Check the content of the received message
    if message == b'ON':
        print('Turning LED ON')
        led.value(1)  # Turn LED ON
    elif message == b'OFF':
        print('Turning LED OFF')
        led.value(0)  # Turn LED OFF
    else:
        print('Unknown command')
    
try:
    # Initialize Wi-Fi
    if not initialize_wifi(config.wifi_ssid, config.wifi_password):
        print('Error connecting to the network... exiting program')
    else:
        # Connect to MQTT broker, start MQTT client
        client = connect_mqtt()
        client.set_callback(my_callback)
        subscribe(client, MQTT_TOPIC_LED)
        
        # Continuously checking for messages
        while True:
            sleep(5)
            client.check_msg()
            print('Loop running')
            if KeyboardInterrupt:
                pico_msg = input('try to type something') 
                publish(client, MQTT_TOPIC_LED, pico_msg)
except Exception as e:
    print('Error:', e)