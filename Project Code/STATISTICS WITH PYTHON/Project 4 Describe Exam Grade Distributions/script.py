import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import codecademylib3_seaborn


np.random.seed(1)

fig, axes = plt.subplots(nrows=4, ncols=1)

plt.subplot(4,1,1)
mu, sigma = 80,5
exam_1 = np.random.normal(mu, sigma, 120)
exam_1[50] = 55
exam_1[51] = 55
count, bins, ignored = plt.hist(exam_1, 25, range=[50, 100])
plt.ylabel("Count", fontsize=12)
plt.title("Exam 1", fontsize=14)




plt.subplot(4,1,2)
mu, sigma = 85,5
exam_2_norm = np.random.normal(mu, sigma, 85)
exam_2_u = np.random.uniform(60, 80, 35)
exam_2 = np.concatenate((exam_2_norm, exam_2_u))

count, bins, ignored = plt.hist(exam_2, 25, range=[50, 100])
plt.ylabel("Count", fontsize=12)
plt.title("Exam 2", fontsize=14)



plt.subplot(4,1,3)
mu, sigma = 85,5
exam_2_norm = np.random.normal(mu, sigma, 70)
exam_2_u = np.random.normal(65, 3.5, 50)
exam_2 = np.concatenate((exam_2_norm, exam_2_u))

count, bins, ignored = plt.hist(exam_2, 25, range=[50, 100])
plt.ylabel("Count", fontsize=12)
plt.title("Exam 3", fontsize=14)



plt.subplot(4,1,4)
mu, sigma = 80,6
exam_2_norm = np.random.normal(mu, sigma, 120)
exam_2 = np.concatenate((exam_2_norm, np.array([96,96])))
print(np.average(exam_2))
print(np.median(exam_2))


count, bins, ignored = plt.hist(exam_2, 25, range=[50, 100])
plt.xlabel("Score (%)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Final Exam", fontsize=14)

fig.tight_layout()

plt.show()