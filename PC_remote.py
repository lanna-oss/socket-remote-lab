#!/usr/bin/env python3

from tkinter import *
from tkinter import font
import socket

HOST = '192.168.4.1'  # The IP address of ESP32. 
PORT = 1234            # The port used by the server.

def get_status(color):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        Message = color+" status"
        s.send(Message.encode("ascii"))
        msg_reply = s.recv(10)
    return msg_reply.decode("utf8")

def set_status(Color,Light):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        Message = Color+" "+Light
        s.send(Message.encode("ascii"))
        msg_reply = s.recv(10)
    return msg_reply.decode("utf8")

def RedSwitch():
    Red_status = get_status("red")
    if(Red_status == "ON"):
        Msg_reply = set_status(Color = "red", Light = "off")
        if(Msg_reply == "Red off"):
            RedButton["text"] = "Red ON"
        else:
            RedButton["text"] = "Red OFF"

    if(Red_status == "OFF"):
        Msg_reply = set_status(Color = "red", Light = "on")
        if(Msg_reply == "Red on"):
            RedButton["text"] = "Red OFF"
        else:
            RedButton["text"] = "Red ON"

def GreenSwitch():
    Green_status = get_status("green")
    if(Green_status == "ON"):
        Msg_reply = set_status(Color = "green", Light = "off")
        if(Msg_reply == "Green off"):
            GreenButton["text"] = "Green ON"
        else:
            GreenButton["text"] = "Green OFF"

    if(Green_status == "OFF"):
        Msg_reply = set_status(Color = "green", Light = "on")
        if(Msg_reply == "Green on"):
            GreenButton["text"] = "Green OFF"
        else:
            GreenButton["text"] = "Green ON"

def YellowSwitch():
    Yellow_status = get_status("yellow")
    if(Yellow_status == "ON"):
        Msg_reply = set_status(Color = "yellow", Light = "off")
        if(Msg_reply == "Yellow off"):
            YellowButton["text"] = "Yellow ON"
        else:
            YellowButton["text"] = "Yellow OFF"

    if(Yellow_status == "OFF"):
        Msg_reply = set_status(Color = "yellow", Light = "on")
        if(Msg_reply == "Yellow on"):
            YellowButton["text"] = "Yellow OFF"
        else:
            YellowButton["text"] = "Yellow ON"

def BlueSwitch():
    Blue_status = get_status("blue")
    if(Blue_status == "ON"):
        Msg_reply = set_status(Color = "blue", Light = "off")
        if(Msg_reply == "Blue off"):
            BlueButton["text"] = "Blue ON"
        else:
            BlueButton["text"] = "Blue OFF"

    if(Blue_status == "OFF"):
        Msg_reply = set_status(Color = "blue", Light = "on")
        if(Msg_reply == "Blue on"):
            BlueButton["text"] = "Blue OFF"
        else:
            BlueButton["text"] = "Blue ON"

def exitProgram():
	print("Exit Button pressed")
	win.quit()	


win = Tk()
myFont = font.Font(family = 'Helvetica', size = 28, weight = 'bold')
font.families()

win.title("Touch Screen Button")
win.geometry('1024x768')

RedButtonMessage = "Red ON"
GreenButtonMessage = "Green ON"
YellowButtonMessage = "Yellow ON"
BlueButtonMessage = "Blue ON"

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 9) 
exitButton.pack(side = BOTTOM)

RedButton = Button(win, text = RedButtonMessage, font = myFont, command = RedSwitch, height = 2, width =9 )
RedButton.pack(side = LEFT)

GreenButton = Button(win, text = GreenButtonMessage, font = myFont, command = GreenSwitch, height = 2, width =9 )
GreenButton.pack(side = LEFT)

YellowButton = Button(win, text = YellowButtonMessage, font = myFont, command = YellowSwitch, height = 2, width =9 )
YellowButton.pack(side = LEFT)

BlueButton = Button(win, text = BlueButtonMessage, font = myFont, command = BlueSwitch, height = 2, width =9 )
BlueButton.pack(side = LEFT)

mainloop()
