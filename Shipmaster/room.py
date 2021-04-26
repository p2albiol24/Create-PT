



class Room():
    def __init__(self, room_name, locked):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.locked = locked

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def get_name(self):
        return self.name

    def get_locked(self):
        if self.locked == 'no':
            return 'no'
        if self.locked == 'yes':
            return 'yes'

    def lock(self):
      self.locked = 'yes'
      return self.locked

    def unlock(self):
        self.locked = 'no'
        return self.locked

    def set_name(self, room_name):
        self.name = room_name

    def set_room(self, room):
        self.room = room
        return self.room

    def describe(self):
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def locker(self):
        if self.get_locked() == 'yes':
            print("This room is locked.")
            if self.name == 'East Engine Room':
                return 'closet1'
            if self.name == 'Maintinence Room':
                return 'ship_log_room'
            if self.name == 'Human Quarters 1':
                return 'midhw'
            if self.name == 'Human Quarters 2':
                return 'bar'
            if self.name == 'Human Quarters 3':
                return 'rroom'
            if self.name == 'Human Quarters 4':
                return 'cafe'
            if self.name == 'Human Quarters 5':
                return 'meet'
            if self.name == 'Gym':
                return 'midhw2'
            if self.name == 'West Gun Platform 1':
                return 'wesc1'
            if self.name == 'West Gun Platform 2':
                return 'whw3'
            if self.name == 'East Gun Platform 1':
                return 'esc1'
            if self.name == 'East Gun Platform 2':
                return 'ehw3'
            if self.name == 'Intelligence Operations Room':
                return 'midhw3'
            if self.name == 'Server Room':
                return 'computer'


    def get_details(self):
        print(self.name)
        print("------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if direction == "n":
                direction = "north"
            if direction == "s":
                direction = "south"
            if direction == "e":
                direction = "east"
            if direction == "w":
                direction = "west"
            if direction == "u":
                direction = "up"
            if direction == "d":
                direction = "down"
            print( "The " + room.get_name() + " is " + direction)






    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            if not direction == 'pour' or 'wear' or 'open' or 'unlock' or 'put' or 'burn' or 'light' or 'type' or 'water' or 'read' or 'drop' or 'grab' or '' or '' or '':
                print("Not a possible direction!")
            return self
    def room_set(self, room):
        self.room = room
        return room












