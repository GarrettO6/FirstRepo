import tkinter as tk

# Window 2 using grid
window2 = tk.Tk()
window2.title("Window 2 - Grid")
window2.geometry("300x200")

label2 = tk.Label(window2, text="This is Window 2")
label2.grid(row=0, column=0, columnspan=2, pady=10)

btn3 = tk.Button(window2, text="Button 1")
btn3.grid(row=1, column=0, padx=10, pady=5)

btn4 = tk.Button(window2, text="Button 2")
btn4.grid(row=1, column=1, padx=10, pady=5)

window2.mainloop()
