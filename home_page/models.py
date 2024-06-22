from project.settings import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(60), nullable = False)
    email = database.Column(database.String(80), nullable = False)
    password = database.Column(database.String(50), nullable = False)
    admin = database.Column(database.Integer, nullable = True)

    def __repr__(self) -> str:
        return f"Користувач {self.name} з id {self.id}, email {self.email}\n"
    
class Product(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(180), nullable = False)
    price = database.Column(database.Integer, nullable = False)
    description = database.Column(database.Text, nullable = False)
    in_stock = database.Column(database.Integer, nullable = False)
    discount = database.Column(database.Integer, nullable = True)
    count = database.Column(database.Integer, nullable = True)
    
    def __repr__(self) -> str: # :cool_emoji:
        return f"Продукт {self.name} з id {self.id}"

class Cart(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    user_id = database.Column(database.Integer, nullable = False)
    products = database.Column(database.Text, nullable = True)
    name = database.Column(database.String(80), nullable = True)
    surname = database.Column(database.String(80), nullable = True)
    phone_number = database.Column(database.String(80), nullable = True)
    email = database.Column(database.String(100), nullable = True)
    city = database.Column(database.String(40), nullable = True)
    post_office = database.Column(database.String(60), nullable = True)
    additional = database.Column(database.Text, nullable = True)