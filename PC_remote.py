#!/usr/bin/env python
# This program running on python3 virtual environment.

from tkinter import *
from tkinter import font
from Light_Bulb import LightBulb

def main():
    def RedSwitch():
        Red_status = red.status()
        if(Red_status == "ON"):
            Msg_reply = red.off()
            if(Msg_reply == "Red off"):
                RedButton["text"] = "Red ON"
            else:
                RedButton["text"] = "Red OFF"

        if(Red_status == "OFF"):
            Msg_reply = red.on()
            if(Msg_reply == "Red on"):
                RedButton["text"] = "Red OFF"
            else:
                RedButton["text"] = "Red ON"


    def GreenSwitch():
        Green_status = green.status()
        if(Green_status == "ON"):
            Msg_reply = green.off()
            if(Msg_reply == "Green off"):
                GreenButton["text"] = "Green ON"
            else:
                GreenButton["text"] = "Green OFF"

        if(Green_status == "OFF"):
            Msg_reply = green.on()
            if(Msg_reply == "Green on"):
                GreenButton["text"] = "Green OFF"
            else:
                GreenButton["text"] = "Green ON"

    def YellowSwitch():
        Yellow_status = yellow.status()
        if(Yellow_status == "ON"):
            Msg_reply = yellow.off()
            if(Msg_reply == "Yellow off"):
                YellowButton["text"] = "Yellow ON"
            else:
                YellowButton["text"] = "Yellow OFF"

        if(Yellow_status == "OFF"):
            Msg_reply = yellow.on()
            if(Msg_reply == "Yellow on"):
                YellowButton["text"] = "Yellow OFF"
            else:
                YellowButton["text"] = "Yellow ON"

    def BlueSwitch():
        Blue_status = blue.status()
        if(Blue_status == "ON"):
            Msg_reply = blue.off()
            if(Msg_reply == "Blue off"):
                BlueButton["text"] = "Blue ON"
            else:
                BlueButton["text"] = "Blue OFF"

        if(Blue_status == "OFF"):
            Msg_reply = blue.on()
            if(Msg_reply == "Blue on"):
                BlueButton["text"] = "Blue OFF"
            else:
                BlueButton["text"] = "Blue ON"

    def exitProgram():
        print("Exit Button pressed.")
        win.quit()	


    win = Tk()
    myFont = font.Font(family = 'Helvetica', size = 28, weight = 'bold')
    font.families()

    win.title("PC remote")
    win.geometry('1024x768')

    red = LightBulb("red")
    if red.connected:
        if red.status() == "ON":
            red.Label = "Red OFF"
        else:
            red.Label = "Red ON"
    else:
        red.Label = "Red none"

    green = LightBulb("green")
    if green.connected:
        if green.status() == "ON":
            green.Label = "Green OFF"
        else:
            green.Label = "Green ON"
    else:
        green.Label = "Green none"

    yellow = LightBulb("yellow")
    if yellow.connected:
        if yellow.status() == "ON":
            yellow.Label = "Yellow OFF"
        else:
            yellow.Label = "Yellow ON"
    else:
        yellow.Label ="Yellow none"

    blue = LightBulb("blue")
    if blue.connected:
        if blue.status() == "ON":
            blue.Label = "Blue OFF"
        else:
            blue.Label = "Blue ON"
    else:
        blue.Label = "Blue none"

    exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 9) 
    exitButton.pack(side = BOTTOM)

    RedButton = Button(win, text = red.Label, font = myFont, command = RedSwitch, height = 2, width =9 )
    RedButton.pack(side = LEFT)

    GreenButton = Button(win, text = green.Label, font = myFont, command = GreenSwitch, height = 2, width =9 )
    GreenButton.pack(side = LEFT)

    YellowButton = Button(win, text = yellow.Label, font = myFont, command = YellowSwitch, height = 2, width =9 )
    YellowButton.pack(side = LEFT)

    BlueButton = Button(win, text = blue.Label, font = myFont, command = BlueSwitch, height = 2, width =9 )
    BlueButton.pack(side = LEFT)

    mainloop()

if __name__ == "__main__":
    main()
