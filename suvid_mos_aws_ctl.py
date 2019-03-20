import boto3

client = boto3.client('iot-data')

response = client.get_thing_shadow(
    thingName='esp8266_10A10D'
)


client = boto3.client('iot-data')

response = client.get_thing_shadow(
    thingName='esp8266_10A10D'
)

print(response)

for s in response['payload']:
    print(s)

response = client.update_thing_shadow(
    thingName='esp8266_10A10D',
    payload=b'{"state":{"desired":{"on":true}}}'
)