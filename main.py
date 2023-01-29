import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

def helo():
  print('hello world!')


hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!",command=helo)
button.pack()

tk.mainloop()