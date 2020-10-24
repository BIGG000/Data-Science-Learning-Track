import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()
print(prod_per_year)
x = df['year']
x = x.values.reshape(-1,1)
print(x)

y =df['totalprod']
print(y)

plt.scatter(x,y)
# plt.show()
regr = linear_model.LinearRegression()
regr.fit(x,y)
print(regr.coef_[0])

y_predict = regr.predict(x)
plt.plot(x,y_predict)
plt.show()

x_future = np.array(range(1,11))
print('before reshaping'+str(x_future))
x_future = x_future.reshape(-1,1)
print('after reshaping'+str(x_future))

future_predict = regr.predict(x_future)

plt.plot(x_future,future_predict)
plt.show()



