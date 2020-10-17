flat_charge = 20.00
price_per_pound = 0
def ground_shipping(weight):
  if weight <=2:
    price_per_pound = 1.50
  elif weight >2 and weight <=6:
    price_per_pound = 3.0
  elif weight > 6 and weight <=10:
    price_per_pound = 4.0
  else:
    price_per_pound = 4.75
  return weight * price_per_pound + flat_charge

# final_price= ground_shipping(8.4)
# print ("Total Cost for ground shipping is "+str(final_price))

premium_ground_shipping = 125
# print ("total cost for premium shipping is " +str(premium_ground_shipping))

drone_price_pound = 0
def drone_shipping(weight):
  if weight<=2:
    drone_price_shipping = 4.50
  elif weight > 2 and weight <= 6:
    drone_price_shipping = 9.00
  elif weight > 6 and weight <= 10:
    drone_price_shipping = 12.00
  else:
    drone_price_shipping = 14.25
  return weight * drone_price_shipping
drone_final_price = drone_shipping(1.5) 
# print("Total Cost for drone shipping is "+ str(drone_final_price))

def cheapest_cost(weight):
  gsc = ground_shipping(weight)
  psc = premium_ground_shipping
  dsc = drone_shipping(weight)
  if gsc < psc and gsc < dsc:
    print("ground shipper is cheaper " + str(gsc))
  elif psc < gsc and psc < dsc:
    print("premium_shipping is cheaper " + str(psc) )
  elif dsc < gsc and dsc < psc:
    print("drone shippier is cheaper " + str(dsc))

least_cost = cheapest_cost(41.5)
print (least_cost)



