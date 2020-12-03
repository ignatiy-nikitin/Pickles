import random
import time

from cloud import send_current_temperature, send_current_humidity, send_reference_humidity, send_reference_temperature


def generate_temperature():
    return random.uniform(20, 30)


def generate_humidity():
    return random.uniform(50, 100)


while True:
    time.sleep(2)
    temperature = generate_temperature()
    humidity = generate_humidity()
    send_current_temperature(temperature)
    send_current_humidity(humidity)
