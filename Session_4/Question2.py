# Solution:

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

UserChoice = input("What would you like? ")

# Check if the item is in the Dictionary
if (UserChoice in chocolates):
    # Output the price by using the UserChoice as the key
    print("This is the price: {}".format(chocolates[UserChoice]))

# Let the user know their choice isn't available
else:
    print("Sorry, that's not available")