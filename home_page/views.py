import flask
from flask_login import current_user

def show_home_page():
    if current_user.is_authenticated:
        return flask.render_template(template_name_or_list = "logined_home.html", username = current_user.name.upper(), admin = current_user.admin)
    else:
        return flask.render_template(template_name_or_list = "not_logined_home.html")
        