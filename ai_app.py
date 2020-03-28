import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.svm
import sklearn.datasets
import numpy

def openfile():
    fpath = fd.askopenfilename()
    if fpath:
        print("파일경로:", fpath)
        data = imagedata(fpath)
        predictDigits(data)

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)

    clf.fit(digits.data, digits.target)

    n = clf.predict([data])
    textLable.configure(text="이그림은 %d 입니다"% n)


def imagedata(filename):
    #DLALWLFMF  8X8의 그래이베으스로 변경
    grayImage= PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8), PIL.Image.ANTIALIAS)

    dispimage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLable.configure(image = dispimage)
    imageLable.image = dispimage

    numimage = numpy.asarray(grayImage, dtype=float)
    numimage = numpy.floor(16-16*(numimage/256))
    numimage = numimage.flatten()
    return numimage

root = tk.Tk()
root.geometry("400x400")

textLable = tk.Label(text="")
btn = tk.Button(root, text="파일 열기",command=openfile)
imageLable = tk.Label()

imageLable.pack()

btn.pack()
textLable.pack()

tk.mainloop()