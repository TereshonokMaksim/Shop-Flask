import flask 

basket_app = flask.Blueprint(
    name = 'basket',
    import_name = 'app',
    template_folder = 'basket_page/templates',
    static_folder = "static/basket_page",
    static_url_path = "/basket/"
)