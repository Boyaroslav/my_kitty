from distutils.command.config import config
import pygame
import time
from text_box import TextBox, Lcd_clock
from config import *
from chat_render import Chat 
from chat_history import History as hist
from chat_parser import Parser
from top_bar import Bar
from importlib import reload
import sys
import pyperclip
from datetime import datetime


'''
Bobylev Yaroslav 2022
This script use pygame library to render the window
'''

# инициализация переменных, не входящих в графическую составляющую

window_size = (1200, 700)


pygame.init() 
root = pygame.display.set_mode(window_size)
pygame.display.set_caption("your kitty :)")
clock = pygame.time.Clock()
history = hist()
parser = Parser(history)
history.pop_last = parser.pop_last

class Kitty:
    def __init__(self, pict, name, font, text_color):
        self.pict = pict
        self.name = name
        self.font = font
        self.text_color = text_color

    def place(self):
        if draw_picture_bar:
            pygame.draw.rect(root, Chat_BG, (kitty_rectangle_place[0] - 10, kitty_rectangle_place[1] - 10, kitty_rectangle_place[2] + 20,kitty_rectangle_place[3] + border_size + 35 ))
        # picture and border
        pygame.draw.rect(root, BorderColor, kitty_rectangle_place)  #  kitty picture border
        root.blit(self.pict, (kitty_rectangle_place[0] + border_size, kitty_rectangle_place[1] + border_size))  # kitty image
        # name and names border
        text = self.font.render(self.name, True, self.text_color)
        wid, hei = self.font.size(self.name)

        
        pygame.draw.rect(root, BorderColor, (kitty_rectangle_place[0], kitty_rectangle_place[1] + kitty_rectangle_place[3] + border_size, wid + 50, 20))
        
        root.blit(text, (kitty_rectangle_place[0] + 10, kitty_rectangle_place[1] + kitty_rectangle_place[3] + border_size + 2))
        

#  нужно для корректировки тем
def hex_to_rgb(hex):
    hex = hex[1:]
    rgb = []
    for i in (0, 2, 4):
        d = int(hex[i:i+2], 16)
        rgb.append(d)
  
    return tuple(rgb)

#  не нужно вовсе
def rgb_to_hex(r, g, b):
    return ('{:X}{:X}{:X}').format(r, g, b)

def normalize(x):
    if type(x) == type((1, 2, 3)):
        return x
    if type(x) == type("Mr Kostil"):
        if x[0] == "#":
            return hex_to_rgb(x)
        else:
            return x


#  перезагружает всю графическую составляющую
def reld():
    config = reload(sys.modules['config'])
    global BG
    global BorderColor
    global clock_colors
    global Chat_BG
    global kitty_name_chatcolor
    global chat_color
    global chat_kitty_text
    global button_color1
    global box_color
    global top_color
    global main_font
    global font
    global main_chr
    global lcd_clock
    global kitty_char
    global box
    global is_backspace
    global chat
    global bar
    global bg_fill
    global BG_IM
    global top_color
    global kitty_name

    #  нормализация переменных (hex строка не принимается)
    BG = normalize(config.BG)
    # не забывайте преобразовывать все данные цвета в кортеж rgb, pygame другое не ест
    BorderColor = normalize(config.BorderColor)
    clock_colors =  [normalize(config.clock_colors[0]), normalize(config.clock_colors[1])]
    Chat_BG = normalize(config.Chat_BG)
    kitty_name_chatcolor =  normalize(config.kitty_name_chatcolor)
    chat_color = normalize(config.chat_color)
    chat_kitty_text = normalize(config.chat_kitty_text)
    button_color1 = normalize(config.button_color1)
    box_color = normalize(config.box_color)
    top_color = normalize(config.top_color)
    # Если кто либо на это покусится, то пойдет куда подальше
    #  initialisation:
    main_font = pygame.font.SysFont(config.text_font, config.text_font_size)
    #  font
    font = pygame.font.Font(config.clock_font, 50)     #  for clock

    #  importing files
    main_chr = pygame.image.load(config.kitty_picture)
    main_chr = pygame.transform.scale(main_chr, config.kitty_image_size)  # rescaling to border size

    #  Lcd clock for time
    lcd_clock = Lcd_clock(font, config.clock_place, config.clock_colors, datetime, root)
    #  window icon
    pygame.display.set_icon(main_chr)
    #  bar to input text
    box = TextBox(root, config.chat_kitty_text, config.box_color, config.text_box_place, main_font, history,  config.maxlen_message, config.button_color1, config.path)
    is_backspace = 0
    # box with chat
    chat = Chat(root, config.chat_box_place, config.Chat_BG, main_font)
    # top bar
    bar = Bar(window_size, root, config.top_color, main_font, config.box_color)
    kitty_char = Kitty(main_chr, config.kitty_name, main_font, config.box_color)
    if type(BG) == type((1, 2, 3)):
        bg_fill = root.fill(BG)

    elif type(BG) == type("Mr Kostil"):
        BG_IM = pygame.image.load(BG)
        BG_IM = pygame.transform.smoothscale(BG_IM, (window_size[0] * BG_blur, window_size[1] * BG_blur))
        BG_IM = pygame.transform.scale(BG_IM, window_size)
    
        bg_fill = root.blit(BG_IM, (0, 0))

reld()

def draw_need_borders():
    #pygame.draw.rect(root, BorderColor, kitty_rectangle_place)  #  kitty picture border
    #root.blit(main_chr, (kitty_rectangle_place[0] + border_size, kitty_rectangle_place[1] + border_size))  # kitty image
    kitty_char.place()

    pygame.draw.rect(root, BorderColor, chat_rectangle_place)  #  char border

#  used to exit the program by plugin  It works well if you start main.pyw as main
def bye():
    quit()


def clear_chat_history():
    history.array.clear()


while True:
    if history:
        if history[len(history) - 1] == [kitty_name, "__clear__"]:
            parser.clear_requested()
            clear_chat_history()
        elif history[len(history) - 1] == [kitty_name, 'reload']:
            history.del_mess(-1)
            history.send_msg(kitty_name, "reloaded!")
            reld()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1 :
                x, y = pygame.mouse.get_pos()
                if (x >= text_box_place[0] and x <= text_box_place[0] + text_box_place[2]) and (y >= text_box_place[1] and y <= text_box_place[1] + text_box_place[3]):
                    box.active
                if draw_buttons:
                    if (x >= text_box_place[0] + text_box_place[2] +10 and x <= text_box_place[0] + text_box_place[2] +10 + (text_box_place[3] // 2) and y >= text_box_place[1] and y <= text_box_place[1] + (text_box_place[3] // 2)):
                        box.clear()
                    elif (x >= text_box_place[0] - 50 and x <= text_box_place[0] and y >= text_box_place[1] and y  <= text_box_place[1] + 45):
                        box.set_history(pygame.K_UP)
                    elif (x >= text_box_place[0] - 50 and x <= text_box_place[0] and y >= text_box_place[1] + 55 and y  <= text_box_place[1] + 100):
                        box.set_history(pygame.K_DOWN)
                    elif (x >= chat.get_butts_pos()[0] and x <= chat.get_butts_pos()[0] + 20 and y >= chat.get_butts_pos()[1] and y <= chat.get_butts_pos()[1] + 20):
                        chat.change_index(-1)
                    elif (x >= chat.get_butts_pos()[0] and x <= chat.get_butts_pos()[0] + 20 and y >= chat.get_butts_pos()[1] + 25 and y <= chat.get_butts_pos()[1] + 45):
                        chat.change_index(1)             
                else:
                    box.disactive()
        if i.type == pygame.KEYDOWN and box.isactive:
            v = str(i)
            if i.key == pygame.K_BACKSPACE:
                is_backspace = 1

            elif i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                box.set_history(i.key)

            elif i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                box.move_point(i.key)
            
            elif i.key == pygame.K_v:
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_CTRL:
                    box.paste(str(pyperclip.paste()))
                else:
                    box.add_let(i.unicode)
                    
            elif i.key == pygame.K_c :
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_CTRL:
                    pyperclip.copy(''.join(box.text))
                else:
                    box.add_let(i.unicode)
            else:
                #box.add_let(v[v.index(':') + 3:v.index(',') - 1])
                box.add_let(i.unicode)
            chat.clear_index()
        if i.type == pygame.KEYUP:
            is_backspace = 0
    if is_backspace:
        box.del_let()
        time.sleep(removing_speed)

    
    bg_fill
    draw_need_borders()


    chat.draw(history.get_history())
    box.draw_bar()
    if draw_buttons:
        box.draw_clear_button()
        box.draw_go_up_down_button()
        chat.draw_buttons()


    #  я понимаю, что это жесткий костыль. Я не придумал пока решения лучше, потому fix needed
    lcd_clock.draw()

    if draw_top_bar:
        bar.draw(["power " + open("/sys/class/power_supply/BAT0/capacity").read() + "%"] +  parser.get_plugs(3))


    pygame.display.update()
    clock.tick(30)
