import os
from flask import render_template, redirect, url_for, request, send_file
from bank_prediction.forms import Prediction, Batch_Prediction
import pandas as pd
import joblib
from bank_prediction.modal import single_predict, batch_predict
from bank_prediction import app, filename


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = Prediction()
    if form.validate_on_submit():
        df = joblib.load(filename)
        df1 = pd.get_dummies(
            pd.DataFrame({'age': [form.age.data], 'job': [form.job.data], 'marital': [form.marital.data],
                          'education': [form.education.data], 'default': [form.default.data],
                          'balance': [form.balance.data],
                          'housing': [form.housing.data], 'loan': [form.loan.data], 'contact': [form.contact.data],
                          'day': [form.day.data], 'month': [form.month.data], 'duration': [form.duration.data],
                          'campaign': [form.campaign.data], 'pdays': [form.pdays.data],
                          'previous': [form.previous.data],
                          'poutcome': [form.poutcome.data]}))
        data = df1.reindex(columns=df.columns, fill_value=0)
        path = os.path.join(app.root_path, 'static', 'Bank_Full_Cleaned.csv')
        NewData = pd.read_csv(path)
        prediction = single_predict(data, NewData)
        return redirect(url_for('result', prediction=prediction))
    return render_template('home.html', title='Home', form=form)


@app.route('/result/<int:prediction>', methods=['GET', 'POST'])
def result(prediction):
    return render_template('result.html', title='Result', prediction=prediction)


@app.route('/batch', methods=['GET', 'POST'])
def batch():
    form = Batch_Prediction()
    if request.method == 'POST':
        data = pd.read_csv(form.file.data)
        path = os.path.join(app.root_path, 'static', 'Bank_Full_Cleaned.csv')
        NewData = pd.read_csv(path)
        batch_predict(data, NewData)
        path = os.path.join('static/data', 'Bank_batch_prediction.xlsx')
        return send_file(path, as_attachment=True)
    return render_template("batch.html", title="Batch-Prediction", form=form)
