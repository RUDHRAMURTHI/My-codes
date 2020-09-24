from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb035d9e3ac1d65c1c37a4af8aa31b1e'

from cseothirdparytemplate import routes
