import streamlit as st


st.header('Simple Sentiment Analyzer App')
st.subheader('This python code is implemented for Streamlit')
st.code('''
        import streamlit as st
        import pandas as pd
        import pickle
        from nltk.corpus import names

        st.title("A Simple Sentiment Analyzer")
        message = st.text_input("Tell me what you feel today: ")

        # Load the trained Naive Bayes classifier from the saved file
        filename = 'pages/sentimentAnalyzerTest_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))

        # Define features (words) and their corresponding labels (positive/negative)
        def word_features(words):
            return dict([(word, True) for word in words])

        message_tone = loaded_model.classify(word_features(message.split()))

        # make a function for your button click

        def sayFeeling():
            # Classify the sentiment
            if message_tone == 'positive':
                st.write("this is :smile:")
            else:
                st.write("this is :disappointed:")
                
        st.button('Say it', on_click=sayFeeling)
    ''')
