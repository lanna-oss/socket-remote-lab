#!/usr/bin/env python3
### Reference:
### https://stackoverflow.com/questions/7678456/local-network-pinging-in-python

import socket
import sys

HOST = '192.168.4.1'  # The IP address of ESP32. 
PORT = 1234            # The port used by the server.


def Light_connected():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((HOST,PORT))
    if result == 0:
        return True
    else:
        return False

def main():
    if not Light_connected():
        print("Can not connect to the Light Server.")
        sys.exit(1)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Message = input("Type a command to ESP32 = ")
    
    try:
        s.connect((HOST, PORT))
        s.settimeout(1)
    except socket.error as err:
        s.close
        print(err)
        sys.exit(1)

    s.send(Message.encode("ascii"))
    content = s.recv(11)
    print("ESP32 reply back = {}".format(content.decode("utf8")))

if __name__ == "__main__":
    main()

