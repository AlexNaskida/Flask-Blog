# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_login import LoginManager
from flask_migrate import Migrate

from src.extensions.database import db

login_manager = LoginManager()
migrate = Migrate()

login_manager.login_view = "auth.login"

extensions = [login_manager, db]
extensions_with_db = [migrate]


