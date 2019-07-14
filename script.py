#method to calculate gorund shipping cost
def ground_shipping(weight):
  if weight <= 2:
    return (weight*1.5)+20
  elif (weight > 2) and (weight <= 6):
    return (weight*3)+20
  elif (weight > 6) and (weight <= 10):
    return (weight*4)+20
  elif (weight > 10):
    return (weight*4.75)+20

#test ground_shipping method
print(ground_shipping(8.4))

#variable to store premium shipping cost, it is only a flat rate
premium_cost = 125.00

#method to calculate drone shipping cost
def drone_shipping(weight):
  if weight <= 2:
    return (weight*4.5)
  elif (weight > 2) and (weight <= 6):
    return (weight*9)
  elif (weight > 6) and (weight <= 10):
    return (weight*12)
  elif (weight > 10):
    return (weight*14.25)

#test drone_shipping method
print(drone_shipping(1.5))  

#method to calculate the cheapest price for a given package weight
def cheapest_price(weight):
  if (ground_shipping(weight) < premium_cost) and (ground_shipping(weight) < drone_shipping(weight)):
    print(ground_shipping(weight))
    return "Ground shipping is the cheapist"
  elif(premium_cost < ground_shipping(weight)) and (premium_cost < drone_shipping(weight)):
    print(premium_cost)
    return "Premium shipping is the cheapest"
  elif(drone_shipping(weight) < premium_cost) and (drone_shipping(weight)< ground_shipping(weight)):
    print(drone_shipping(weight))
    return "Drone shipping is the cheapest"

#test chaepest price method 
print(cheapest_price(41.5))
print(cheapest_price(4.8))
