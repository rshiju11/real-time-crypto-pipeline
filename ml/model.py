"""
model.py
ML module for crypto price prediction
"""

import numpy as np
from sklearn.linear_model import LinearRegression

"""
Prepare df for ML
Convert time into numerical index
"""

def prepare_data(df):
    df_ml = df.copy()
    df_ml["time_index"]=np.arange(len(df_ml))

    return df_ml

"""
Train linear regression model
"""
def train_model(df_ml):
    X = df_ml[["time_index"]]
    y = df_ml["price_usd"]

    model = LinearRegression()
    model.fit(X,y)

    return model

#predict next proce
def predict_next(model, df_ml):
    next_time = [[len(df_ml)]]
    prediction = model.predict(next_time)

    return prediction[0]

# prediction function to call from dashboard
def get_prediction(df):
    if len(df) < 2:
        return None
    
    df_ml = prepare_data(df)
    model = train_model(df_ml)
    prediction = predict_next(model, df_ml)

    return prediction[0]

def moving_average_prediction(df, window=5):
    if len(df) < window:
        return None
    
    return df["price_usd"].tail(window).mean()

