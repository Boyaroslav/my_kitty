'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''


import os

path = os.path.dirname(__file__)

# all plugins in /plugins directory
plugins = os.listdir(path + "/plugins")

plugins.remove('standart_output.py')


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


Chat_BG = (17, 20, 24)

kitty_name_chatcolor = (255, 200, 200)

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 65

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

border_size = 5  #  pixels

kitty_image_size = (kittty_rectangle_place[2] - (border_size * 2), kittty_rectangle_place[3] - (border_size * 2))

text_box_place = (500, 550, 600, 100)

chat_box_place = (chat_rectangle_place[0] + border_size, chat_rectangle_place[1] + border_size, 600 - (border_size * 2), 500 - (border_size * 2))


text_font = None

box_color = (200, 255, 200)


removing_speed = 0.1