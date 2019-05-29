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

# comment for Git
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Put some items in the rooms
room['foyer'].items = ['sword']

user = Player(room['outside'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

while True:
    cmd = input('...').split(' ')
    if len(cmd) == 1:
        cmd = cmd[0]
    print(cmd)
    if cmd == 'q':
        break
    elif cmd == 'describe':
        print(user.current_room.description)
    elif cmd == 'room':
        print(user.current_room.name)
    elif cmd[0] == 'move':
        print(user.move_rooms(cmd[1]))

    # Commands relating to the room

    elif cmd[0] == 'room':
        if cmd[1] == 'items':
            print(user.current_room.items)

    #

    elif cmd[0] == 'my':
        if cmd[1] == 'items':
            print(user.items)

    elif cmd[0] == 'get':
        if cmd[1] in user.current_room.items:
            user.get_item(cmd[1])
            user.current_room.remove_item_from_room(cmd[1])
            print(f'You grabbed the {cmd[1]}')
        else:
            print(f'There is no {cmd[1]} in this room')
