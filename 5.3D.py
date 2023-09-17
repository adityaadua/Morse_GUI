from tkinter import *
import tkinter.font
import time
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.LOW)

dictionary = {
'A' : '.-' ,
'B' : '-...' ,
'C' : '-.-.' ,
'D' : '-..' ,
'E' : '.' ,
'F' : '..-.' ,
'G' : '--.' ,
'H' : '....' ,
'I' : '..' ,
'J' : '.---' ,
'K' : '-.-' ,
'L' : '.-..' ,
'M' : '--' ,
'N' : '-.' ,
'O' : '---' ,
'P' : '.--.' ,
'Q' : '--.-' ,
'R' : '.-.' ,
'S' : '...' ,
'T' : '-' ,
'U' : '..-' ,
'V' : '...-' ,
'W' : '.--' ,
'X' : '-..-' ,
'Y' : '-.--' ,
'Z' : '--..'
}

win = Tk()
win.title("Morse_GUI")
myFont=tkinter.font.Font(family='Helvetica',size=13,weight="bold")

def dash():
    GPIO.output(7,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(7,GPIO.LOW)
    time.sleep(1.0)
def dot():
    GPIO.output(7,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(7,GPIO.LOW)
    time.sleep(0.5)
    

def command_morse():
    input=input_char.get()
    if (len(input) > 12):
        print("THE SIZE OF THE INPUT IS GREATER THAN 12")
        return 
    for letter in input:
        for symbol in dictionary[letter.upper()]:
            if symbol=='.':
                dot()
            elif symbol=='-':
                dash()
            else:
                time.sleep(1.5)
            
input_char=Entry(win,font=myFont,width=24,bg='white')
input_char.grid(row=0,column=0)

button = Button(win, text = 'ENTER', font = myFont, command = command_morse, height = 2, width = 20)
button.grid( row =0, column = 3)

win.mainloop()