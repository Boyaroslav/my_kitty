#  box class where the input is rendered
import pygame


'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

class TextBox:
    def __init__(self, root, color, BGcolor, place, font, history, maxlen_message, button_color1, path):
        self.color1 = color
        self.BGcolor = BGcolor
        self.place = place
        self.root = root
        self.font = font
        self.color = color
        self.text = []
        self.active = 0
        self.history = history
        self.maxlen_message = maxlen_message
        self.button_color1 = button_color1
        self.path = path
    def draw_bar(self):
        pygame.draw.rect(self.root, self.color1, self.place)
        if len(self.text) < self.maxlen_message:
            leng = 0
        else:
            leng = len(self.text) - self.maxlen_message
        if self.active:
            #  dont work
            pygame.draw.rect(self.root, (0,0,0), (self.place[0] + (len(self.text[leng:]) * 25), self.place[1], 20, self.place[3]))
        text2 = self.font.render(''.join(self.text[leng:]), True, self.BGcolor)
        self.root.blit(text2, self.place[:2])
    def active(self):
        self.color1 = (250, 200, 200)
        self.active = 1
    def disactive(self):
        self.color1=self. color
        self.active = 0
    def add_let(self, input):
        self.text.append(input)
        if self.text == ["\r", "\r"] or self.text == ["\r"]:
            self.text = []        
        if input == "\r" and len(self.text) > 1:
            self.history.send_msg(''.join(self.text).replace('\r', ''))
            self.text = []


    def del_let(self):
        if len(self.text) != 0:
            del self.text[-1]

    def isactive(self):
        return self.active
    def draw_clear_button(self):
        pygame.draw.rect(self.root, self.button_color1, (self.place[0] + self.place[2] + 10, self.place[1], self.place[3] // 2, self.place[3] // 2))
        arrow = pygame.image.load(self.path + "arrow.png")
        self.root.blit(arrow, (self.place[0] + self.place[2] + 10, self.place[1]))
    def clear(self):
        self.text = []


class Lcd_clock:
    def __init__(self, font, place, color, date, root):
        self.font = font
        self.place = place
        self.color = color
        self.lcd_text = date
        self.root = root
        

    def draw(self):
        self.nw = self.lcd_text.now()
        text = self.nw.strftime("%H:%M:%S")
        pygame.draw.rect(self.root, self.color[1], self.place)
        rend = self.font.render(text, False, self.color[0])
        self.root.blit(rend, (self.place[0] + 60, self.place[1] + 5))
