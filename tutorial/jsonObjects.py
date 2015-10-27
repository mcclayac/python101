import json



from classes.monster import Monster

monster = Monster(name="Orc", mclass="evil", hitpoints= 32, armor= 12)


#  print(monster)

dicMonster = vars(monster)

print(dicMonster)

f = open("monster.json", "w+")
json.dump(dicMonster, f, indent=2)
f.close()

