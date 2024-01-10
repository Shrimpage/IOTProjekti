import paho.mgtt.client as mqtt
import time

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected {rc}")

client.on_connect = on_connect
client.connect("192.168.0.140", 1883, 60)
for i in range(5):
    client.publish('rasp/topic', payload=i, qos=0, retain=False)
    print(f"send {i} to rasp/topic")
    time.sleep(1)
client.loop_forever()