from flask import Blueprint, render_template
from src.modules.auth.models import User, db
from flask_login import login_required, current_user

dashboard_blueprint = Blueprint(
    "dashboard", __name__, template_folder="templates", url_prefix=""
)

@dashboard_blueprint.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    id = current_user.id
    return render_template("dashboard.html", id=id)