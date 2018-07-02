
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,  SubmitField

class PitchForm(FlaskForm):
    title = StringField('Pitch Name', validators = [Required()])
    post = TextAreaField('Pitch', validators = [Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    review = TextAreaField('Comments', validators = [Required()])
    submit = SubmitField('Submit')
