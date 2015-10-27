__author__ = 'anthonymcclay'
__project__ = 'pycharm'
__date__ = '7/30/15'
__revision__ = '$'
__revision_date__ = '$'


i = 0
while i < 5:
	print(i)
	i += 1


not_done = True
while not_done:
	# some block of code
	# when finished call break
	break


class Tony(object):
    pass



value = int(input("Enter#: "))
counter =int(value ** 0.5)  # sq root

while counter > 1:
    if value % counter == 0:
        print(value, " is composite")
        break
    counter -= 1
else:
    print(value, " is prime")




