from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddForm(FlaskForm):
    name = StringField("Pet Name", validators =[InputRequired(message="Name cannot be blank")])
    species = SelectField("Species",
              choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )
    photo_url= StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Put a note", validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url= StringField("Photo URL", validators=[Optional()])
    notes = TextAreaField("Put a note", validators=[Optional()])
    available = BooleanField("Available?")

