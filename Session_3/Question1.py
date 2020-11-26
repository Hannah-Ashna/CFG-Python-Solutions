# Solution:

# Take user input, it's already a string so no need to use str()
UserInput = input("Is it raining? (y/n): ")

# Is their answer yes?
if (UserInput == "y"):
    print("Take an umbrella ...")

# Is their answer no?
elif (UserInput == "n"):
    print("You do not need an umbrella ...")

# This is in case they can't figure out how to press y/n!
else:
    print("Thats not an option!")