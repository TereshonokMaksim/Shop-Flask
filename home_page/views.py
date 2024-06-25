import flask  # Імпорт бібліотеки Flask / Import the Flask library
from flask_login import current_user  # Імпорт змінної поточного користувача з flask_login / Import the current user variable from flask_login

def show_home_page():  # Визначення функції для показу домашньої сторінки / Define a function to show the home page
    if current_user.is_authenticated:  # Перевірка, чи користувач автентифікований / Check if the user is authenticated
        return flask.render_template(  # Повернення шаблону з параметрами / Return the template with parameters
            template_name_or_list="logined_home.html",  # Назва шаблону для автентифікованих користувачів / Template name for authenticated users
            username=current_user.name.upper(),  # Ім'я користувача у верхньому регістрі / User's name in uppercase
            admin=current_user.admin  # Статус адміністратора користувача / User's admin status
        )
    else:  # Якщо користувач не автентифікований / If the user is not authenticated
        return flask.render_template(template_name_or_list="not_logined_home.html")  # Повернення шаблону для неавтентифікованих користувачів / Return the template for non-authenticated users

        