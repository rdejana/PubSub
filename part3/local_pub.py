import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST = "localhost"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "local_topic"


def on_connect_local(client, userdata, flags, rc):
    print("local publisher connected to edge broker with rc: " + str(rc))


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# publish the message
print("Sending ->  \"A message for the edge broker\"")
local_mqttclient.publish(LOCAL_MQTT_TOPIC, "A message for the edge broker")