import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(2))

#2
most_view = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(most_view)

#3
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(2))

#4
click_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print (click_by_source)

#5
click_pivot = click_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()
print (click_pivot)

#6
click_pivot['percent_clicked'] = click_pivot[True]/(
  click_pivot[True] + click_pivot[False])
print (click_pivot)

#7
experimental = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print (experimental)

#8
per_checking = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print (per_checking)



#9
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
print (a_clicks.head(2))

#10
# aaclick = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
# bbclick = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
# pivot_a = aaclick.pivot(
#   columns = 'day',
#   index = ' is_click',
#   values = 'user_id').reset_index()
# print(pivot_a)
aclicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
bclicks= b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()

aclicks_pivot = aclicks.pivot(columns='is_click',index='day',values='user_id')
aclicks_pivot['percent_clicked'] = \
	aclicks_pivot[True] /\
  (aclicks_pivot[True] + 
  aclicks_pivot[False])
print aclicks_pivot
bclicks_pivot = bclicks.pivot(columns='is_click',index='day',values='user_id')
bclicks_pivot['percent_clicked'] = \
	bclicks_pivot[True] /\
  (bclicks_pivot[True] + 
  bclicks_pivot[False])
print (bclicks_pivot)
