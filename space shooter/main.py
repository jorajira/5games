import pygame;
from os.path import join
from random import randint
# Do a general setup.  Initialize pygame.
pygame.init();
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720;
#Set the name of the display and create a display surface, store inside of a variable.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT));
display_title = pygame.display.set_caption('Space Shooters');
running = True;

#Surface of the actual gameplay itself.
surf = pygame.Surface((100, 200));
surf.fill('orange');
x = 100

#Import images for player, star surface, run convert method to fix transparency issues.
path = join('images', 'player.png')
print(path)
player_surf = pygame.image.load(join('space shooter', 'images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('space shooter', 'images', 'star.png')).convert_alpha()
#Make sure window stays open using a while loop.
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False;

    # draw the game
    # fill the window with red color
    display_surface.fill("darkgray")
    x += 0.1
    # attaches surf to window, first number is from the left, height is from top left corner.
    display_surface.blit(player_surf, (100,150))
    #generate 20 stars on the screen at a time
    for i in range(20):
        display_surface.blit(star_surf, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
    #this puts the game on the screen
    pygame.display.flip() #update and flip do the same thing.
    
# End the program.
pygame.quit()