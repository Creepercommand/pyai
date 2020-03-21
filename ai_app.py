import tkinter as tk
import tkinter.filedialog as fd

def openfile():
    fpath = fd.askopenfilename()
    if fpath:
            print("파일경로:", fpath)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="파일 열기",command=openfile)
imageLable = tk.Label()

imageLable.pack()

btn.pack()

tk.mainloop()