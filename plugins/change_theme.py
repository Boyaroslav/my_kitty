def change_config(msg):
    import os
    #  getting absolutr path ans opening config.py file
    
    if "/" in os.path.abspath(__file__):
        slash = "/"
    else:
        slash = "\\"
    path = os.path.abspath(__file__)
    index = -1
    while path[index] != slash:
        index -= 1
    path = str(path[:index])
    path = path[:path.index("plugins")]
    conf_path = path + "config.py"
    config = open(conf_path, "r+")
    config_data = config.readlines()

    #  opening theme in theme directory
    print(path + "/themes/" + ' '.join(msg))
    if os.path.exists(path + "themes" + slash + ' '.join(msg)):
        theme = open(path + "themes" + slash + ' '.join(msg), "r")
    else:
        config.close()
        return "нет такой темы"
    theme_data = theme.readlines()
    # 1 - BG
    # 2 - BorderColor
    # 3 - Chat_BG
    # 4 - kitty_name_chatcolor
    # 5 - chat_kitty_text
    # 6 - button_color1
    # 7 - box_color
    # 8 - clock_colors
    # 9 - chat_color
    # 10 - kitty_name
    keys = {
            "BG":0,
            "BorderColor":1,
            "Chat_BG":2,
            "kitty_name_chatcolor":3,
            "chat_kitty_text":4,
            "button_color1":5,
            "box_color":6,
	    "clock_colors":7,
            "chat_color":8,
            "kitty_name":9
            }

    for i in range(0, len(config_data)):
        for j in keys:
            if j in config_data[i]:
                config_data[i] = str(j + " = " + theme_data[keys[j]])
                print(config_data[i])
    config.writelines(config_data)

    theme.close()    
    config.close()
    return "конфиг изменен! Перезапустите меня :("


def answer(msg):
    msg = msg.split()
    if ' '.join(msg[:2]) in ["установи тему", "set theme"]:
        x = change_config(msg[2:])
        return x