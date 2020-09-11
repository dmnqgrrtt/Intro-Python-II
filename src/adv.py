from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[Item("Sword", "Sword of Gryffindor"), Item("Wand", "Elder wand")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[Item("Cloak", "Cloak of invisibility"), Item("Book", "Spell Book")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Item("Potion", "Polyjuice Potion"), Item("Fang", "Basilisk Fang")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[Item("Stone", "Sorcerer's Stone"), Item("Necklace", "Time Turner")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[Item("Diadem", "Ravenclaw's Diadem"), Item("Cup", "Hufflepuff's Cup")]),
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
player_1 = Player("Player 1", room['outside'], [])

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
    if len(player_1.current_room.items) == 0:
        print("There are no items available here")
        print("\n")
    else:
        print("These items are available here:")
        for item in player_1.current_room.items:
            print(f"Name: {item.name}")
            print(f"Description: {item.description}")
        print("\n")

    print("Here is a list of available commands:")
    print("Move your player by entering 'n' for North, 's' for South, 'e' for East, or 'w' for West")
    print("Pick up an item by entering 'get/take [name of the item]'")
    print("Drop an item by entering 'drop [name of the item]'")
    print("View your inventory by entering 'i' or 'inventory'")
    print("Quit the game by entering 'q'")
    print("\n")
    selection = input("Enter a command: ").lower()
    print("\n")

    
    command = selection.split(" ")

    if len(command) > 2:
        print("Sorry that is an invalid option")
    elif len(command) == 2:
        if command[0] == "get" or command[0] == "take":
            itemExists = False
            pickedUp = {}
            for item in player_1.current_room.items:
                if command[1] == item.name.lower():
                    itemExists = True
                    pickedUp = item
            if itemExists == True:
                player_1.inventory.append(pickedUp)
                player_1.current_room.items.remove(pickedUp)
                print(pickedUp.on_take())

            else:
                print("Sorry that item is not available here")
        elif command[0] == "drop":
            itemExists = False
            dropped = {}
            for item in player_1.inventory:
                if command[1] == item.name.lower():
                    itemExists = True
                    dropped = item
            if itemExists == True:
                player_1.inventory.remove(dropped)
                player_1.current_room.items.append(dropped)
                print(dropped.on_drop())

            else:
                print("Sorry that item is not in your inventory")
        else:
            print("Sorry, that is not a valid action")
    else:
        

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
        elif selection == "i" or selection == "inventory":
                    
                    if len(player_1.inventory) == 0:
                        print("You do have have any items in your inventory")
                        print("\n")
                    else:
                        print("Here is the list of current items in your inventory:")
                        for item in player_1.inventory:
                            print(f"Name: {item.name}")
                            print(f"Description: {item.description}")
                    print("\n")
        else:
            print("Sorry, valid directions are n for north, s for south, e for east, and w for west")