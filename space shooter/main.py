import pygame;

# Do a general setup.  Initialize pygame.
pygame.init();
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720;
#Set the name of the display.
display_title = pygame.display.set_caption('Space Shooters');
#Create a display surface, store inside of a variable.
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT));

running = True;

#Surface of the actual gameplay itself.
surf = pygame.Surface((100, 200));
surf.fill('blue')
#Attach this surface to the game display surface.


#Import images for player,

player_surf = pygame.image.load('space shooter\images\player.png');
#Make sure window stays open using a while loop.
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False;

    # draw the game
    # fill the window with red color
    display_surface.fill("darkgray")
    # attaches surf to window, first number is from the left, heigh is from top left corner.
    display_surface.blit(surf, (100,150))

    #this puts the game on the screen
    pygame.display.flip() #update and flip do the same thing.
    
# End the program.
pygame.quit()