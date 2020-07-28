#!/usr/bin/env python
import socket

class LightBulb:
    HOST = '192.168.4.1'  # The IP address of ESP32. 
    PORT = 1234           # The port used by the Light Server.
    color = ""
    Label = ""
    connected = False
    msg_reply = ""
    msg_send = ""
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
            s.settimeout(5)
            try:
                s.connect((self.HOST, self.PORT))
            except socket.error as err:
                self.error_msg = err
                msg_reply = "Unreachable"
            else:
                self.msg_send = self.color+" status"
                s.send(self.msg_send.encode("ascii"))
                try:
                    msg_reply = s.recv(11).decode('ascii')
                except socket.error as err:
                    self.error_msg = err
                    msg_reply = "Not reply"
            finally:
                s.close()
            if not msg_reply:
                msg_reply = "Empty"
            return msg_reply
        else:
            return "Not connected"

    def on(self):
        if self.connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            try:
                s.connect((self.HOST, self.PORT))
            except socket.error as err:
                self.error_msg = err
                self.msg_reply = "Uneachable"
            else:
                self.msg_send= self.color+" on"
                s.send(self.msg_send.encode("ascii"))
                try:
                    self.msg_reply = s.recv(11)
                except socket.error as err:
                    self.error_msg = err
            finally:
                s.close
            return self.msg_reply
        else:
            return "Not connected"

    def off(self):
        if self.connected:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            try:
                s.connect((self.HOST, self.PORT))
            except socket.error as err:
                self.error_msg = err
                self.msg_reply = "Uneachable"
            else:                            
                self.msg_send = self.color+" off"
                s.send(self.msg_send.encode("ascii"))
                try:
                    self.msg_reply = s.recv(11)
                except socket.error as err:
                    self.error_msg = err
            finally:
                s.close
            return self.msg_reply
        else:
            return "Not connected"

    def __del__(self):
        return 0
