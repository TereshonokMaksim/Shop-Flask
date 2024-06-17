import flask
from home_page.models import User
from flask_login import login_user, current_user

def show_login_page():
    print(current_user.is_authenticated)
    if flask.request.method == "POST":
        form_data = dict(flask.request.form)
        print(form_data)
        for user in [*User.query.filter_by(name = form_data['name']), *User.query.filter_by(email = form_data["name"])]:
           login_user(user) 
           return flask.redirect("/")
        return flask.render_template(template_name_or_list = "login.html", not_registrated = True)
    return flask.render_template(template_name_or_list = "login.html")