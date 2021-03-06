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
        self.text_history = ['']
        self.index = 0
        self.pointer = 0



        self.arrow = pygame.image.load(self.path + "arrow.png")

        self.ar_up = pygame.image.load(self.path + "arrow_up.png")

        self.ar_down = pygame.image.load(self.path + "arrow_down.png")

    def draw_bar(self):
        # рисует окошко и курсор
        pygame.draw.rect(self.root, self.color1, self.place)
        if len(self.text) < self.maxlen_message:
            leng = 0
        else:
            leng = len(self.text) - self.maxlen_message

        text2 = self.font.render(''.join(self.text[leng:]), True, self.BGcolor)
        self.root.blit(text2, self.place[:2])
        wid, hei = self.font.size(''.join(self.text[leng:self.pointer]))
        pygame.draw.rect(self.root, self.button_color1,  (self.place[0] + wid, self.place[1], 2, hei))

    def active(self):
        self.color1 = (250, 200, 200)
        self.active = 1

    def disactive(self):
        self.color1=self. color
        self.active = 0
    
    def paste(self, x):
        self.text = self.text + list(x)
        self.pointer = len(self.text)

    def add_let(self, input):
        # добавляет юникодный(и не очень) символ
        self.text = self.text[:self.pointer] + [input] + self.text[self.pointer:]
        self.text_history[0] = self.text
        if self.text == ["\r", "\r"] or self.text == ["\r"]:
            self.text = []        
        if input == "\r" and len(self.text) > 1:
            self.history.send_msg(''.join(self.text[:-1]).replace('\r', '').lstrip())
            self.index = 0
            self.text_history[0] = ""
            self.text_history = [self.text_history[0]]+ [''.join(self.text[:-1])] + self.text_history[1:]
            self.text = []
        self.pointer += 1
    
    def add_word(self, input):
        self.text = self.text[:self.pointer] + list(input) + [" "] + self.text[self.pointer:]
        self.pointer += len(input) + 1


    def del_let(self):
        if len(self.text) != 0 and self.pointer <= len(self.text) and self.pointer > 0:
            self.pointer -= 1
            del self.text[self.pointer]
        if self.pointer > len(self.text):
            self.pointer = len(self.text)

    def set_history(self, but):
        # but содержит в себе событие клавиши вниз / вверх. Меняет self.text на предыдущие сообщения
        if but == pygame.K_UP:
            self.index += 1
            if self.index >= len(self.text_history) :
                self.index -= 1
            self.text = list(self.text_history[self.index])
            self.pointer = len(self.text)


        elif but == pygame.K_DOWN:
            self.index -= 1
            if self.index < 0:
                self.index = 0
            self.text = list(self.text_history[self.index])

    def isactive(self):
        return self.active

    def draw_clear_button(self):
        # кнопка очистки
        pygame.draw.rect(self.root, self.button_color1, (self.place[0] + self.place[2] + 10, self.place[1], self.place[3] // 2, self.place[3] // 2))
        self.root.blit(self.arrow, (self.place[0] + self.place[2] + 10, self.place[1]))

    def draw_go_up_down_button(self):
        # рисует бесполезные кнопки перемотки истории
        pygame.draw.rect(self.root, self.button_color1,  (self.place[0] - 50, self.place[1], 45, 45))

        pygame.draw.rect(self.root, self.button_color1,  (self.place[0] - 50, self.place[1] + 55, 45, 45))

        self.root.blit(self.ar_up, (self.place[0] - 50, self.place[1]))

        self.root.blit(self.ar_down, (self.place[0] - 50, self.place[1] + 55))

    def move_point(self, move):
        #  двигает указатель (ну штука та которая текст рожает)
        if move == pygame.K_LEFT:
            if self.pointer > 0:
                self.pointer -= 1

        elif move == pygame.K_RIGHT:
            if self.pointer < len(self.text):
                self.pointer += 1
    
    def clear(self):
        self.text = []


class Lcd_clock:
    # часы под иконкой kitty
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
