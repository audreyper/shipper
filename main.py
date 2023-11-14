
weight = 41.5

ground_price = ''

if weight <= 2:
  ground_price = (1.50 * weight) + 20
elif weight > 2 and weight <= 6:
  ground_price = (3 * weight) + 20 
elif weight > 6 and weight <= 10:
  ground_price = (4 * weight) + 20 
elif weight > 10:
  ground_price = (4.75 * weight) + 20 

print("Your price for Ground Shipping will be $", ground_price)

print("Your price for Ground Shipping Premium will be $125.00")

drone_price = ''

if weight <= 2:
  drone_price = 4.50 * weight
elif weight > 2 and weight <= 6:
  drone_price = 9 * weight 
elif weight > 6 and weight <= 10:
  drone_price = 12 * weight 
elif weight > 10:
  drone_price = 14.25 * weight

print("Your price for Drone Shipping will be $" + str(drone_price))









