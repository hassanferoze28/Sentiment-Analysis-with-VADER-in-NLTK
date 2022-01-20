#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[42]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics
import os


# In[43]:


import nltk
nltk.download('vader_lexicon')


# # Input the Poems Datasets

# In[44]:


Poems = []
Pnames = []


# In[45]:


os.getcwd()
os.chdir('C:/Users/muham/OneDrive/Desktop/textdata')
os.getcwd()
fo = open("Shakespeare_Blow, Blow, Thou Winter Winda.txt","r", encoding = 'utf-8')
Poems.append(fo.read())
Pnames.append(os.path.basename(fo.name))
fo = open("Shakespeare_Sonnet 130.txt","r", encoding = 'utf-8')
Poems.append(fo.read())
Pnames.append(os.path.basename(fo.name))
fo = open("Shakespeare_Juliet's Soliloquy.txt","r", encoding = 'utf-8')
Poems.append(fo.read())
Pnames.append(os.path.basename(fo.name))
fo = open("Shakespeare_Fear No More.txt","r", encoding = 'utf-8')
Poems.append(fo.read())
Pnames.append(os.path.basename(fo.name))
fo = open("Shakespeare_A Fair Song.txt","r", encoding = 'utf-8')
Poems.append(fo.read())
Pnames.append(os.path.basename(fo.name))


# In[46]:


Poems


# In[47]:


Pnames


# # (1.1) Getting a score of Overall Sentiment of Entire Text

# In[58]:


def get_sentiment_Poems(Poem):
#input: no of texts with multiple sentences
#usage: sentiment analysis with nltk_vader
#return: score of overall sentiment
    scores = []
    compound = []
    # tokenize the text into sentences
    sentences = nltk.sent_tokenize(Poem)
    sid = SentimentIntensityAnalyzer()
    
    for sent in sentences:
        scores.append(sid.polarity_scores(sent))
    for score in scores:
        compound.append(score["compound"])
    return statistics.mean(compound)    
    
    


# In[59]:


#get sentiments
scores = []
for Poem in Poems:
    scores.append(get_sentiment_of_poems(Poem))
    print(get_sentiment_of_poems(Poem))


# # (1.2) Rank Sentiment from positive to negative

# In[60]:


dict = {}
i = 0
for score in scores:
    dict[Pnames[i]] = score
    i = i + 1


# In[61]:


dict


# In[62]:


#Rank sentiments from positive to negative
from operator import itemgetter
sorted(dict.items(), key = itemgetter(1), reverse = True)


# # (1.4)

# Shakespeare_Juliet's Soliloquy is talking about his lost love, death, getting married at the wrong time so these sentiments are correctly stated as the lowest negative whereas Shakespeare_Sonnet is praising the beauty of his Mistress so sentiments are positive.
# 
# The statistics method i used was MEAN as it evenly distribute the scores across the documents.
# 
# Sentiment scores and analysis can be used for newspaper Articles related different companies for investment decisions based on the overall sentiments.
