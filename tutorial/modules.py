
from random import randint

i = randint(0,10)
print(i)


d = {}
for i in range(1000):
    n = randint(0,10)
    if n in d:
        d[n] += 1
    else:
        d[n] = 1



for n in d:
    print (n, "-", d[n])


from random import choice
snacks = ['apple', 'candy','popcorn', 'chips']

snack = choice(snacks)
print(snack)

print("\n\n\nDate Time")
from datetime import time
lunch = time(hour=11, minute=30)
print(lunch.hour)

snack = time(hour=14)
print(lunch < snack)


from datetime import date
today = date.today()
print(today)
y2k = date(month=12, day=1, year=2000)
daysSince = today - y2k
print(daysSince)


from datetime import datetime
bday = datetime(month=3, day=29, year=1969)
diff = datetime.now() - bday
print(diff)
diff.days
print(diff/365.0, " years")


