from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Upload(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    file = FileField('Text File', validators=[
        FileRequired(),
        FileAllowed(['txt'], '*.txt file only') ])
    submit = SubmitField('Загрузить')
    #title = 'Uploading...'

    
