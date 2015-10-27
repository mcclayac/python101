firstName = input ("Firts Name")
lastName  = input ("Last name:")

test1 = input("Test 1 :")
test2 = input("Test 2 :")
test3 = input("Test 3 :")
test1 = int(test1)
test2 = int(test2)
test3 = int(test3)

average = (test1 + test2 + test3) / 3
print(average)


report = "{last}, {first}\n\
Test 1: {test1}\n\
Test 2: {test2}\n\
Test 3: {test3}\n\
===================\n\
Average: {average}"


print(report.format(last=lastName, first=firstName, test1=test1, test2=test2, test3=test3,
                    average=average))

