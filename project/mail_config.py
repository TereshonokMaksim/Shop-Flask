from .settings import project
import flask_mail

ADMINISTRATION_ADRESS = "m.tereshonok2020@gmail.com"
ADMINISTRATION_PASSWORD = "gkoi ufje okhw wscv"

project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["MAIL_PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
project.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD

mail = flask_mail.Mail(app = project)

def send_basket(mail_user: str, username: str, basket_text: str):
    print("sent 1")
    message = flask_mail.Message(subject = "Ваш кошик", 
                                 recipients = [mail_user],
                                 body = f"Привіт, {username}!\n\n Ваше замовлення: \n\n{basket_text}\n\nДякуємо за замовлення, гарного дня!",
                                 sender = ADMINISTRATION_ADRESS)
    print("sent 2")
    mail.send(message = message)
    print("sent orig")
    
def reject_basket(mail_user: str, username: str):
    message = flask_mail.Message(subject = "Статус вашого замовлення", 
                                 recipients = [mail_user],
                                 body = f"Привіт, {username}!\n\n Ваше замовлення було відхилено продавцем магазину.\n\n,Вибачаемося за незручності, гарного дня!",
                                 sender = ADMINISTRATION_ADRESS)
    mail.send(message = message)
    
def complete_basket(mail_user: str, username: str):
    message = flask_mail.Message(subject = "Статус вашого замовлення", 
                                 recipients = [mail_user],
                                 body = f"Привіт, {username}!\n\n Ваше замовлення вже зібрано та відправлено у дорогу!\n\nДякуємо за ваше замовлення, гарного дня!",
                                 sender = ADMINISTRATION_ADRESS)
    mail.send(message = message)
    
