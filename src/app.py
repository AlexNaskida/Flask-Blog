import logging

from flask import Flask, render_template
from src.settings import settings
from src.extensions import extensions, extensions_with_db, login_manager
from src.extensions.database import db
from src.modules.auth.models import User


def import_models():
    # Course models
    from src.modules.auth.models import User


def register_extensions(app):
    """Register Flask extensions."""
    for extension in extensions:
        extension.init_app(app=app)

    for extension in extensions_with_db:
        extension.init_app(app=app, db=db)


def register_blueprints(app: Flask):
    """
    Method to register list of blueprints to the app

    param app: Flask application
    """
    # To check if app contains blueprints we need to be inside the app context
    from src.blueprints import blueprints

    if not blueprints and app.get("CHECK_FOR_BLUEPRINTS") is True:
        message = "The list of blueprints is empty. App won't have any blueprints."
        logging.warning(message)
    else:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)


def register_error_handlers(app):
    @app.errorhandler(404)
    def error_code_404(e):
        return render_template('error_pages/404.html'), 404

    @app.errorhandler(500)
    def error_code_500(e):
        return render_template("error_pages/500.html"), 500


def register_shell_context(app):
    pass


def register_commands(app):
    pass


def configure_logger(app):
    pass


def create_app():

    app = Flask(__name__)
    app.config.from_object(settings)

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_shell_context(app)
    register_commands(app)
    configure_logger(app)
    import_models()

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)

    return app