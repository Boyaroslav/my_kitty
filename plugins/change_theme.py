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
    config.close()
    if msg[0][0] != "#":

        if os.path.exists(path + "themes" + slash + ' '.join(msg)):
            theme = open(path + "themes" + slash + ' '.join(msg), "r")
        else:
            #config.close()
            return "нет такой темы"  
        config = open(conf_path, "w")    

        #  opening theme in theme directory
        theme_data = theme.readlines()
        for i in range(0, len(config_data)):
            if "=" in config_data[i]:
                for j in theme_data:
        

                    if config_data[i][:config_data[i].index("=") - 1].strip() == j[:j.index("=") - 1].strip():
                        if j[-1] != '\n':
                            config_data[i] = j + "\n"
                        else:
                            config_data[i] = j

        config.writelines(config_data)

        theme.close()    
        config.close()
        return "конфиг изменен! Перезапустите меня :( Ну или обновите --"
    else:
        config = open(conf_path, "w")
        
        for i in range(0, len(config_data)):
            if "=" in config_data[i]:
                if config_data[i][:config_data[i].index("=") - 1] == "BG":
                    config_data[i] = "BG = '" + msg[1][:-1] + "'" + '\n'
                elif config_data[i][:config_data[i].index("=") - 1] == "BorderColor":
                    config_data[i] = "BorderColor = '" + msg[0][:-1] + "'" + '\n'
                elif config_data[i][:config_data[i].index("=") - 1] == "chat_kitty_text":
                    config_data[i] = "chat_kitty_text = '" + msg[2][:-1]  + "'" + "\n"
                elif config_data[i][:config_data[i].index("=") - 1] == "chat_color":
                    config_data[i] = "chat_color = '" + msg[3][:-1] + "'\n"
                elif config_data[i][:config_data[i].index("=") - 1] == "kitty_name_chatcolor":
                    config_data[i] = "kitty_name_chatcolor = '" + msg[4][:-1] + "'\n"
                elif config_data[i][:config_data[i].index("=") - 1] == "button_color1":
                    config_data[i] = "button_color1 = '" + msg[5][:-1] + "'\n"
                elif config_data[i][:config_data[i].index("=") - 1] == "box_color":
                    config_data[i] = "box_color = '"  + msg[6][:-1] + "'\n"
                elif config_data[i][:config_data[i].index("=") - 1] == "clock_colors":
                    config_data[i] = 'clock_colors = ["' + msg[1][:-1] + '", "' + msg[7][:-1] + '"]\n'
                elif config_data[i][:config_data[i].index("=") - 1] == "top_color":
                    config_data[i] = "top_color = '" + msg[8][:-1] + "'\n"

                
        config.writelines(config_data)
        config.close()



def answer(msg, **args):
    msg = msg.split()
    if ' '.join(msg[:2]) in ["установи тему", "set theme"]:
        
        if len(msg) == 2:
            from . import my_plugs_themes
            return my_plugs_themes.answer("themes")
            

        x = change_config(msg[2:])
        return x

