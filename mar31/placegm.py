import tkinter as tk

# Window 3 using place
window3 = tk.Tk()
window3.title("Window 3 - Place")
window3.geometry("300x200")

label3 = tk.Label(window3, text="This is Window 3")
label3.place(x=100, y=20)

btn5 = tk.Button(window3, text="Button 1")
btn5.place(x=50, y=80)

btn6 = tk.Button(window3, text="Button 2")
btn6.place(x=150, y=80)

window3.mainloop()
