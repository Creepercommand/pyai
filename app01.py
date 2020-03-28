import random
import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

ans = random.randint(1,100)


def text():
    a = int(inum.get())
    if ans == a:
        lbl.configure(text = "정답!")
        box.configure(state = 'readonly')
    else:

        if a > ans:
            lbl.configure(text = "내려")
        else:
            lbl.configure(text = "올려")

inum = tk.StringVar()
lbl = tk.Label(text = "")
btn = tk.Button(text = "찍기", command = text)
box = tk.Entry(textvariable =inum)

lbl.pack()
box.pack()
btn.pack()

tk.mainloop()