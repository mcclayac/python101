
from random import choice


cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus!"
print "you can see", len(cave_numbers), " caves"
print "to play, just type the number"
print "of the cave you wish to enter next"

while (player_location == wumpus_location or
       player_location == wumpus_friend_location ):
    print "you are in cave", player_location
    if (player_location == wumpus_location - 1 or
        player_location == wumpus_location + 1 ) :
        print "I smell a wumpus"

    if (player_location == wumpus_friend_location -1 or
        player_location == wumpus_friend_locaion +1 ):
        print "I smell an even stinkier wumpus!"

    print "which cave next?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in cave_numbers):
        print planer_input, "is not a cave!"

    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Aargh! you got eaten by a wupus!"
            break
        if player_location == wumpus_friend_location:
            print "Aargh! you got eaten by a friend wumpus!"
            break
