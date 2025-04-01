from tkinter import *
from tkinter import ttk
root = Tk()
btn1 = ttk.Button(root), #text = "click here", )
btn1.grid() #configure the geometry manager on its own line after the button has been created 
btn1.config(text = "Click!")
root.mainloop()
