import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
# print(df.head())

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head(2))
sns.set_style('whitegrid')
sns.set_context('poster',font_scale=0.8)
sns.barplot(data=df,x='Year',y='Total Goals')
f, ax=plt.subplots(figsize=(12,7))
ax = sns.barplot(data=df,x='Year',y='Total Goals')
ax.set_title('Average Number Of Goals Scored In World Cup Matches By Year')
plt.show()

# plt.clf()

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
# sns.set_style('whitegrid')
sns.set_context('notebook',font_scale=1.25)
f, ax2=plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=df_goals,x='year',y='goals',)
ax2.set_title('number of goals in all years')
plt.show()