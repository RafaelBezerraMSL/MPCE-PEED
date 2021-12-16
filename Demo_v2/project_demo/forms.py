from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.choices import RadioField, SelectMultipleField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuário',validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class ProcForm(FlaskForm):
    id = StringField('ID do Procedimento', validators=[DataRequired()])
    title = StringField('Título do Procedimento', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])