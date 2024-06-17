import flask 

registration_app = flask.Blueprint(
    name = "registration",
    import_name = "app",
    template_folder = "registration_page/templates",
    static_folder = "static/registration_page",
    static_url_path = "/registration/"
)