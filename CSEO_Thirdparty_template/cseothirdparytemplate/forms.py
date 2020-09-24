from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, ValidationError
import pandas as pd


class UploadFile(FlaskForm):
    app_name = StringField('Application Name (Required)', validators=[DataRequired()])
    file = FileField('Upload Your File (Required)', validators=[FileRequired(), FileAllowed(['xlsx'],
                                                                                            "Invalid file format, "
                                                                                            "allowed format "
                                                                                            "is: .xlsx")])
    submit = SubmitField('Submit')

    def validate_file(self, file):
        data = pd.read_excel(file.data)
        req_columns = {'ID', 'Title', 'Repro Steps', 'Severity', 'State', 'Tags'}
        data_columns = set(data.columns)
        if req_columns != data_columns:
            raise ValidationError('The uploaded file contains unwanted columns or does not contains required columns, '
                                  'Please visit the Instructions page for help!')


class DownloadFile(FlaskForm):
    submit = SubmitField('Download Template')
