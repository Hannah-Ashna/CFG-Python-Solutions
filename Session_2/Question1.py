# Explanation: 
# 1) This program loops 100 times
# 2) It stores an output which is 'o' multiplied by the current number
# 3) It outputs this

# Hence, at the end of the loop you should have the final line output 'o' 99 times
# This is because the loop will end at 99 since it starts at 0 ...
for number in range(100):
    output = 'o' * number
    print(output)