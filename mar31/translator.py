import tkinter as tk

def translate(language):
    """Change the label text based on the selected language."""
    translations = {
        "Espanol": "Hola",
        "Francais": "Bonjour",
        "Deutsch": "Hallo",
        "English": "Hello"
    }
    label.config(text=translations[language])

# Main window
window = tk.Tk()
window.title("Hello Translator")
window.geometry("400x300")

# Buttons for language selection
btn_es = tk.Button(window, text="Espanol", command=lambda: translate("Espanol"))
btn_es.pack(side=tk.LEFT, padx=10, pady=20)

btn_fr = tk.Button(window, text="Francais", command=lambda: translate("Francais"))
btn_fr.pack(side=tk.LEFT, padx=10, pady=20)

btn_de = tk.Button(window, text="Deutsch", command=lambda: translate("Deutsch"))
btn_de.pack(side=tk.LEFT, padx=10, pady=20)

btn_en = tk.Button(window, text="English", command=lambda: translate("English"))
btn_en.pack(side=tk.LEFT, padx=10, pady=20)

# Label to display the translation
label = tk.Label(window, text="Press a button", font=("Helvetica", 16))
label.pack(pady=20)

# Main loop
window.mainloop()
