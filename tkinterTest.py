import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter", foreground="white", background="black", width=25, height=10)
greeting.pack()

entry = tk.Entry(fg="white", bg="black", width=25)
entry.pack()

button = tk.Button(text="Click me", width=25, height=5, bg="white", fg="black")
button.pack()

window.mainloop()