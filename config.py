'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''



import os

# fix lash on windows

slash = "/"

if os.name == "nt":
    slash = '\\'
    


path = os.path.dirname(__file__) + slash

# all plugins in /plugins directory
plugins = os.listdir(path + slash + "plugins")


plugins.remove('standart_output.py')
plugins.remove("__init__.py")
if "__pycache__" in plugins:
    plugins.remove("__pycache__")  # Better leave it here, okay?


BG = path + "etc/wp9.jpg"

BorderColor = (227, 191, 158)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(236, 200, 165), (109, 22, 25)]


Chat_BG = (52, 51, 50)

kitty_name_chatcolor = (119, 118, 22)

chat_color = (163, 156, 163)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (71, 78, 87)

button_color1 = (67, 93, 110)

kitty_picture = path + "kitty.jpg"

border_size = 5  #  pixels

kitty_image_size = (kittty_rectangle_place[2] - (border_size * 2), kittty_rectangle_place[3] - (border_size * 2))

text_box_place = (500, 550, 600, 100)

chat_box_place = (chat_rectangle_place[0] + border_size, chat_rectangle_place[1] + border_size, 600 - (border_size * 2), 500 - (border_size * 2))


text_font_size = 15
#  choose one if you want
text_font = 'URW Gothic'
#  text_font = None
#  text_font = "Noto Sans"
#  text_font = "Hack"

box_color = (176, 158, 105)


removing_speed = 0.1


notify_size = (400, 150)