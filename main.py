import pygame
import store_view as lvl
import player as player
import npc as npc


pygame.init()
screen = pygame.display.set_mode((816, 816))
clock = pygame.time.Clock()
main_actor = player.Player()
walking = False
level = lvl.Level(main_actor, map="map.npy", collision_map="BigMapCollision.npy")
level.check_for_items(screen)
npc(pygame.image.load("Legend_of_Zink_Asset_Pack\Legend_of_Zink_Asset_Pack\Extra_Characters\PNG\sprToadEatWithTongue.png"), (10, 6))
while True:
    pressed = pygame.key.get_pressed()
    for i, v in enumerate(pressed):
        if v:
            if i == 22:
                main_actor.set_facing(2)
                main_actor.walk(level)
            if i == 7:
                main_actor.set_facing(1)
                main_actor.walk(level)
            if i == 4:
                main_actor.set_facing(3)
                main_actor.walk(level)
            if i == 26:
                main_actor.set_facing(0)
                main_actor.walk(level)
    level.draw_background(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
            
    level.check_for_items(screen)
    level.draw_character(screen)
    pygame.display.update()
    clock.tick(100)