#!/usr/bin/env python3


# def function(parameters):
#      instructions
#      return value


def f(x):
    return x*x

print(f(3))


def f(x,y):
    print('You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y))
    print('x * y = ' + str(x*y))

print(f(3,2))


def f2(x,y,z):
    return x+y+z   # this will return the sum because all variables are passed as parameters

sum = f2(3,2,1)
print(sum)


def highFive():
    return 5

def f(x,y):
    z = highFive()    # we get the variable contents from highFive()
    return x+y+z      # returns x+y+z. z is reachable becaue it is defined above

result = f(3,2)
print(result)


def doA():
    a = 5

def doB(a):
    print(a)   # we pass variable as parameter, this will work

print('dob:', doB(3))


