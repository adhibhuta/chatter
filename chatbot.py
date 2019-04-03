from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_response(usrText):
    bot = ChatBot('bot')
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break
        

        
