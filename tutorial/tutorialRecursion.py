



def sum(list):
    sum = 0

    # Add every number in the list.
    for i in range(0, len(list)):
        sum = sum + list[i]

    # Return the sum.
    return sum

print(sum([5,7,3,8,10]))



def sum2(list):
   if len(list) == 1:
        return list[0]
   else:
        return list[0] + sum2(list[1:])

print('sum2:', sum2([5,7,3,8,10]))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print('Factorial 3:', factorial(3))



print('Factorial 9:', factorial(9))


import sys

sys.setrecursionlimit(5000)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3000))







