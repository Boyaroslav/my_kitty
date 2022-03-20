#  box class where the input is rendered
import pygame
import chat_history

class TextBox:
    def __init__(self, root, color, BGcolor, place, font):
        self.color1 = color
        self.BGcolor = BGcolor
        self.place = place
        self.root = root
        self.font = font
        self.color = color
        self.text = []
        self.active = 0
    def draw_bar(self):
        pygame.draw.rect(self.root, self.color1, self.place)
        if self.active:
            pygame.draw.rect(self.root, (0,0,0), (self.place[0] + (len(self.text) * 25), self.place[1], 20, self.place[3]))
        text2 = self.font.render(''.join(self.text), True, self.BGcolor)
        self.root.blit(text2, self.place[:2])
    def active(self):
        self.color1 = (250, 200, 200)
        self.active = 1
    def disactive(self):
        self.color1=self. color
        self.active = 0
    def add_let(self, input):
        self.text.append(input)
        if input == "\r" and len(self.text) > 1:
            chat_history.send_msg(''.join(self.text).replace('\r', ''))
            self.text = []


    def del_let(self):
        if len(self.text) != 0:
            del self.text[-1]

    def isactive(self):
        return self.active
    
