import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

greeting = tk.Label(text="Name:", foreground="white", background="black", width=25, height=10)

entry = tk.Entry(fg="white", bg="black", width=25)

button = tk.Button(text="Click me", width=25, height=5, bg="white", fg="black")

greeting.pack()
entry.pack()
button.pack()

window.mainloop()