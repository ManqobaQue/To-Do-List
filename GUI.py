import tkinter as tk

def greet():
    print("Hello, world!")
    print("Manqoba")

root = tk.Tk()
root.title("My First Graphical User Interface")

button = tk.Button(root, text="Click me", command=greet)
button.pack()

root.mainloop()
