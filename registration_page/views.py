import flask
from flask_login import current_user
from home_page.models import User, database

def show_registration_page():
    print(current_user.is_authenticated)
    if flask.request.method == "POST":
        form_data = dict(flask.request.form)
        print(form_data)
        user = User(name = form_data["name"], email = form_data["email"], password = form_data["password"], admin = 0)
        is_registered = True
        database.session.add(user)
        database.session.commit()
    else:
        is_registered = False

    print(is_registered)
    return flask.render_template(template_name_or_list = "registration.html", is_registrated = is_registered)