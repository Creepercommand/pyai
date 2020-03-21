import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

def imagedata(filename):
    grayImage= PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8), PIL.Image.ANTIALIAS)

    numIamge = numpy.asarray(grayImage, dtype=float)
    numIamge = numpy.floor(16*16*(numIamge/256))
    numIamge = numIamge.flatten()

    return numIamge

def prediction(data):
    digits = sklearn.datasets.load_digits()

    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data,digits.target)

    n= clf.predict([data])
    print("예측값:", n)


data = imagedata("2.png")
prediction(data)
print(data)