from src.modules.auth.models import User, db
from src.modules.auth.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, flash, redirect, url_for

auth_blueprint = Blueprint(
    "auth", __name__, template_folder="templates", url_prefix="/auth"
)


@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    email = None
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email:
            if check_password_hash(email.password, form.password.data):
                login_user(email)
                flash("Login Successful")
                return redirect(url_for('dashboard.dashboard'))
            else:
                flash("Wrong password for account")
        else:
            flash("User doesn't exists")

    return render_template("login.html", email=email, form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect((url_for('main.main')))


@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    username = None
    email = None
    form = RegisterForm()

    if form.validate_on_submit():
        filter_email = User.query.filter_by(email=form.email.data).first()
        if filter_email is None:
            hash_pw = generate_password_hash(form.password.data, "sha256")
            user = User().create(
                name=form.firstname.data,
                lastname=form.lastname.data,
                username=form.username.data,
                email=form.email.data,
                password=hash_pw
            )
            flash("New User created")
            return redirect(url_for('auth.login'))

    return render_template("signup.html", email=email, username=username, form=form)

