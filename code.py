
#importing the required modules and packages.
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
#Loading the dataset using pandas.
df = pd.read_csv("IMDB-Dataset.csv")


#cleaning the text data.
import re
from wordcloud import *

def cleaning(text):
    stopwords = set(STOPWORDS)
    text = ' '.join(word for word in text.split() if word not in stopwords)
    return text

text = ' '.join(df['review'].astype(str).tolist())
text = re.sub(r'[^A-Za-z\s]', '', text)
text = text.lower()

text = cleaning(text)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text) 
plt.figure(figsize=(10, 5)) 
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis('off') 
plt.title("IMDB Movie Reviews Word Cloud") 
plt.show()