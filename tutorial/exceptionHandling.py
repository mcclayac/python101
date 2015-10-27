__author__ = 'anthonymcclay'
__project__ = 'pycharm'
__date__ = '7/30/15'
__revision__ = '$'
__revision_date__ = '$'



#try:
    # statements to monitor
#except ErrorName as reason
    # Handler to the exception


try:
    f = open('/Users/anthonymcclay/Documents/testfile.txt', "r" )
    all = f.readlines()
    f.close()
    for line in all:
        print(line,end=' ')
except IOError as e:
    print("File open error: %s" % str(e))
finally:
    #f.close()
    print("this happens last")

data = 3
data = 'tony'

assert( isinstance(data, int), 'must be int')






