from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,RadioField, SubmitField
from wtforms.validators import Required

class OrderForm(FlaskForm):
    size = RadioField('Size', choices=[('value','Large'),('value_two','Medium'),('value_two','Small')])
    toppings = StringField('Pizza', validators = [Required()])