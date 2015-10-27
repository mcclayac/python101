from sys import stdout

__author__ = 'anthonymcclay'
__project__ = 'pycharm'
__date__ = '7/30/15'
__revision__ = '$'
__revision_date__ = '$'


try:
    f = open('/Users/anthonymcclay/Documents/testfile.txt', "r" )
    all = f.readlines()
    f.close()
    for line in all:
        print(line,end=' ')
except IOError as e:
    print("error:", e)





