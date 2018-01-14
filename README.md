### MQTT Publisher-Subscriber example on Raspberry Pi 3

Publisher, Subscriber codes for RaspberryPi in python using paho mqtt, regular expressions and subprocess.

The publisher and subscriber can run on either the rapberry pi, or the local host, but in this code the publisher fetches temperature data from the RPi using vcgencmd.

The codes have been made using the mqtt paho library for python.

This code also involves file write operation just to log gathered data to a temporary file 'output.txt'.
