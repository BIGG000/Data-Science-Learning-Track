import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

print(inventory.head(10))

staten_island = inventory.head(10)

product_request = staten_island.product_description
print (product_request)

seed_request = inventory[(inventory.location =='Brooklyn') & (inventory.product_type == 'seeds')]
print (seed_request)

inventory['in_stock'] = inventory.apply(lambda x: True if ['quantity'] > 0 else False, axis=1)
print(inventory.head())

inventory['total_value'] = inventory.apply(lambda x: x.price * x.quantity, axis = 1)
print(inventory.head())

combine_lambda = lambda row:'{} - {}'.format(row.product_type,row.product_description)
print(inventory.head(2))


inventory['full_discription'] = inventory.apply(lambda x: (x.product_type, x.product_description), axis = 1)
print(inventory.head(3))






