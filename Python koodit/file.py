# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import math
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P2)
#chan1 = AnalogIn(mcp, MCP.P1)

print("Raw ADC Value: ", chan.value >> 6)
print("ADC Voltage: " + str(chan.voltage) + "V")
#print("Raw ADC Value1: ", chan1.value)
#print("ADC Voltage1: " + str(chan1.voltage) + "V")


import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected {rc}")


client.on_connect = on_connect
client.connect("192.168.0.141", 1883, 60)

for i in range(151):
    #Asteiden laskua "https://learn.sunfounder.com/lesson-10-thermistor-2/"
    #beta=4090
    #sisus = (1025.0*10/(chan.value >>6)-10)/10
    #print (sisus)
    #logaritmi = math.log(sisus)
    #tempC = beta/((logaritmi)+beta/298)-273.0
    
    analogVal = (chan.value >>6) # Muutetaan 16-bittisestä 10-bittiseksi
    #print(analogVal)
    Vr = 5 * float(analogVal) / 1023
    Rt = 10000 * Vr / (5 - Vr)
    #print(Rt)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+21)))
    tempC = temp - 273.15
    tempC = round(tempC,1)
    print ('temperature = ', tempC, 'C')

    client.publish('rasp/topic', payload=tempC, qos=0, retain=False)
    print(f"send {tempC} to rasp/topic")
    time.sleep(300)
client.loop_forever()