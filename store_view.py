import pygame
import numpy
import random
from items import *
import os
from items.potions import *
import importlib

# colors that the background creator pulls from
BACK_COLORS = ((80, 198, 0), (0, 190, 9), (23, 198, 0))
BLACK_COLORS = ((0, 0, 0), (255, 255, 255))
TILE_SET_LOCATION = "tileBaseTileset.png"


def initialize_background(static=False):
    # PyCharm gets mad if this isn't here
    # This creates a background which is essentially each pixel being a random color in the BACK_COLORS list

    background = []
    for i in range(350):
        layer1 = []
        for j in range(350):
            if static:
                layer1.append(random.choice(BLACK_COLORS))
            else:
                layer1.append(random.choice(BACK_COLORS))
        background.append(layer1)
    # I need to fix this array obsession
    return numpy.asarray(background)


class Level:
    def __init__(self, map_file="map.npy", collision_map="BigMapCollision"):
        # Creates map from passed in map files
        self.map = map_file
        self.font = pygame.font.init()
        self.collision_map = collision_map
        # This gets a background from the background array (see: Level.initialize_background() for details)
        self.backdrop = initialize_background()
        # This is predefining the center variable, which is used when placing the character
        self.center = (384, 360)
        # This initializes the dictionary that contains the map
        self.level = self.initialize_map_dict()
        # This initializes the dictionary for the collision in the map
        self.collision = self.initialize_collision()
        # This is the variable that stores the tileset that's used for getting all the tile subsurfaces
        tileset = pygame.image.load(TILE_SET_LOCATION)
        # This is the image for the frog npc that is used a couple of times, which sadly lost tile priveleges
        self.frogNPC = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Extra_Characters/PNG/sprToadEatWithTongue.png")
        #
        # This is the dictionary that maps each tile name (str) to a subsurface that can be put on the string
        # A number at the end of the string indicates that it is part of an animation (4 keyframes per, no exceptions)
        
        self.time = 255
        self.time_mult = 100 / (60 * 100)
        
        self.items = {
            "Wall": pygame.transform.scale(tileset.subsurface(pygame.Rect(465, 272, 15, 15)), (30, 30)),
            "Cabinet": pygame.transform.rotate(tileset.subsurface(pygame.Rect(513, 257, 30, 30)), 90),
            "Counter": tileset.subsurface(pygame.Rect(545, 257, 30, 30)),
            '': pygame.transform.scale(tileset.subsurface(pygame.Rect(659, 305, 29, 29)), (30, 30)),
            "Stash1": tileset.subsurface(pygame.Rect(370, 255, 30, 30)),
            "L_TorchN1": pygame.transform.scale(tileset.subsurface(pygame.Rect(737, 356, 15, 30)), (30, 30)),
            "L_TorchN2": pygame.transform.scale(tileset.subsurface(pygame.Rect(753, 356, 15, 30)), (30, 30)),
            "L_TorchN3": pygame.transform.scale(tileset.subsurface(pygame.Rect(769, 356, 15, 30)), (30, 30)),
            "L_TorchN4": pygame.transform.scale(tileset.subsurface(pygame.Rect(785, 356, 15, 30)), (30, 30)),
            "L_TorchS1": pygame.transform.scale(tileset.subsurface(pygame.Rect(737, 386, 15, 30)), (30, 30)),
            "L_TorchS2": pygame.transform.scale(tileset.subsurface(pygame.Rect(753, 386, 15, 30)), (30, 30)),
            "L_TorchS3": pygame.transform.scale(tileset.subsurface(pygame.Rect(769, 386, 15, 30)), (30, 30)),
            "L_TorchS4": pygame.transform.scale(tileset.subsurface(pygame.Rect(785, 386, 15, 30)), (30, 30)),
            "L_FloorTorch1": pygame.transform.scale(tileset.subsurface(pygame.Rect(736, 320, 15, 15)), (30, 30)),
            "L_FloorTorch4": pygame.transform.scale(tileset.subsurface(pygame.Rect(784, 320, 15, 15)), (30, 30)),
            "L_FloorTorch3": pygame.transform.scale(tileset.subsurface(pygame.Rect(768, 320, 15, 15)), (30, 30)),
            "L_FloorTorch2": pygame.transform.scale(tileset.subsurface(pygame.Rect(752, 320, 15, 15)), (30, 30)),
            "Frog1": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(0, 0, 24, 24)), (30, 30)),
            "Frog2": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(24, 0, 24, 24)), (30, 30)),
            "Frog3": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(48, 0, 24, 24)), (30, 30)),
            "Frog4": pygame.transform.scale(self.frogNPC.subsurface(pygame.Rect(72, 0, 24, 24)), (30, 30))
        }
        # This is the variable for storing the current keyframe for tiles with animations
        self.keyframe = 1
        self.init_inventory()

    def initialize_map_dict(self):
        # This takes the map file and returns the dictionary extrapolated from it.
        # I have no idea why I leave this as a numpy array file. It works though and saves a bit of processing.
        # This file is pregenerated, that's why it exists
        arr = numpy.load(self.map)
        dictionary = {}
        # This iterates through the array from the numpy file, adding each item to a dictionary
        for row_num, row in enumerate(arr):
            for column_num, column in enumerate(row):
                dictionary[(row_num * 30, column_num * 30)] = column
        return dictionary

    def initialize_collision(self):
        # This does the exact same as the map function but for collision instead
        # They may potentially be merged later on
        carr = numpy.load(self.collision_map)
        dictionary = {}
        for row_num, row in enumerate(carr):
            for column_num, column in enumerate(row):
                dictionary[(row_num * 30, column_num * 30)] = column
        return dictionary
    
    def init_inventory(self):
        # This guys job is to find all the items in the items folder
        blacklist = ("shopitem.py", "potion.py") # This is a tuple of all the files to ignore when finding items
        self.inventory = {}
        selfdir = os.path.dirname(os.path.realpath(__file__))
        folders = (f"{selfdir}\\items\\potions\\", f"{selfdir}\\items\\")
        if len(folders) == 1:
            raise "Tuple too small. len of tuple MUST be over 1"
        for folder in folders:
            for root, dirs, files in os.walk(folder):
                for file_name in files:
                    # Append the absolute path of each file to the list
                    if not file_name in blacklist and not ".pyc" in file_name:
                        module = __import__(file_name[0:-3], file_name.capitalize())
                        classobj = getattr(module, file_name[0:-3].capitalize())
                        if classobj.get_ids()["consumable"]:
                            count = 100
                        else:
                            count = 1
                        self.inventory[classobj] = count
                        
    def init_gui(self, screen):
        self.gui_height = screen.get_height() // 2
        self.width = screen.get_width()
        self.gui_rows = 2
        self.gui_layout = []
        keys = list(self.inventory.keys())
        for i in range(self.gui_rows):
            self.gui_layout.append([])
        if len(self.inventory) % self.gui_rows != 0:
            overflow = len(self.inventory) % self.gui_rows != 0
        else:
            overflow = 0
        for num in range(self.gui_rows):
            for i in range(len(self.inventory) // self.gui_rows + 1):
                self.gui_layout[num].append(keys[i])
            else:
                overflow -= 1
        self.side_length = min(self.gui_height / self.gui_rows, self.width / len(self.gui_layout[0]))

    def draw_background(self, screen):
        # It puts the background on the screen that's really it
        screen.blit(pygame.transform.scale(pygame.surfarray.make_surface(self.backdrop), (816, 816)), (0, 0))
        if pygame.key.get_pressed()[pygame.K_END]:
            self.static = 1
            self.backdrop = initialize_background(static=True)

    def draw_character(self, screen, player):
        # This puts the character on the screen utilizing its builtin get player method
        screen.blit(player.get_player(), self.center)

    def place_items(self, screen, player):
        # This puts all the items on the screen in their locations in respect to the players location
        coords = player.get_coords()
        # This goes through every item, though when necessary will be modified to only render items in a certain area
        # Around the player
        for key in reversed(self.level):
            # It will try to just place the current item on the screen
            try:
                screen.blit(self.items[self.level[key]], (key[0] + 208 - coords[0], key[1] + 208 + coords[1]))
            except KeyError:
                # The KeyError either means I did something wrong, or the tile has an animation
                self.keyframe += 0.006
                item = self.level[key]
                # This is a funky way of doing it. It takes the rounded version of whatever keyframe its on and appends
                # It to the name of whatever it's trying to put on
                item += str(round(self.keyframe))
                # It will then attempt to put it that edited name on the screen (Hence why all animations have a number
                # at the end)
                try:
                    screen.blit(self.items[item], (key[0] + 208 - coords[0], key[1] + 208 + coords[1]))
                except KeyError:
                    # If it can't put it on the screen, reset the animation keyframe. If for some reason it's still not
                    # There animations will break. Will be patched in a later update
                    self.keyframe = 0.9

    def check_collision(self, coords):
        # This function takes a set of coords and returns if collision is there or not
        # This essentially adjusts the coords to match the top left corner of the tile,
        # because that value is what's stored
        tile = (coords[0] - coords[0] % 30 + 270, coords[1] - coords[1] % 30 + (480 * 3) - 180)
        try:
            collision = self.collision[tile]
            # This is what I get when I use Google sheets to create my map
            if collision == "TRUE":
                return True
            else:
                return False
        except KeyError:
            # This catches out of bounds collision checks
            return False
        
    def store_gui(self, screen):
        back = pygame.surface.Surface((screen.get_width(), screen.get_height()))
        back.fill((0, 0, 0, 220))
        back.set_alpha(220)
        screen.blit(back, (0, 0))


# This is so it always runs the game file even if I accidentally try to run this one
if __name__ == "__main__":
    import main
