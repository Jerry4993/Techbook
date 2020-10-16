#This mini-project about Chatbot with intents
import nltk;
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import json
import random
import tensorflow
import pickle
import tkinter as Tk


# root = Tk()                             
# user = StringVar()                          
# bot  = StringVar()                          
                                    
# root.title(" Simple ChatBot ")                  
# Label(root, text=" user : ").pack(side=LEFT)                
# Entry(root, textvariable=user).pack(side=LEFT)          
# Label(root, text=" Bot  : ").pack(side=LEFT)                
# Entry(root, textvariable=bot).pack(side=LEFT)
# Button(root, text="speak", command=main).pack(side=LEFT) 
#take out the document containing data
stemmer = LancasterStemmer()
with open("C:/Users/Jasreen/Documents/Python Scripts/chatbot_with_intents/json-file/intents.json") as f:
	data = json.load(f)

try:
	with open("data.pickle","rb") as f:
		words,labels,training,output = pickle.load(f)

except:
	words =[]
	labels = []
	data_x=[]
	data_y=[]

	#scan through the document to take out patterns and tokenize them
	#add all the tokenized words in a single list
	#split the patterns and tags(data_x and data_y)
	#take out distinct tags (labels)
	#a lexicon is created(words)
	for intent in data["intents"]:
		for pattern in intent["patterns"]:
			wrds = nltk.word_tokenize(pattern)
			words.extend(wrds)
			data_x.append(wrds)
			data_y.append(intent["tag"])

		if(intent["tag"] not in labels):
			labels.append(intent["tag"])
	words =[stemmer.stem(w) for w in words if w != "?"]
	words = sorted(list(set(words)))
	labels = sorted(labels)

	training = []
	output = []
	out_empty = [0 for _ in range(len(labels))]

	for x,doc in enumerate(data_x):
		bag = []
		wrds = [stemmer.stem(w) for w in doc]
		for w in words:
			if w in wrds:
				bag.append(1)
			else:
				bag.append(0)

		output_row = out_empty[:]
		output_row[labels.index(data_y[x])]=1

		training.append(bag)
		output.append(output_row)
		with open("data.pickle","wb") as f:
			pickle.dump((words,labels,training,output),f)

	training = numpy.array(training)
	output = numpy.array(output)


tensorflow.reset_default_graph()
net = tflearn.input_data(shape=[None,len(training[0])] )
#net - tflearn.fully_connected(net,6)
#net = tflearn.fully_connected(net,8)
net = tflearn.fully_connected(net,len(output[0]),activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)

#try:
#	model.load("model.tflearn")
#except:
model.fit(training,output,n_epoch=100,batch_size=5)
model.save("model.tflearn")

         
def bag_of_words(s,lexicon):
	bag = [0 for _ in range(len(lexicon))]
	s_words = nltk.word_tokenize(s);
	s_words = [stemmer.stem(w.lower()) for w in s_words]
	for se in s_words:
		for x,wor in enumerate(lexicon) :
			if(wor ==se):
				bag[x]=1
	return numpy.array(bag)

def chat(query):
	
	while True:
		# inp = user.get()
		inp = query
		if(inp.lower() == "quit"):
			break
		results = model.predict([bag_of_words(inp,words)])[0]
		max_pred = numpy.argmax(results)
		
		if(results[max_pred]<0.7):
			# bot.set("Sorry ! my second brain has stopped working ! please ask another question !!")

			return " Sorry ! my second brain has stopped working ! please ask another question !!"
		else :
			tag = labels[max_pred]
			for tg in data['intents']:
				if(tg['tag']== tag):
					response = tg['responses']
			# bot.set(random.choice(response))
			print("Jasreen: ",random.choice(response))
			return random.choice(response)


# mainloop()









