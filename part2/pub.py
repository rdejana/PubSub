import paho.mqtt.client as mqtt

# connection info
LOCAL_MQTT_HOST = "localhost"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "test_topic"

# set things up
local_mqttclient = mqtt.Client()
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

# publish the message
local_mqttclient.publish(LOCAL_MQTT_TOPIC, "Hello MQTT...")