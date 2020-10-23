import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(webpage.content,'html.parser')
# print (soup)
rating_data = soup.find_all(attrs={"class":"Rating"})

rating=[]

for ratings in rating_data[1:]:
  rating.append(float(ratings.string))
print(rating)

plt.hist(rating)
plt.xlabel('rating')
plt.show()
plt.clf()

company_data = soup.select('.Company')
print(company_data)

company_names = []

for companies in company_data[1:]:
  company_names.append(companies.get_text())

print(company_names)

d={"Company":company_names,'Rating':rating}
df=pd.DataFrame.from_dict(d)
print(df)

mean_value = df.groupby("Company").Rating.mean()
top_ten = mean_value.nlargest(10)
print(top_ten)

#is more cacoa better
cacoa_data = soup.select('.CocoaPercent')
cacoa=[]
for i in cacoa_data[1:]:
  percent = float(i.get_text().strip('%'))
  cacoa.append(percent)
print(cacoa)

df['CocoaPercentage'] = cacoa
print(df.head())

plt.scatter(df.CocoaPercentage,df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")

plt.show()