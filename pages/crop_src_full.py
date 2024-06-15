import streamlit as st


st.header('Crop Recommendation App')
st.subheader('This model was trained using a dataset')
st.code('''
        ## Data Preparation
import pandas_profiling as p_prof
import pandas as pd_basic

# Display the count of unique crops
# Filter the dataset for 'mungbean'
datasetCSV = pd_basic.read_csv('crop_recom.csv')
datasetCSV.head
single_data = datasetCSV[datasetCSV['label'] == 'rice']
# # print(datasetCSV['label'].unique())
# # Display the optimal values for 'mungbean'
# print(mungbean_data.describe())
#report = p_prof.ProfileReport(datasetCSV, explorative=True)
# report
report = p_prof.ProfileReport(single_data, title="Single Crop Report", explorative=True)
report
# Machine Learning Model Training

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd

# Load the dataset
datasetCSV = pd.read_csv('crop_recom.csv')

# Preprocess the data
X = datasetCSV[['N', 'P', 'K']]
y = datasetCSV['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Define the parameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
     'kernel': ['rbf', 'poly', 'sigmoid']
}

# Create a GridSearchCV object
# grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)

# Choose a machine learning model
grid = RandomForestClassifier(n_estimators=100)

# Train the model
grid.fit(X_train, y_train)

# Print the best parameters
# print(grid.best_params_)


## Performance Test (Accuracy)
# Evaluate the model
y_pred = grid.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Use the model to make predictions
def predict_crop(N, P, K):
    return grid.predict([[N, P, K]])

# print(predict_crop(30, 70))
print(predict_crop(92, 20, 25))import streamlit as st
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
