#!/usr/bin/env python3


s = 'Hello Python'
print(s)
print(s[0])      # H
print( s[0:2] )    # HE
print(s[2:4])    # ll
print(s[6:])     # Python
print(s + ' ' + s)
print(s.replace('Hello', 'Thanks'))


sentence = 'The cat is brown'
q = 'cat'

if q == sentence:
    print ('equal')
else:
    print('not equal')

if q in sentence:
    print(q + 'found in : ' , sentence)


