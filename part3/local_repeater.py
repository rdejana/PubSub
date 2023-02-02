import paho.mqtt.client as mqtt
import sys

# the local/edge info
LOCAL_MQTT_HOST = "localhost"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "local_topic"

# the cloud info
CLOUD_MQTT_TOPIC = "cloud_topic"
CLOUD_MQTT_HOST = "localhost"
CLOUD_MQTT_PORT = 2883

# creat the objects
local_mqttclient = mqtt.Client()
cloud_mqttclient = mqtt.Client()

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

# the message handler, now with a reference to the cloud clien
def on_message(client, userdata, msg):
    try:
        print("repeater:  message received -> ", str(msg.payload.decode("utf-8")))
        # if we wanted to re-publish this message, something like this should work
        msg = msg.payload
        cloud_mqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])


# setting up call to cloud broker
cloud_mqttclient.connect(CLOUD_MQTT_HOST,CLOUD_MQTT_PORT)

# and setting up call to the local broker
local_mqttclient.on_connect = on_connect_local
local_mqttclient.on_message = on_message
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)


# go into a loop and start listening
local_mqttclient.loop_forever()