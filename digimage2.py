import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

for idx in range(50):
    plt.subplot(5,10, idx +1)
    plt.axis("off")
    plt.imshow(digits.images[idx], cmap = "Greys")
    plt.title(digits.target[idx])

plt.show()