import serial
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Glove Bobby")
window.geometry("400x700")

ser = serial.Serial("COM6", baudrate = 9600, timeout =1)

hand = Image.open("hand.png")
hand = ImageTk.PhotoImage(hand)
my_label = Label(window, image = hand, bd = 2, relief = "groove")
my_label.pack(pady=20)

ice = Image.open("bee.png").resize((30, 30))
ice = ImageTk.PhotoImage(ice)
label2 = Label(window, image=ice)
label3 = Label(window, image=ice)
label4 = Label(window, image=ice)
label5 = Label(window, image = ice)
label6 = Label(window, image = ice)



def imageOn():
    label2.place(x=130, y=75)
    label3.place(x=80, y=100)
    label4.place(x=180, y=60)
    label5.place(x=230, y=75)
    label6.place(x=310, y=220)


def imageOff():
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    label5.place_forget()
    label6.place_forget()  # hides it without clearing image


def turnOn():
    ser.write(b'o')
def turnOff():
    ser.write(b'x')


def first():
    turnOn()
    imageOn()

def second():
    turnOff()
    imageOff()

my_button = Button(window, text="Turn on", command=first)
my_button.pack(pady=20)

my_button2 = Button(window, text="Turn off", command=second)
my_button2.pack()


window.mainloop()
