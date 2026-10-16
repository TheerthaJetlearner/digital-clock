from tkinter import *
from tkinter.ttk import *

#importing strftime funtion to retrieve the apple mac's time
from time import strftime

root = Tk()
root.title('Clock')

#This function is used to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget do that clock will look more attractive
lbl = Label(root, font = ('calibiri', 40, 'bold'), bg ='orange', fg = 'white')

#Placing clock at the centre
lbl.pack(anchor='center')
time()

mainloop()
