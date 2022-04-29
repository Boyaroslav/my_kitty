import pygame

import config



'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

class Chat:
    def __init__(self, root, place, BGcolor, font):
        self.root = root
        self.place = place
        self.BGcolor = BGcolor
        self.font = font
        self.history = []
        self.index = 0
    def draw(self, history):
        self.history = history

        
        pygame.draw.rect(self.root, self.BGcolor, self.place)
        if len(history) > 0:
            self.end = len(history) - config.count_messages_visible
            if len(history) < config.count_messages_visible:
                self.end = 0
                self.index = 0

            else:
                self.end = len(history) - config.count_messages_visible - 1
            if self.end < 0:
                self.end = 0


            messy = self.place[1] + (0  * 25) + 25



            for i in range(self.end + self.index, len(history) + self.index, 1):
                mess = history[i][1]
                if len(mess) < config.maxlen_message:
                    lenmes = len(mess)
                else:
                    lenmes = len(mess) - config.maxlen_message
                #  WARNING!!! iF YOU WROTE YOUR OWN PLUGIN, BE SURE WHAT OUTPUT LENGTH LOWER THAN maxlen_message 
                text = self.font.render(str(mess[:lenmes ]), True, config.chat_color)

                self.root.blit(text, ((self.place[0] + 55, messy)))


                if history[i][0] == config.kitty_name:
                    k_name = self.font.render(str(history[i][0]), True, config.kitty_name_chatcolor)
                    self.root.blit(k_name, (self.place[0] + 5, messy))
                elif history[i][0] == "you":
                    k_name = self.font.render(str(history[i][0]), True, config.BorderColor)
                    self.root.blit(k_name, (self.place[0] + 5, messy))
                messy += 25
    def draw_buttons(self):
        pygame.draw.rect(self.root, config.button_color1, (self.place[0] + self.place[2] + 10, self.place[1], 20, 20))

        pygame.draw.rect(self.root, config.button_color1, (self.place[0] + self.place[2] + 10, self.place[1] + 25, 20, 20))

        ar_up = pygame.image.load(config.path + "arrow_up.png")
        ar_up = pygame.transform.scale(ar_up, (20, 20)) 

        ar_down = pygame.image.load(config.path + "arrow_down.png")
        ar_down = pygame.transform.scale(ar_down, (20, 20)) 

        self.root.blit(ar_up, (self.place[0] + self.place[2] + 10, self.place[1]))
        self.root.blit(ar_down, (self.place[0] + self.place[2] + 10, self.place[1] + 25))
    
    def get_butts_pos(self):
        print(self.index)
        return (self.place[0] + self.place[2] + 10, self.place[1])
    def change_index(self, i):
        if len(self.history) > config.count_messages_visible:
            if self.end + self.index + i >= 0:
                if self.end + self.index + i <= len(self.history) and len(self.history) + self.index + i <= len(self.history):
                    self.index += i
    
    def clear_index(self):
        self.index = 0
        


        



            
            
            
