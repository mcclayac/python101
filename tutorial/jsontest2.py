
import json


f =open('game.json')
game = json.load(f)
f.close()

print(game)


game['price'] = 15.99

f = open('game.json', "w")
json.dump(game, f, indent=2)
f.close()


