# importing libraries

from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from functions import *
import pickle

# Page title

image = Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/image7.png')

st.image(image, use_column_width= True)

st.write('''
# Cyberbulling Tweet Recognition App

This app predicts the nature of the tweet into 6 Categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying

***
''')

# Text Box
st.header('Enter Tweet ')
tweet_input = st.text_area("Tweet Input", height= 150)
print(tweet_input)
st.write('''
***
''')

# print input on webpage
st.header("Entered Tweet Text ")
if tweet_input:
    tweet_input
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')

# Output on the page
st.header("Prediction")
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    if prediction == "Age":
        image1=Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/age.png')
        st.image(image1, use_column_width= True)
        #st.image('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/image7.png',use_column_width= True)
        st.write('age_cyberbullying')
    elif prediction == "Ethnicity":
        image2=Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/ethi.png')
        st.image(image2, use_column_width= True)
        #st.image("C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/ethnicity_cyberbullying.png")
        st.write('ethnicity_cyberbullying')
    elif prediction == "Gender":
        image3=Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/gen.png')
        st.image(image3, use_column_width= True)
        #st.image("C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/gender_cyberbullying.png",use_column_width= True)
        st.write('Gender_cyberbullying')
    elif prediction == "Not Cyberbullying":
        image4=Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/not_cyberbullying.png')
        st.image(image4, use_column_width= True)
        #st.image("C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/not_cyberbullying.png",use_column_width= True)
        st.write('Not Cyberbullying')
    elif prediction == "Other Cyberbullying":
        image5=Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/cyberbully.png')
        st.image(image5, use_column_width= True)
        #st.image("C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/other_cyberbullying.png",use_column_width= True)
        st.write('Other_cyberbullying')
    elif prediction == "Religion":
        image6=Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/rel.png')
        st.image(image6, use_column_width= True)
        #st.image("C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/religion_cyberbullying.png",use_column_width= True)
        st.write('Religion_cyberbullying')
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')

st.write('''***''')

# Project objective
st.write(
    """# Project Motivation
    Our project was born out of a deep concern for the well-being of individuals who have been victimized by cyberbullying. With the increasing use of technology in our daily lives,
    the prevalence of cyberbullying has also risen, leaving countless individuals feeling isolated, anxious, and helpless. We understand that this issue is not one that can be resolved overnight, 
    but we remain committed to providing a safe and supportive platform that empowers individuals to combat cyberbullying. Our team has worked tirelessly to create a user-friendly website that is 
    both informative and engaging, featuring resources and tools that enable victims to take control of their situation and seek the help they need. Through our project, we hope to raise awareness of the 
    damaging effects of cyberbullying and inspire positive change in the digital community. """
)
image7 = Image.open('C:/Users/Pc/Documents/GitHub/cyberbullying-tweet-recognition-app/images/R.png')

st.image(image7, use_column_width= True)
# About section
expand_bar = st.expander("About")
expand_bar.markdown('''
* **Created By:** [https://www.linkedin.com/in/srishrachamalla-28b177194],[https://www.linkedin.com/in/naman-jaiswal-b94883193],[https://www.linkedin.com/in/rishab-reddy-53622a193]
* **Source Code:** [https://github.com/srishrachamalla7)
* **Dataset:** [https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')


