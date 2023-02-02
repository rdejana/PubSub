# PubSub

This example simulates an edge to cloud MQTT example.

## Install MQTT Client libraries
`pip3 install paho-mqtt`

## Install Mosquitto client
This depends on your OS.

For Ubuntu: `sudo apt install -y mosquitto-clients`

For macOS `brew install mosquitto`

## Build MQTT image
Change to the broker directory and run the following command to build mqtt image:
```
docker build -t mqtt .  
```

## Starting and running the edge broker
To start and run the edge broker, run the following command:

```
docker run -d --name edge_broker -p 1883:1883 mqtt
```
This starts the mqtt container with the name `edge_broker` running on port `1883` and runs the container in the background.

The container can be stopped with `docker stop edge_broker`, restarted with `docker start edge_broker` and deleted with 
`docker rm edge_broker` (note, this requires that the container first be stoped).

You can also get the container logs with the command `docker logs edge_container`.


## Part 1
In this part, we'll test our edge broker and make sure we can connect to it with a simple set of scripts.
1. Make sure your edge broker container is running (see "Starting and running the edge broker")
2. Open two terminals. 
3. In the first terminal, run the command `mosquitto_sub -t 'test_topic'`. This connects to the edge broker and listens to the topic `test_topic`. 
4. In the second terminal, run the command `mosquitto_pub -t 'test_topic' -m 'Hello World!'`. This connects to the edge broker and sends the message `Hello World!` to the topic `test_topic`. 
5. In the first terminal, you should now see the message `Hello World!`. 
6. Stop the `mosquitto_sub` in the first terminal with the command `ctrl-c`.

## Part 2
In this part you'll run pair of simple python scripts that listen and publish to a topic on the edge broker.
1. Review the files 'sub.py' and 'pub.py' in the directory part2.  `sub.py` is the subscription/listener script while `pub.py` is responsible for publishing a message.
2. Make sure your edge broker is running.
3. Start `sub.py` and then run `pub.py`.  In `sub.py`'s console, you should see the message `Hello MQTT...`.
4. Stop `sub.py`.

## Part 3a.
In this part, you'll simulate a remote broker.  You'll reuse your mqtt image and start a container listening on a new port.
```
docker run -d --name cloud_broker -p 2883:1883 mqtt
```
This binds the container port 1883 to 2883 on the host.
You can test that the cloud broker is running correctly by using the `mosquitto_sub` and `mosquitto_pub` commands.
You'll add the `-p` option to specific the port to connect to.
```
    mosquitto_sub -t test_topic -p 2883
```
```
    mosquitto_pub -t test_topic -p 2883 -m 'Hello Cloud!'
```

## Part 3b
In this part, we'll run four python scripts and use both the edge and cloud brokers.
You'll want to review the following files in the directory `part3`. 

`local_pub.py` - publishes a message to the `edge_broker` on the topic `local_topic`

`local_logger.py` -  listens to the `edge_broker` on the topic `local_topic` and logs out any message it receives.

`local_repeater.py` - listens to the `edge_broker` on the topic `local_topic` and forwards the message to the `cloud_broker` using the topic `cloud_topic`.

`cloud_listener.py` - listens to the 'cloud_broker' on the topic `cloud_topi` and prints the messages.

```
                                    local_logger.py
                                   /  
                                  /
  local_pub.py ----> edge_broker
                                 \
                                  \
                                   local_repeater.py ---> cloud_broker ----> cloud_listener.py


```

1. Make sure both the edge and cloud brokers are running
2. Start `cloud_listener.py`
3. Start `local_repeater.py`
4. Start `local_logger.py`
5. Run `local_pub.py`

You should see the following:
- In `local_logger.py`'s console: `local logger ->  A message for the edge broker`
- In `local_repeater.py`'s console: `repeater:  message received ->  A message for the edge broker`
- In `cloud_listner.py`'s console: `cloud listener ->  A message for the edge broker`

