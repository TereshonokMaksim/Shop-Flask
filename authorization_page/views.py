import flask  # Імпорт бібліотеки Flask / Import the Flask library
from home_page.models import User  # Імпорт моделі User з модуля home_page / Import the User model from the home_page module
from flask_login import login_user, current_user  # Імпорт функції для входу користувача та змінної поточного користувача / Import the function to log in a user and the current user variable

def show_login_page():  # Визначення функції для показу сторінки входу / Define a function to show the login page
    print(current_user.is_authenticated)  # Виведення статусу автентифікації поточного користувача / Print the authentication status of the current user
    if flask.request.method == "POST":  # Перевірка методу запиту / Check the request method
        form_data = dict(flask.request.form)  # Отримання даних форми з запиту / Get form data from the request
        print(form_data)  # Виведення даних форми для дебагу / Print the form data for debugging
        for user in [*User.query.filter_by(name = form_data['name']), *User.query.filter_by(email = form_data["name"])]:  # Прохід по користувачах, знайдених за ім'ям або email / Loop through users found by name or email
           login_user(user)  # Вхід користувача / Log in the user
           return flask.redirect("/")  # Перенаправлення на головну сторінку після входу / Redirect to the main page after login
        return flask.render_template(template_name_or_list = "login.html", not_registrated = True)  # Повернення шаблону сторінки входу з помилкою / Return the login page template with an error
    return flask.render_template(template_name_or_list = "login.html")  # Повернення шаблону сторінки входу / Return the login page template
