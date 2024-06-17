import home_page, authorization_page, registration_page, shop_page, basket_page, admin_page
import registration_page.app
from .settings import project

home_page.home_app.add_url_rule(
    rule = "/",
    view_func = home_page.show_home_page
)

registration_page.registration_app.add_url_rule(
    rule = "/registration/",
    view_func = registration_page.show_registration_page,
    methods = ["GET", "POST"]
)

authorization_page.login_app.add_url_rule(
    rule = "/authorization/",
    view_func = authorization_page.show_login_page,
    methods = ["GET", "POST"]
)

shop_page.shop_app.add_url_rule(
    rule = "/shop/",
    view_func = shop_page.show_shop_page
) 

basket_page.basket_app.add_url_rule(
    rule = "/basket/",
    view_func = basket_page.show_basket_page,
    methods = ["GET", "POST"]
)

admin_page.admin_app.add_url_rule(
    rule = "/admin/",
    view_func = admin_page.show_admin_page,
    methods = ["GET", "POST"]
)

project.register_blueprint(blueprint = authorization_page.login_app)
project.register_blueprint(blueprint = registration_page.registration_app)
project.register_blueprint(blueprint = home_page.home_app)
project.register_blueprint(blueprint = shop_page.shop_app)
project.register_blueprint(blueprint = basket_page.basket_app)
project.register_blueprint(blueprint = admin_page.admin_app)