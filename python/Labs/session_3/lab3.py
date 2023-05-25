# Import Library 
from tkinter import *
window = Tk()

def Func():
	print("Engy")
	
	
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newwindow = Toplevel(window)
    # sets the title of the
    # Toplevel widget
    newwindow.title("New Window")
    # sets the geometry of toplevel
    newwindow.geometry("500x500")
    # A Label widget to show in toplevel
    Label(newwindow,text ="User Name").pack()
    
          
 

# Name the window 
window.title("Tkinter First App ")

#control widow size
window.geometry('500x500')

# Print label to window app 

label  = Label(window , text = "Engy")
# set lable at top 

label.pack(side = TOP)

# Adding a photo image object to use image 
photo = PhotoImage(file='b1.png')

#Create Button 
buttonbox = Button(window , text ="Print Name",bd='10',image = photo,command = Func,background="black")
buttonbox.pack(side = TOP)

#Create Button 
buttonbox1 = Button(window , text ="B4",bd='10',background="black",fg="cyan",font = ('Verdana',18),height= 1, width=5)
buttonbox1.pack(side = RIGHT)

#Create Button 
buttonbox2 = Button(window , text ="Enter User",bd='10',background="black",fg="cyan",font = ('Verdana',18),height= 1, width=5,command = openNewWindow)

buttonbox2.pack(side = LEFT)

#Create Button 
buttonbox3 = Button(window , text ="Close Window",bd='10',command = window.destroy,background="black",fg="cyan",font = ('Verdana',18))
buttonbox3.pack(side = BOTTOM)


# display app
label.mainloop()
