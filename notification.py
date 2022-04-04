import pygame
'''
Bobylev Yaroslav 2022
Github - https://github.com/Boyaroslav
'''


class Notification:
    def __init__(self, root, color, font):
        self.root, self.color = root, color
        self.font = font


    def draw_not(self, msg, frm):
        pygame.draw.rect(self.root, self.color[0], (400, 10, 400, 50))
        text = self.font.render(frm + " " + msg, False, self.color[1])
        self.root.blit(text, (450, 20))

        pygame.display.update()
        import time
        time.sleep(0.5)
        