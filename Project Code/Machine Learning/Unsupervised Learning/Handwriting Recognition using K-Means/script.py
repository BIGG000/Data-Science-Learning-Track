import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans


digits = datasets.load_digits()
print(digits.target)

plt.gray()
plt.matshow(digits.images[100])
plt.show()
print(digits.target[100])

model = KMeans(n_clusters = 10, random_state=42)

model.fit(digits.data)

fig=plt.figure(figsize=(8,3))

fig.suptitle('Cluster center images',fontsize=14,fontweight='bold')
for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()

new_samples = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.60,7.32,0.99,0.00,0.00,0.00,0.00,0.00,2.06,7.62,1.98,0.00,0.00,0.00,0.00,0.00,1.52,7.62,2.29,0.00,0.00,0.00,0.00,0.00,1.07,7.63,3.21,0.00,0.00,0.00,0.00,0.00,0.00,7.62,3.81,0.00,0.00,0.00,0.00,0.00,0.00,7.39,3.58,0.00,0.00,0.00,0.00,0.00,0.00,0.99,0.23,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.92,3.90,5.85,7.40,6.03,0.38,0.00,2.67,7.40,7.47,5.80,4.80,7.62,2.98,0.53,7.55,6.03,0.84,0.00,0.77,7.62,3.51,0.76,7.62,3.05,0.00,0.00,0.07,6.63,5.64,1.14,7.62,5.11,3.05,3.05,3.74,7.09,5.64,0.00,4.66,7.62,7.62,7.62,7.63,5.87,1.98],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.54,0.00,0.00,0.00,0.00,0.00,0.00,1.83,7.55,1.15,0.00,0.00,0.00,0.00,0.00,2.29,7.62,1.52,0.00,0.00,0.00,0.00,0.00,2.29,7.62,1.52,0.00,0.00,0.00,0.00,0.00,2.29,7.62,1.52,0.00,0.00,0.00,0.00,0.00,2.21,7.62,1.45,0.00,0.00,0.00,0.00,0.00,0.08,1.98,0.00,0.00,0.00],
[0.00,0.00,3.35,7.62,7.62,4.73,0.00,0.00,0.00,0.00,3.73,7.62,7.40,7.62,2.44,0.00,0.00,0.00,1.91,7.62,3.13,6.18,6.71,0.15,0.00,0.00,4.42,7.47,0.53,2.29,7.62,2.67,0.00,0.15,7.02,5.11,0.00,0.92,7.63,3.51,0.00,2.29,7.62,3.13,3.36,6.86,7.62,2.59,0.00,3.05,7.62,7.62,7.63,6.10,1.83,0.00,0.00,0.76,3.81,3.58,1.15,0.00,0.00,0.00]
])
new_labels = model.predict(new_samples)
print(new_labels)
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')

