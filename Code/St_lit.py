import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder, RobustScaler
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import warnings
import joblib
warnings.filterwarnings('ignore')

# Title of the Streamlit app
st.title('Suicide Rate Prediction App')

# Loading the dataset
@st.cache_resource
def load_data():
    df = pd.read_csv("Suicide Rates Overview 1985 to 2016 Data.CSV")
    df.columns = ['country', 'year', 'gender', 'age', 'suicide_count', 'population', 'suicide_rate', 'country-year', 'HDI_for_year',
                  'gdp_for_year', 'gdp_per_capita', 'generation']
    df = df.drop(['country-year', 'HDI_for_year'], axis=1)
    df['gdp_for_year'] = df['gdp_for_year'].str.replace(',', '').astype(float)
    return df

df = load_data()

# Encode categorical variables
def encode_features(df, fit=False):
    categorical = ['country', 'gender', 'age', 'generation']
    le_dict = {}
    if fit:
        for column in categorical:
            le = LabelEncoder()
            le.fit(list(df[column].unique()) + ['Unknown'])
            df[column] = le.transform(df[column])
            le_dict[column] = le
    return df, le_dict

df_encoded, label_encoders = encode_features(df, fit=True)

# Scale numerical features
def scale_features(df):
    numerical = ['suicide_count', 'population', 'gdp_for_year', 'gdp_per_capita']
    rc = RobustScaler()
    df[numerical] = rc.fit_transform(df[numerical])
    return df, rc

df_scaled, scaler = scale_features(df_encoded)

# Preparing the data for the model
X = df_scaled.drop('suicide_rate', axis=1)
y = df_scaled['suicide_rate']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Train the XGBoost model
with open('xg_boost.pkl', 'rb') as f:
    model = joblib.load(f)

# User inputs
st.sidebar.header('User Input Features')

# Function to get user input
def user_input_features():
    country = st.sidebar.selectbox('Country', df['country'].unique())
    year = st.sidebar.slider('Year', int(df['year'].min()), int(df['year'].max()), int(df['year'].min()))
    gender = st.sidebar.selectbox('Gender', df['gender'].unique())
    age = st.sidebar.selectbox('Age', df['age'].unique())
    suicide_count = st.sidebar.number_input('Suicide Count', value=int(df['suicide_count'].mean()))
    population = st.sidebar.number_input('Population', value=int(df['population'].mean()))
    gdp_for_year = st.sidebar.number_input('GDP for Year', value=int(df['gdp_for_year'].mean()))
    gdp_per_capita = st.sidebar.number_input('GDP per Capita', value=int(df['gdp_per_capita'].mean()))
    generation = st.sidebar.selectbox('Generation', df['generation'].unique())

    data = {'country': country,
            'year': year,
            'gender': gender,
            'age': age,
            'suicide_count': suicide_count,
            'population': population,
            'gdp_for_year': gdp_for_year,
            'gdp_per_capita': gdp_per_capita,
            'generation': generation}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Function to safely transform input using LabelEncoder
def safe_transform(le, value):
    try:
        return le.transform([value])[0]
    except ValueError:
        return le.transform(['Unknown'])[0]

# Function to apply encoding and scaling transformations
def transform_input(input_df, label_encoders, scaler):
    input_encoded = input_df.copy()
    for column in ['country', 'gender', 'age', 'generation']:
        input_encoded[column] = input_encoded[column].apply(lambda x: safe_transform(label_encoders[column], x))
    
    # Scale numerical features based on the scaler from training
    numerical_features = ['suicide_count', 'population', 'gdp_for_year', 'gdp_per_capita']
    input_encoded[numerical_features] = scaler.transform(input_encoded[numerical_features])
    
    return input_encoded

# Display user input features with original values
st.subheader('User Input features')
st.write(input_df)

# Button to submit user inputs and predict the suicide rate
if st.button('Predict Suicide Rate'):
    # Transform inputs for prediction
    input_encoded = transform_input(input_df, label_encoders, scaler)

    # Predict and display the output
    prediction = model.predict(input_encoded)

    st.subheader('Predicted Suicide Rate')
    st.write(prediction[0])
