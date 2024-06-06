import streamlit as st


st.header('Crop Recommendation App')
st.subheader('This model was trained using a dataset')
st.code('''
        import streamlit as st
        import pandas as pd
        import pickle
        from nltk.corpus import names

        # Load the trained Naive Bayes classifier from the saved file
        filename = 'pages/crop_recom_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))

        # # Use the model to make predictions
        def predict_crop():
            st.text("The crop is " + crop_name)
            return
                
        st.title("Crop Recommendation Predictor :smile:")
        st.subheader("Enter a set of NPK levels to determine what crop best fits:")
        n_input = st.slider("Nitrogen: ",0,500)
        p_input = st.slider("Phosphorus: ",0,500)
        k_input = st.slider("Potassium: ",0,500)
        if n_input == 0 & p_input == 0 & k_input == 0:
            crop_name = ""
        else:
            crop_name = loaded_model.predict([[pd.to_numeric(n_input),pd.to_numeric(p_input),pd.to_numeric(k_input)]])

        st.text("The crop suitable for this NPK level:")
        st.text_area(label ="",value=crop_name, height =100)
    ''')
