from datetime import datetime

f = open("tonyfile.txt")
lines = f.readlines()
print(lines)
f.close()

tmp = []
for line in lines:
    tmp.append(line.strip())
print(tmp)

lines = tmp

f = open("tonyfile.txt", "a")
tmp = "Tony -" + datetime.now().__str__()
f.write(tmp +"\n")
f.write("\n")
f.close()


import os
#os.mkdir('tonydir')
listsDir = os.listdir('.')
print(listsDir)

