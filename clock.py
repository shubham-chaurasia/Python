from tkinter import *
# import tkinter : - it is a GUI builder library in python 
import tkinter as tk
# here i gave it a name as tk to access further with this name
from tkinter.ttk import *
# here ttk is installed from tkinter , it is used for styling 
from time import strftime
# now time module to fetch real time time from the device 

root = Tk()
root.title("Clock")

# this function is for providing time lable on the window 

def time():
    string = strftime('%X %p')
    lbl.config(text= string)
    lbl.after(1000,time)
    
lbl = Label(root,font= ('ds-digital' ,80, 'bold'),background = 'black',foreground = 'cyan')
lbl.pack()

time()
mainloop()


# happy coding 
# credit :- from geeks for geeks and google 