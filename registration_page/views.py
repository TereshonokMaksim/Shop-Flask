import flask  # Імпорт бібліотеки Flask / Import the Flask library
from flask_login import current_user  # Імпорт змінної поточного користувача з flask_login / Import the current user variable from flask_login
from home_page.models import User, database, Cart  # Імпорт моделей User, database та Cart з модуля home_page / Import the User, database, and Cart models from the home_page module

def show_registration_page():  # Визначення функції для показу сторінки реєстрації / Define a function to show the registration page
    print(current_user.is_authenticated)  # Виведення статусу автентифікації поточного користувача / Print the authentication status of the current user
    if flask.request.method == "POST":  # Перевірка методу запиту / Check the request method
        form_data = dict(flask.request.form)  # Отримання даних форми з запиту / Get form data from the request
        print(form_data)  # Виведення даних форми для дебагу / Print the form data for debugging
        # Створення нового користувача з даними з форми / Create a new user with data from the form
        user = User(name=form_data["name"], email=form_data["email"], password=form_data["password"], admin=0)
        is_registered = True  # Позначення, що користувач зареєстрований / Indicate that the user is registered
        database.session.add(user)  # Додавання нового користувача до сесії бази даних / Add the new user to the database session
        database.session.commit()  # Фіксація змін у базі даних / Commit the changes to the database
    else:  # Якщо метод запиту не POST / If the request method is not POST
        is_registered = False  # Позначення, що користувач не зареєстрований / Indicate that the user is not registered

    print(is_registered)  # Виведення статусу реєстрації для дебагу / Print the registration status for debugging
    # Повернення шаблону сторінки реєстрації з параметром is_registered / Return the registration page template with the is_registered parameter
    return flask.render_template(template_name_or_list="registration.html", is_registrated=is_registered)
