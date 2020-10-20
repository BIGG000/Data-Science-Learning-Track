# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

#plt hist()
plt.figure(1)
plt.subplot(211)
plt.hist(flights, range = (0,365),bins = 365,edgecolor = 'black')
plt.xlabel('days')
plt.ylabel('flight rate')
plt.title('Day by Day flight rate')

plt.subplot(212)
plt.hist(in_bloom,range = (0,365),bins = 365)
plt.title("Flower Blooms and Flights by Day")
plt.ylabel("Bloom Count")
plt.xlabel("Day of the Year")



plt.show()