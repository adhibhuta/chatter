from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer # Method to train the chatbot
from chatterbot import ChatBot #Import the chatbot

chatbot = ChatBot('bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english.conversations', 'chatterbot.corpus.custom')



while True:
	request = input('You: ')
	response = chatbot.get_response(request)
	print(response.confidence)
	print('SCPay: {}'.format(response))
