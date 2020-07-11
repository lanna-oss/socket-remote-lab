#!/usr/bin/env python3

import socket

HOST = '192.168.4.1'  # The IP address of ESP32. 
PORT = 1234            # The port used by the server.

def Light_connected():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((HOST,PORT))
    except:
        return False
    else:
        if result == 0:
            return True

def ESP32Conversation():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Message = input("Type a command to ESP32 = ")
    
    try:
        s.connect((HOST, PORT))
        s.settimeout(5)
    except socket.error as err:
        s.close
        print(err)

    s.send(Message.encode("ascii"))
    content = s.recv(11)
    print("ESP32 reply back = {}".format(content.decode("utf8")))

def main():
    if Light_connected():
        ESP32Conversation()
    else:
        print("Can not connect to the Light Server.")

if __name__ == "__main__":
    main()
