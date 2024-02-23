import streamlit as st
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# page_bg_img="""
# <style>
# [data-testid='stAppViewContainer']{
# background_image:url("D:\SentimentalAnalysis\sa.jpg")
# background size:cover
# }
# </style>
# """

# st.markdown(page_bg_img,unsafe_allow_html=True)
st.title("Sentimental Analysis")

sentence=st.text_area("please Enter your text")

# def sentiment_score(sentence):
if st.button('Analyse'):
    so=SentimentIntensityAnalyzer()
    sentiment_dict=so.polarity_scores(sentence)
    st.write(sentiment_dict['pos']*100,'%Positive')
    st.write(sentiment_dict['neg']*100,'% Negative')
    st.write(sentiment_dict['neu']*100,'%Neutral')
    st.success(sentiment_dict)
    if sentiment_dict['compound']>=0.05:
        st.success('Positive',icon='😎')
    elif sentiment_dict['compound']<=-0.05:
        st.success('Negative',icon='☹')
    else:
        st.success('Neutral',icon='😶')
