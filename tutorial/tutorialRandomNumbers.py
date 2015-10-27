#!/usr/bin/env python3

from random import *


print(random())


# randint
for i in range(1,101):
    print(randint(1,100))




#To generate a random floating point number between 1 and 10 you can use the uniform() function

print('uniform:', uniform(1, 10))

#We can shuffle a list with this code:

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(items)
print(items)



# To pick a random number from a list:
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = sample(items,  1)   # Pick a random item from the list
print(x[0])

y = sample(items, 4)    # Pick 4 random items from the list
print('4 random numbers from a lisy', y)



items = ['Alissa','Alice','Marco','Melissa','Sandra','Steve']

x = sample(items,  1)   # Pick a random item from the list
print(x[0])

y = sample(items, 4)    # Pick 4 random items from the list
print(y)


