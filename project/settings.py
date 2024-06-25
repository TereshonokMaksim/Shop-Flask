import flask, os, flask_migrate, flask_sqlalchemy

# Створення Flask додатку з налаштуваннями / Creating a Flask application with settings
project = flask.Flask(
    import_name = "settings",  # Ім'я імпорту для додатку / Import name for the application
    template_folder = "project/templates",  # Папка з шаблонами / Template folder
    instance_path = os.path.abspath(__file__ + "/.."),  # Абсолютний шлях до папки з екземплярами / Absolute path to the instance folder
    static_folder = "static"  # Папка зі статичними файлами / Static files folder
)

# Налаштування URI для бази даних / Setting the database URI
project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Ініціалізація SQLAlchemy з додатком / Initializing SQLAlchemy with the application
database = flask_sqlalchemy.SQLAlchemy(app = project)
# Ініціалізація Flask-Migrate з додатком та базою даних / Initializing Flask-Migrate with the application and database
migrate = flask_migrate.Migrate(app = project, db = database)