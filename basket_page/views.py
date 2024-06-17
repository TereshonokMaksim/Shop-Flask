import flask 
from home_page.models import Product
from flask_login import current_user, UserMixin

def show_basket_page():
    if isinstance(current_user, UserMixin): 
        unique_product = {}
        all_price = 0
        num_products = 0
        all_discount = 0
        if flask.request.cookies.get("product") != None:
            for id_product in flask.request.cookies.get("product").split(" "):
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

        return flask.render_template(template_name_or_list = "basket.html", products = list(unique_product.values()), 
                                    all_price = all_price, number_of_products = num_products, 
                                    username = current_user.name.upper(), all_discount = round(all_discount, 2),
                                    admin = current_user.admin)
    else:
        return flask.redirect(location = "/")