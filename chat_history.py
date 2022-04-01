import config

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''


name = config.kitty_name



# you can change start message ^ ^
class History:
    def __init__(self):
        self.array = [
        [name, "Привет! Рада Тебя видеть!"]
        ]
        self.pop_last = None
    
    def send_msg(self, msg, user="you"):
        self.array.append([user, msg])
        if user == "you":
            self.pop_last(self.array[-1])

    def clear_chat_history(self):
        print(self.array)
        self.array[:]
       

    def get_history(self):
        return self.array

    def __getitem__(self, i):
        return self.array[i]

    def __len__(self):
        return len(self.array)

    
