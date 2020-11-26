# Solution: The error is telling us that our my_name variable is undefined
# It's not sure what Penelope is ... to resolve it, we need to tell it that Penelope is
# a string by surrounnding it with " "

my_name = "Penelope" # Originally just Penelope without the quotes
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)