from random import choice

'''
Bobylev Yaroslav 2022
github - https://github.com/Boyaroslav
'''

def answer(msg, *args):


    what_are_you_doing = ["что делаешь?", "что делаешь", "what are you doing", "what are you doing?"]

    what_are_you_doing_answer = ["общаюсь с тобой ; )", "разговариваю с тобой", "сижу в твоём гаджете"]

    compliments = ["i love you", "я тебя люблю", "ты", "мне нравится с тобой общаться"]

    compliments_answer = ["спасибо (*^.^*)", "благодарю (//ω//)"]

    sadness = ["я скучаю", "мне не хватает тебя", "мне грустно", "я грущу", "скучно"]

    sadness_answer = ["надеюсь, тебе нравится с тобой общаться (´• ω •)", "постараюсь помочь тебе", "постараюсь сделать тебе приятно ( ´•=´• *)"]

    what_are_you_feeling = ["что ты чувствуешь?", "what are you feeling", "как настроение", "как самочувствие"]

    what_are_you_feeling_answer = ["когда я с тобой, я рада", "мне хорошо с тобой", "у меня все хорошо\( ˘ . ˘ )/"]

    if msg.lower() in what_are_you_doing:
        return choice(what_are_you_doing_answer)

    for i in compliments:
        if i in msg.lower():
            return choice(compliments_answer)

    for i in sadness:
        if i in msg.lower():
            return choice(sadness_answer)

    for i in what_are_you_feeling:
        if i in msg.lower():
            return choice(what_are_you_feeling_answer)

    