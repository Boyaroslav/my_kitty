import pygame

import config

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

class Chat:
    def __init__(self, root, place, BGcolor, color, font):
        self.root = root
        self.place = place
        self.BGcolor = BGcolor
        self.color = color
        self.font = font
    def draw(self):
        from chat_history import history
        
        pygame.draw.rect(self.root, self.BGcolor, self.place)
        end = len(history) - config.count_messages_visible
        if len(history) < config.count_messages_visible:
            end = 0
        else:
            end = len(history) - config.count_messages_visible - 1
        messy = self.place[1] + ((0 ) * 25) + 50


        for i in range(end, len(history) , 1):
            mess = history[i][1]
            if len(mess) < config.maxlen_message:
                lenmes = len(mess)
            else:
                lenmes = len(mess) - config.maxlen_message
            text = self.font.render(str(mess[:lenmes ]), True, config.chat_color)
            self.root.blit(text, ((self.place[0] + 55, messy)))


            if history[i][0] == config.kitty_name:
                k_name = self.font.render(str(history[i][0]), True, config.kitty_name_chatcolor)
                self.root.blit(k_name, (self.place[0] + 5, messy))
            elif history[i][0] == "you":
                k_name = self.font.render(str(history[i][0]), True, config.BorderColor)
                self.root.blit(k_name, (self.place[0] + 5, messy))
            messy += 25
            
            
            