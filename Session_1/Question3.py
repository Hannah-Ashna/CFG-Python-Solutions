# Solution:

# Define your Variables - Question specifies that values should be easily modified if needed
EggsPerOmelette = 4
EggsPerBox = 6
NumOfBoxes = 6

# Our formula to calculate the number of Omelettes
NumOfOmelettes = int((NumOfBoxes * EggsPerBox) / EggsPerOmelette)
# Output
print("You can make {} omelettes with {} boxes of eggs.".format(NumOfOmelettes, NumOfBoxes))