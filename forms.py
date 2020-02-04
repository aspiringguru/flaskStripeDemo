from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError


class ContactForm(Form):
   name = TextField("Name Of Student")
   submit = SubmitField("Send")
