from .settings import project # Імпортуємо веб додаток з головного файлу
import flask_mail # Імпортуємо модуль з flask для роботи з електроною поштою
from home_page.models import User

# Адреса для відправлення повідомлень / Administration address
ADMINISTRATION_ADRESS = "m.tereshonok2020@gmail.com"
# Пароль для відправки повідомлень / Administration password
ADMINISTRATION_PASSWORD = "gkoi ufje okhw wscv"
# Створюємо список для електронних скриньок адміністрації / We are creating a list for administration email boxes
admin_addresses = []

# Налаштування сервера для надсилання пошти / Configuring the mail server
project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["MAIL_PORT"] = 587  # Порт для сервера / Server port
project.config["MAIL_USE_TLS"] = True  # Дозволяємо використання TLS / Allowing use of TLS
project.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS  # Задаємо пошту / Setting mail
project.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD  # Пароль / Password

# Ініціалізація Flask-Mail з додатком / Initializing Flask-Mail with the application
mail = flask_mail.Mail(app = project)

# Функція для відправки кошика користувачеві / Function to send the basket to the user
def send_basket(mail_user: str, username: str, basket_text: str):
    # Створюємо повідомлення для користувача / Creating message for a user
    message = flask_mail.Message(
        subject = "Ваш кошик",  # Тема листа / Email subject
        recipients = [mail_user],  # Одержувачі / Recipients
        body = f"Привіт, {username}!\n\n Ваше замовлення: \n\n{basket_text}\n\nДякуємо за замовлення, гарного дня!",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    # Створюємо повідомлення для адміністрації / Creating message for the administration
    admin_message = flask_mail.Message(
        subject = "Ваш кошик",  # Тема листа / Email subject
        recipients = admin_addresses,  # Одержувачі / Recipients
        body = f"Користувач {username} оформив нове замовлення.\n\n Його кошик складається з: \n\n{basket_text}\n\nЩоб змінити його статус перейдіть у телеграмі і гілці Кошик.",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    mail.send(message = admin_message) # Відправляємо повідомлення адміністрації / Sending message to administration
    mail.send(message = message) # Відправляємо повідомлення / Sending message

# Функція для відхилення кошика користувача / Function to reject the user's basket
def reject_basket(mail_user: str, username: str):
    # Створюємо повідомлення / Creating message
    message = flask_mail.Message(
        subject = "Статус вашого замовлення",  # Тема листа / Email subject
        recipients = [mail_user],  # Одержувачі / Recipients
        body = f"Привіт, {username}!\n\n Ваше замовлення було відхилено продавцем магазину.\n\nВибачаемося за незручності, гарного дня!",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    mail.send(message = message) # Відправляємо повідомлення / Sending message

# Функція для підтвердження виконання замовлення / Function to confirm order completion
def complete_basket(mail_user: str, username: str):
    # Створюємо повідомлення / Creating message
    message = flask_mail.Message(
        subject = "Статус вашого замовлення",  # Тема листа / Email subject
        recipients = [mail_user],  # Одержувачі / Recipients
        body = f"Привіт, {username}!\n\n Ваше замовлення вже зібрано та відправлено у дорогу!\n\nДякуємо за ваше замовлення, гарного дня!",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    mail.send(message = message) # Відправляємо повідомлення / Sending message

# Функція для надсилання повідомлення про скасування кошику
def cancel_basket(cart):
    # Створюємо повідомлення / Creating message
    message = flask_mail.Message(
        subject = "Скасування вашого замовлення",  # Тема листа / Email subject
        recipients = [cart.email],  # Одержувачі / Recipients
        body = f"Привіт, {cart.name}!\n\n Ви скасували своє замовлення на {len(cart.products.split(' '))} товарів.",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    # Створюємо повідомлення / Creating message
    admin_message = flask_mail.Message(
        subject = "Статус вашого замовлення",  # Тема листа / Email subject
        recipients = admin_addresses,  # Одержувачі / Recipients
        body = f"Користувач {cart.name} скасував своє замовлення.n\nНомер кошику: {cart.id} \nКошик складався з {len(cart.products.split(' '))} товарів. \n\nПовідомлення з телеграму було автоматично видалено.",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    mail.send(message = admin_message) # Відправляємо повідомлення адміністрації / Sending message to administration
    mail.send(message = message) # Відправляємо повідомлення / Sending message
    