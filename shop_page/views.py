import flask
from flask_login import current_user, UserMixin
from home_page.models import Product, Cart
from project.settings import database

def show_shop_page():
    if isinstance(current_user, UserMixin):
        products = Product.query.all()
        return flask.render_template(template_name_or_list = 'shop.html', products = products, username = current_user.name.upper(), admin = current_user.admin)
    else:
        return flask.redirect("/")