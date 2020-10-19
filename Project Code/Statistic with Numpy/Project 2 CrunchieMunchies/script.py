import codecademylib

import numpy as np

calorie_stats = np.genfromtxt('cereal.csv',delimiter=',')

average_calories = np.mean(calorie_stats)
print('maximum calories '+str(np.max(calorie_stats)))
print('Minimum calories '+ str (np.min(calorie_stats)))
print('average calories ' +str(average_calories))

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.mean(calorie_stats)
print('median of calories is '+str(median_calories))

nth_percentile = np.percentile(calorie_stats,62)
print(nth_percentile)

more_calories = np.mean(calorie_stats > 60)
print('percentage is '+ str(more_calories))

calorie_std = np.std(calorie_stats)
print('standard deviation is ' +str(calorie_std))