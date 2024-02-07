import sys
# This sketchy looking code allows me to import modules from parent directories
a = sys.path[0].split('\\')
a.append("items")
sys.path.append("\\".join(a))
a.append("potions")
sys.path.append("\\".join(a))
import pygame
import store_view as lvl
import player as player
from shop import Shop

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

level.init_gui(screen)

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
    if pressed[pygame.K_p]:
        print(f"FPS: {clock.get_fps()}")
        print(f"Coords: {main_actor.get_coords()}")
    directions = []
    # S key
    if pressed[pygame.K_s]:
        # Each block in the if statement changes where the character is facing, then tells it to move
        directions.append(2)
    # D key
    if pressed[pygame.K_d]:
        directions.append(1)
    # A key
    if pressed[pygame.K_a]:
        directions.append(3)
    # W key
    if pressed[pygame.K_w]:
        directions.append(0)
    sprint = 1
    if pressed[pygame.K_LSHIFT]:
        sprint = sprint*2
    if pressed[pygame.K_RSHIFT]:
        sprint = sprint * 2
    main_actor.crouching = 1
    if pressed[pygame.K_LCTRL]:
        main_actor.crouching = main_actor.crouching * 2
    if pressed[pygame.K_RCTRL]:
        main_actor.crouching = main_actor.crouching * 2
    else:
        main_actor.crouching = 1
    for i in directions:
        main_actor.set_facing(i)
        main_actor.walk(level, 1/len(directions)*sprint)
    
    if pressed[pygame.K_p]:
        level.debug = True
    # Using my background as the bottom layer
    level.draw_background(screen)
    # Places the level on top of that
    level.place_items(screen, main_actor)
    # Adds the character
    level.draw_character(screen, main_actor)
    level.store_gui(screen)
    # Updates everything
    pygame.display.update()
    # This is technically the basic tick speed
    clock.tick(100)
