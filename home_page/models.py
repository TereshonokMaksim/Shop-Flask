from project.settings import database # Імпортуємо датабазу / We import the database
from flask_login import UserMixin # Імпортуємо клас для створення класу користувача / # Import the class to create the user class

# Створюємо модель користувача / We create a user model
class User(database.Model, UserMixin):
    # Створюємо колонку id яка автоматично заповнюється при створенні нового користувача / We create an id column that is automatically filled in when a new user is created
    id = database.Column(database.Integer, primary_key = True)
    # Створюємо колонку імені користувача котра обов'язкова повинна бути не пустою / We create a username column, which must not be empty
    name = database.Column(database.String(60), nullable = False)
    # Створюємо колонку EMail користувача котра обов'язкова повинна бути не пустою / We create the user's EMail column, which must not be empty
    email = database.Column(database.String(80), nullable = False)
    # Створюємо колонку паролю користувача котра обов'язкова повинна бути не пустою / We create a user password column, which must not be empty
    password = database.Column(database.String(50), nullable = False)
    # Створюємо колонку чи є користувач адміністратором / We create a column whether the user is an administrator
    admin = database.Column(database.Integer, nullable = True)

    # Створюємо функцію для текстового відображення моделі / We create a function for text display of the model
    def __repr__(self) -> str:
        # Повертаємо строкове значення яке буде відображено на екрані / We return a string value that will be displayed on the screen
        return f"Користувач {self.name} з id {self.id}, email {self.email}\n"
    
# Створюємо модель продукта / We create a product model
class Product(database.Model):
    # Створюємо колонку id яка автоматично заповнюється при створенні нового користувача / We create an id column that is automatically filled in when a new user is created
    id = database.Column(database.Integer, primary_key = True)
    # Створюємо колонку імені продукта котра обов'язкова повинна бути не пустою / We create a product name column, which must not be empty
    name = database.Column(database.String(180), nullable = False)
    # Створюємо колонку вартості продукта котра обов'язкова повинна бути не пустою / We create a product price column, which must not be empty
    price = database.Column(database.Integer, nullable = False)
    # Створюємо колонку опису продукта котра обов'язкова повинна бути не пустою / We create a product description column, which must not be empty
    description = database.Column(database.Text, nullable = False)
    # Створюємо колонку чи є продукт в наявності котра обов'язкова повинна бути не пустою / We create a column whether the product is available, which must not be empty
    in_stock = database.Column(database.Integer, nullable = False)
    # Створюємо колонку знижки продукта / We create a product discount column
    discount = database.Column(database.Integer, nullable = True)
    # Створюємо колонку кількості продукта / We create a product quantity column
    count = database.Column(database.Integer, nullable = True)
    
    # Створюємо функцію для текстового відображення моделі / We create a function for text display of the model
    def __repr__(self) -> str:
        # Повертаємо строкове значення яке буде відображено на екрані / We return a string value that will be displayed on the screen
        return f"Продукт {self.name} з id {self.id}"

# Створюємо модель кошику / We create a basket model
class Cart(database.Model):
    # Створюємо колонку id яка автоматично заповнюється при створенні нового користувача / We create an id column that is automatically filled in when a new user is created
    id = database.Column(database.Integer, primary_key = True)
    # Створюємо колонку id користувача кошика котра обов'язкова повинна бути не пустою / We create a cart user id column, which must not be empty
    user_id = database.Column(database.Integer, nullable = False)
    # Створюємо колонку id продуктів кошика котра обов'язкова повинна бути не пустою / We create a cart product id column, which must not be empty
    products = database.Column(database.Text, nullable = True)
    # Створюємо колонку імені замовника кошика / We create a column for the name of the customer of the shopping cart
    name = database.Column(database.String(80), nullable = True)
    # Створюємо колонку прізвища замовника кошика / We create a column for the name of the customer of the shopping cart
    surname = database.Column(database.String(80), nullable = True)
    # Створюємо колонку номеру телефону замовника кошика / We create a column for the phone number of the customer of the shopping cart
    phone_number = database.Column(database.String(80), nullable = True)
    # Створюємо колонку EMail замовника кошика / We create the EMail column of the customer of the shopping cart
    email = database.Column(database.String(100), nullable = True)
    # Створюємо колонку міста замовника кошика / We create a column of the city of the customer of the cart
    city = database.Column(database.String(40), nullable = True)
    # Створюємо колонку відділення пошти замовника кошика / We create a column for the post office of the customer of the basket
    post_office = database.Column(database.String(60), nullable = True)
    # Створюємо колонку додаткових побажань замовника кошика / We create a column of additional wishes of the customer of the basket
    additional = database.Column(database.Text, nullable = True)