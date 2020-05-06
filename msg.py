#!/usr/bin/env python3

import socket

HOST = '192.168.4.1'  # The IP address of ESP32. 
PORT = 1234            # The port used by the server.

Message = input("Type any message to send to ESP32 = ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(Message.encode("ascii"))
    content = s.recv(10)
    print("ESP32 reply back = {}".format(content.decode("utf8")))

