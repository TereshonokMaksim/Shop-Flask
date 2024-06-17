from flask_login import LoginManager
from .settings import project
from home_page.models import User

project.secret_key = "😎😎😎"

login_manager = LoginManager(app = project)
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)