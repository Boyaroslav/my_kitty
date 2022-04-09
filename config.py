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
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)]             # (font color)(bg color)


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (255, 255, 255)

BorderColor = (0, 0, 0)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(0, 0, 0), (255, 255, 255)]


BG = (255, 255, 255)

kitty_name = "Doggy"

chat_color = (100, 100, 100)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Doggy"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
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


BG = (17, 20, 24)

BorderColor = (60, 150, 60)

clock_font = 'lcd.ttf'

clock_place = (50, 500, 300, 60)

clock_colors = [(45, 194, 126), (0, 0, 0)] 


BG = (17, 20, 24)

kitty_name = "Kitty"

chat_color = (255, 255, 255)

kittty_rectangle_place = (50, 50,300, 400)

kitty_name = "Kitty"


chat_rectangle_place = (500, 50, 600, 500)

count_messages_visible = 15
maxlen_message = 100

chat_kitty_text = (0, 50, 50)

button_color1 = (0, 100, 100)

kitty_picture = path + "/kitty.jpg"

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

box_color = (200, 255, 200)


removing_speed = 0.1
