import pygame

pygame.init()

screensize = (800, 600)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Algo Visualizer")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()  # Update the display

pygame.quit()
# End of the main loop