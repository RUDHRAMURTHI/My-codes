from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
import pandas as pd
import os
from bank_prediction import app


def single_predict(data, NewData):
    NewData['default'] = NewData['default'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['housing'] = NewData['housing'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['loan'] = NewData['loan'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['y'] = NewData['y'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['job'] = NewData['job'].str.replace('.', '')
    X = NewData.drop(['y'], axis=1)
    X = pd.get_dummies(X)
    y = NewData['y']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=50)
    sm = SMOTE(random_state=50)
    X_train, y_train = sm.fit_sample(X_train, y_train)
    clf = XGBClassifier()
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    print('F1Score:', f1_score(y_test, pred))
    print('Accuracy:', accuracy_score(y_test, pred))
    print('Precision:', precision_score(y_test, pred))
    print('Precision:', recall_score(y_test, pred))
    prediction = clf.predict(data)
    return prediction[0]


def batch_predict(data, NewData):
    NewData['default'] = NewData['default'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['housing'] = NewData['housing'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['loan'] = NewData['loan'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['y'] = NewData['y'].apply(lambda x: 0 if x == 'no' else 1)
    NewData['job'] = NewData['job'].str.replace('.', '')
    X = NewData.drop(['y'], axis=1)
    X = pd.get_dummies(X)
    y = NewData['y']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=50)
    sm = SMOTE(random_state=50)
    X_train, y_train = sm.fit_sample(X_train, y_train)
    clf = XGBClassifier()
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    print('F1Score:', f1_score(y_test, pred))
    print('Accuracy:', accuracy_score(y_test, pred))
    print('Precision:', precision_score(y_test, pred))
    print('Precision:', recall_score(y_test, pred))
    prediction = clf.predict(data)
    batch = pd.DataFrame(columns=['S.no', 'Prediction'])
    batch['S.no'] = range(1, len(prediction) + 1)
    batch['Prediction'] = prediction
    path = os.path.join(app.root_path, 'static/data', 'Bank_batch_prediction.xlsx')
    batch.to_excel(path, index=False)
