# Importing required libraries
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import streamlit as st

nltk.download('punkt')

st.title("Advanced News Article Summarizer")

projectAbout = '<span style="font-family:sans-serif; color:Blue; font-size:25px font-weight:20;">Here You can summarize any article by just entering URL</span>'
st.markdown(projectAbout, unsafe_allow_html=True)



url = st.text_input("Paste the URL of article")

btn = st.button('Summarize')

if(btn):
    if(len(url) > 0):
        article = Article(url)
        if(article.is_valid_url()):
            article.download()
            article.parse() 
            article.nlp()
            title = article.title
            authors = article.authors
            publish_date = article.publish_date
            summary = article.summary
            keywords = article.keywords
            analysis  = TextBlob(article.text)
            sentiment_Score = analysis.polarity

            st.header("Your Summary")
            
            st.subheader("Title: ")
            titleContainer = st.container()
            titleContainer.write(title)

            
            st.subheader("Publish Date: ")
            st.text(publish_date)

            st.subheader("Authors: ")
            if(len(authors) > 0):
                st.text(authors[0])
            else:
                st.text("Author name not given.")
            
            st.subheader("Summary of article: ")
            container = st.container()
            container.write(summary)

            if(sentiment_Score > 0):
                positive = '<span style="font-family:sans-serif; color:Green; font-size:15px font-weight:20;">POSITIVE</span>'
                st.markdown(f"Sentiment of the article: {positive}", unsafe_allow_html=True)
            elif(sentiment_Score < 0):
                negative = '<span style="font-family:sans-serif; color:Red; font-size:15px font-weight:20 margin-top:0.5px;">NEGATIVE</span>'
                st.markdown(f"Sentiment of the article: {negative}", unsafe_allow_html=True)
            else:
                neutral = '<span style="font-family:sans-serif; color:Orange; font-size:15px font-weight:20 margin-top:0.5px;">NEUTRAL</span>'
                st.markdown(f"Sentiment of the article: {neutral}", unsafe_allow_html=True)

            st.subheader("Keywords: ")
            keyContainer = st.container()
            keyContainer.write(keywords)

        else:
            st.error("Please Enter Valid URL")







