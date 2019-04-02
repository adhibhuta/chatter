from chatterbot.trainers import ListTrainer # Method to train the chatbot

from chatterbot import ChatBot #Import the chatbot

chatbot = ChatBot('bot')

conversation = open('chat.txt', 'r').readlines()

#bot.set_trainer(ListTrainer) # There are other trainers as well go through them once

#bot.train(conversation)

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while True:
	request = input('You: ')
	response = chatbot.get_response(request)

	print('SCPay: {}'.format(response))
