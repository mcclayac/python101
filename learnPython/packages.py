from random import randint

d = {}
for i in range(1000):
    n = randint(0,10)
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

for n in d:
    print(n, " - ", d[n])


