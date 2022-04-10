import pygame
import time
from text_box import TextBox, Lcd_clock
from config import *
from chat_render import Chat 
from chat_history import History as hist
from chat_parser import Parser
from notification import Notification


from datetime import datetime



'''
Bobylev Yaroslav 2022
This script use pygame library to render the window
'''





#  initialisation:

pygame.init() 
root = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("your kitty :)")
clock = pygame.time.Clock()
main_font = pygame.font.SysFont(text_font, text_font_size)
history = hist()
parser = Parser(history)
history.pop_last = parser.pop_last

#  font

font = pygame.font.Font(path + clock_font, 50)     #  for clock

# notification

notify = Notification(root, clock_colors, font)


#  importing files

main_chr = pygame.image.load(kitty_picture)
main_chr = pygame.transform.scale(main_chr, kitty_image_size)  # rescaling to border size




#  Lcd clock for time

lcd_clock = Lcd_clock(font, clock_place, clock_colors, datetime, root)


#  window icon

pygame.display.set_icon(main_chr)

#  bar to input text

box = TextBox(root, chat_kitty_text, box_color, text_box_place, main_font, history,  maxlen_message, button_color1, path)


is_backspace = 0



# box with chat

chat = Chat(root, chat_box_place, Chat_BG, main_font)


def draw_need_borders():
    pygame.draw.rect(root, BorderColor, kittty_rectangle_place)  #  kitty picture border
    root.blit(main_chr, (kittty_rectangle_place[0] + border_size, kittty_rectangle_place[1] + border_size))  # kitty image


    pygame.draw.rect(root, BorderColor, chat_rectangle_place)  #  char border

#  used to exit the program by plugin  It works well if you start main.pyw as main
def bye():
    quit()


def clear_chat_history():
    history.array.clear()






while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1 :
                x, y = pygame.mouse.get_pos()
                if (x >= text_box_place[0] and x <= text_box_place[0] + text_box_place[2]) and (y >= text_box_place[1] and y <= text_box_place[1] + text_box_place[3]):
                    box.active
                elif (x >= text_box_place[0] + text_box_place[2] +10 and x <= text_box_place[0] + text_box_place[2] +10 + (text_box_place[3] // 2) and y >= text_box_place[1] and y <= text_box_place[1] + (text_box_place[3] // 2)):
                    box.clear()
                elif (x >= text_box_place[0] - 50 and x <= text_box_place[0] and y >= text_box_place[1] and y  <= text_box_place[1] + 45):
                    box.set_history(pygame.K_UP)
                elif (x >= text_box_place[0] - 50 and x <= text_box_place[0] and y >= text_box_place[1] + 55 and y  <= text_box_place[1] + 100):
                    box.set_history(pygame.K_DOWN)
                else:
                    box.disactive()
        if i.type == pygame.KEYDOWN and box.isactive:
            v = str(i)
            if i.key == pygame.K_BACKSPACE:
                is_backspace = 1

            elif i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                box.set_history(i.key)
            else:
                #box.add_let(v[v.index(':') + 3:v.index(',') - 1])
                box.add_let(i.unicode)
        if i.type == pygame.KEYUP:
            is_backspace = 0
    if is_backspace:
        box.del_let()
        time.sleep(removing_speed)

    
    root.fill(BG)
    draw_need_borders()


    chat.draw(history.get_history())
    box.draw_bar()
    box.draw_clear_button()
    box.draw_go_up_down_button()


    #  я понимаю, что это жесткий костыль. Я не придумал пока решения лучше, потому fix needed
    lcd_clock.draw()
    if history:
        if history[len(history) - 1] == [kitty_name, "__clear__"]:
            parser.clear_requested()
            clear_chat_history()



    pygame.display.update()
    clock.tick(30)
