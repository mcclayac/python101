from classes.monster import Monster
from functionsExamples import foo

__author__ = 'anthonymcclay'
__project__ = 'pycharm'
__date__ = '7/31/15'
__revision__ = '$'
__revision_date__ = '$'


foo()


m = Monster(name="orc", hitpoints=12, mclass='spider', armor=33)

print(m)

print(m.version)

m.version = 3.0

print(m.version)

print(Monster.version)

print('get attr1:', m.__getattribute__('name'),'|')

# print('get attr2:', m.__getattribute__('home'),'|')

print('get attr3:', m.__getattribute__('hitpoints'),'|')