import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

print(digits.images[3])

plt.imshow(digits.images[3], cmap = 'Greys')
plt.show()