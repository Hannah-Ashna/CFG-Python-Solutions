# Solution:

import requests

# Declare a list with some Pokemon ID numbers, we're keeping it simple here :D
PokeID = [1, 2, 3, 4, 5, 6]

# Declare an empty list to store the Pokemon's names
PokeName = []

# Using a for loop, let's get the pokemon's names and store it in the list
for x in range (0, len(PokeID), 1):
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(PokeID[x])
    response = requests.get(url)
    pokemon = response.json()
    # Get the name value from the json and store it in the list
    PokeName.append(pokemon['name'])

# Now we'll create a text file and store the names into it
with open('pokemon.txt', 'w') as PokeFile:
    # Loop through each name in the list one by one
    for y in range (0, len(PokeName), 1):
        # Writes the name to a new line in the file because of "\n"
        PokeFile.write(PokeName[y] + "\n")



