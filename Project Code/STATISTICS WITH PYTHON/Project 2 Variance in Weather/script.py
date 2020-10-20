import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data


#print(london_data.iloc[100:200])
#print (len(london_data))

temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
#print('average temperature is ' + str (average_temp))

temperature_var= np.var(temp)
#print('variance of temperature '+str(temperature_var))

temperature_standard_deviation = np.std(temp)
#print ('temperature_standard_deviation is ' + str(temperature_standard_deviation))

#print(london_data.head())

june = london_data.loc[london_data['month'] == 6]['TemperatureC']

july = london_data.loc[london_data['month']==7]['TemperatureC']

print('mean value of june is '+str(np.mean(june)))
print('mean value of june is '+str(np.mean(july)))

