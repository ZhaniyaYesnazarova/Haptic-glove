import serial
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Glove Bobby")
window.geometry("400x700")

ser = serial.Serial("COM16", baudrate=9600, timeout=1)

hand = Image.open("hand.png")
hand = ImageTk.PhotoImage(hand)
my_label = Label(window, image=hand, bd=2, relief="groove")
my_label.pack(pady=20)

ice = Image.open("fire.png").resize((100, 100))
ice = ImageTk.PhotoImage(ice)
label2 = Label(window, image=ice)

button = False

def change():
    global button
    if not button:
        ser.write(b'o')
        label2.place(x=130, y=300)
        toggle_button.config(text="STOP", bg="red", width=15, height=5)
        button = True
    else:
        ser.write(b'x')
        label2.place_forget()
        toggle_button.config(text="START", bg="green")
        button = False


toggle_button = Button(window, text="START", bg="green", command=change, width=15, height=5)
toggle_button.pack(pady=20)

window.mainloop()
