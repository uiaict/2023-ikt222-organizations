class Building:
    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def remove_room(self, name):
        del self.rooms[name]
