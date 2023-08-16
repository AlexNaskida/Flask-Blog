from flask import Blueprint
from src.extensions.api import  api_blueprint
from src.modules.auth.views import auth_blueprint
from src.modules.main.views import main_blueprint
from src.modules.post.views import post_blueprint
from src.modules.searchbar.views import searchbar_blueprint
from src.modules.dashboard.views import dashboard_blueprint

blueprints: list[Blueprint] = [auth_blueprint, main_blueprint, dashboard_blueprint, post_blueprint, searchbar_blueprint, api_blueprint]
