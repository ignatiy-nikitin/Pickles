import requests

from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

HOST = 'demo.thingsboard.io'
TEMPERATURE_DEVICE_TOKEN = 'v1DnrTPOhDjbCPSAHvF0'
HUMIDITY_DEVICE_TOKEN = 'WdxDe0n8xMEw44YlyFde'
TEMPERATURE_DEVICE_ID = '8e571e80-340f-11eb-b861-97130ea8d378'
HUMIDITY_DEVICE_ID = '95088750-340f-11eb-b861-97130ea8d378'
TOKEN = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJpZ25hdC5ub0B5YW5kZXgucnUiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sInVzZXJJZCI6IjBjNzc0OTMwLTM0MGYtMTFlYi1iODYxLTk3MTMwZWE4ZDM3OCIsImZpcnN0TmFtZSI6IklnbmF0aXkiLCJsYXN0TmFtZSI6Ik5pa2l0aW4iLCJlbmFibGVkIjp0cnVlLCJwcml2YWN5UG9saWN5QWNjZXB0ZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiIwYmRkYTE0MC0zNDBmLTExZWItYjg2MS05NzEzMGVhOGQzNzgiLCJjdXN0b21lcklkIjoiMTM4MTQwMDAtMWRkMi0xMWIyLTgwODAtODA4MDgwODA4MDgwIiwiaXNzIjoidGhpbmdzYm9hcmQuaW8iLCJpYXQiOjE2MDY4NTI1MTIsImV4cCI6MTYwODY1MjUxMn0.dz7b7sXtCtSkA4_HYvIqQ5KdvraXGmHGUo2UcL8pNv8mbyxrwAAeeIZlJw1zZQHKuzsnSGw20pHPL6f2yytG8A'


def _send(token, data):
    client = TBDeviceMqttClient(HOST, token)
    client.connect()
    result = client.send_telemetry(data)
    success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
    client.disconnect()


def _get_telemetry(device_id):
    return requests.get(
        url='http://demo.thingsboard.io/api/plugins/telemetry/DEVICE/{}/values/timeseries'.format(device_id),
        headers={'X-Authorization': TOKEN},
    ).json()


def send_current_temperature(value):
    _send(TEMPERATURE_DEVICE_TOKEN, {'current_temperature': value})


def send_reference_temperature(value):
    _send(TEMPERATURE_DEVICE_TOKEN, {'reference_temperature': value})


def send_current_humidity(value):
    _send(HUMIDITY_DEVICE_TOKEN, {'current_humidity': value})


def send_reference_humidity(value):
    _send(HUMIDITY_DEVICE_TOKEN, {'reference_humidity': value})


def get_current_temperature():
    telemetry = _get_telemetry(TEMPERATURE_DEVICE_ID)
    return telemetry['current_temperature'][0]['value']


def get_current_humidity():
    telemetry = _get_telemetry(HUMIDITY_DEVICE_ID)
    return telemetry['current_humidity'][0]['value']


def get_reference_temperature():
    telemetry = _get_telemetry(TEMPERATURE_DEVICE_ID)
    return telemetry['reference_temperature'][0]['value']


def get_reference_humidity():
    telemetry = _get_telemetry(HUMIDITY_DEVICE_ID)
    return telemetry['reference_humidity'][0]['value']
