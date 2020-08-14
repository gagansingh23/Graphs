from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def trvl_path(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'

paths = Stack()
visited = set()

# in order to create a complete transversal we will have to compare visited to len of rooms


while len(visited) < len(world.rooms):
    exits = player.current_room.get_exits()
    print('Room:', player.current_room)
    print('exits available', exits)
    path = []
    for x in exits:
        if x is not None and player.current_room.get_room_in_direction(x) not in visited: #if exit exists and we haven't visited
            path.append(x)
            print(path, '<~ path')
    visited.add(player.current_room)
    if len(path) > 0:
        move = random.randint(0, len(path) - 1) #give choices of random index to choose from to navigate
        paths.push(path[move])
        player.travel(path[move])
        traversal_path.append(path[move])
        print('more rooms to explore')
    else:
        end = paths.pop()
        player.travel(trvl_path(end))
        traversal_path.append(trvl_path(end))
        print('End of this path')



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
