#1
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#2
lovely_loveseat_price = 254.00

#3
stylish_settee_description ="Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#4
stylish_settee_price = 180.50

#5
luxurious_lamp_description = "Luxurious Lamp. customer_one_totalGlass and iron. 36 inches tall. Brown with cream shade."

#6
luxurious_lamp_price = 52.15

#7
sales_tax = 0.088

#8 
customer_one_total = 0

#9
customer_one_itemization = ""

#10
customer_one_total += lovely_loveseat_price

#11
customer_one_itemization += lovely_loveseat_description

#12
customer_one_total += luxurious_lamp_price

#13
customer_one_itemization +=luxurious_lamp_description

#14
customer_one_tax = customer_one_total * sales_tax

#15
customer_one_total += customer_one_tax

#16 
print ("Customer One Items:")

#17
print (customer_one_itemization)

#18
print ("Customer One Total:")

#19
print (customer_one_total)

#20 






















