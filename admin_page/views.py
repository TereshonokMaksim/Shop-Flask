import flask
from flask_login import current_user
import os
from project.settings import database
from home_page.models import Product

def show_admin_page():
    # try:
        if current_user.admin != 0:
            if flask.request.method == "POST":
                form_data = dict(flask.request.form)
                if 'new_product' in form_data.keys():
                    new_product = Product(
                        name = form_data['product_name'], 
                        description = form_data['product_description'],
                        price = int(form_data['product_price']),
                        discount = int(form_data['product_discount']),
                        in_stock = 1
                        )
                    flask.request.files['product_image'].save(dst = os.path.abspath(__file__ + f'/../../static/shop_page/images/{new_product.name}.png'))
                    database.session.add(new_product)
                    database.session.commit()

                elif 'delete_product' in form_data.keys():
                    delete_product = Product.query.get(form_data['delete_product'])
                    if delete_product != None:
                        image_path = os.path.abspath(__file__ + f'/../../static/shop_page/images/{delete_product.name}.png')
                        # Были ошибки во время работы с телеграм ботом которые запрещали работу коду
                        if os.path.exists(image_path):
                            os.remove(image_path)
                        database.session.delete(delete_product)
                        database.session.commit()
                else:
                    if list(flask.request.files.values())[0] != None:
                        input_key = list(form_data.keys())[0]
                        value = form_data[input_key]
                    else:
                        input_key = list(flask.request.files.keys())[0] 
                    print(input_key, input_key)
                    product = Product.query.get(input_key.split("-")[2])
                    print(form_data, product, input_key.split("-")[2])
                    if "name" in input_key:
                        os.rename(os.path.abspath(__file__ + f"/../../static/shop_page/images/{product.name}.png"), 
                                os.path.abspath(__file__ + f"/../../static/shop_page/images/{value}.png"))
                        product.name = value

                    elif "discount" in input_key:
                        product.discount = int(value)
                    elif "price" in input_key:
                        product.price = round(int(value), 2)
                    elif "property" in input_key:
                        product = Product.query.get(input_key.split("-")[-2])
                        base_properties = product.description.split(";")
                        input_data = input_key.split("-")[1:]
                        for base_property in base_properties:
                            print(base_property, input_data)
                            if input_data[-1] in base_property:
                                print("im in")
                                new_property = base_property.split(": ")[-1].split("/")
                                new_property[int(input_data[0].replace("property", ""))] = value
                                new_property = "/".join(new_property)
                                base_properties[base_properties.index(base_property)] = ": ".join([base_property.split(": ")[0], new_property])
                        print(base_properties)
                        product.description = "; ".join(base_properties)

                    elif "image" in input_key:
                        image = flask.request.files["new-value"]
                        path = os.path.abspath(__file__ + f"/../../static/shop_page/images/{product.name}.png")
                        if os.path.exists(path):
                            os.remove(path)
                        image.save(path)
                    print(product)

                    database.session.add(product)
                    database.session.commit()


            return flask.render_template(template_name_or_list = "admin.html", products = Product.query.all(), admin = current_user.admin, username = current_user.name)
        else:
            return flask.redirect(location = "/")
    # except Exception as error:
    #     print(f"An error has occured while there was an attempt to load the page.\nError log: {error}")
    #     return flask.redirect(location = "/")
