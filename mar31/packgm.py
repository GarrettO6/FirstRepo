import tkinter as tk

# Window 1 using pack
window1 = tk.Tk()
window1.title("Window 1 - Pack")
window1.geometry("300x200")

label1 = tk.Label(window1, text="This is Window 1")
label1.pack(pady=10)

btn1 = tk.Button(window1, text="Button 1")
btn1.pack(side=tk.LEFT, padx=10)

btn2 = tk.Button(window1, text="Button 2")
btn2.pack(side=tk.RIGHT, padx=10)

window1.mainloop()

