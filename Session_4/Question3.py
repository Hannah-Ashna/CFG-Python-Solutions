# Solution:

# We'll need random to help us generate values later
import random

# Declare two lists, one with the LotteryTicket and an empty list with the User's ticket
LotteryTicket = [30, 24, 2, 45, 19, 40, 4]
UserTicket = []

# We also need a counter to check how many matches we get!
MatchCounter = 0

# Let us also make a dictionary for our prizes to make things simpler
Prizes = {
    3 : "$20",
    4 : "$40",
    5 : "$100",
    6 : "$10000",
    7 : "$1000000"
}

# Randomly populate the User's ticket with 7 numbers from 0, 50
# Note: You can alter this range to make it easier to test ... otherwise it may take forever!
for x in range (0, 7, 1):
    UserTicket.append(random.randint(0,50))

# Output the UserTicket:
print("Your ticket: ", UserTicket)

# Time to check for matches, we'll loop through each list and compare all values against
# the other's values one by one
for x in range (0, len(LotteryTicket), 1):
    for y in range (0, len(UserTicket), 1):
        if UserTicket[x] == LotteryTicket[y]:
            # If there's a match, increment the counter by 1
            MatchCounter+=1

# Let's check if we've won any prizes ...
# Check if the number of matches we have is in the prizes
if (MatchCounter in Prizes):
    # If successful, let's output how much money the user has won
    # We do this by using MatchCounter as a key for the dictionary!
    print("You've won: {}!!".format(Prizes[MatchCounter]))

# Matches < 3? Let the user know they've lost
else:
    print("Guess there weren't enough matches ... sorry!")