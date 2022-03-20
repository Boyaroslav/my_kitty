import os

path = os.path.dirname(__file__)

# all plugins in /plugins directory
plugins = os.listdir(path + "/plugins")
plugins.remove('standart_output.py')


BG = (50, 50, 50)

BorderColor = (100, 50, 50)


Chat_BG = (50, 50, 60)

kitty_name_chatcolor = (255, 200, 200)

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (255, 192, 203)

kitty_picture = path + "/kitty.jpg"

border_size = 5  #  pixels

kitty_image_size = (kittty_rectangle_place[2] - (border_size * 2), kittty_rectangle_place[3] - (border_size * 2))

text_box_place = (500, 550, 600, 100)

chat_box_place = (chat_rectangle_place[0] + border_size, chat_rectangle_place[1] + border_size, 600 - (border_size * 2), 500 - (border_size * 2))


text_font = None

box_color = (150, 100, 100)


removing_speed = 0.1