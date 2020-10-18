import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(2))
print(cart.head(2))
print(checkout.head(2))
print(purchase.head(2))

visits_cart = pd.merge(visits,cart,how = 'left')

print(len(visits_cart))

visits_cart_Length = len(visits_cart)
cart_time_null = len(visits_cart[visits_cart.cart_time.isnull()])
print(cart_time_null)

non_customer = float(cart_time_null)*100/(visits_cart_Length)
print(non_customer)

cart_checkout = pd.merge(cart,checkout,how ='left')
null_checkout = len(cart_checkout.checkout_time.isnull())
no_of_checkout_percentage = (float(null_checkout) * 100) / float(len(cart_checkout))

print(no_of_checkout_percentage)

all_data = visits.merge(cart,how= 'left').merge(checkout,how ='left').merge(purchase,how='left')
print (all_data.head(4))

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print (all_data.head(1))

checkout_purchase = pd.merge(checkout, purchase, how='left')
print(checkout_purchase.head(2))
null_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
null_purchase_percentage = (float(null_purchase)*100)/float(len(checkout_purchase))
print(null_purchase_percentage)
print(all_data.time_to_purchase.mean())









