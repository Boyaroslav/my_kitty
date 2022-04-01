import pygame
'''
Bobylev Yaroslav 2022
Github - https://github.com/Boyaroslav
'''


class Notification:
    def __init__(self, root, color, font):
        self.root, self.color = root, color
        self.font = font
        self.clock = pygame.time.Clock()

    def draw_not(self, msg, frm):
        pygame.draw.rect(self.root, self.color, (400, 10, 400, 50))
        text = self.font.render(frm + " " + msg, False, self.color)
        self.root.blit(text, (450, 20))

        pygame.display.update()
        for i in rang(1000):
            clock.tick(30)
        