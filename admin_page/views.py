import flask  # Імпорт бібліотеки Flask / Import the Flask library
from flask_login import current_user  # Імпорт змінної для отримання поточного користувача / Import a variable to get the current user
import os  # Імпорт бібліотеки для роботи з операційною системою / Import the library for operating system tasks
from project.settings import database  # Імпорт налаштувань бази даних з проекту / Import the database settings from the project
from home_page.models import Product, Cart  # Імпорт моделей Product і Cart з модуля home_page / Import the Product and Cart models from the home_page module

def show_admin_page():  # Визначення функції для показу адміністративної сторінки / Define a function to show the admin page
    try:  # Початок блоку обробки виключень / Start of the exception handling block
        if current_user.admin != 0:  # Перевірка, чи користувач є адміністратором / Check if the user is an admin
            if flask.request.method == "POST":  # Перевірка методу запиту / Check the request method
                form_data = dict(flask.request.form)  # Отримання даних форми з запиту / Get form data from the request
                if 'new_product' in form_data.keys():  # Перевірка наявності ключа 'new_product' у формі / Check if 'new_product' key is in the form
                    new_product = Product(  # Створення нового продукту / Create a new product
                        name = form_data['product_name'],  # Встановлення імені продукту / Set the product name
                        description = form_data['product_description'],  # Встановлення опису продукту / Set the product description
                        price = int(form_data['product_price']),  # Встановлення ціни продукту / Set the product price
                        discount = int(form_data['product_discount']),  # Встановлення знижки на продукт / Set the product discount
                        in_stock = 1  # Встановлення наявності продукту в наявності / Set the product as in stock
                        )
                    # Збереження зображення продукту / Save the product image
                    flask.request.files['product_image'].save(dst = os.path.abspath(__file__ + f'/../../static/shop_page/images/{new_product.name}.png'))
                    database.session.add(new_product)  # Додавання нового продукту до сесії бази даних / Add the new product to the database session
                    database.session.commit()  # Фіксація змін у базі даних / Commit the changes to the database

                elif 'delete_product' in form_data.keys():  # Перевірка наявності ключа 'delete_product' у формі / Check if 'delete_product' key is in the form
                    delete_product = Product.query.get(form_data['delete_product'])  # Отримання продукту для видалення з бази даних / Get the product to delete from the database
                    if delete_product != None:  # Перевірка, чи існує продукт / Check if the product exists
                        image_path = os.path.abspath(__file__ + f'/../../static/shop_page/images/{delete_product.name}.png')  # Отримання шляху до зображення продукту / Get the product image path
                        
                        if os.path.exists(image_path):  # Перевірка, чи існує зображення / Check if the image exists
                            os.remove(image_path)  # Видалення зображення продукту / Remove the product image
                        database.session.delete(delete_product)  # Видалення продукту з бази даних / Delete the product from the database
                        database.session.commit()  # Фіксація змін у базі даних / Commit the changes to the database
                else:  # Інші дії з продуктами / Other actions with products
                    if list(flask.request.files.values())[0] != None:  # Перевірка наявності файлів у запиті / Check if files are present in the request
                        input_key = list(form_data.keys())[0]  # Отримання ключа з форми / Get the key from the form
                        value = form_data[input_key]  # Отримання значення з форми / Get the value from the form
                    else:
                        input_key = list(flask.request.files.keys())[0]  # Отримання ключа файлу з запиту / Get the file key from the request
                    print(input_key, input_key)  # Виведення ключа для дебагу / Print the key for debugging
                    product = Product.query.get(input_key.split("-")[2])  # Отримання продукту за ключем / Get the product by key
                    print(form_data, product, input_key.split("-")[2])  # Виведення даних для дебагу / Print the data for debugging
                    if "name" in input_key:  # Перевірка, чи ключ містить 'name' / Check if the key contains 'name'
                        # Перейменування зображення продукту / Rename the product image
                        os.rename(os.path.abspath(__file__ + f"/../../static/shop_page/images/{product.name}.png"), 
                                os.path.abspath(__file__ + f"/../../static/shop_page/images/{value}.png"))
                        product.name = value  # Оновлення імені продукту / Update the product name

                    elif "discount" in input_key:  # Перевірка, чи ключ містить 'discount' / Check if the key contains 'discount'
                        product.discount = int(value)  # Оновлення знижки продукту / Update the product discount
                    elif "price" in input_key:  # Перевірка, чи ключ містить 'price' / Check if the key contains 'price'
                        product.price = round(int(value), 2)  # Оновлення ціни продукту / Update the product price
                    elif "property" in input_key:  # Перевірка, чи ключ містить 'property' / Check if the key contains 'property'
                        product = Product.query.get(input_key.split("-")[-2])  # Отримання продукту за ключем / Get the product by key
                        base_properties = product.description.split(";")  # Розбиття опису продукту на властивості / Split the product description into properties
                        input_data = input_key.split("-")[1:]  # Отримання даних з ключа / Get the data from the key
                        for base_property in base_properties:  # Прохід по базових властивостях / Loop through base properties
                            print(base_property, input_data)  # Виведення властивостей для дебагу / Print properties for debugging
                            if input_data[-1] in base_property:  # Перевірка, чи містить властивість потрібні дані / Check if the property contains the required data
                                print("im in")  # Виведення повідомлення для дебагу / Print a message for debugging
                                new_property = base_property.split(": ")[-1].split("/")  # Розбиття властивості на частини / Split the property into parts
                                new_property[int(input_data[0].replace("property", ""))] = value  # Оновлення властивості новим значенням / Update the property with the new value
                                new_property = "/".join(new_property)  # Об'єднання частин властивості / Join the property parts
                                base_properties[base_properties.index(base_property)] = ": ".join([base_property.split(": ")[0], new_property])  # Оновлення властивості в базі / Update the property in the base
                        print(base_properties)  # Виведення оновлених властивостей для дебагу / Print the updated properties for debugging
                        product.description = "; ".join(base_properties)  # Оновлення опису продукту / Update the product description

                    elif "image" in input_key:  # Перевірка, чи ключ містить 'image' / Check if the key contains 'image'
                        image = flask.request.files["new-value"]  # Отримання нового зображення з запиту / Get the new image from the request
                        path = os.path.abspath(__file__ + f"/../../static/shop_page/images/{product.name}.png")  # Отримання шляху до зображення продукту / Get the product image path
                        if os.path.exists(path):  # Перевірка, чи існує зображення / Check if the image exists
                            os.remove(path)  # Видалення старого зображення / Remove the old image
                        image.save(path)  # Збереження нового зображення / Save the new image
                    print(product)  # Виведення продукту для дебагу / Print the product for debugging

                    database.session.add(product)  # Додавання продукту до сесії бази даних / Add the product to the database session
                    database.session.commit()  # Фіксація змін у базі даних / Commit the changes to the database

            # Повернення шаблону адміністративної сторінки з продуктами / Return the admin page template with products
            return flask.render_template(template_name_or_list = "admin.html", products = Product.query.all(), admin = current_user.admin, username = current_user.name)
        else:  # Якщо користувач не адміністратор, перенаправити на головну сторінку / If the user is not an admin, redirect to the main page
            return flask.redirect(location = "/")
    except Exception as error:  # Обробка винятків / Handle exceptions
        print(f"An error has occured while there was an attempt to load the page.\nError log: {error}")  # Виведення повідомлення про помилку / Print the error message
        return flask.redirect(location = "/")  # Перенаправлення на головну сторінку / Redirect to the main page

