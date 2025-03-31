import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    """Prints feedback to the console and clears the text fields."""
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_text.get("1.0", tk.END).strip()

    if name and email and feedback:
        # Print feedback to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Feedback: {feedback}")
        print("-" * 30)

        # Clear the fields
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_text.delete("1.0", tk.END)

        # Confirmation message
        messagebox.showinfo("Thank You", "Feedback submitted successfully!")
    else:
        messagebox.showwarning("Incomplete", "Please fill out all fields!")

# Main window
window = tk.Tk()
window.title("Customer Feedback")
window.geometry("400x400")
window.config(padx=20, pady=20)

# Labels and Entry Fields
tk.Label(window, text="Name:").pack(anchor="w")
name_entry = tk.Entry(window, width=50)
name_entry.pack(pady=5)

tk.Label(window, text="Email:").pack(anchor="w")
email_entry = tk.Entry(window, width=50)
email_entry.pack(pady=5)

tk.Label(window, text="Feedback:").pack(anchor="w")
feedback_text = tk.Text(window, height=10, width=50)
feedback_text.pack(pady=5)

# Submit Button
submit_btn = tk.Button(window, text="Submit", command=submit_feedback)
submit_btn.pack(pady=10)

# Main loop
window.mainloop()
