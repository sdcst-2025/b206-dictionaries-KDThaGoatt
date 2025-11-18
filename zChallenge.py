#!python3
# Explain what this code does

import random
x = []
for i in range(40):
    if random.randint(0,1):
        x.append(random.randint(1,10))
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10)

print(x)


'''
The code generates a list with 40 random numbers
these numbers are determined by a true/false system with if random.randint(0,1)
1 = True and 0 = False
if the number generated is 1 (True)
it will append a random integer from 1 to 10 to the list
if the number generated is 0 (False)
it will append a random integer from 1 to 10 plus a random integer from 1 to 10 divided by 10, making a decimal
basically this code generates a list of 40 random numbers from 1 to 10 with a 50/50 chance of each number being a decimal
'''
