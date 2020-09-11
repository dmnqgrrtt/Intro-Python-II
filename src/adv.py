from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Player 1", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

selection = "x"
while selection != "q":

    print("\n")
    print(f"{player_1.name}")
    print(f"Current Room: {player_1.current_room.name}")
    print(f"Room Description: {player_1.current_room.description}")
    print("\n")

    selection = input("Please enter the direction you would like the player to move: ").lower()
    print("\n")

    if selection == "n" or selection == "s" or selection == "e" or selection == "w":
        if(player_1.current_room == room['outside']):
            if(selection == "n"):
                player_1.current_room = room['outside'].n_to
            
            else:
                print("The only direction you can move from the  Outside Cave Entrance is North")
        elif(player_1.current_room == room['foyer']):
            if(selection == "n"):
                player_1.current_room = room['foyer'].n_to
            elif(selection == "s"):
                player_1.current_room = room['foyer'].s_to
            elif(selection == "e"):
                player_1.current_room = room['foyer'].e_to
            else:
                print("You cannot move west from the Foyer")
                print("\n")
        elif(player_1.current_room == room['overlook']):
            if(selection == "s"):
                player_1.current_room = room['overlook'].s_to
            else:
                print("You can only move south from the Grand Overlook")
                print("\n")
        elif(player_1.current_room == room['narrow']):
            if(selection == "w"):
                player_1.current_room = room['narrow'].w_to
            elif(selection == "n"):
                player_1.current_room = room['narrow'].n_to
            else:
                print("You can only move North or West from the Narrow Passage")
                print("\n")
        elif(player_1.current_room == room['treasure']):
            if(selection == "s"):
                player_1.current_room = room['treasure'].s_to
            else:
                print("You can only move south from the Treasure Chamber")
                print("\n")

    elif selection == "q":
                print("Thanks for playing!")
                print("\n")
    else:
        print("Sorry, valid directions are n for north, s for south, e for east, and w for west")