import pygame
pygame.init()
root = pygame.display.set_mode((100,100))
bg = (50,0,0)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:quit()
        if i.type == pygame.KEYDOWN:
            if i.type == pygame.K_QUOTE:
                bg = (255,255,255)
    root.fill(bg)
    pygame.display.update()

