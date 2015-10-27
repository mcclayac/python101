from math import ceil

__author__ = 'anthonymcclay'
__project__ = 'pycharm'
__date__ = '7/31/15'
__revision__ = '$'
__revision_date__ = '$'


def tonyfunction(host, port=80):
    "connect to host/port pair"
    pass

#  doc string
# Default aurguments
# =80 is the default value
# * inner functions
# Functions returns none if there is not an explicit return
#  only one return value
#  none, object, tuple
#


x = 2
def foo():
    global x
    y =3
    print(x)
    print(y)
    x = 1
    print(x)
    print("local")


foo()
print(x)
print("Result")

def add_one(x):
    return x + 1



print("Lambda function")
x = 33
add_onea = lambda x : x + 1
print(add_onea)

get_areacode = lambda phone: phone[1:4]

i = 33.7
round_up = lambda i: int(ceil(float(i)))
print(i)


bad = ['and', 'or']
s = "This is an example of an example lambda expression"
filt = lambda s: ''.join(c for c in s if c not in bad)

#  is_num = lamdba n: isinstance(n, (int, float, complex))



def foo2(pos1, pos2='abc', *args, **kvargs):
    print('pos arg1:', pos1)
    print('pos arg2:', pos2)
    for arg in args:
        print ('extra arg:', arg)
    for k, v in kvargs.items():
        print('extra args: %s=%s' % (k, v))

print('calling foo')
dic = {'bar' : 'cheers'}
foo2('bar', 'xyz', 'one more', bar3='tony')



add3 = lambda x, y, z: x + y + z

xlist = [ 1, 2, 3]
result1 = add3(xlist[0], xlist[1], xlist[2])

result2 = add3(*xlist)
print('Rsult 1 = ' , result1)
print('Rsult 2 = ' , result2)

