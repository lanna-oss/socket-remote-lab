#!/usr/bin/env python
import socket

class LightBulb:
    HOST = '192.168.4.1'  # The IP address of ESP32. 
    PORT = 1234           # The port used by the Light Server.
    color = ""
    Label = ""
    connected = False
    error_msg = ""
    def __init__(self,color):
        self.color = color
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((self.HOST,self.PORT))
        except socket.error as err:
            self.connected = False
            self.error_msg = err
        else:
            if result == 0:
                self.connected = True
        finally:
            sock.close
           
    def status(self):
        if self.connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((self.HOST, self.PORT))
            except socket.error as err:
                self.error_msg = err
                msg_reply = "Unreachable"
            else:
                Message = self.color+" status"
                s.send(Message.encode("ascii"))
                msg_reply = s.recv(10)
            finally:
                s.close()
            return msg_reply.decode("utf8")
        else:
            return "Not connected"

    def on(self):
        if self.connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((self.HOST, self.PORT))
            except socket.error as err:
                self.error_msg = err
                msg_reply = "Uneachable"
            else:
                Message = self.color+" on"
                s.send(Message.encode("ascii"))
                msg_reply = s.recv(10)
            finally:
                s.close
            return msg_reply.decode("utf8")
        else:
            return "Not connected"

    def off(self):
        if self.connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((self.HOST, self.PORT))
            except socket.error as err:
                self.error_msg = err
                msg_reply = "Uneachable"
            else:                            
                Message = self.color+" off"
                s.send(Message.encode("ascii"))
                msg_reply = s.recv(10)
            finally:
                s.close
            return msg_reply.decode("utf8")
        else:
            return "Not connected"

    def __del__(self):
        return 0