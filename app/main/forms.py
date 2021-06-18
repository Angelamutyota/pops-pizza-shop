from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,RadioField, SubmitField
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')


class OrderForm(FlaskForm):
    size = RadioField('Pizza Size', choices=[('value','Large'),('value_two','Medium'),('value_two','Small')])
    toppings = RadioField('Pizza Topping', choices=[('value','Pepperoni'),('value_two','Mushroom'),('value_two','Chicken')])
    submit = SubmitField('Add to cart')


    submit = SubmitField('Save')
