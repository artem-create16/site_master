from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired
import enum


class Place(enum.Enum):
    windows_doors = 'Рольставни на окна и двери'
    garage = 'Рольставни на гараж'
    veranda = 'Рольставни на веранду'
    home = 'Рольставни на дом'
    toilet = 'Рольставни в ванную'
    shop = 'Роллеты в магазин'


class Kind(enum.Enum):
    foam = 'Пенозаполненный'
    anti_vandal = 'Антивандальный'
    lattice = 'Решетчатый'
    steel = 'Стальной'
    steel_lattice = 'Стальной решетчатый'
    transparent = 'Прозрачный'


class Control(enum.Enum):
    crank = 'Ручной воротковатый'
    spring = 'Ручной пружинный'
    auto = 'Автоматический с пульта'


class Services(enum.Enum):
    buy = 'Покупка рольставни'
    deliver = 'Доставка рольставни'
    mounting = 'Монтаж рольставни'
    automation = 'Автоматизация рольставни'


class CalculatorForm(FlaskForm):
    place = RadioField('Place', choices=[place.name for place in Place])
    size = StringField('Size', validators=[DataRequired()])
    kind = RadioField('Kind', choices=[kind.name for kind in Kind])
    control = RadioField('Control', choices=[control.name for control in Control])
    services = SelectMultipleField('Services', choices=[service.name for service in Services])
    name = StringField('Size', validators=[DataRequired()])
    number = StringField('Size', validators=[DataRequired()])
    submit = SubmitField('Go')
