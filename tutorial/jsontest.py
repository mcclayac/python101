import json

#f = open("cars.json")
#cars = json.load(f)

#print(cars)



game = {"title" : "professor X",
        "ratings" : "E10",
        "system" : "Nintendo DS",
        "price"  : 19.99,
        "in_stock" : True,
        "alex" : False }


f = open("game.json", "w+")
json.dump(game, f, indent=2)
f.close()




