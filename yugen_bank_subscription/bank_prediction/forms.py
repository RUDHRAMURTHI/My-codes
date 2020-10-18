from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, NumberRange


class Prediction(FlaskForm):
    age = IntegerField('AGE', validators=[DataRequired(), NumberRange(min=18, max=95)])
    default = SelectField('Default', choices=[(0, 'No'), (1, 'Yes')], validators=[DataRequired()])
    balance = IntegerField('Balance', validators=[DataRequired(), NumberRange(min=-8019, max=102127)])
    housing = SelectField('Housing', choices=[(0, 'No'), (1, 'Yes')], validators=[DataRequired()])
    loan = SelectField('Loan', choices=[(0, 'No'), (1, 'Yes')], validators=[DataRequired()])
    day = IntegerField('DAY', validators=[DataRequired(), NumberRange(min=1, max=31)])
    duration = IntegerField('Duration', validators=[DataRequired(), NumberRange(min=0, max=4918)])
    campaign = IntegerField('Campaign', validators=[DataRequired(), NumberRange(min=1, max=63)])
    pdays = IntegerField('Pdays', validators=[DataRequired(), NumberRange(min=-1, max=871)])
    previous = IntegerField('Previous', validators=[DataRequired(), NumberRange(max=275)])
    job = SelectField('Job', choices=[('blue-collar', 'BlueCollar'), ('management', 'Management'),
                                      ('technician', 'Technician'),
                                      ('admin', 'Admin'), ('services', 'Services'), ('retired', 'Retired'),
                                      ('self-employed', 'Self-Employed'), ('entrepreneur', 'Entrepreneur'),
                                      ('unemployed', 'UnEmployed'), ('student', 'Student'), ('unknown', 'UnKnown'),
                                      ('mgmt', 'MGMT')], validators=[DataRequired()])
    marital = SelectField('Marital', choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced')],
                          validators=[DataRequired()])
    education = SelectField('Education',
                            choices=[('secondary', 'Secondary'), ('tertiary', 'Tertiary'), ('primary', 'Primary'),
                                     ('unknown', 'UnKnown')], validators=[DataRequired()])
    contact = SelectField('Contact',
                          choices=[('cellular', 'Cellular'), ('unknown', 'Unknown'), ('telephone', 'Telephone')],
                          validators=[DataRequired()])
    month = SelectField('Month',
                        choices=[('jan', 'Jan'), ('feb', 'Feb'), ('mar', 'Mar'), ('apr', 'Apr'), ('may', 'May'),
                                 ('jun', 'Jun'), ('jul', 'Jul'), ('aug', 'Aug'), ('sep', 'Sep'), ('oct', 'Oct'),
                                 ('nov', 'Nov'), ('dec', 'Dec')], validators=[DataRequired()])
    poutcome = SelectField('Poutcome',
                           choices=[('unknown', 'Unknown'), ('failure', 'Failure'), ('other', 'Others'),
                                    ('success', 'Success')], validators=[DataRequired()])

    submit = SubmitField('Predict')


class Batch_Prediction(FlaskForm):
    file = FileField('Upload Your File for Prediction', validators=[FileRequired(), FileAllowed(['csv'],
                                                                                                "Invalid file format, "
                                                                                                "allowed format "
                                                                                                "is: .csv")])
    submit = SubmitField('Predict')
