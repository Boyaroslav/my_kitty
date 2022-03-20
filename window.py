import pygame
import time
from text_box import TextBox
from config import *
from chat_render import *  
from chat_history import *
'''
Bobylev Yaroslav 2022
This script use pygame library to render the window
'''

pygame.init() 


#  initialisation:

root = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("your kitty :)")
clock = pygame.time.Clock()
main_font = pygame.font.Font(text_font, 25)


#  importing files

main_chr = pygame.image.load(kitty_picture)
main_chr = pygame.transform.scale(main_chr, kitty_image_size)  # rescaling to border size


#  bar to input text

box = TextBox(root, chat_kitty_text, box_color, text_box_place, main_font)


is_backspace = 0



# box with chat

chat = Chat(root, chat_box_place, Chat_BG, chat_kitty_text, main_font)


def draw_need_borders():
    pygame.draw.rect(root, BorderColor, kittty_rectangle_place)  #  kitty picture border
    root.blit(main_chr, (kittty_rectangle_place[0] + border_size, kittty_rectangle_place[1] + border_size))  # kitty image


    pygame.draw.rect(root, BorderColor, chat_rectangle_place)  #  char border


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            print(box.text)
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1 :
                x, y = pygame.mouse.get_pos()
                if (x >= text_box_place[0] and x <= text_box_place[0] + text_box_place[2]) and (y >= text_box_place[1] and y <= text_box_place[1] + text_box_place[3]):
                    box.active
                else:
                    box.disactive
        if i.type == pygame.KEYDOWN and box.isactive:
            v = str(i)
            if i.key == pygame.K_BACKSPACE:
                is_backspace = 1
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


    chat.draw()
    box.draw_bar()


    pygame.display.update()
    clock.tick(60)