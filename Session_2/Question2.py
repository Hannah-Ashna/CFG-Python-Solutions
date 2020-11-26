# Solution: The issue is that the function calculate_vat does not return anything
# Simply add 'return' to the beginning of the line

def calculate_vat(amount):
    return amount * 1.2 # Add return to the beginning of this line to fix the function

total = calculate_vat(100)
print(total)
