from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class Problema(FlaskForm):
    honorario=FloatField("Honorarios", validators=[DataRequired()])
    submit=SubmitField("Calcular honorarios")
