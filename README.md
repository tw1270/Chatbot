# Why your business needs a Chatbot? 
**Tenzin Wangdu** 

May 03, 2021

## Table of Contents
---
- [Background](#Background)
- [Problem Statement](#Problem-Statement)
- [Different methods](#Different-methods)
    - [Creating your own data/intents](#Creating-your-own-data/intents)
    - [RASA Framework](#RASA-Framework)
    - [Creating your own framework](#Creating-your-own-framework)
        -[EDA/Preprocessing the Customer Tweet](#EDA/Preprocessing-the-Customer-Tweet)
        -[Creating Intents](#Creating-Intents)
        -[Modeling](#Modeling)
- [Overall Conclustion](#Overall-Conclusion)
- [Areas for Further Research](#Areas-for-Further-Research)
        


## Background
---
* First Chatbot was developed in 1966 at MIT called ELIZA
* ELIZA was simple decision tree questions that answer a few questions
* Now it is developed into everyday life with messenger apps, voice assistant
* Chatbots are quickly replacing human for technical support and customer service

## Problem Statement
---
Every business needs a chatbot for their website or app. Chatbot can replace a customer service agents for a 24 hour services and help business save money

## Different methods
---
#### Creating your own data/intents
* Intents are categories of the text of user’s input
* Ex: ‘Hi’ would be a greeting, ‘how can you help me?’ would be a help intents
* Creating different intent  for different purpose 
* It is Great for FAQ and easy to create
* Creating different responses to those intents

#### RASA Framework
* Creating Intents
* Allows us create a storyline and it can store the previous answers 
* So, the bot can continue a conversation

#### RASA Pipeline
* Whitespace Tokenizer (using whitespaces as a separator)
* Count Vectors Featurize(Creates bag-of-words representation of user messages, intents, and responses) 
* N-gram from 1-4
* NLU model (Natural language understanding)

#### Creating your own framework
* Data: Twitter Customer Service Tweets(3.8 millions tweets)

##### EDA/Preprocessing the Customer Tweet
* Remove all the non-english tweets
* Lemmatize
* Remove stopwords, href, @ handles
* Setting a limit on the length of the tweet at 5-40

##### Creating Intents
* The interpretation of a statement is what allows chatbot to formulate the best possible response.
* Matching tweets with the intents of the customer (Battery, Update, Macbook, and etc)

##### Modeling
* RNN Neural Network to train the model
* It had a 99.4% of train accuracy, and 93% of testing accuracy

### Overall Conclusions
---
* Chatbot allows business to be to available to customer 24x7
* Huge expense cut/Alternative to customer service if needed
* Building chatbot based on your business


### Areas for Further Research
---
* Launching my own framework
* Deploying the other model on flask and heroku
* Connected the chatbot to SQL

