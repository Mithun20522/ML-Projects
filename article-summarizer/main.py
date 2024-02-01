# Importing required libraries
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# nltk.download('punkt')

url = 'https://www.livemint.com/politics/news/hemant-soren-news-jharkhand-news-hemant-soren-party-kalpana-soren-hemant-soren-wife-jharkhand-cm-hemant-soren-11706693857857.html'
# url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

article = Article(url)
article.download()
article.parse()

article.nlp()

print(f"Title: {article.title}")
print(f"Authors: {article.authors}")
print(f"Publication Date: {article.publish_date}")
print(f"Summary: {article.summary}")
