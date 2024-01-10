import paho.mqtt.client as mqtt # Tuodaan kirjastot

client = mqtt.Client() # Tehdään client

def on_connect(client,userdata,flags,rc): # Yhteyden muodostuessa
    if rc == 0: # Suoritetaan tämä funktio
        print("Connect OK")
    else:
        print(f"Connect fail. Error: {rc}")

client.on_connect = on_connect # Liitetään on_connect funktioon
client.connect("192.168.0.140", 1883, 60) #muodostetaan yhteys
client.loop_forever()    