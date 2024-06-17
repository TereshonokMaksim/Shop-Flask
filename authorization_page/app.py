import flask 

login_app = flask.Blueprint(
    name = "authorization",
    import_name = "app",
    template_folder = "authorization_page/templates",
    static_folder = "static/authorization_page",
    static_url_path = "/authorization/"
)