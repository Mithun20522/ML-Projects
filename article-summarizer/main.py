# Importing required libraries
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import streamlit as st

# nltk.download('punkt')

# url = 'https://www.livemint.com/politics/news/hemant-soren-news-jharkhand-news-hemant-soren-party-kalpana-soren-hemant-soren-wife-jharkhand-cm-hemant-soren-11706693857857.html'
# # url = 'https://edition.cnn.com/2020/09/13/tech/microsoft-tiktok-bytedance/index.html'

# article = Article(url)
# article.download()
# article.parse()

# article.nlp()

# title = article.title
# authors = article.authors
# publish_date = article.publish_date
# summary = article.summary
# keywords = article.keywords

# print(f"Title: {title}")
# print(f"Authors: {authors}")
# print(f"Publication Date: {publish_date}")
# print(f"Summary: {summary}")
# print(f"Keywords: {keywords}")

# analysis  = TextBlob(article.text)

# sentiment_Score = analysis.polarity

# print(analysis.polarity)
# print(f'Sentiment: {"positive" if sentiment_Score > 0 else "negative" if sentiment_Score < 0 else "neutral"}')



st.title("Advanced News Article Summarizer")
st.text("Here You can summarize any article by just entering URL")

# new_url = st.text_input("Paste the URL")

# root = tk.Tk()
# root.title("Advanced News Article Summarizer")
# root.geometry('1200x600')

# root.mainloop()

