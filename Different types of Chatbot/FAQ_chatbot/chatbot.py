# import 
import numpy as np
import nltk 
import tflearn 
import tensorflow 
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import random
import json
import pickle

with open("intents.json") as file:
    data = json.load(file)

try: 
    # if the data is already saved then it runs the save data
    with open('data.pickle', 'rb') as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    for intent in data['intents']:
        for pattern in intent['patterns']:
            ## seprating the word into a list 
            wrds = nltk.word_tokenize(pattern)
            ## adding all to the list
            words.extend(wrds)
            ## append the tokenize words
            docs_x.append(wrds)
            ## append the tag of the intent
            docs_y.append(intent['tag'])
        if intent['tag'] not in labels:
            labels.append(intent['tag'])
    ## lowering the words to avoid confusing
    ## removing the ? 
    words = [stemmer.stem(w.lower()) for w in words if w not in '?']
    ## Removing all the duplicates
    words = sorted(list(set(words)))

    labels = sorted(labels)

    ## creating a bagged of words in binary to train the model 
    ## So we can do one hot-encoding with the words
    training = []
    output = []

    ## list of tags into one hot-encoding
    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w) for w in doc]

        for w in words: 
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1
        training.append(bag)
        output.append(output_row)
    ## switching the list into an array for input into a model
    training = np.array(training)
    output = np.array(output)
    ## saving the preprocessing 
    with open('data.pickle', 'wb') as f:
        pickle.dump((words, labels, training, output), f)
## defines the input shape for the model
net = tflearn.input_data(shape = [None, len(training[0])])
## adding to the neural network to 2 hidden layers 
## more hidden layers for more complex problem
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
## output layers activation will allow us to get probablity for each neuron.
net = tflearn.fully_connected(net, len(output[0]), activation = 'softmax')
net = tflearn.regression(net)
## Deep Neural Networl model
model = tflearn.DNN(net)
try:
    model.load('model.tflearn')
except:
    model.fit(training, output, n_epoch = 1000, batch_size = 8, show_metric = True)
    model.save('model.tflearn')
    

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)

def chat():
    print('Start talking with the bot! (type q to stop) !')
    while True:
        inp = input('You: ')
        if inp.lower() == 'q':
            break
        ## it will giveout a probablity
        results = model.predict([bag_of_words(inp,words)])[0]
        ## gives an index of the largest probablity, so you can display the best answer
        results_index = np.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.7:
            for tg in data['intents']:
                if tg['tag'] == tag:
                    responses = tg['responses']

            print(random.choice(responses))
        else: 
            print("I didn't really get that, I still need to improve!!!")
chat()