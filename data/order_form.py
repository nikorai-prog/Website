from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, Form, IntegerField, FormField, TelField, widgets, DateField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers
from sqlalchemy_utils import PhoneNumberType


class OrderForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    middle_name = StringField('Отчество')
    email = EmailField('E-mail', validators=[DataRequired()])
    # phone = PhoneNumberType('Телефон', validators=[DataRequired()])
    #phone = TelField('Телефон', validators=[DataRequired()])
    telep = IntegerField(widget=widgets.Input(input_type="tel"))
    dead_name = StringField('Имя', validators=[DataRequired()])
    dead_surname = StringField('Фамилия', validators=[DataRequired()])
    dead_middle_name = StringField('Отчество')
    birthday = DateField('День рождения')
    deathday = DateField('День рождения')
    text = BooleanField('Текст')
    photo = BooleanField('Фотография')
    ornament = BooleanField('Орнамент по бокам керамики', default=True)

    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')