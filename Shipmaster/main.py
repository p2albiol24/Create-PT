



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
        return self.locked

    def lock(self):
      self.locked = 'yes'
      return self.locked

    def unlock(self):
        self.locked = 'no'
        return self.locked
        
    def set_lock(self, lock):
        self.locked = lock
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

    def save_deets(ooga):
        return ooga.description + "\n" + ooga.locked + '\n'
    
    def set_save(self, if_locked):
        self.locked = if_locked

    
    def locker(self):
        if self.get_locked() != 'no':
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
            if direction == "s" or "n" or "e" or "w" or "u" or "d":
                print("Not a possible direction!")
            return self
           
    def room_set(self, room):
        self.room = room
        return room
    
    def get_index(room):
        if room == "Hangar":
            return Rooms[0]
        if room == "Ship Log Room":
            return Rooms[1]
        if room == "Middle Hallway":
            return Rooms[3]
        if room == "East Hallway":
            return Rooms[4]
        if room == "West Hallway":
            return Rooms[5]
        if room == "Closet":
            return Rooms[6]
        if room == "East Storage":
            return Rooms[7]
        if room == "West Storage":
            return Rooms[8]
        if room == "East Bathroom":
            return Rooms[9]
        if room == "Stairs":
            return Rooms[10]
        if room == "Recreation Room":
            return Rooms[11]
        if room == "Meeting Room":
            return Rooms[12]
        if room == "Bridge":
            return Rooms[13]
        if room == "Bar":
            return Rooms[14]
        if room == "Cafe":
            return Rooms[15]
        if room == "Maintinence Room":
            return Rooms[16]
        if room == "West Engine Room":
            return Rooms[17]
        if room == "Human Quarters 1":
            return Rooms[18]
        if room == "Human Quarters 2":
            return Rooms[19]
        if room == "Human Quarters 3":
            return Rooms[20]
        if room == "Human Quarters 4":
            return Rooms[21]
        if room == "Human Quarters 5":
            return Rooms[22]
        if room == "Maze":
            return Rooms[23]
        if room == "Observation Tower":
            return Rooms[24]
        if room == "Top of Observation Tower":
            return Rooms[25]
        if room == "Back of Closet":
            return Rooms[26]
        if room == "Upstairs":
            return Rooms[27]
        if room == "Hangar Observation Room":
            return Rooms[28]
        if room == "Gym":
            return Rooms[29]
        if room == "Bathroom":
            return Rooms[30]
        if room == "Waiting Room":
            return Rooms[31]
        if room == "Library":
            return Rooms[32]
        if room == "Medical Bay":
            return Rooms[33]
        if room == "Medical Closet":
            return Rooms[34]
        if room == "East Engine Room":
            return Rooms[35]
        if room == "Computer Room":
            return Rooms[36]
        if room == "Computer Tool Room":
            return Rooms[37]
        if room == "Server Room":
            return Rooms[38]
        if room == "IT Quarters":
            return Rooms[39]
        if room == "Up Middle Hallway":
            return Rooms[40]
        if room == "Up East Hallway":
            return Rooms[41]
        if room == "Up West Hallway":
            return Rooms[42]
        if room == "Bridge Maintinence Room":
            return Rooms[43]
        if room == "Officer Bedroom":
            return Rooms[44]
        if room == "Captain Bedroom":
            return Rooms[45]
        if room == "Up Elevator":
            return Rooms[46]
        if room == "Recreation Elevator":
            return Rooms[47]
        if room == "Military Elevator":
            return Rooms[48]
        if room == "Recreation Observation Room":
            return Rooms[49]
        if room == "Military Observation Room":
            return Rooms[50]
        if room == "Pool":
            return Rooms[51]
        if room == "Bowling Alley":
            return Rooms[52]
        if room == "Snow Recreation Room":
            return Rooms[53]
        if room == "Garden":
            return Rooms[54]
        if room == "Tennis Courts":
            return Rooms[55]
        if room == "Mess Hall":
            return Rooms[56]
        if room == "Kitchen":
            return Rooms[57]
        if room == "Game Room":
            return Rooms[58]
        if room == "Board Game Room":
            return Rooms[59]
        if room == "Simulation Room":
            return Rooms[60]
        if room == "Music Room":
            return Rooms[61]
        if room == "Science Lab":
            return Rooms[62]
        if room == "Plant Lab":
            return Rooms[63]
        if room == "Planet & Stars Observatory":
            return Rooms[64]
        if room == "Recreation Middle Hallway":
            return Rooms[65]
        if room == "Recreation East Hallway":
            return Rooms[66]
        if room == "Recreation West Hallway":
            return Rooms[67]
        if room == "Military Middle Hallway":
            return Rooms[68]
        if room == "Military East Hallway":
            return Rooms[69]
        if room == "Military West Hallway":
            return Rooms[70]
        if room == "Family Quarters 1":
            return Rooms[71]
        if room == "Family Quarters 2":
            return Rooms[72]
        if room == "Family Quarters 3":
            return Rooms[73]
        if room == "Family Quarters 4":
            return Rooms[74]
        if room == "Command Operations Room":
            return Rooms[75]
        if room == "West Escape Pod 1":
            return Rooms[76]
        if room == "West Escape Pod 2":
            return Rooms[77]
        if room == "East Escape Pod 1":
            return Rooms[78]
        if room == "East Escape Pod 2":
            return Rooms[79]
        if room == "Middle Escape Pod":
            return Rooms[80]
        if room == "West Gun Platform 1":
            return Rooms[81]
        if room == "West Gun Platform 2":
            return Rooms[82]
        if room == "East Gun Platform 1":
            return Rooms[83]
        if room == "East Gun Platform 2":
            return Rooms[84]
        if room == "West Gun Ammunition Storage":
            return Rooms[85]
        if room == "East Gun Ammunition Storage":
            return Rooms[86]
        if room == "East Missile Launch Platform":
            return Rooms[87]
        if room == "West Missile Launch Platform":
            return Rooms[88]
        if room == "Intelligence Operations Room":
            return Rooms[89]
        if room == "West Brig Security Room":
            return Rooms[90]
        if room == "East Brig Security Room":
            return Rooms[91]
        if room == "West Brig":
            return Rooms[92]
        if room == "East Brig":
            return Rooms[93]
        if room == "Movie Theater":
            return Rooms[94]
        if room == "Dead":
            return Rooms[95]
        if room == "Shuttle":
            return Rooms[96]

Rooms = [hangar, ship_log_room, midhw, ehw, whw, closet1, estorage, wstorage, br1, mstairs, rroom, meetroom, bridge, bar, cafe, maint, engine, bed1, be2, bed3, bed4, bed5, maze, observe, upserve, closet2, ustairs, habserve, gym, bathroom, waiting, library, medbay,  medclo, engine2, compute, tool  server, it, midhw1, ehw1, whw1, brmaint, offbr, capbr, elev1, eleev2, elev3, robserve, mobserve, pool, bowl, snow, garden, tennis, mess, kitchen, game, board, sim, music, science, plant, observatory, middhw2, ehw2, whw2, midhw3, eh3, whw3, fq1, fq2, fq3, fq4, cor, wesc1, wesc2, esc1, esc2, esc, gpw1, gpw2, gpe1, gpe2, battery1, battery2, missile1, missile2, Intelligence,  srw, sre, wbrig, ebrig, movie, dead, shuttle]










class Item():
    def __init__(self, name, description, item_room):
        self.name = name
        self.description = description
        self.room = item_room
        
    def set_description(self, item_description):
        self.description = item_description
        return self.description

    def set_rom(self, item, room):
        self.room = item.room
        return self.room

    def get_room(item):
        return item.room

    def get_details(item):
        return item.room



    def inventory(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18):
        print()
        print()
        print('INVENTORY')
        print('--------------------')
        if item1.room == 'inv':
            print(item1.name)
            print(item1.description)
            print()
        if item2.room == 'inv':
            print(item2.name)
            print(item2.description)
            print()
        if item3.room == 'inv':
            print(item3.name)
            print(item3.description)
            print()
        if item4.room == 'inv':
            print(item4.name)
            print(item4.description)
            print()
        if item5.room == 'inv':
            print(item5.name)
            print(item5.description)
            print()
        if item6.room == 'inv':
            print(item6.name)
            print(item6.description)
            print()
        if item7.room == 'inv':
            print(item7.name)
            print(item7.description)
            print()
        if item8.room == 'inv':
            print(item8.name)
            print(item8.description)
            print()
        if item9.room == 'inv':
            print(item9.name)
            print(item9.description)
            print()
        if item10.room == 'inv':
            print(item10.name)
            print(item10.description)
            print()
        if item11.room == 'inv':
            print(item11.name)
            print(item11.description)
            print()
        if item12.room == 'inv':
            print(item12.name)
            print(item12.description)
            print()
        if item13.room == 'inv':
            print(item13.name)
            print(item13.description)
            print()
        if item14.room == 'inv':
            print(item14.name)
            print(item14.description)
            print()
        if item15.room == 'inv':
            print(item15.name)
            print(item15.description)
            print()
        if item16.room == 'inv':
            print(item16.name)
            print(item16.description)
            print()
        if item17.room == 'inv':
            print(item17.name)
            print(item17.description)
            print()
        if item18.room == 'inv':
            print(item18.name)
            print(item18.description)




















shuttle = Room("Shuttle", 'no')
shuttle.set_description("A shuttle in the hangar.")
shuttle.unlock

hangar = Room("Hangar", 'no')
hangar.set_description("It is a large, open, spacious hangar with private space shuttles and scattered supply boxes. You remember that you are in the futuristic space ship, 'The Blazing Donkey.' ")
hangar.unlock

ship_log_room = Room("Ship Log Room", 'no')
ship_log_room.set_description("A small room with security cameras, a desk, and a computer log, probably for checking who enters and who leaves the room.")
ship_log_room.unlock

midhw = Room("Middle Hallway", 'no')
midhw.set_description("A hallway leading into the rest of the ship from the hangar. The door to the private bedroom is locked.")
midhw.unlock

ehw = Room("East Hallway", 'no')
ehw.set_description("A hallway leading into the rest of the ship from the middle hallway.")
ehw.unlock

whw = Room("West Hallway", 'no')
whw.set_description("A hallway leading into the rest of the ship from the middle hallway.")
whw.unlock


closet1 = Room("Closet", 'no')
closet1.set_description("A closet off to the side of the hallway, full of cleaning equipment. The mop is extremely dry. The door to the east is the engine room, but it needs a maintinence code.")
closet1.unlock

estorage = Room("East Storage", 'no')
estorage.set_description("A large storage room, full of 500 boxes, east of the hangar.")
estorage.unlock

wstorage = Room("West Storage", 'no')
wstorage.set_description("A large storage room, full of 500 boxes, west of the hangar.")
wstorage.unlock

br1 = Room("East Bathroom", 'no')
br1.set_description("A bathroom to east of the east hallway with a sink, toilet and mirror.")
br1.unlock

mstairs = Room("Stairs", 'no')
mstairs.set_description("The stairs leading upwards.")
mstairs.unlock

rroom = Room("Recreation Room", 'no')
rroom.set_description("A room clearly meant for recreation with televisions, game systems and books. There are comfy couches and a mirror on the wall. The door to the private bedroom is locked.")
rroom.unlock

meetroom = Room("Meeting Room", 'no')
meetroom.set_description("A standard meeting room, with breakfast bagels and coffee on a large oval table. The door to the private bedroom is locked.")
meetroom.unlock

bridge = Room("Bridge", 'no')
bridge.set_description("The bridge of the ship with a Captain’s Chair at the center and various monitors, consoles, and instruments in the walls around the room.  An alarm light for the West Engine Room is amber, indicating … something.")
bridge.unlock

bar = Room("Bar", 'no')
bar.set_description("A standard bar, with a robot butler and nice tables and chairs about. There is an untouched vodka martini and a glass of chardonnay at a vacant table in the corner. The door to the private bedroom is locked.")
bar.unlock

cafe = Room("Cafe", 'no')
cafe.set_description("A room with a long counter down one side with stools. Several tables and chairs fill the cafe, with the smell of coffee and freshly baked croissants, most likely placed by the automatic breakfast robot. There are standard cafe items, for example, a cigar lighter. The door to the private bedroom is locked.")
cafe.unlock

maint = Room("Maintinence Room", 'yes')
maint.set_description("A room that contains a large map of the ship, a box of tools for fixing up various things, and a workers only sign on a door to the west. There appears to be a location marked on the map.")
maint.lock

engine = Room("West Engine Room", 'no')
engine.set_description("A room for controlling the engines, fixing the engines, and upgrades/overdrive with a Safety and Precaution sign on the wall. There is a sticky substance on the floor in the corner of the room.")
engine.unlock

bed1 = Room("Human Quarters 1", 'yes')
bed1.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nightstand, cabinet and closet are inside. A singular shoe lies under the bed.")
bed1.lock

bed2 = Room("Human Quarters 2", 'yes')
bed2.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nightstand, cabinet and closet are inside.")
bed2.lock

bed3 = Room("Human Quarters 3", 'yes')
bed3.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nghtstand, cabinet and closet are inside.")
bed3.lock

bed4 = Room("Human Quarters 4", 'yes')
bed4.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nghtstand, cabinet and closet are inside.")
bed4.lock

bed5 = Room("Human Quarters 5", 'yes')
bed5.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nghtstand, cabinet and closet are inside.")
bed5.lock

maze = Room("Maze", 'no')
maze.set_description("A twisty little area with hallways all alike...")
maze.unlock

observe = Room("Observation Tower", 'no')
observe.set_description("An observatory tower for surveying the spaceship with a nice view of outer space. Camera feeds from key locations on the ship are on display in this room.")
observe.unlock

ubserve = Room("Top of Observation Tower", 'no')
ubserve.set_description("The top of the observatory tower with a nice view of outer space and a few scattered controls. A pair of black leather gloves rests on the console.")
ubserve.unlock

closet2 = Room("Back of Closet", 'no')
closet2.set_description("Back of closet.")
closet2.unlock

ustairs = Room("Upstairs", 'no')
ustairs.set_description("The level of stairs above the bottom layer")
ustairs.unlock

habserve = Room("Hangar Observation Room", 'no')
habserve.set_description("The observation deck of the spaceships hangar. Several swivel chairs are in the room. To the east, there is a door that has a sign which warns, 'WE CANNOT GET RID OF THIS DOOR. UNDER NO CIRCUMSTANCES MAY ANYONE ENTER WITHOUT MAINTINENCE GLASSES!' ")
habserve.unlock

gym = Room("Gym", 'yes')
gym.set_description("A large, open, spacious room with various workout machines scattered about. A television monitor hangs on the wall, but is turned off. An open bottle of some sort of energy drink or thick, lime-green liquid sits in the treadmill holder.")
gym.lock

bathroom = Room("Bathroom", 'no')
bathroom.set_description("A small room with a sink, toilet, and a mirror.")
bathroom.unlock

waiting = Room("Waiting Room", 'no')
waiting.set_description("A small room with a couch, tv, remote, and tablestands. Soft music plays from a nearby speaker.")
waiting.unlock

library = Room("Library", 'no')
library.set_description("A library packed with a large selection of books. On the third shelf down, a few books in from the wall, a book is missing.")
library.unlock

medbay = Room("Medical Bay", 'no')
medbay.set_description("A room with gurneys, medical instruments, sinks, and a supply closet. A small pool of a clear liquid, with a strong acidic odor, rests by the sink.")
medbay.unlock

medclo = Room("Medical Closet", 'no')
medclo.set_description("A small closet filled with alcohol, bandages, and a bunch of other medical supplies that you don't recognize.")
medclo.unlock

engine2 = Room("East Engine Room", 'yes')
engine2.set_description("A room for controlling the engines, fixing the engines, and a safety precaution sign on the wall. A pair of safety goggles hang from a hook on the wall.")
engine2.lock

compute = Room("Computer Room", 'no')
compute.set_description("A small room that houses the ships servers and memories, it also has a IT guy only sign. The door to the server room can only be opened by the ships AI.")
compute.unlock

tool = Room("Computer Tool Room", 'no')
tool.set_description("A small room that holds various computer repair tools, none of which you recognize except for a crowbar.")
tool.unlock

server = Room("Server Room", 'yes')
server.set_description("A room that houses the ship’s, along with a few computers to access the ships mainframe. A command is displayed on the screen and the cursor flashes, waiting endlessly for it to be entered.")
server.lock

it = Room("IT Quarters", 'no')
it.set_description("The quarters of the IT guys, filled with unknown nerdy posters and figurines. The only one you recognize is some sort of cowboy, but it is holding a missing cigar.")
it.unlock

midhw1 = Room("Up Middle Hallway", 'no')
midhw1.set_description("A hallway leading into the rest of the ship from the hangar.")
midhw1.unlock

ehw1 = Room("Up East Hallway", 'no')
ehw1.set_description("A hallway leading into the rest of the ship from the middle hallway.")
ehw1.unlock

whw1 = Room("Up West Hallway", 'no')
whw1.set_description("A hallway leading into the rest of the ship from the middle hallway.")
whw.unlock

brmaint = Room("Bridge Maintinence Room", 'no')
brmaint.set_description("A room to perform maintenance on the bridge. An instruction manual on the table has something circled in red.")
brmaint.unlock

offbr = Room("Officer Bedroom", 'yes')
offbr.set_description("A comfortable sized room with a bed, couch, nightstand, closet and a small table. A crystal bottle of thick, lime-green liquid and a shockingly clean drinking glass are on the table. A note is next to the previous residents computer.")
offbr.lock

capbr = Room("Captain Bedroom", 'yes')
capbr.set_description("A larger room with a bed, nightstand and closet in one area and a couch, coffee table and comfy chairs in a sitting area. The remnants of a half-smoked cigar lie cold in an ashtray on the coffee table.")
capbr.lock

elev1 = Room("Up Elevator", 'no')
elev1.set_description("A standard mirrored elevator with an AI communicator on the wall. A poster has been hung on the wall advertising a social event. The display shows top floor. The Captain and Officer rooms both need cards to access.")
elev1.unlock

elev2 = Room("Recreation Elevator", 'no')
elev2.set_description("A standard mirrored elevator with an AI communicator on the wall. A poster has been hung on the wall advertising a social event. The display shows recreation floor.")
elev2.unlock

elev3 = Room("Military Elevator", 'no')
elev3.set_description("A standard mirrored elevator with an AI communicator on the wall. A poster has been hung on the wall advertising a social event. The display shows military floor.")
elev3.unlock

robserve = Room("Recreation Observation Room", 'no')
robserve.set_description("A utilitarian room with a swivel chair and monitors displaying various feeds from around the ship. One of the walls is a large titanium-glass wall, with a beautiful view of space.")
robserve.unlock

mobserve = Room("Military Observation Room", 'no')
mobserve.set_description("A medium sized room with a swivel chair and monitors.  The monitors are displaying various feeds from the military deck.")
mobserve.unlock

pool = Room("Pool", 'no')
pool.set_description("A large, still pool of glassy blue water surrounded by gray tile. There is a pungent smell of chlorine but not a ripple in the water. A window over the pool provides a beautiful view of outer space.")
pool.unlock

bowl = Room("Bowling Alley", 'no')
bowl.set_description("A six lane bowling alley with bowling balls of various colors and sizes stacked against one wall. The pins stand tall in each lane, waiting for bowlers.  Oddly, there is only one pin in the second alley.")
bowl.unlock

snow = Room("Snow Recreation Room", 'no')
snow.set_description("A vast room with a large snow hill to one side.  Its very cold here, and the air feels fresh.  Sleds, tubes, skis and other strange looking recreation items are in a closet on the other side of the room. The snow looks strangely deformed.")
snow.unlock

garden = Room("Garden", 'no')
garden.set_description("A large room with a lovely English-style garden. Many strange plants are growing here that you do not recognize.  A large red flower hangs over from its own weight, petals drooping open like an awaiting something ...")
garden.unlock

tennis = Room("Tennis Courts", 'no')
tennis.set_description("Two regulation-sized tennis courts with benches on each side. Rackets and balls can be seen stacked in the corner. An opened can of some type of thick, lime-green smoothie or energy drink sits on one of the benches.")
tennis.unlock

mess = Room("Mess Hall", 'no')
mess.set_description("A large canteen with long tables and chairs and a service counter on one side.  A logo hangs behind the service counter that reads, To Serve Man.")
mess.unlock

kitchen = Room("Kitchen", 'no')
kitchen.set_description("A large kitchen with vast counters, sinks, ovens, grills, appliances and utensils. A walk-in freezer sits in the back corner of the room. A large butcher's knife hangs over the chopping block. An opened bottle lays on its side, thick lime-green liquid spilled across the counter.")
kitchen.unlock

game = Room("Game Room", 'no')
game.set_description("A small room with video screens and couches. Headsets hang on a wall. There is a random power outlet on the wall with nothing plugged into it, yet you can tell the TV has power because of the light in the bottom of the corner. The ancient cushions on the couch seem to have mountains of lost items piled beneath.")
game.unlock

board = Room("Board Game Room", 'no')
board.set_description("A small cozy room with various size tables, chairs and couches. Games and puzzles are neatly stacked on shelves along the walls. The tables are empty except for a single game of chess with a pawn in the queens starting position next to the king.")
board.unlock

sim = Room("Simulation Room", 'no')
sim.set_description("A large empty room with an array of specialized electronic implements covering the walls and ceiling. The room lighting colors are fluctuating and changing like an underwater aquarium. Strange sounds abound and there is a familiar smell but you can’t quite place it.")
sim.unlock

music = Room("Music Room", 'no')
music.set_description("A large, acoustically tuned room with a small stage and several rows of seats. Behind the stage are many instruments of various sizes and shapes. A crumpled music program can been seen under one of the chairs.")
music.unlock

science = Room("Science Lab", 'no')
science.set_description("A room with rows of steel tables, strong overhead lights and scientific equipment. The entrance to this room has an air lock and small vestibule for sanitization. A microscope on one of the tables has a very strange, thick, lime-green liquid in a petri dish.")
science.unlock

plant = Room("Plant Lab", 'no')
plant.set_description("A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Carbon Disulfate, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk.")
plant.unlock

observatory = Room("Planet & Stars Observatory", 'no')
observatory.set_description("A small room with planets and stars painted on the walls. A tremendous viewing scope offers views of distant space objects and there is a space history viewing table that is displaying a single orange colored planet. There are some scattered notes.")
observatory.unlock

midhw2 = Room("Recreation Middle Hallway", 'no')
midhw2.set_description("A hallway leading into the rest of the ship from the hangar.")
midhw2.unlock

ehw2 = Room("Recreation East Hallway", 'no')
ehw2.set_description("A hallway leading into the rest of the ship from the middle hallway.")
ehw2.unlock

whw2 = Room("Recreation West Hallway", 'no')
whw2.set_description("A hallway leading into the rest of the ship from the middle hallway.")
whw2.unlock

midhw3 = Room("Military Middle Hallway", 'no')
midhw3.set_description("A hallway leading into the rest of the ship from the hangar. The door to the Intelligence room is locked.")
midhw3.unlock

ehw3 = Room("Military East Hallway", 'no')
ehw3.set_description("A hallway leading into the rest of the ship from the middle hallway. The door to the Gun Platform is locked with an extruding electronic lock.")
ehw3.unlock

whw3 = Room("Military West Hallway", 'no')
whw3.set_description("A hallway leading into the rest of the ship from the middle hallway. The door to the Gun Platform is locked.")
whw3.unlock

fq1 = Room("Family Quarters 1", 'no')
fq1.set_description("A large bedroom with 3 beds, 4 closets, 3 bathrooms, and some scattered clothing. There is what seems like a work-from-home set up, with notes and files around a monitor extruding from the wall.")
fq1.unlock

fq2 = Room("Family Quarters 2", 'no')
fq2.set_description("A large bedroom with 3 beds, 4 closets, 3 bathrooms, and some scattered clothing. There is what seems like a work-from-home set up, with notes and files around a monitor extruding from the wall.")
fq2.unlock

fq3 = Room("Family Quarters 3", 'no')
fq3.set_description("A large bedroom with 3 beds, 4 closets, 3 bathrooms, and some scattered clothing. There is what seems like a work-from-home set up, with notes and files around a monitor extruding from the wall. Next to the sink, there is a toothbrush along with some other oral hygene items.")
fq3.unlock

fq4 = Room("Family Quarters 4", 'no')
fq4.set_description("A large bedroom with 3 beds, 4 closets, 3 bathrooms, and some scattered clothing. There is what seems like a work-from-home set up, with notes and files around a monitor extruding from the wall.")
fq4.unlock

cor = Room("Command Operations Room", 'no')
cor.set_description("3 computer monitors extrude from the wall, all with a few previous command inputs, and all with a blinking cursor, forever blinking. Pawns, little ships, and symbols are scattered around in an interactive hologram. Each ship has a serial number. There seems to be a small graphical glitch in place of one of the spaceships in a formation, d3682. Occasionally, this ship blinks to a deformed version of the same ship, with thick, lime-green liquid on the inside. The ship next to this one seems to be highlighted, the ship being d3681.")
cor.unlock

wesc1 = Room("West Escape Pod 1", 'no')
wesc1.set_description("A small room with a sealable doorway to the escape pod. The pod holds up to 16 personnel and has communications and stores. There is a cabinet on the wall. The door to the Gun Platform is locked.")
wesc1.unlock

wesc2 = Room("West Escape Pod 2", 'no')
wesc2.set_description("A small room with a sealable doorway to the escape pod. The pod holds up to 16 personnel and has communications and stores. There is a cabinet on the wall. On the other wall, there is a 'MAYDAY' button along with a 1-ish centimeter hole for an activation key.")
wesc2.unlock

esc1 = Room("East Escape Pod 1", 'no')
esc1.set_description("A small room with a sealable doorway to the escape pod. The pod holds up to 16 personnel and has communications and stores. There is a cabinet on the wall. The door to the Gun Platform is locked.")
esc1.unlock

esc2 = Room("East Escape Pod 2", 'no')
esc2.set_description("A small room with a sealable doorway to the escape pod. The pod holds up to 16 personnel and has communications and stores. There is a cabinet on the wall.")
esc2.unlock

esc = Room("Middle Escape Pod", 'no')
esc.set_description("A small room with a sealable doorway to the escape pod. The pod holds up to 16 personnel and has communications and stores. There is a cabinet on the wall.")
esc.unlock

gpw1 = Room("West Gun Platform 1", 'yes')
gpw1.set_description("A small room with a gunner’s platform, equipment, controls and chairs. The room curves outward allowing for a 270° view of space. Names of gunners are inscribed on the back of the seat.")
gpw1.lock

gpw2 = Room("West Gun Platform 2", 'yes')
gpw2.set_description("A small room with a gunner’s platform, equipment, controls and chairs. The room curves outward allowing for a 270° view of space. Names of gunners are inscribed on the back of the seat.")
gpw2.lock

gpe1 = Room("East Gun Platform 1", 'yes')
gpe1.set_description("A small room with a gunner’s platform, equipment, controls and chairs. The room curves outward allowing for a 270° view of space. Names of gunners are inscribed on the back of the seat.")
gpe1.lock

gpe2 = Room("East Gun Platform 2", 'yes')
gpe2.set_description("A small room with a gunner’s platform, equipment, controls and chairs. The room curves outward allowing for a 270° view of space. Names of gunners are inscribed on the back of the seat. On a metal panel next to the controls, the same names are in separate columns, each with a unique tally mark under it. The numbers go: ‘Atriox: 12, Decimus: 17, Benarnex: 23, Crenel: 29.’")
gpe2.lock

battery1 = Room("West Gun Ammunition Storage", 'no')
battery1.set_description("A small storage room with rows and rows of various types of ammunition, labeled and categorized. A box in one of the rows has a lime-green tinge at the bottom, especially in the corners.")
battery1.unlock

battery2 = Room("East Gun Ammunition Storage", 'no')
battery2.set_description("A small storage room with rows and rows of various types of ammunition, labeled and categorized. A box in one of the rows has a lime-green tinge at the bottom, especially in the corners.")
battery2.unlock

missile1 = Room("East Missile Launch Platform", 'no')
missile1.set_description("A large cabinet that holds 2 types of cylinders, one that is glowing, and one that has an odd, 3 way symbol on the side. The cylinders are neatly lined up in an autoloader. The loader is hooked up to a large contraption in the center of the room, facing down. The contraption has 3 buttons, a green button and 2 identical buttons, one that says Nuclear Launch, and the other says Photon Launch.")
missile1.unlock

missile2 = Room("West Missile Launch Platform", 'no')
missile2.set_description("A large cabinet that holds 2 types of cylinders, one that is glowing, and one that has an odd, 3 way symbol on the side. The cylinders are neatly lined up in an autoloader. The loader is hooked up to a large contraption in the center of the room, facing down. The contraption has 3 buttons, a green button and 2 identical buttons, one that says Nuclear Launch, and the other says Photon Launch.")
missile2.unlock

Intelligence = Room("Intelligence Operations Room", 'yes')
Intelligence.set_description("A large room with three large screens in the front of the room. Rows of consoles, each with its own set of controls and headsets, fill the room. Many random instruments dot the walls. An eerie feeling shivers down your spine every time one of the instruments beep. Labels mark each of the Intelligence stations. One of the wall consoles is awaiting a command, maybe a password, but it is using a diffeent OS than the other consoles.")
Intelligence.lock

srw = Room("West Brig Security Room", 'no')
srw.set_description("A small room with swivel chairs and monitors of the adjacent Brig. There is also a filing cabinet. Occasionally, a warbling sound will be played. Every time one of the sounds is emitted, a very brief, pungent smell is observable.")
srw.unlock

sre = Room("East Brig Security Room", 'no')
sre.set_description("A small room with swivel chairs and monitors of the adjacent Brig. Occasionally, a warbling sound will be played.")
sre.unlock

wbrig = Room("West Brig", 'no')
wbrig.set_description("A small room with three holding cells, each containing a flat bench and some controls on the wall. Occasionally, a light beam will scan the cell, emitting somewhat calming warbling sounds. There is a strong odor. ")
wbrig.unlock

ebrig = Room("East Brig", 'no')
ebrig.set_description("A small room with three holding cells, each containing a flat bench and some controls on the wall. Occasionally, a light beam will scan the cell, emitting somewhat calming warbling sounds.")
ebrig.unlock

movie = Room("Movie Theater", 'no')
movie.set_description("A large room with a giant screen, hidden speakers and a sloped floor. Comfortable massage recliners spread across the floor. A piece of clothing is lying across one of the recliners. Occasionally, a robot with scan the area for trash, then retreat into a hole in the wall.")
movie.unlock

dead = Room("Dead", 'no')
dead.set_description("Not in any room or inventory")
dead.unlock











goggles = Item("Goggles", "A pair of goggles with 'CAPTAIN' inscribed on the back.", "East Engine Room")
goggles.set_description("A pair of goggles with 'CAPTAIN' inscribed on the back.")
goggles.room = "East Engine Room"

tooth = Item("Toothbrush", "A Toothbrush with a diameter of about 1 centimter.", "Family Quarters 3")
tooth.set_description("A Toothbrush with a diameter of about 1 centimter.")
tooth.room = "Family Quarters 3"

ccard = Item("ID Card", "An ID card with an unreadable name. It appears to be a captains card.", "dead")
ccard.set_description("An ID card with an unreadable name. It appears to be a captains card.")
ccard.room = "dead"

cig = Item("Indefinetly Lit Cigar", "An indefinetly lit e-cigar.", "Captain Bedroom")
cig.set_description("An indefinetly lit e-cigar.")
cig.room = "Captain Bedroom"

cow = Item("Cowboy Figurine", "A cowboy figurine holding a missing cigar.", "IT Quarters")
cow.set_description("A cowboy figurine holding a missing cigar.")
cow.room = "IT Quarters"

tv = Item("T.V. Remote", "A T.V. remote", "Waiting Room")
tv.set_description("A T.V. remote")
tv.room = "Waiting Room"

cush = Item("Cushions", "Cushions on a couch. They seem to have snagged countess items from unaware people.", "Game Room")
cush.set_description("Cushions on a couch. They seem to have snagged countess items from unaware people.")
cush.room = "Game Room"

ocard = Item("ID Card", "An ID card with an unreadable name. It appears to be an officers card.", "Game Room")
ocard.set_description("An ID card with an unreadable name. It appears to be an officers card.")
ocard.room = "Game Room"

dpetri = Item("Petri Dish", "A petri dish with a thin, cactus-green liquid.", 'dead')
dpetri.set_description("A petri dish with a thin, cactus-green liquid.")
dpetri.room = 'dead'

bottle = Item("Bottle", "An opened can of some type of thick, lime-green smoothie or energy drink.", 'Gym')
bottle.set_description("An opened can of some type of thick, lime-green smoothie or energy drink.")
bottle.room = 'Gym'

shoe = Item("Shoe", "A Shoe", 'Human Quarters 1')
shoe.set_description("A Shoe")
shoe.room = 'Human Quarters 1'

fshoe = Item("Flaming Shoe", "A flaming shoe", 'dead')
fshoe.set_description("A flaming shoe")
fshoe.room = 'dead'

gas = Item("Liquid", "Spilled clear liquid with a strong acidic odor.", "Medical Bay")
gas.set_description("Spilled clear liquid with a strong acidic odor.")
gas.room = "Medical Bay"

crow = Item("Crowbar", "A crowbar", "Computer Tool Room")
crow.set_description("A crowbar. You could probably crack open some boxes with this.")
crow.room = "Computer Tool Room"

lighter = Item("Cigarrette Lighter", "A traditional cigarrette lighter.", "Cafe")
lighter.set_description("A traditional cigarrette lighter.")
lighter.room = "Cafe"

petri = Item("Liquid in Petri Dish", "A thick, lime-green liquid in a petri dish.", "Science Lab")
petri.set_description("A thick, lime-green liquid in a petri dish.")
petri.room = "Science Lab"

key = Item("Key", "A key that probably goes to something.", 'dead')
key.set_description("A key that probably goes to something.")
key.room = 'dead'

log = Item("Computer", "A computer log of all who enter the ship from the hangar.", "Ship Log Room")
log.set_description("A computer log of all who enter the ship from the hangar.")
log.room = 'Ship Log Room'

spill_water = Item("Spilled Water", "Spilled water from the plant.", "Plant Lab")
spill_water.set_description("Spilled water from the plant.")
spill_water.room = "Plant Lab"

mop = Item("Mop", "An extremely dry mop.", "Closet")
mop.set_description("An extremely dry mop.")
mop.room = "Closet"

ai = Item("Ship AI Chip", "A chip of the ships AI, Burning Mule.", 'dead')
ai.set_description("A chip of the ships AI, Burning Mule.")
ai.room = 'dead'

box = Item("Weak Box", "An old box, very weak from years of use, then abandonement.", "East Storage")
box.set_description("An old box, very weak from years of use, then abandonement.")
box.room = "East Storage"

shuttlecard = Item("ShuttleCard", "A previous passengers ShuttleCard to a private shuttle", 'dead')
shuttlecard.set_description("A previous passengers ShuttleCard to a private shuttle")
shuttlecard.room = 'dead'
















observe.link_room(bridge, "s")
bridge.link_room(observe, "n")

hangar.link_room(ship_log_room, "n")
ship_log_room.link_room(hangar, "s")

hangar.link_room(estorage, "e")
estorage.link_room(hangar, "w")

hangar.link_room(wstorage, "w")
wstorage.link_room(hangar, "e")

ship_log_room.link_room(midhw, "n")
midhw.link_room(ship_log_room, "s")

ehw.link_room(midhw, "w")
midhw.link_room(ehw, "e")

ehw.link_room(br1, "e")
br1.link_room(ehw, "w")

whw.link_room(midhw, "e")
midhw.link_room(whw, "w")

ehw.link_room(closet1, "s")
closet1.link_room(ehw, "n")

mstairs.link_room(whw, "e")
whw.link_room(mstairs, "w")

rroom.link_room(ehw, "s")
ehw.link_room(rroom, "n")

rroom.link_room(meetroom, "n")
meetroom.link_room(rroom, "s")

bridge.link_room(meetroom, "e")
meetroom.link_room(bridge, "w")

bridge.link_room(cafe, "w")
cafe.link_room(bridge, "e")

bar.link_room(cafe, "n")
cafe.link_room(bar, "s")

whw.link_room(bar, "n")
bar.link_room(whw, "s")

ship_log_room.link_room(maint, "w")
maint.link_room(ship_log_room, "e")

maint.link_room(engine, "w")
engine.link_room(maint, "e")

bar.link_room(bed2, "w")
bed2.link_room(bar, "e")

cafe.link_room(bed4, "w")
bed4.link_room(cafe, "e")

bed3.link_room(rroom, "w")
rroom.link_room(bed3, "e")

bed5.link_room(meetroom, "w")
meetroom.link_room(bed5, "e")

midhw.link_room(bed1, "n")
bed1.link_room(midhw, "s")

closet1.link_room(closet2, "w")
closet2.link_room(closet1, "e")

closet1.link_room(engine2, "e")
engine2.link_room(closet1, "w")

mstairs.link_room(ustairs, "u")
ustairs.link_room(mstairs, "d")

whw1.link_room(ustairs, "w")
ustairs.link_room(whw1, "e")

whw1.link_room(midhw1, "e")
midhw1.link_room(whw1, "w")

elev1.link_room(midhw1, "n")
midhw1.link_room(elev1, "s")

whw1.link_room(waiting, "n")
waiting.link_room(whw1, "s")

ehw1.link_room(midhw1, "w")
midhw1.link_room(ehw1, "e")

habserve.link_room(elev1, "n")
elev1.link_room(habserve, "s")

habserve.link_room(maze, "e")


capbr.link_room(elev1, "w")
elev1.link_room(capbr, "e")

ship_log_room.link_room(elev1, "u")
elev1.link_room(ship_log_room, "d")

ship_log_room.link_room(elev2, "d")
elev2.link_room(ship_log_room, "u")

elev3.link_room(elev2, "u")
elev2.link_room(elev3, "d")

offbr.link_room(elev1, "e")
elev1.link_room(offbr, "w")

gym.link_room(midhw1, "s")
midhw1.link_room(gym, "n")

ehw1.link_room(bathroom, "e")
bathroom.link_room(ehw1, "w")

ehw1.link_room(compute, "n")
compute.link_room(ehw1, "s")

tool.link_room(compute, "s")
compute.link_room(tool, "n")

server.link_room(compute, "w")
compute.link_room(server, "e")

tool.link_room(brmaint, "w")
brmaint.link_room(tool, "e")

tool.link_room(it, "e")
it.link_room(tool, "w")

ubserve.link_room(brmaint, "s")
brmaint.link_room(ubserve, "n")

ubserve.link_room(observe, "d")
observe.link_room(ubserve, "u")

medbay.link_room(brmaint, "e")
brmaint.link_room(medbay, "w")

medbay.link_room(brmaint, "e")
brmaint.link_room(medbay, "w")

medbay.link_room(medclo, "w")
medclo.link_room(medbay, "e")

medbay.link_room(waiting, "s")
waiting.link_room(medbay, "n")

library.link_room(waiting, "e")
waiting.link_room(library, "w")

whw1.link_room(waiting, "n")
waiting.link_room(whw1, "s")

robserve.link_room(mobserve, "d")
mobserve.link_room(robserve, "u")

robserve.link_room(observe, "u")
observe.link_room(robserve, "d")

robserve.link_room(pool, "s")
pool.link_room(robserve, "n")

bowl.link_room(pool, "w")
pool.link_room(bowl, "e")

bowl.link_room(snow, "e")
snow.link_room(bowl, "w")

bowl.link_room(garden, "s")
garden.link_room(bowl, "n")

tennis.link_room(garden, "w")
garden.link_room(tennis, "e")

ehw2.link_room(garden, "n")
garden.link_room(ehw2, "s")

ehw2.link_room(sim, "e")
sim.link_room(ehw2, "w")

ehw2.link_room(midhw2, "w")
midhw2.link_room(ehw2, "e")

whw2.link_room(midhw2, "e")
midhw2.link_room(whw2, "w")

movie.link_room(midhw2, "s")
midhw2.link_room(movie, "n")

elev2.link_room(midhw2, "n")
midhw2.link_room(elev2, "s")

whw2.link_room(fq3, "w")
fq3.link_room(whw2, "e")

whw2.link_room(kitchen, "n")
kitchen.link_room(whw2, "s")


fq2.link_room(kitchen, "e")
kitchen.link_room(fq2, "w")

mess.link_room(kitchen, "s")
kitchen.link_room(mess, "n")

mess.link_room(fq1, "w")
fq1.link_room(mess, "e")

mess.link_room(pool, "e")
pool.link_room(mess, "w")

elev2.link_room(science, "s")
science.link_room(elev2, "n")

elev2.link_room(game, "w")
game.link_room(elev2, "e")

elev2.link_room(music, "e")
music.link_room(elev2, "w")

plant.link_room(science, "e")
science.link_room(plant, "w")

observatory.link_room(science, "w")
science.link_room(observatory, "e")

mobserve.link_room(cor, "s")
cor.link_room(mobserve, "n")

wesc1.link_room(cor, "e")
cor.link_room(wesc1, "w")

esc1.link_room(cor, "w")
cor.link_room(esc1, "e")

esc1.link_room(gpe1, "e")
gpe1.link_room(esc1, "w")

esc1.link_room(missile1, "s")
missile1.link_room(esc1, "n")


battery1.link_room(missile1, "w")
missile1.link_room(battery1, "e")

ehw3.link_room(missile1, "n")
missile1.link_room(ehw3, "s")

ehw3.link_room(gpe2, "e")
gpe2.link_room(ehw3, "w")

ehw3.link_room(midhw3, "w")
midhw3.link_room(ehw3, "e")

whw3.link_room(midhw3, "e")
midhw3.link_room(whw3, "w")

Intelligence.link_room(midhw3, "s")
midhw3.link_room(Intelligence, "n")

elev3.link_room(midhw3, "n")
midhw3.link_room(elev3, "s")

elev3.link_room(srw, "w")
srw.link_room(elev3, "e")

wbrig.link_room(srw, "e")
srw.link_room(wbrig, "w")

elev3.link_room(sre, "e")
sre.link_room(elev3, "w")

ebrig.link_room(sre, "w")
sre.link_room(ebrig, "e")

elev3.link_room(esc, "s")
esc.link_room(elev3, "n")

wesc2.link_room(esc, "e")
esc.link_room(wesc2, "w")

esc2.link_room(esc, "w")
esc.link_room(esc2, "e")

whw3.link_room(gpw2, "w")
gpw2.link_room(whw3, "e")

whw3.link_room(missile2, "n")
missile2.link_room(whw3, "s")

wesc1.link_room(missile2, "s")
missile2.link_room(wesc1, "n")

battery2.link_room(missile2, "e")
missile2.link_room(battery2, "w")

wesc1.link_room(gpw1, "w")
gpw1.link_room(wesc1, "e")

wesc1.link_room(cor, "e")
cor.link_room(wesc1, "w")

board.link_room(game, "e")
game.link_room(board, "w")






def grab(item, rooom):
    if item == 'goggles' or item == 'Goggles' or item == 'goggle' or item == 'Goggle':
        if rooom == goggles.room:
            goggles.room = "inv"
            print("You have grabbed the goggles.")
            engine2.set_description("A room for controlling the engines, fixing the engines, and a safety precaution sign on the wall.")

    if item == 'toothbrush' or item == 'Toothbrush' or item == 'brush' or item == 'Brush':
        if rooom == tooth.room:
            tooth.room = "inv"
            print("You have grabbed the toothbrush.")
            fq3.set_description("A large bedroom with 3 beds, 4 closets, 3 bathrooms, and some scattered clothing. There is what seems like a work-from-home set up, with notes and files around a monitor extruding from the wall. Next to the sink, there are some oral hygene items.")

    if item == 'captain card' or item == 'Captain Card' or item == 'captains card' or item == 'Captains Card' or item == 'id card' or item == 'ID Card' or item == 'ID card':
        if rooom == ccard.room:
            ccard.room = "inv"
            print("You have grabbed the captain card.")

    if item == 'officer card' or item == 'Officer Card' or item == 'officers card' or item == 'Officers Card' or item == 'id card' or item == 'ID Card' or item == 'ID card':
        if rooom == ocard.room:
            ocard.room = "inv"
            print("You have grabbed the officer card.")

    if item == 'Cigarette' or item == 'cigarette' or item == 'Cigar' or item == 'cigar':
        if rooom == cig.room:
            cig.room = "inv"
            print("You have grabbed the cigar.")
            capbr.set_description("A larger room with a bed, nightstand and closet in one area and a couch, coffee table and comfy chairs in a sitting area.")
            

    if item == 'Remote' or item == 'remote' or item == 'tv remote' or item == 'TV remote' or item == 'TV Remote':
        if rooom == tv.room:
            print(tv.room)
            tv.set_room = "inv"
            print("You have grabbed the remote.")
            waiting.set_description("A small room with a couch, tv, and tablestands. Soft music plays from a nearby speaker.")

    if item == 'cushions' or item == 'Cushions' or item == 'Couch Cushions' or item == 'couch cushions':
        if rooom == cush.room:
            cush.room = "inv"
            print("You have grabbed the cushions.")
            ocard.set_room(game)
            game.set_description("A small room with video screens and couches. Headsets hang on a wall. There is a random power outlet on the wall with nothing plugged into it, yet you can tell the TV has power because of the light in the bottom of the corner. The cushions are on the floor.")
            

    if item == 'petri dish' or item == 'Petri Dish' or item == 'petri' or item == 'Petri':
        if not dpetri.room == 'dead':
            if rooom == dpetri.room:
                dpetri.room = 'inv'
                print("You have grabbed the petri dish.")
        else:
            if rooom == petri.room:
                petri.room = "inv"
                print("You have grabbed the petri dish.")
                science.set_description("A room with rows of steel tables, strong overhead lights and scientific equipment. The entrance to this room has an air lock and small vestibule for sanitization. A microscope on one of the tables has a very strange, thick, burned, dark green liquid in a petri dish.")

    if item == 'Bottle' or item == 'bottle' or item == 'Smoothie' or item == 'smoothie':
        if rooom == bottle.room:
            bottle.room = "inv"
            print("You have grabbed the bottle.")
            gym.set_description("A large, open, spacious room with various workout machines scattered about. A television monitor hangs on the wall, but is turned off.")
    
    if item == 'shoe' or item == 'Shoe':
        if not fshoe.room == 'dead':
            if rooom == fshoe.room:
                fshoe.set_room = "inv"
                print("You have grabbed the shoe.")
                bed1.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nightstand, cabinet and closet are inside. No shoes lie under the bed.")
        else:
            if rooom == shoe.room:
                shoe.room = "inv"
                print("You have grabbed the shoe.")
                bed1.set_description("Private sleeping/living quarters for one member of the crew, only a bed, nightstand, cabinet and closet are inside. No shoes lie under the bed.")

    if item == 'crowbar' or item == 'Crowbar' or item == 'bar' or item == 'Bar':
        if rooom == crow.room:
            crow.room = "inv"
            print("You have grabbed the crowbar.")
            tool.set_description("A small room that holds various computer repair tools, none of which you recognize.")

    if item == 'key' or item == 'Key':
        if rooom == key.room:
            key.room = "inv"
            print("You have grabbed the key.")

    if item == 'mop' or item == 'Mop' or item == 'broom' or item == 'Broom':
        if rooom == mop.room:
            mop.room = "inv"
            print("You have grabbed the mop.")
            closet1.set_description("A closet off to the side of the hallway, full of cleaning equipment. The door to the east is the engine room, but it needs a maintinence code.")

    if item == 'ai chip' or item == 'AI chip' or item == 'chip' or item == 'Chip' or item == 'ai' or item == 'AI Chip' or item == 'AI':
        if rooom == ai.room:
            ai.room = "inv"
            print("You have grabbed the AI chip.")

    if item == 'shuttle card' or item == 'Shuttle Card' or item == 'card' or item == 'Card' or item == 'ID card' or item == 'ID Card' or item == 'id' or item == 'ID':
        if rooom == shuttlecard.room:
            shuttlecard.room = "inv"
            print("You have grabbed the shuttlecard.")
            
    elif not item == 'shuttle card' and not item == 'Shuttle Card' and not item == 'card' and not item == 'Card' and not item == 'ID card' and not item == 'ID Card' and not item == 'id' and not item == 'ID' and not item == 'ai chip' and not item == 'AI chip' and not item == 'chip' and not item == 'Chip' and not item == 'ai' and not item == 'AI Chip' and not item == 'AI' and not item == 'mop' and not item == 'Mop' and not item == 'broom' and not item == 'Broom' and not item == 'key' and not item == 'Key' and not item == 'crowbar' and not item == 'Crowbar' and not item == 'bar' and not item == 'Bar' and not item == 'shoe' and not item == 'Shoe' and not item == 'Bottle' and not item == 'bottle' and not item == 'Smoothie' and not item == 'smoothie' and not item == 'petri dish' and not item == 'Petri Dish' and not item == 'petri' and not item == 'Petri' and not item == 'cushions' and not item == 'Cushions' and not item == 'Couch Cushions' and not item == 'couch cushions' and not item == 'Remote' and not item == 'remote' and not item == 'tv remote' and not item == 'TV remote' and not item == 'TV Remote' and not item == 'Cigarette' and not item == 'cigarette' and not item == 'Cigar' and not item == 'cigar' and not item == 'officer card' and not item == 'Officer Card' and not item == 'officers card' and not item == 'Officers Card' and not item == 'id card' and not item == 'ID Card' and not item == 'ID card' and not item == 'captain card' and not item == 'Captain Card' and not item == 'captains card' and not item == 'Captains Card' and not item == 'id card' and not item == 'ID Card' and not item == 'ID card' and not item == 'toothbrush' and not item == 'Toothbrush' and not item == 'brush' and not item == 'Brush' and not item == 'goggles' and not item == 'Goggles' and not item == 'goggle' and not item == 'Goggle':
        print("That does not exist here.")







def drop(item, room):
    if item.room == "inv":
        item.room = current_room
        print("You have dropped " + Item.name)
    else:
        print("You don't have that item.")

def read(room, item):
    print(room)
    if room == 'Officer Bedroom':
        print(item)
        if item == 'Notes' or item == 'notes' or item == "Note" or item == 'note':
            print("These beans are good. 11/26/~~82")
            print("Tell Janitor to use mop more. 8/9/~~86")
            print("Fix 'Green Sludge' glitch in ship systems. 7/4/~293")
            print("Server Room Code: 4dY7bU. 3/12/~~76")
        else:
            print("wat? You can't read that.")

    if room == 'West Brig Security Room' or room == 'East Brig Security Room' and file == 'open':
        if item == 'file' or item == 'File' or item == 'files' or item == 'Files':
            print("Ship Log Room Code: Urm478e1")
        else:
            print("wat? You can't read that.")

    if room == 'Ship Log Room':
        if item == 'computer' or item == 'Computer' or item == 'Log' or item == 'log':
            if input("Code?") == 'Urm478e1':
                print("Log: 1/26/~~46: A Kosmukian by the name of Snaeb has boarded for 3 Edays to: 'Try Beans and chill at the bar'.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 1/29/~~46: A Kosmukian by the name of Snaeb has exited after 3 Edays.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 2/13/~~46: An Otnip Deirfer by the name of Neerg Egduls has boarded for l̷̬̩̤̜̀̈́̎̈͗̎͗̏̀͂̚̚̚͠͝ days to s̶͍̹͖̠̥̼̐̐͋́͑̃͊͝͝l̸̢̡̺̮̝̥͍̪͑̉́̄͊́̕͜͠g̴̨̡̰̗͖̬̰̫̍̌͂̈́͊̃̕̚͝r̵̛̠̙̥͐̿͋͂̀á̸̞̘͍̻̝͇͛̀̀n̸̡̧̛̳͉̳͔̫̰͓̗͉̗͇̗̑́̅̅͊̿͛̐̿̋̚͜s̶̟̮̫̩̾̿̎̓̎̌̍͂̏͛̔͠u̶̧͔͇̫͍̻͓͗̊̈́͗n̷̡̡̘̱̜͉͖̭̹̰̥̺̺͓͗́̔̈̽͒̀͗̑͆͜ȅ̴̘̮̜̘͕̠̪͖̙͓̗̖͕̞̎͊̓̐̍͆͠ą̸̧̡͓͈̺̮̯̝̞̫̩̍̆͒̾̏͐̀̀͐̕͠.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 3/12/~~46: j̶̢̛͖̗̯̲̜̖̣̪͓̲̤͚͇̺̎̉̏̔̍̾͝ḃ̴̡̡̧̪̫͎̙̤̻̗̹̳̿̎̔̓͗̋̒̂̕͠͝k̴̮̗̓̌̄̊̾͛̀́̀͛̀͆̐̏͘f̶̡̡̯̯̦͇̫͚̥̮͉̱̍́͛̏̾̌͜ḇ̸̢̖̞̘͔͖̼̤͗̀͂̎̃̾̈́̃̉̍̿͛͆́͘k̷̪̻̈́͋̔́̑̈́̕̕̚̕͝͝g̵͍̲̞̳̞̠̭͙̟͕͎̈̒̑̉̎̃͒̽̐̂̐͘c̸̞̪̗̩̘̤͉̭͖̙͛̔ḟ̷̛̖̝̗͇͇̞̻̱͉͝d̶͍̦̟̤͍̆̇̀̓̆́́́̔̂̅͋͆̓͝h̷̻̯̬̺̗̦̝̾̓͗̋̽͊͜k̶̢̘̫̻̪͊͒ư̷̢͎̯̫̰̮͔͖̲̱͝á̴̧̧̞̼͚̟̩̜̤̯͇̥̝̉̇̐̏̓̓̉̏͊͌͘͜͝ņ̶̦̖̘̗̗̪̠̑̒͐̒̾͗́̐͐̇͛̕͠͝s̵͖͈̹͚͚͒̏̈̑̾͑̑̃̽͊̆̎̀̒̌i̷̢̲̪̦̰̯̦̘̹̻̟͂̏͐̑͑u̶͓̠͇͕̯͍̭̿̅͗̇́̄̋̍͠c̸̛̛̛̻̯̙̤̅̉̓̔͆͂͝f̷̡̙͚͈̭͓̘̫̘͕̲͖̂͌̈̋͂̏͐̋͊̋̓̉̒͝ų̵̨͖̦̜̤͓͉̅̽̒̏̇ͅy̴̨̢̨̛̳͎̜̼̪̟͚̾̒̄̃̆̋̐͆͊̑̇͜͠͠a̴̧̖̹̺̠̥̣̼̼̍́̾͛̆͋̌͂̌́͋̔͑͒h̸̡̡͓̹̰͇͙̼̗̮͈̋̔̄̐̅͆̅̄̕s̵̳̰͈̘̮̟̫̯͙̖̙̟̯̖̐́̎̒̌͘d̵̨͙̮̫̖͗̇̾͌̃͂̿̈́͛̄͆͊͋͝f̴͕̪̹̣̖̫̣̬̤̺͖̭̣̮̈͋̅̅̔̚i̷̭̦̮̭͕̒̅̐̃̈́̇̀͠u̶̢͎͙̭͇̰̦͎̳̦͌̓̀̊̉̽̕͠ͅͅv̷̢̖͇̘̘̘̟̹̈͗͗̓͒̏͛̿͌̎̽̆͆͒͝x̴̨̛͙͎̮̜̮͍̫̲̼̰͙͉͋̔̾͂̌̎́͐i̴̭̗̪͐̈̓͛͒̓̀́͑͆͆̔̚n̷̜̗͕͙̉͐͒́͒̅̈́̋͌͝g̴̜͇̤̮̝̳̟͙̻̜̩̐͐̏̏͑͑̈͋̽͜͜ṫ̶̛̝̍̇́̓͘̕i̸̡̧͈̩̹̠̼̩̫͖̱͂̄r̷̢̧̨͚͎͚͙̖̗̜̣̥͚̒̈̇̿́͊͋̄̕̕g̸̲̥̲͎̹̏̾̎n̷̻͉̈́̇͝b̸̨͎͊̅̽̇̇̅͆̈́͑̇̈̑̍̏̚d̵̙̪̑̀̆͠h̶͙͙̬̯̹̦̣̗̳̫͑̂̋̊̌̀̾͐̽̈͠d̵̡̧̛̛̬̱͖̱̺͈͆͂͛̾̓̚͝͝͝h̷̨̧͙̗̜̝̹͙͖͇̹̺̲̩͐́̏͊́͗̃̇̇͛̂͠d̶̳̒̓̋̿ḫ̸̢̫̥̭̻̲̟͓͉͚̰͎̙̑́̉̏̈́̑̾d̵̬̠͇̗̬̓̓̒̏̈͌̾͛͊̿͒͛͋̚͜͝h̴͕̞̹̘͈̝̮͕̩͚̩͓̤̭̀͐̽͋͐̾̽̈͘͘d̴͚͎̒̇̊̆̅͌̆̓̒̐͝h̷͍͉͍͙̜͇̺̞̪̼̏̀̚d̶̢̻̻̩͖̾̂̇͐̇̒͛̍̄̑̕͘͝ḧ̵̡̧̨̹͕͚͉̮̹̹͓̩̜́͗̐̅͠d̸̼̻͇͚̘̟̼̯̰̖̰̠͈̑̏ͅh̷̨̧̡͍͎̗̩̼͓͈̮̝͈̰̉͋͠d̴̲͓̘̱̺̉͐͂̊͒͒̾͑̔͌͜h̴̛͚͈̰̤͔͈̺̬̠̗́͆͆͛̄ḓ̶̥̠̼͉̃͂̀̍͌͒̌̋̈́̈́̚̕͘͝h̷̡̡̠̻̗͎̽͗́̆̈́̀x̴̻͈͇̪͉̳̝͓̾́̿̆j̴̢͔̥͕̗̐̋̋͋̊̐͗͗̀̌̂͛̓̇̕a̵͇͔̠̓̎̊͗̍͗̃̊̏̚̕͘͠n̷͔͖̍͒̅̽͐̽͠")
                print("")
                print("")
                print("")
                print("")
                print("Log: 3/25/~~46: Unidentified form located on ship, not logged.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 4/3/~~46: Neerg Egduls has been put in West Brig for s̷̨̧̤͈̗͇̘̪̫̘̥͙͖͊̌̈́̀̐͜͠h̸͚͓̑̈́̽̆͂́̽͘͝m̸̢̘̬̭̞̪̗̟̝̜͚͐͗́͑̿̅̔͜͝͝i̶̧̛̲̘̲̬̒̍͗̋̿̀͊̄͋̚̚ḡ̵̖̆̽̅́͗g̸̮̺͓̼͎̙̖̈́͌̑̿̈́́͆l̸̨̘̥̜̞̐͜ȩ̵̛͍̞͕̝̦͚͚͉͇̟̭̭̝͆̑́̉͂͆̿̈̍̒̓͛̏͝.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 8/32/~~46: Error: Guest: Shmiggle has overstayed their stay.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 8/~~/~~46: Error: '26' visitors has overstayed their stay.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 4/20/~~47: Error: Error: Captain off board. No log of exit.")
                print("")
                print("")
                print("")
                print("")
                print("Log: 9/3/~~52: Error: Flaming Donkey has not docked at 'Mashinkey' within the required time.")
                print("")
                print("")
                print("")
                print("")
                print("Error: Lost past 193 Logs")
                print("")
                print("")
                print("")
                print("")
                print("Broadcast: 6/17/~~72: Evacuate.")
            else:
                print("Incorrect")
        else:
            print("Ya can't read that.")

    if room == 'Garden':
        if item == 'plants' or item == 'Plants':
            print("Plant: Cremini mushrooms(1)")
            print("Plant: bacon bush(3)")
            print("Plant: Strawberry yellow(2)")
            print("Plant: grshk shrshk(90)")
            print("Plant: flennel: flegel (6)")
        else:
            ("Ya can't read that here.")


    if room == 'East Storage' or room == 'Hangar':
        if item == 'card' or item == 'Card':
            if shuttlecard.room == "inv":
                print("ID: Snaeb Neerg")
                print("Race: Kosmukian")
                print("Beans: 412")
                print("Shuttle Code: 123456")
            else:
                print("Ya don't have it on you.")

    else:
        print("There's nothing else to read here.")


def water(item, room):
    if room == 'Plant Lab':
        if item == "Carbon Disulfate" or item == 'carbon disulfate':
            print("The plant starts shaking and vibrating. After about 30 seconds, it belches out a huge pool of distinctly water.")
            plant.set_description("A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk. There is a large puddle of water next to the plant you just watered.")
        else:
            print("Nothing happens to the plant. There is still liquid in the bottle.")
    else:
        print("Water what?")

def type(room):
    if room == 'Server Room':
        if input("Code?") == '4dY7bU':
            print("Gym Opened.")
            gym.unlock()
        else:
            print("Incorrect")

    if room == 'Command Operations Room':
        if input("Code?") == '12232917':
            print("Weapons now ready for use.")
            global weapons
            weapons = 'yes'

    if room == 'Command Operations Room':
        target = input("Target?")
        if target == 'd3682':
            print("Target Locked.")
            global targ
            targ = 'good'
        elif target == 'd3681':
            print("Target Locked.")
            targ = 'bad'
        elif not target == 'd3681' or not target == 'd3681' 'd3682':
            print("Invalid Target.")

    if room == 'Intelligence Operations Room':
        if input("Code?") == 'Cd1H3a':
            print("Bridge Maintinence Room AI chip unlocked.")
            global brmaintai
            brmaintai = 'yes'
            ai.set_rom(ai, brmaint)
            ai.room = brmaint
            ai.room = 'Bridge Maintinence Room'
        else:
            print("Incorrect")

    elif plant.description == 'A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk. The floor is extremely clean.':
        Intelligence = input("Do you want to unlock the Intelligence Room?")
        if Intelligence == 'yes' or Intelligence == 'Yes' or Intelligence == 'y' or Intelligence == 'Y' or Intelligence == 'Yeah' or Intelligence == 'yeah' or Intelligence == 'sure' or Intelligence == 'Sure':
            if input("Code?") == 't3H1dq':
                print("Intelligence Ops room unlocked.")
                global intelunlock
                intelunlock = 'yes'
                Intelligence = Room("Intelligence Operations Room", 'no')
                Intelligence.locked = 'no'
                Intelligence.unlock()
                Intelligence.unlock
                plant.set_description("A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk.")
            else:
                print("Incorrect")
        else:
            print("Come back when you have the code.")

def light(room, item):
    if item == 'shoe' and shoe.room == 'inv' or item == 'Shoe' and shoe.room == 'inv':
        if room == 'Cafe':
            if crow.room == "inv":
                print("You light the shoe on fire with the cigarrette lighter and hold it at a distance with the crowbar.")
                shoe.room = "dead"
                fshoe.room = "inv"
            else:
                print("You would burn your hand. You need something to hold it with at a distance.")
        else:
            print("With what?")
    else:("You simply can't light that on fire.")

def burn(room, item):
    if item == "Petri Dish" or item == 'petri dish' and fshoe.room == 'inv':
        if room == 'Science Lab':
            if fshoe.room == "inv":
                print("You burn the liquid in the petri dish, it withers, then melts into a smooth, thin, dark-green liquid.")
                dpetri.room = "inv"
                fshoe.room = "dead"
            else:
                print("What do you burn it with? Stupid")
        else:
            print("Where is it? Stupid.")
    else:("You simply can't burn that.")



def put(room, item):
    if room == 'West Escape Pod 2':
        if item == "Brush" or item == "brush" or item == "Toothbrush" or item == "toothbrush" and tooth.room == 'inv':
            tooth.room = dead
            print("You put the toothbrush in the hole, and a broadcast is sounded.")
            print("'MAYDAY signal launched. Emergency rooms unlocked and opened.'")
            engine2.unlock()
            maint.unlock()
        else:
            print("That would seem pointless.")

    if room == 'Library':
        if item == "remote" or "Remote" and tv.get_room() == 'inv':
            print("Nothing happens for about 10 seconds.")
            print("The ships AI, BM, asks, 'Attention, are you metally well?'")
            server.unlock()
        else:
            print("I do not see a place to put it anywhere.")
    else:
        if room == 'IT Quarters':
            if item == "cigar" or "Cigar" and cig.get_room() == 'inv':
                cig.room = "dead"
                print("The figurine falls down because of the weight")
                print("On the bottom, it says 'Sometimes, a remote can fit in the place of a book'")
            else:
                print("I do not see a place to put it anywhere.")
        else:
            ("I see no point in that.")
    if current_room.name == "Hangar" or current_room.name == "Shuttle":
        if item == "chip" or item == "Chip" or item == 'ai chip' or item == 'AI chip' or item == 'ai Chip' or item == 'AI Chip' and ai == 'yes':
            if shuttle == 'yes':
                print("You input the chip in the AI slot.")
                print("The Burning Mule awakens, and says: 'As soon as you launch, I will guide us to the nearest station, Mashinkey.'")





def unlock(room, item):
    if room == "Up Elevator":
        if item == 'captains' or item == 'Captains' or item == 'captains bedroom' or item == 'Captains Bedroom' or item == 'captain bedroom'and ccard.room == 'inv':
            capbr.unlock()
            print("You slide in the card, and hear a mechanical whisk and whir.")
            print("The door slides open.")

        elif item == 'officers' or item == 'Officers' or item == 'officers bedroom' or item == 'Officers Bedroom'  or item == 'officer bedroom'  or item == 'Officers Bedroom' and ocard.room == 'inv':
            offbr.unlock()
            print("You slide in the card, and hear a mechanical whisk and whir.")
            print("The door slides open.")
        else:
            print("You cannot open that here.")

    elif room == "West Brig Security Room":
        if item == 'file' or item == 'File' or item == 'filing cabinet' or item == 'Filing Cabinet':
            keycheck = input("With what?")
            if keycheck == 'key' or keycheck == 'Key':
                if key.room == 'inv':
                    print("You open the filing cabinet with the key.")
                    global file
                    file = 'open'
    elif plant.description == 'A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk. The floor is extremely clean.':
        Intelligence = input("Do you want to unlock the Intelligence Room?")
        if Intelligence == 'yes' or Intelligence == 'Yes' or Intelligence == 'y' or Intelligence == 'Y' or Intelligence == 'Yeah' or Intelligence == 'yeah' or Intelligence == 'sure' or Intelligence == 'Sure':
            if input("Code?") == 't3H1dq':
                print("Intelligence Ops room unlocked.")
                global intelunlock
                intelunlock = 'yes'
                Intelligence = Room("Intelligence Operations Room", 'no')
                Intelligence.locked = 'no'
                Intelligence.unlock()
                Intelligence.unlock
                plant.set_description("A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk.")
            else:
                print("Incorrect")
        else:
            print("Come back when you have the code.")









def wear(room):
    if goggles.room == "inv":
        if room == "Maze":
            print("You wear the goggles.")
            print("An ID card appears on the floor")
            ccard.room = "Maze"
            global gogglewear
            gogglewear = 'yes'
        else:
            print("You wear the goggles.")
    else:
        print("Wear what?")


def pour(room):
    if room == 'Military East Hallway':
        print("You pour the smoothie on the extruding electronic lock.")
        print("The electronic lock sparks and sputters, then fizzles out and smokes. After about 20 seconds, the lock falls off, revealing a hole in the wall that leads to nothing.")
        gpe2.unlock()
        gpe1.unlock()
        gpw1.unlock()
        gpw2.unlock()
    else:
        print("That is pointless and fruitless, but most importantly, beanless.")

def push(room, button):
    if room == 'Shuttle':
        if button == 'anything' or button == 'Anything' or button == 'button' or button == 'Button' or button == 'buttons' or button == 'Buttons' or button == 'Ignition' or button == 'ignition' or button == 'launch' or button == 'Launch' or button == 'launch button' or button == 'Launch Button' or button == 'fire' or button == 'Fire' or button == 'fire button' or button == 'Fire Button' or button == 'beans' or button == 'things' or button == 'Things':
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('')
            print("THE END")
            print("_________________________________________________________________")
            print("You push the ignition button and wait. Nothing happens.")
            print("Out of nowhere, the shuttle shudders and creaks, it moans and groans, and it starts to count down from 10.")
            print("When it reaches 0, everything stops moving and the shuttle is still.")
            print("BM announces: 'The Shuttle should have taken off by no-''")
            print("The shuttle launches into space, as BM is: 'Plotting a course to Mashinky'")
            print("You rest back in your seat, and fall asleep, ready for the long ride that awaits.")
            print("_________________________________________________________________")
            print("Thanks for playing! Mark Albiol worked very hard on this game, with much trial and error.")
            print("I am glad you played, and to be honest, amazing job completing the game as fast as you did. I thought it would have taken twice as long.")
            print("The next time you meet Mark, tell him the secret word is: 'PB & J (Pinto Beans & Jesus)'")
            print("When you are done reading, hit space then enter.")
            while True:
                if input("> ") == " ":
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print('')
                    print("As The Legend sleeps in the shuttle, the AI announces: 'Docking at Mashinkey.'")
                    print("The Legend awakens, and is greeted by: 'Passenger: Attention. No heat or life sources located at Mashinkey station.'")
                    print("'Ship fuel at 0.5%. Must refuel. Burning Mule going dark. Good Luck.")

    if room == 'Game Room':
        if button == 'cushions' or button == 'Cushions':
            ocard.set_rom(ocard, game)
            print("Among many other things, an ID card is laying under the cushions.")
    if room == 'East Missile Launch Platform' or room == "West Missile Launch Platform":
        if button == 'green nuclear' or button == 'Green Nuclear' or button == 'green photon' or button == 'Green Photon':
            if targ == 'good':
                print("The cylinder is loaded into the machine. You hear a whoosh as the contraption yeets the cylinder into space. It then shudders, and you feel an explosion in the distance.")
                print("After about 30 seconds, a MAYDAY received signal is broadcast across the ship.")
                print("'MAYDAY. Ship d3682 destroyed. Private rooms unlocked.'")
                bed1.unlock()
                bed2.unlock()
                bed3.unlock()
                bed4.unlock()
                bed5.unlock()
            if targ == 'bad':
                print("The cylinder is loaded into the machine. You hear a whoosh as the contraption yeets the cylinder into space.")
                print("After about 10 seconds, you hear a loud explosion that shakes the ship with the force of a god raining his fury down above. The lights go out and son after red lights flash on. The ship broadcasts a message.")
                print("'MISSILE HIT. SHIELDS LOST. POWER RECONSTRUCTIONS IMMINENT. CLOAK ACTIVATED.'")
                print("The lights return.")

        else:
            print("Nothing happens.")


def look(room):
    if input("In which direction?") == 'up':
        if room == "Board Game Room":
            print("On the ceiling, you see 'Intelligence Room Ship AI Unlock Code: Cd1H3a'")
        else:
            print("You look and see a wall.")
    else:
        print("You look and see a wall.")

def dry(room):
    if room == 'Plant Lab':
        if mop.room == 'inv':
            print("You clean up the mess with your broom.")
            print("The AI announces: 'You must be the janitor. Janitor Code: t3H1dq'")
            plant.set_description("A room with rows and rows of vertical stands holding thousands of categorized plants. The plants appear to be healthy and trimmed. A single vine with pink striations on the dark green leaves has grown from the side of the room, spreading its tentacles across the rows of the other plants. In many different glass bottles, there are different chemicals, including Ammonia, Ethanol, Hydrochloric Acid, Dihydrogen Monoxide, Liquid Pressurized Carbon Dioxide, Bicarbonate Sulfuric Acid, and Milk. The floor is extremely clean.")

def crack(room):
    if room == 'East Storage':
        opener = input("What would you like to crack open?")
        if opener == 'box' or opener == 'Box' or opener == 'boxes' or opener == 'Boxes' or opener == 'crate' or opener == 'Crate' or opener == 'crates' or opener == 'Crates':
            if crow.room == 'inv':
                print("You swing at the first box with your crowbar, and it satisfyingly cracks open.")
                print("Some sort of card falls out from the inside.")
                shuttlecard.set_rom(shuttlecard, estorage)
                shuttlecard.room = estorage
                shuttlecard.room = 'East Storage'
            else:
                print("With What? Your hands? You are crazy.")
        else:
            print("I don't see any of those around")
    else:
        print("Theres not much to crack here. Maybe try a storage full of boxes or something like that.")
        
test = '1'

weapons = 'no'

targ = 'uno'

shuttle = 'no'

file = 'duo'

gogglewear = 'treso'

intelunlock = 'no'

brmaintai = 'no'

shuttleunlock = 'no'

def save_game():

    saver = open("save.txt", "w+")
    
    saver.write(current_room_save + "\n")#0

    
    
    saver.write(test + "\n")#1
    saver.write(weapons + '\n')
    saver.write(targ + "\n")
    saver.write(shuttle + "\n")
    saver.write(file + "\n")
    saver.write(gogglewear + "\n")
    saver.write(intelunlock + "\n")
    saver.write(brmaintai + "\n")
    saver.write(shuttleunlock + "\n")
   
    saver.write(Item.get_details(goggles) + '\n')#10
    saver.write(Item.get_details(tooth) + '\n')
    saver.write(Item.get_details(ccard) + '\n')
    saver.write(Item.get_details(cig) + '\n')
    saver.write(Item.get_details(cow) + '\n')
    saver.write(Item.get_details(tv) + '\n')
    saver.write(Item.get_details(cush) + '\n')
    saver.write(Item.get_details(ocard) + '\n')
    saver.write(Item.get_details(dpetri) + '\n')
    saver.write(Item.get_details(bottle) + '\n')
    saver.write(Item.get_details(shoe) + '\n')
    saver.write(Item.get_details(fshoe) + '\n')
    saver.write(Item.get_details(gas) + '\n')
    saver.write(Item.get_details(crow) + '\n')
    saver.write(Item.get_details(lighter) + '\n')
    saver.write(Item.get_details(petri) + '\n')
    saver.write(Item.get_details(key) + '\n')
    saver.write(Item.get_details(log) + '\n')
    saver.write(Item.get_details(spill_water) + '\n')    
    saver.write(Item.get_details(mop) + '\n')
    saver.write(Item.get_details(ai) + '\n')
    saver.write(Item.get_details(box) + '\n')
    saver.write(Item.get_details(shuttlecard) + '\n')
    
    saver.write(Room.save_deets(engine2))#33
    saver.write(Room.save_deets(fq3))
    saver.write(Room.save_deets(capbr))
    saver.write(Room.save_deets(waiting))
    saver.write(Room.save_deets(game))
    saver.write(Room.save_deets(science))
    saver.write(Room.save_deets(gym))
    saver.write(Room.save_deets(bed1))
    saver.write(Room.save_deets(tool))
    saver.write(Room.save_deets(closet1))

def open_save_file():
    reader = open("save.txt")
    
    content = reader.readlines()
    print(content[0])
    
    #removethis = '\n'
    #tempor = content[0]
    
    if removethis in tempor:
        tempor.replace(removethis, '')
        
    Room.get_index(tempor)
    
    test = content[1]
    weapons = content[2]
    targ = content[3]
    shuttle = content[4]
    file = content[5]
    gogglewear = content[6]
    intelunlock = content[7]
    brmaint = content[8]
    shuttleunlock = content[9]
    

    goggles.room = content[10]
    tooth.room = content[11]
    ccard.room = content[12]
    cig.room = content[13]
    cow.room = content[14]
    tv.room = content[15]
    cush.room = content[16]
    ocard.room  = content[17]
    dpetri.room  = content[18]
    bottle.room  = content[19]
    shoe.room  = content[20]
    fshoe.room  = content[21]
    gas.room  = content[22]
    crow.room  = content[23]
    lighter.room  = content[24]
    petri.room  = content[25]
    key.room  = content[26]
    log.room  = content[27]
    spill_water.room  = content[28]
    mop.room  = content[29]
    ai.room  = content[30]
    box.room  = content[31]
    shuttlecard.room = content[32]
    
    engine2.set_description(content[33])
    engine2.set_save(content[34])
    fq3.set_description(content[35])
    fq3.set_save(content[36])
    capbr.set_description(content[37])
    capbr.set_save(content[38])
    waiting.set_description(content[39])
    waiting.set_save(content[40])
    game.set_description(content[41])
    game.set_save(content[42])
    science.set_description(content[43])
    sceince.set_save(content[44])
    gym.set_description(content[45])
    gym.set_save(content[46])
    bed1.set_description(content[47])
    bed1.set_save(content[48])
    tool.set_description(content[49])
    tool.set_save(content[50])
    closet1.set_description(content[51])
    closet1.set_save(content[52])
    print('success')















print("Welcome to Shipmaster")
print("------------------------------")
print("As previously stated, this game is a text adventure created by Mark Albiol.")
print("To play, you may move in the 4 cardinal directions as in")
print("East, West, North, South or Up and Down, but to move, only")
print("input the first letter in lowercase, so to move East, say e,")
print("then hit enter. To perform actions, type the action in and")
print("hit enter, then you will be prompted to be more specific.")
print("For example, if you wanted to grab something, you would")
print("type grab, hit enter, then the game will ask you what to grab.")
print("There are a few bugs, but nothing that will crash the game.")
print("If you enter a locked room while it is still locked,")
print("you will still have to exit, so if you went 'n' to get")
print("into a locked room, you will have to go 's' to get out.")
print("This will make more sense when you are playing.")
print("To print out your inventory, input: 'inventory'")
print("Try to have fun playing, and I will talk to you at the end.")
print("Good Luck. You will need it.")


current_room = hangar


while True:
    print("\n")
    print(current_room.get_locked())
    if current_room.get_locked() != 'no' and current_room.get_locked() != 'no\n':
        current_room_name = current_room.set_room(current_room.locker())
    else:
        current_room.get_details()


    command = input("> ")
    current_room = current_room.move(command)
    
    if intelunlock == 'yes':
        Intelligence.unlock()
        Intelligence.unlock
        Intelligence.locked = 'no'
        Intelligence.locked = Intelligence.unlock()
        Intelligence.locked = Intelligence.unlock
    if command == 'open save':
        open_save_file()
    
    if command == "grab":
        grab(input("What would you like to grab? "), current_room.name)

    if command == 'type':
        type(current_room.name)

    if command == "drop":
        drop(input("What would you like to drop? "), current_room.name)

    if command == "water":
        water(input("What do you want to water with?"), current_room.name)

    if command == "light":
        light(current_room.name, input("What do you want to light on fire?"))

    if command == "burn":
        burn(current_room.name, input("What do you want to burn?"))

    if command == "put":
        put(current_room.name, input("What do you want to put there?"))

    if command == "read":
        read(current_room.name, input("What do you want to read?"))

    if command == "open":
        unlock(current_room.name, input("Which room would you like to unlock?"))

    if command == "unlock":
        unlock(current_room.name, input("Which room would you like to unlock?"))

    if command == "wear":
        wear(current_room.name)

    if command == 'pour':
        pour(current_room.name)

    if command == 'push':
        push(current_room.name, input("What do you want to push?"))

    if command == 'dry':
        dry(current_room.name)

    if command == 'look':
        look(current_room.name)

    if command == 'inventory':
        Item.inventory(goggles, tooth, ccard, ocard, cig, cow, tv, cush, dpetri, bottle, shoe, fshoe, crow, petri, key, mop, ai, shuttlecard)

    if command == 'crack' or command == 'break':
        crack(current_room.name)
        
    if command == 'save':
        current_room_save = current_room.name
        save_game()
        
        
    if dpetri.room == 'inv' and current_room.name == "Simulation Room":
        print("Out of nowhere, the simulation room starts to activate.")
        print("You don't understand what it is displaying, but you feel peace and prosprity.")
        key.room = 'Simulation Room'
        print("A key is displayed in front of you.")
        dpetri.room = 'dead'
    if shuttlecard.get_room() == 'inv':
        shuttle = 'yes'
    if gogglewear == 'yes':
        maze.link_room(habserve, "w")
        maze.link_room(maze, "n")
        maze.link_room(maze, "e")
        maze.link_room(maze, "s")
        maze.link_room(maze, "d")
        maze.link_room(maze, "u")
    else:
        maze.link_room(maze, "w")
        maze.link_room(maze, "n")
        maze.link_room(maze, "e")
        maze.link_room(maze, "s")
        maze.link_room(maze, "d")
        maze.link_room(maze, "u")

    if shuttlecard.room == 'inv':
        shuttleunlock = 'yes'
        
    if shuttleunlock == 'yes':
        shuttle = Room("Shuttle", 'no')
        shuttle.set_description("A shuttle in the hangar.")
        shuttle.unlock
        shuttle.link_room(hangar, 'n')
        hangar.link_room(shuttle, 's')
        

