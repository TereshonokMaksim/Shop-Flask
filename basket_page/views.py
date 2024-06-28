import flask  # Імпорт бібліотеки Flask / Import the Flask library
from home_page.models import Product, Cart  # Імпорт моделей Product та Cart з модуля home_page / Import the Product and Cart models from the home_page module
from flask_login import current_user, UserMixin  # Імпорт поточного користувача та UserMixin з flask_login / Import current user and UserMixin from flask_login
from project.settings import database  # Імпорт налаштувань бази даних з проекту / Import the database settings from the project
from bot import send_cart, delete_cart  # Імпорт функцій send_cart та delete_cart з модуля bot / Import send_cart and delete_cart functions from the bot module
from project.mail_config import cancel_basket

def show_basket_page():  # Визначення функції для показу сторінки кошика / Define a function to show the basket page
    if isinstance(current_user, UserMixin):  # Перевірка, чи поточний користувач є екземпляром UserMixin / Check if the current user is an instance of UserMixin
        unique_product = {}  # Ініціалізація словника для унікальних продуктів / Initialize a dictionary for unique products
        all_price = 0  # Ініціалізація загальної ціни / Initialize total price
        num_products = 0  # Ініціалізація кількості продуктів / Initialize number of products
        all_discount = 0  # Ініціалізація загальної знижки / Initialize total discount
        cookies_products = flask.request.cookies.get("product")  # Отримання продуктів з cookies / Get products from cookies
        print(flask.request.method, "METHOD")  # Виведення методу запиту / Print the request method
        if flask.request.method == "POST":  # Перевірка методу запиту / Check the request method
            form = flask.request.form  # Отримання даних форми з запиту / Get form data from the request
            print(form, "WHERE")  # Виведення даних форми для дебагу / Print the form data for debugging
            if "submit_delivery" in form.keys():  # Перевірка, чи натиснута кнопка "submit_delivery" / Check if the "submit_delivery" button is pressed
                user_cart = Cart(user_id = current_user.id,  # Створення нового об'єкта Cart / Create a new Cart object
                                products = cookies_products,  # Збереження продуктів з cookies / Save products from cookies
                                name = form["name"],  # Збереження імені з форми / Save name from the form
                                surname = form["surname"],  # Збереження прізвища з форми / Save surname from the form
                                phone_number = form["phone_number"],  # Збереження номера телефону з форми / Save phone number from the form
                                email = form["email"],  # Збереження email з форми / Save email from the form
                                city = form["city"],  # Збереження міста з форми / Save city from the form
                                post_office = form["post_office"],  # Збереження поштового відділення з форми / Save post office from the form
                                additional = form["additional"])  # Збереження додаткової інформації з форми / Save additional information from the form
                database.session.add(user_cart)  # Додавання нового об'єкта Cart до сесії бази даних / Add the new Cart object to the database session
                database.session.commit()  # Фіксація змін у базі даних / Commit the changes to the database
                send_cart(cart = user_cart)  # Виклик функції send_cart з новим об'єктом Cart / Call the send_cart function with the new Cart object
            elif "cancel_delivery" in form.keys():  # Перевірка, чи натиснута кнопка "cancel_delivery" / Check if the "cancel_delivery" button is pressed
                for cart in Cart.query.filter_by(user_id = current_user.id): cart_to_delete = cart  # Отримання корзини для видалення / Get the cart to delete
                cancel_basket(cart = cart_to_delete) # Надсилаємо повідомлення на пошту про скасування замовлення / Sending message to the mail about canceling the order
                delete_cart(cart_id = cart_to_delete.id)  # Виклик функції delete_cart з id корзини / Call the delete_cart function with the cart id
                database.session.delete(cart_to_delete)  # Видалення корзини з бази даних / Delete the cart from the database
                database.session.commit()  # Фіксація змін у базі даних / Commit the changes to the database

        if cookies_products != None:  # Перевірка, чи продукти в cookies не є пустими / Check if products in cookies are not empty
            for id_product in cookies_products.split(" "):  # Прохід по кожному продукту в cookies / Loop through each product in cookies
                try:
                    print(id_product)  # Виведення id продукту для дебагу / Print the product id for debugging
                    current_product = Product.query.get(id_product)  # Отримання поточного продукту з бази даних за id / Get the current product from the database by id
                    all_price += current_product.price  # Додавання ціни продукту до загальної ціни / Add the product price to the total price
                    all_discount += int(current_product.price * current_product.discount / 100)  # Додавання знижки продукту до загальної знижки / Add the product discount to the total discount
                    num_products += 1  # Збільшення кількості продуктів на 1 / Increment the number of products by 1
                    if id_product in list(unique_product.keys()):  # Перевірка, чи продукт вже є в унікальних продуктах / Check if the product is already in unique products
                        unique_product[id_product][1] += 1  # Збільшення кількості даного продукту на 1 / Increment the quantity of this product by 1
                    else:
                        unique_product[id_product] = [current_product, 1]  # Додавання нового продукту до унікальних продуктів / Add a new product to unique products
                except:  # Обробка виключень / Handle exceptions
                    print(f"Cookie {id_product} is wrong!")  # Виведення повідомлення про помилковий cookie / Print a message about the wrong cookie
        cart_num = 0  # Ініціалізація кількості корзин / Initialize the number of carts
        for cart in Cart.query.filter_by(user_id = current_user.id):  # Прохід по всіх корзинах користувача / Loop through all user's carts
            cart_num += 1  # Збільшення кількості корзин на 1 / Increment the number of carts by 1
        print(cart_num)  # Виведення кількості корзин для дебагу / Print the number of carts for debugging
        if cart_num == 0:  # Перевірка, чи немає корзин / Check if there are no carts
            template_name = "basket.html"  # Встановлення шаблону "basket.html" / Set the template to "basket.html"
        else:
            template_name = "basket_send.html"  # Встановлення шаблону "basket_send.html" / Set the template to "basket_send.html"

        # Повернення шаблону сторінки з переданими параметрами / Return the template with the passed parameters
        return flask.render_template(template_name_or_list = template_name, 
                                    products = list(unique_product.values()),  # Передача унікальних продуктів / Pass unique products
                                    all_price = all_price,  # Передача загальної ціни / Pass total price
                                    number_of_products = num_products,  # Передача кількості продуктів / Pass number of products
                                    username = current_user.name.upper(),  # Передача імені користувача у верхньому регістрі / Pass the username in uppercase
                                    all_discount = round(all_discount, 2),  # Передача загальної знижки / Pass total discount
                                    admin = current_user.admin)  # Передача статусу адміністратора / Pass admin status
    else:  # Якщо користувач не автентифікований / If the user is not authenticated
        return flask.redirect(location = "/")  # Перенаправлення на головну сторінку / Redirect to the main page
