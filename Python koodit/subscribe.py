import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected {rc}")
client.subscribe("rasp/topic")
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}") 

client.on_connect = on_connect
client.on_message = on_message
client.will_set('rasp/status',b'{"status": "Off" }')
client.connect("192.168.0.140", 1883, 60)
client.loop_forever()