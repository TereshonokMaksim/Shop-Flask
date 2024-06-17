import flask 

admin_app = flask.Blueprint(
    name = "admin",
    import_name = 'app',
    template_folder = 'admin_page/templates',
    static_folder = "static/admin_page",
    static_url_path = "/admin/"
)