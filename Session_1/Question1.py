# Solution: The value of chairs is originally a string
# Hence, we need to change it to an int by simply removing the quotations

chairs = 15 # Original was '15'
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)

print('You need to buy {} nails'.format(message))
