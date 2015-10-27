#!/usr/bin/env python3


tuple = ()

tuple3 = (3,)

personalinfo = ("Diana", 32, "New york")

print(personalinfo[0])
print(personalinfo[1])
print(personalinfo[2])


name, age, country, career = ("Diana", 32, 'Cananda', 'CompSci')

print('name:' , name)
print('country:', country)



listNumbers = [ 6, 3, 7, 4]
# python 3
#tupleList = tuple(listNumbers)
#print(tupleList)

listNumbers2 = list(personalinfo)
print('tuple:', personalinfo)
print('list:', listNumbers2)

# Python3 issues
#person = ('Alison','Victoria','Brenda','Rachel','Trevor')
#person = tuple(sorted(person))
#print(person)


