import time

from cloud import get_current_temperature, send_current_temperature, send_current_humidity
from cloud import get_reference_temperature
from cloud import get_current_humidity
from cloud import get_reference_humidity


def regulate_temperature(current_temperature_, reference_temperature_):
    print('--regulate temperature. current: {}, reference: {}---'.format(current_temperature_, reference_temperature_))


def regulate_humidity(current_humidity_, reference_humidity_):
    print('--regulate humidity. current: {}, reference: {}---'.format(current_humidity_, reference_humidity_))


while True:
    time.sleep(5)
    current_temperature = get_current_temperature()
    reference_temperature = get_reference_temperature()
    current_humidity = get_current_humidity()
    reference_humidity = get_reference_humidity()

    regulate_temperature(current_temperature, reference_temperature)
    regulate_humidity(current_humidity, reference_humidity)

    send_current_temperature(reference_temperature)
    send_current_humidity(reference_humidity)
