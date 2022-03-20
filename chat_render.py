import pygame
from chat_history import *

class Chat:
    def __init__(self, root, place, BGcolor, color, font):
        self.root = root
        self.place = place
        self.BGcolor = BGcolor
        self.color = color
        self.font = font
    def draw(self):
        pygame.draw.rect(self.root, self.BGcolor, self.place)
        end = len(history) - config.count_messages_visible
        if len(history) < config.count_messages_visible:
            end = 0
        else:
            end = len(history) - config.count_messages_visible - 1

        for i in range(end, len(history) , 1):
            if history[i][0] == config.kitty_name:
                k_name = self.font.render(str(history[i][0]), True, config.kitty_name_chatcolor)
                self.root.blit(k_name, (self.place[0] + 5, self.place[1] + (i * 25) + 50))
            else:
                k_name = self.font.render(str(history[i][0]), True, config.BorderColor)
                self.root.blit(k_name, (self.place[0] + 5, self.place[1] + (i * 25) + 50))
            if len(history[i][1]) < config.maxlen_message:
                lenmes = len(history[i][1])
            else:
                lenmes = len(history[i][1]) - config.maxlen_message
            text = self.font.render(str(history[i][1][:lenmes ]), True, config.chat_color)
            self.root.blit(text, ((self.place[0] + 75, self.place[1] + (i * 25) + 50)))