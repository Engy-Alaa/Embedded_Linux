# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
FullInput = ""

# 'InputButtonsPress' Function To Update Input
# In The Text Entry Box
def InputButtonsPress(Num):
    global FullInput
    FullInput +=  str(Num)
    InputText.set(FullInput)

# 'ClearPress' Function To Clear Screen(widget)
def ClearPress(): 
    global FullInput 
    FullInput = "" 
    InputText.set("")
 
# 'EqualPress' Function To Calculate the Result 
# present in input field
 
def EqualPress():
    global FullInput
    # 'eval':This function is used to evaluates the string expression directly
    Result = str(eval(FullInput)) 
    #Set The Result On The Widget 
    InputText.set(Result)

#Create Window Then Set It's Size And Tiltle
window = Tk() 
window.geometry("360x370")   
window.title("Calculator")

 
# Declaring string variable
# For storing Input

InputText = StringVar()
 
#Set Screen Frame Settings
 
ScreenFrame = Frame(window,  bd=0)
 
ScreenFrame.pack(side=TOP)
 
#Set Screen Input Settings
 
ScreenInput = Entry(ScreenFrame, fg = "white",font=('Verdana', 20, 'bold'), 
				textvariable=InputText, bg="#6b314f", justify=CENTER)
 
ScreenInput.grid(row=0, column=0)
# 'ipady' is internal padding to increase the height of input field 
ScreenInput.pack(ipady=18) 
 
#Set Buttons Frame Settings
 
ButtonsFrame = Frame(window, bg="#481640")
 
ButtonsFrame.pack()
 
# first row
ReminderButton = Button( ButtonsFrame, text = "%", fg = "white",font = ('Verdana',10), 
						width = 10, height = 3, bg = "#6C4966", command = lambda: InputButtonsPress("%")).grid(row = 0, column = 0)

CButton = Button( ButtonsFrame, text = "C", fg = "white",font = ('Verdana',10), 
				width = 10, height = 3, bg = "#6C4966",  command = lambda: ClearPress()).grid(row = 0, column = 1)

CEButton = Button( ButtonsFrame, text = "CE", fg = "white",font = ('Verdana',10),  
				 width = 10, height = 3, bg = "#6C4966", command = lambda: ClearPress()).grid(row = 0, column = 2)

Divide = Button( ButtonsFrame, text = "/", fg = "white",font = ('Verdana',10),  
				 width = 10, height = 3, bg = "#6C4966",  command = lambda: InputButtonsPress("/")).grid(row = 0, column = 3)
 
# second row
 
SevenButton = Button( ButtonsFrame, text = "7", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(7)).grid(row = 1, column = 0)
 
EightButton = Button( ButtonsFrame, text = "8", fg = "white",font = ('Verdana',10),  
					 width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(8)).grid(row = 1, column = 1)
 
NineButton = Button( ButtonsFrame, text = "9", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(9)).grid(row = 1, column = 2)
 
MultiplyButton = Button( ButtonsFrame, text = "*", fg = "white",font = ('Verdana',10),  
						width = 10, height = 3,  bg = "#6C4966",  command = lambda: InputButtonsPress("*")).grid(row = 1, column = 3)
 
# third row
 
FourButton = Button( ButtonsFrame, text = "4", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(4)).grid(row = 2, column = 0)
 
FiveButton = Button( ButtonsFrame, text = "5", fg = "white",font = ('Verdana',10) , 
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(5)).grid(row = 2, column = 1)
 
SixButton = Button( ButtonsFrame, text = "6", fg = "white",font = ('Verdana',10) , 
					width = 10, height = 3, bg = "#632545", command = lambda: InputButtonsPress(6)).grid(row = 2, column = 2)
 
SubtractButton = Button( ButtonsFrame, text = "-", fg = "white",font = ('Verdana',10) , 
						width = 10, height = 3,  bg = "#6C4966",  command = lambda: InputButtonsPress("-")).grid(row = 2, column = 3)
 
# fourth row
 
OneButton = Button( ButtonsFrame, text = "1", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(1)).grid(row = 3, column = 0)
 
TwoButton = Button( ButtonsFrame, text = "2", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(2)).grid(row = 3, column = 1)
 
ThreeButton = Button( ButtonsFrame, text = "3", fg = "white",font = ('Verdana',10),  
						width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(3)).grid(row = 3, column = 2)
 
AddButton = Button( ButtonsFrame, text = "+", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3, bg = "#6C4966",  command = lambda: InputButtonsPress("+")).grid(row = 3, column = 3)
 
# fourth row

EmptyButton = Button( ButtonsFrame, fg = "white",font = ('Verdana',10),  
						width = 10, height = 3,  bg = "#632545" ).grid(row = 4, column = 0,  padx = 1, pady = 1)
 
ZeroButton = Button( ButtonsFrame, text = "0", fg = "white",font = ('Verdana',10),  
					width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(0)).grid(row = 4, column = 1)

PointButton = Button( ButtonsFrame, text = ".", fg = "white",font = ('Verdana',10),  
						width = 10, height = 3,  bg = "#632545",  command = lambda: InputButtonsPress(".")).grid(row = 4, column = 2) 

EqualButton = Button( ButtonsFrame, text = "=", fg = "black",font = ('Verdana',10),  
						width = 10, height = 3, bg = "#cb33d5", command = lambda: EqualPress()).grid(row = 4, column = 3)
 
window.mainloop()
