import flask

# Створення Blueprint для адміністративної частини додатку / Creating a Blueprint for the admin part of the application
admin_app = flask.Blueprint(
    name = "admin",  # Назва Blueprint / Name of the Blueprint
    import_name = 'app',  # Імпортний шлях до Blueprint / Import path for the Blueprint
    template_folder = 'admin_page/templates',  # Шлях до папки з шаблонами / Path to the templates folder
    static_folder = "static/admin_page",  # Шлях до статичних файлів / Path to the static files
    static_url_path = "/admin/"  # URL-префікс для статичних файлів / URL prefix for the static files
)