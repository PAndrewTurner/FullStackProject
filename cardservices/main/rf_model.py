import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import warnings
import pickle as pk
from django.shortcuts import render, redirect

def process_data(credit_profile):
    # Extracting data
    data = {
        'no_of_dependents': [credit_profile.no_of_dependents],
        'education': [credit_profile.education],
        'self_employed': [credit_profile.self_employed],
        'annual_income': [credit_profile.annual_income],
        'loan_amount': [credit_profile.loan_amount],
        'credit_score': [credit_profile.credit_score],
        'res_assets': [credit_profile.res_assets],
        'com_assets': [credit_profile.com_assets],
        'bank_assets': [credit_profile.bank_assets],
        'total_assets': [credit_profile.total_assets]
    }

    df = pd.read_csv('loan_approval_dataset.csv')

    test = pd.DataFrame(data)

    #test[self_employed] = df[self_employed].replace({'Yes': 1, 'No': 0})
    #df[self_employed] = df[self_employed].replace({'Yes': 1, 'No': 0})
    
    warnings.simplefilter(action='ignore', category=FutureWarning)

    for col in df.columns:
        df[col] = df[col].replace({'Yes': 1, 'No': 0})
    
    for col in test.columns:
        test[col] = test[col].replace({'Yes': 1, 'No': 0})
    
    df.dropna()

    x = 0
    y = df.shape[0]-1

    df = df.drop('loan_id', axis=1)

    df = df.drop('self_employed', axis=1)
    test = test.drop('self_employed', axis=1)

    # print(df.columns)
    df_train = pd.get_dummies(df)
    # print(df_train.columns)
    for col in df_train.columns:
        df_train[col] = df_train[col].replace({'Yes': 1, 'No': 0})
    
    labels = np.array(df_train['loan_status'])
    df_train = df_train.drop('loan_status', axis=1)
    # feature_list = list(df_train.columns)
    
    df_train = np.array(df_train)

    train_features, test_features, train_labels, test_labels = train_test_split(df_train, labels, test_size=0.2, random_state=42)

    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    rf.fit(train_features, train_labels)
    pk.dump(rf, open("model.pkl", 'wb'))

    model = pk.load(open("model.pkl", 'rb'))

    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    # print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

    # test = pd.read_csv('test.csv')
    test = np.array(test)
    y_pred = model.predict(test)
    # print(y_pred)
    if y_pred > 0.50:
        message = "Approved"
    else:
        message = "Denied"

    return y_pred, message