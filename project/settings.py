import flask, os, flask_migrate, flask_sqlalchemy

project = flask.Flask(
    import_name = "settings",
    template_folder = "project/templates",
    instance_path = os.path.abspath(__file__ + "/.."),
    static_folder = "static"
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

database = flask_sqlalchemy.SQLAlchemy(app = project)
migrate = flask_migrate.Migrate(app = project, db = database)