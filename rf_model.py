import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import warnings
import pickle as pk

warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('loan_approval_dataset.csv')

df.dropna()

x = 0
y = df.shape[0]-1

df = df.drop('loan_id', axis=1)

print(df.columns)
df_train = pd.get_dummies(df)
print(df_train.columns)

labels = np.array(df_train['loan_status'])
df_train = df_train.drop('loan_status', axis=1)
feature_list = list(df_train.columns)
df_train = np.array(df_train)

train_features, test_features, train_labels, test_labels = train_test_split(df_train,
                                                                            labels, test_size=0.2, random_state=42)

rf = RandomForestRegressor(n_estimators=1000, random_state=42)
rf.fit(train_features, train_labels)
pk.dump(rf, open("model.pkl", 'wb'))

model = pk.load(open("model.pkl", 'rb'))

predictions = model.predict(test_features)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

test = pd.read_csv('test.csv')
test = np.array(test)
y_pred = model.predict(test)
print(y_pred)
if y_pred > 0.50:
    print("Congratulations, you've been approved!")
else:
    print("Sorry, you were not approved for this service.")
