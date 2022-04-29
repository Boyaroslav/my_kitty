import pygame
'''
Bobylev Yaroslav 2022
This script use pygame library to render the window
'''

class Bar:
    def __init__(self, win_size, root, color, fnt, fnt_col):
        self.win_size = win_size
        self.root = root
        self.color = color
        self.font = fnt
        self.fnt_col = fnt_col

    
    def draw(self, data):
        pygame.draw.rect(self.root, self.color, (10, 10, self.win_size[0] - 20, 20))
        leng = 0
        output = data[::-1]
        wid, hei = self.font.size(' | '.join(map(str,output)))

        text = self.font.render(' | '.join(map(str, output)), True, self.fnt_col)
        self.root.blit(text, ((self.win_size[0] - wid)// 2, 12))
            
            