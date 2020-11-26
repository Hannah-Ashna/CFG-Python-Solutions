# Solution: The input is a string (a python standard)
# We're not allowed to compare a str and int so we need to convert it to an integer!
# To do this, we use int()

# The next issue we run into is that when we have enough money it tells us we can't afford the boat?
# We need to change the < sign to > to fix it ... 
my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')