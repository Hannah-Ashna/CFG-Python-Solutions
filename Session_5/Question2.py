# Solution: You're opening the file to 'r'- read only
# We need to instead open it to 'w' - write 

poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file: # Change 'r' to 'w'
    poem_file.write(poem)
