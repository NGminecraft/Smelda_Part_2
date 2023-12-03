import pygame
import numpy
import random
import copy

# colors that the background creator pulls from
BACK_COLORS = ((80, 198, 0), (0, 190, 9), (23, 198, 0))
TILE_SET_LOCATION = "tileBaseTileset.png"


class Level:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
        self.backdrop = pygame.surfarray.make_surface(self.initialize_background())
        self.backdrop = pygame.transform.scale(self.backdrop, (816, 816))
        self.characterN = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png")
        self.characterE = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png")
        self.characterS = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png")
        self.characterW = pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png")
        self.objects = self.initialize_dict()
        self.items = {
            "Wall": (pygame.Rect(25, 63, 30, 30), False),
            "Cabinet": (pygame.Rect(513, 257, 30, 30), False),
            "Counter": (pygame.Rect(545, 257, 30, 30), False),
            '': (pygame.Rect(238, 100, 30, 30), False),
            "Stash1": (pygame.Rect(370, 255, 30, 30), False)
        }
        print(self.objects[(0, 0)])
        self.facing = 2
        self.walkKeyframe = 0
        self.coords = [0, 0]
        self.resize()

    def resize(self):
        self.characterN = pygame.transform.scale_by(self.characterN, 3)
        self.characterE = pygame.transform.scale_by(self.characterE, 3)
        self.characterS = pygame.transform.scale_by(self.characterS, 3)
        self.characterW = pygame.transform.scale_by(self.characterW, 3)

    def initialize_dict(self):
        arr = numpy.load("map3.npy")
        dictionary = {}
        for row_num, row in enumerate(arr):
            for column_num, column in enumerate(row):
                dictionary[(row_num * 30, column_num * 30)] = column
        return dictionary

    def initialize_background(self):
        background = []
        for i in range(350):
            layer1 = []
            for j in range(350):
                layer1.append(random.choice(BACK_COLORS))
            background.append(layer1)
        return numpy.asarray(background)

    def draw_background(self, screen):
        screen.blit(self.backdrop, (0, 0))
        screen.blit(self.font.render(str(self.coords), (255, 0, 0), (0, 0, 0)), (0, 10))

    def draw_character(self, screen):
        # Image is (96, 48) pixels
        rect = pygame.Rect(0, 0, 46 * 3, 46 * 3)
        if self.facing == 0:
            screen.blit(self.characterN, (screen.get_width() / 2 - self.characterN.get_width() / 4,
                                          screen.get_height() / 2 - self.characterN.get_height()), rect)
        elif self.facing == 3:
            screen.blit(self.characterW, (screen.get_width() / 2 - self.characterW.get_width() / 4,
                                          screen.get_height() / 2 - self.characterW.get_height()), rect)
        elif self.facing == 2:
            screen.blit(self.characterS, (screen.get_width() / 2 - self.characterS.get_width() / 4,
                                          screen.get_height() / 2 - self.characterS.get_height()), rect)
        elif self.facing == 1:
            screen.blit(self.characterE, (screen.get_width() / 2 - self.characterE.get_width() / 4,
                                          screen.get_height() / 2 - self.characterE.get_height()), rect)

    def walk(self):
        if self.facing == 0:
            self.coords[1] += 8
        if self.facing == 1:
            self.coords[0] += 8
        if self.facing == 2:
            self.coords[1] -= 8
        if self.facing == 3:
            self.coords[0] -= 8
        print(self.coords)

    def check_for_items(self, screen):
        try:
            for key in self.objects:
                if not self.items[self.objects[key]][1]:
                    screen.blit(pygame.image.load("tileBaseTileset.png"),
                                (key[0] + 208 - self.coords[0], key[1] + 208 + self.coords[1]),
                                self.items[self.objects[key]][0])
                else:
                    rect = copy.deepcopy(self.items[self.objects[key]][0])
                    rect.width = rect.width * 1.875
                    rect.height = rect.height * 1.875
                    rect.topleft = (rect.left * 1.875, rect.top * 1.875)
                    rect = (rect.x, rect.y, rect.w, rect.h)
                    print(rect)
                    screen.blit(pygame.transform.scale(pygame.image.load("tileBaseTileset.png"),
                                                       self.items[self.objects[key]][1]),
                                (key[0] + 208 - self.coords[0], key[1] + 208 + self.coords[1]), rect)
        except KeyError:
            pass


# This is so it always runs the game file even if I accidentaly try to run this onex                c
if __name__ == "__main__":
    import main
