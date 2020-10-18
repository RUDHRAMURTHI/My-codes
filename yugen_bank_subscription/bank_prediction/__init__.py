import os
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb035d9e3ac1d65c1c37a4af8aa31b1e'
filename = os.path.join(app.root_path, 'static', 'dummies_tranformation.sav')

from bank_prediction import routes



