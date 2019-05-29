# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def move_rooms(self, direction):
        if direction == 'n' and self.n_to != None:
            return self.n_to
        elif direction == 'e' and self.e_to != None:
            return self.e_to
        elif direction == 's' and self.s_to != None:
            return self.s_to
        elif direction == 'w' and self.w_to != None:
            return self.w_to
        else:
            return 'error'

    def put_item_in_room(self, item):
        self.items.append(item)

    def remove_item_from_room(self, item):
        self.items.remove(item)
