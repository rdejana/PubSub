#!/bin/bash

mosquitto_pub -t 'test_topic' -m 'Hello World!'
echo 'message sent'