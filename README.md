# PubSub

## Install MQTT Client libraries
`pip3 install paho-mqtt`

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
- Make sure your edge broker container is running (see "Starting and running the edge broker")
- Open two terminals.
- In the first terminal, run the command `mosquitto_sub -t 'test_topic`. This connects to the edge broker and listens to the topic `test_topic`.
- In the second terminal, run the command `mosquitto_pub -t 'test_topic' -m 'Hello World!'`. This connects to the edge broker and sends the message `Hello World!` to the topic `test_topic`.
- In the first terminal, you should now see the message `Hello World!`.
- Stop the `mosquitto_sub` in the first terminal with the command `ctrl-c`.

## Part 2
In this part you'll run pair of simple python scripts that listen and publish to a topic on the edge broker.
