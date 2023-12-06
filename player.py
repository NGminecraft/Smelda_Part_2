import pygame


class Player:
    # This is the class for storing players, and player like objects
    def __init__(self):
        # These are the starting coords
        self.coords = [1200, -515]
        self.facing = 3
        self.walk_speed = 4
        # This is they keyframe for the walking animation
        self.walking_animation = 1
        # This loads the character and all of it's orientations
        self.characterN = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkN.png"), 3)
        self.characterE = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkE.png"), 3)
        self.characterS = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkS.png"), 3)
        self.characterW = pygame.transform.scale_by(pygame.image.load(
            "Legend_of_Zink_Asset_Pack/Legend_of_Zink_Asset_Pack/Zink/PNG/Zink_Only/sprZinkWalkW.png"), 3)

    def walk(self, level):
        # Move the character
        # Depending on whichever way it's facing:
        if self.facing == 0:
            # Check the level object that's passed in for collision
            if not level.check_collision((self.coords[0] - 15, self.coords[1] + 30)) and not level.check_collision(
                    (self.coords[0] + 15, self.coords[1] + 30)):
                # If no collision move forward at walk speed
                self.coords[1] += self.walk_speed
        # If there is collision check to see if your actually walking into something instead or just up against a wall
            elif not level.check_collision((self.coords[0] - 10, self.coords[1])) and not level.check_collision(
                    (self.coords[0] - 15, self.coords[1] + 30)):
                self.coords[1] += self.walk_speed
        # That runs depending on which way your facing and changes either your x or y depending on orientation
        if self.facing == 1:
            if not level.check_collision((self.coords[0] + 5, self.coords[1])):
                self.coords[0] += self.walk_speed
        if self.facing == 2:
            if not level.check_collision((self.coords[0] - 15, self.coords[1] - 4)) and not level.check_collision(
                    (self.coords[0] + 15, self.coords[1] - 4)):
                self.coords[1] -= self.walk_speed
            elif not level.check_collision((self.coords[0] - 10, self.coords[1])) and not level.check_collision(
                    (self.coords[0] - 15, self.coords[1] - 4)):
                self.coords[1] -= self.walk_speed
        if self.facing == 3:
            if not level.check_collision((self.coords[0] - 45, self.coords[1])):
                self.coords[0] -= self.walk_speed
        # This function is about as sturdy as my sanity (not)
        self.walking_animation += 0.05

    def get_player(self, keyframe=False):
        # This returns the image of the character, including walking animation
        # Checks for keyframe overrides and adjust the keyframe variable to allow for looping and rounding
        if self.walking_animation >= 1 and not keyframe:
            self.walking_animation = 0
        elif keyframe:
            self.walking_animation = keyframe
        # This "rounds" the keyframe variable
        if self.walking_animation >= 0.5:
            keyframe = 1
        else:
            keyframe = 0
        # This creates the rectangle part of the image depicting the character in that keyframe
        rect = pygame.Rect(keyframe * (self.characterN.get_width() / 2), 0, self.characterN.get_width() / 2,
                                       self.characterN.get_height())
        # Returns a character subsurface based off of its orientation and the rectangle above
        if self.facing == 0:
            return self.characterN.subsurface(rect)
        elif self.facing == 3:
            return self.characterW.subsurface(rect)
        elif self.facing == 2:
            return self.characterS.subsurface(rect)
        elif self.facing == 1:
            return self.characterE.subsurface(rect)

    def get_coords(self):
        # Basic coordinate getter
        return self.coords

    def set_facing(self, facing):
        # Basic facing setter, may improve later on to protect against invalid inputs
        self.facing = facing


if __name__ == "__main__":
    import main
