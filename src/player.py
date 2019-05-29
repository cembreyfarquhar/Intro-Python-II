# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move_rooms(self, direction):
        if self.current_room.move_rooms(direction) != 'error':
            self.current_room = self.current_room.move_rooms(direction)
            return f'Moved to room {self.current_room}'

