"""
    CommunistBadger v1.0.0
    This is the code for the predicting the sentiment from news scrapped from news sources.
"""

from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import numpy as np
import re
import pandas as pd
import glob
import matplotlib.pyplot as plt



class SentimentNews():
    def __init__(self, article_name):
        self.articles = []
        self.pos_list = []
        self.neg_list = []
        self.coeff = 0.01
        self.article_name = article_name
        self.file_name = "Articles/"
        self.model = load_model('Models/conv-1D-1.6-weights.h5')
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.max_features = 400000  # vocabulary size

    def cleansing(self, article):
        article.lower()
        article = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', article)
        article = re.sub('@[^\s]+', ' ', article)
        article = re.sub('[\s]+', ' ', article)
        article = re.sub(r'#([^\s]+)', r'\1', article)
        article = re.sub(r'\W*\b\w{1,3}\b', '', article)
        return article

    def parse_news(self):
        for ix in glob.glob(self.file_name+"*.csv"):
            if self.article_name in ix:
                data_frame = pd.read_csv(ix)
        articles = data_frame['Article']
        for article in articles:
            self.articles.append(self.cleansing(article))

    def get_sentiment(self):
        self.parse_news()
        tokenizer = Tokenizer(num_words=40000)
        tokenizer.fit_on_texts(self.articles)
        tokenizer_padded = tokenizer.texts_to_sequences(self.articles)
        x = np.array(sequence.pad_sequences(tokenizer_padded, maxlen=20, padding='post'))
        out = self.model.predict_classes(x, batch_size=1)
        flat_out = [y for x in out for y in x]
        pos_count = 0; neg_count = 0
        for index in range(len(flat_out)):
            if flat_out[index] == 1:
                pos_count += 1
                self.pos_list.append(self.articles[index])
            else:
                neg_count += 1
                self.neg_list.append(self.articles[index])
        assert pos_count + neg_count == len(flat_out)
        return pos_count, neg_count, len(flat_out), flat_out

    def graph_sentiment(self):
        pos_count, neg_count, total_count, sentiments = self.get_sentiment()
        if total_count > 20:
            objects = tuple(x for x in range(20))
            y_pos = np.arange(20)
            plt.bar(y_pos, sentiments[:20], align='center', alpha=0.5)
        else:
            objects = tuple(x for x in range(total_count))
            y_pos = np.arange(total_count)
            plt.bar(y_pos, sentiments, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Sentiment')
        plt.xlabel('Article Count')
        plt.title('News Sentiment Graph for {}'.format(self.article_name))
        plt.savefig('sentiment_results_news_{}.png'.format(self.article_name))

    def compute_score(self):
        pos_count, neg_count, total_count, _ = self.get_sentiment()
        pos_percentage = (pos_count / total_count)
        neg_percentage = (neg_count / total_count)
        if pos_percentage > neg_percentage:
            neg_percentage *= self.coeff
        else:
            pos_percentage *= self.coeff
        return pos_percentage, neg_percentage
