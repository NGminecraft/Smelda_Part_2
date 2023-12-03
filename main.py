import pygame
import store_view as lvl
import player as player

# Setting up the pygame window
pygame.init()
screen = pygame.display.set_mode((816, 816))
clock = pygame.time.Clock()
# This builds the player, Hopefully in a way I can make multiple later on
main_actor = player.Player()
# This is our level, using my largest map
level = lvl.Level(map_file="map.npy", collision_map="BigMapCollision.npy")
# This places the first items before putting everything else on top.
level.place_items(screen, main_actor)

# Main game loop
while True:
    # This actually terminates the game, when you try to terminate the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Takes all the keys that are being pressed and checks to see if any of the movement keys are pressed
    # This is going to be improved later
    pressed = pygame.key.get_pressed()
    for i, v in enumerate(pressed):
        if v:
            # S key
            if i == 22:
                # Each block in the if statement changes where the character is facing, then tells it to move
                main_actor.set_facing(2)
                main_actor.walk(level)
            # D key
            elif i == 7:
                main_actor.set_facing(1)
                main_actor.walk(level)
            # A key
            elif i == 4:
                main_actor.set_facing(3)
                main_actor.walk(level)
            # W key
            elif i == 26:
                main_actor.set_facing(0)
                main_actor.walk(level)
    # Using my background as the bottom layer
    level.draw_background(screen)
    # Places the level on top of that
    level.place_items(screen, main_actor)
    # Adds the character
    level.draw_character(screen, main_actor)
    # Updates everything
    pygame.display.update()
    # This is technically the basic tick speed
    clock.tick(100)
