import paho.mqtt.client as mqtt
import sys

# host, port, and topic to use
LOCAL_MQTT_HOST = "localhost"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "test_topic"

# useful method to confirm that we are connecting
def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

# the function to handle a message
def on_message(client, userdata, msg):
    try:
        print("message received: ", str(msg.payload.decode("utf-8")))
        # if we wanted to re-publish this message, something like this should work
        # msg = msg.payload
        # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except:
        print("Unexpected error:", sys.exc_info()[0])

# let's connect
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# start the listening loop
local_mqttclient.loop_forever()