toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("we sell " +str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices,toppings))
print (pizzas)

pizzas.sort()
cheapest_pizza = pizzas[1]
priciest_pizza = pizzas[-1]

three_cheapeast = pizzas[:2]

print("cheapeast",three_cheapeast)

num_two_dollar_slices = prices.count(2)
