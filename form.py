from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class Prediction(FlaskForm):
    bedrooms = IntegerField('Number of Bedrooms',validators=[DataRequired()])
    bathrooms= IntegerField('Number of bathrooms', validators=[DataRequired()])
    sqft_living= DecimalField('Sqft living', validators=[DataRequired()])
    sqft_lot = DecimalField('sqft lot', validators=[DataRequired()])
    floors = IntegerField('Floors', validators=[DataRequired()])
    sqft_above = DecimalField('Sqft above', validators=[DataRequired()])
    sqft_lot15 =DecimalField('sqft lot15', validators=[DataRequired()])
    yr_built = IntegerField('Year built',validators=[DataRequired()])
    condition = IntegerField('Condition',validators=[DataRequired()])
    Zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Predict')