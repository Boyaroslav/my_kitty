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


BG = path + "etc/spikebg.jpg"

BorderColor = (38, 23, 16)

clock_font = path + 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(161, 76, 78), (73, 58, 91)]


Chat_BG = (142, 58, 47)

kitty_name_chatcolor = (97, 207, 95)

chat_color = (138, 204, 0)

kitty_rectangle_place = (50, 50,300, 400)

kitty_name = "Spike"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 17
maxlen_message = 100

chat_kitty_text = (0, 77, 31)

button_color1 = (43, 95, 43)

kitty_picture = path + "etc/spike_image.jpg"

border_size = 5  #  pixels

kitty_image_size = (kitty_rectangle_place[2] - (border_size * 2), kitty_rectangle_place[3] - (border_size * 2))

text_box_place = (500, 550, 600, 100)

chat_box_place = (chat_rectangle_place[0] + border_size, chat_rectangle_place[1] + border_size, 600 - (border_size * 2), 500 - (border_size * 2))


text_font_size = 15
#  choose one if you want
text_font = 'URW Gothic'
#  text_font = None
#  text_font = "Noto Sans"
#  text_font = "Hack"

box_color = (254, 99, 160)


removing_speed = 0.1


notify_size = (400, 150)
