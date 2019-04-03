from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer # Method to train the chatbot
import os
from chatterbot import ChatBot #Import the chatbot

chatbot = ChatBot('bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english.conversations', 'chatterbot.corpus.custom')

data_path = '/home/debjyoti/Dev/chatterbot-corpus/chatterbot_corpus/data/english/'


''' 
for files in os.listdir(data_path):
	conversation = open(data_path+files,'r').readlines()
	print(conversation)
	trainer.train(conversation)
'''

#conversation = open('chat.txt', 'r').readlines()

#chatbot.set_trainer(ListTrainer) # There are other trainers as well go through them once

#chatbot.train(conversation)



while True:
	request = input('You: ')
	response = chatbot.get_response(request)
	print(response.confidence)
	print('SCPay: {}'.format(response))
