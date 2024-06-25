import flask  # Імпорт бібліотеки Flask / Import the Flask library
from flask_login import current_user, UserMixin  # Імпорт поточного користувача та UserMixin з flask_login / Import current user and UserMixin from flask_login
from home_page.models import Product, Cart  # Імпорт моделей Product та Cart з модуля home_page / Import the Product and Cart models from the home_page module
from project.settings import database  # Імпорт налаштувань бази даних з проекту / Import the database settings from the project

def show_shop_page():  # Визначення функції для показу сторінки магазину / Define a function to show the shop page
    if isinstance(current_user, UserMixin):  # Перевірка, чи поточний користувач є екземпляром UserMixin / Check if the current user is an instance of UserMixin
        products = Product.query.all()  # Отримання всіх продуктів з бази даних / Get all products from the database
        # Повернення шаблону сторінки магазину з переданими параметрами / Return the shop page template with passed parameters
        return flask.render_template(
            template_name_or_list='shop.html',  # Назва шаблону для сторінки магазину / Template name for the shop page
            products=products,  # Передача всіх продуктів / Pass all products
            username=current_user.name.upper(),  # Ім'я користувача у верхньому регістрі / User's name in uppercase
            admin=current_user.admin  # Статус адміністратора користувача / User's admin status
        )
    else:  # Якщо користувач не автентифікований / If the user is not authenticated
        return flask.redirect("/")  # Перенаправлення на головну сторінку / Redirect to the main page
