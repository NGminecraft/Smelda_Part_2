import pygame


class NPC:
    def __init__(self, location, item, keyframes = False):
        self.location = location
        self.image = item
        if not keyframes:
            self.keyframes = self.image.get_width() / self.image.get_height()
        else:
            self.keyframes = keyframes
        self.keyframe = 0
            
    def place_npc_in_rel_to(self, screen, coords):
        screen.blit(self.image, (self.location[0] + 208 - coords[0], self.image[1] + 208 + coords[1]))
        
    def get_npc(self):
        while True:
            yield self.image.subsurface((0, ))