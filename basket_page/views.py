import flask 
from home_page.models import Product, Cart
from flask_login import current_user, UserMixin
from project.settings import database
from bot import send_cart, delete_cart

def show_basket_page():
    if isinstance(current_user, UserMixin): 
        unique_product = {}
        all_price = 0
        num_products = 0
        all_discount = 0
        cookies_products = flask.request.cookies.get("product")
        print(flask.request.method, "METHOD")
        if flask.request.method == "POST":
            form = flask.request.form
            print(form, "WHERE")
            if "submit_delivery" in form.keys():
                user_cart = Cart(user_id = current_user.id, 
                                products = cookies_products,
                                name = form["name"],
                                surname = form["surname"],
                                phone_number = form["phone_number"],
                                email = form["email"],
                                city = form["city"],
                                post_office = form["post_office"],
                                additional = form["additional"])
                database.session.add(user_cart)
                database.session.commit()
                send_cart(cart = user_cart)
            elif "cancel_delivery" in form.keys():
                for cart in Cart.query.filter_by(user_id = current_user.id): cart_to_delete = cart
                delete_cart(cart_id = cart_to_delete.id)
                database.session.delete(cart_to_delete)
                database.session.commit()

        if cookies_products != None:
            for id_product in cookies_products.split(" "):
                try:
                    print(id_product)
                    current_product = Product.query.get(id_product)
                    all_price += current_product.price
                    all_discount += int(current_product.price * current_product.discount / 100)
                    num_products += 1
                    if id_product in list(unique_product.keys()):
                        unique_product[id_product][1] += 1
                    else:
                        unique_product[id_product] = [current_product, 1]
                except:
                    print(f"Cookie {id_product} is wrong!")
        cart_num = 0
        for cart in Cart.query.filter_by(user_id = current_user.id):
            cart_num += 1
        print(cart_num)
        if cart_num == 0:
            template_name = "basket.html"
        else:
            template_name = "basket_send.html"

        return flask.render_template(template_name_or_list = template_name, 
                                    products = list(unique_product.values()), 
                                    all_price = all_price, 
                                    number_of_products = num_products, 
                                    username = current_user.name.upper(), 
                                    all_discount = round(all_discount, 2),
                                    admin = current_user.admin)
    else:
        return flask.redirect(location = "/")