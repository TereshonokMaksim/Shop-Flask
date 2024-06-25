from flask_login import LoginManager # Імпортуємо клас мененджера логіну для 
from .settings import project
from home_page.models import User

# Секретний ключ для додатку / Secret key for the application
project.secret_key = "😎😎😎"

# Ініціалізація LoginManager з додатком / Initializing LoginManager with the application
login_manager = LoginManager(app = project)

# Функція завантаження користувача / User loader function
@login_manager.user_loader
def load_user(id):
    # Повертає користувача за його ID / Returns a user by their ID
    return User.query.get(id)