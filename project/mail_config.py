from .settings import project # Імпортуємо веб додаток з головного файлу
import flask_mail # Імпортуємо 

# Адреса адміністрації / Administration address
ADMINISTRATION_ADRESS = "m.tereshonok2020@gmail.com"
# Пароль адміністрації / Administration password
ADMINISTRATION_PASSWORD = "gkoi ufje okhw wscv"

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
    # Створюємо повідомлення / Creating message
    print("sent 1")
    message = flask_mail.Message(
        subject = "Ваш кошик",  # Тема листа / Email subject
        recipients = [mail_user],  # Одержувачі / Recipients
        body = f"Привіт, {username}!\n\n Ваше замовлення: \n\n{basket_text}\n\nДякуємо за замовлення, гарного дня!",  # Тіло листа / Email body
        sender = ADMINISTRATION_ADRESS  # Відправник / Sender
    )
    print("sent 2")
    mail.send(message = message) # Відправляємо повідомлення / Sending message
    print("sent orig")

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