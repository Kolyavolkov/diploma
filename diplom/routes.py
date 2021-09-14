from flask import render_template, url_for, flash, redirect, request
from diplom import app, db, bcrypt
from diplom.forms import RegistrationForm, LoginForm
from diplom.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        "author": "Kolya Volkov",
        "title": "Blog post 1",
        "content": "First post ever",
        "date": "September 6, 2021 ",
    },
    {
        "author": "Dick Tracy",
        "title": "Blog post 2",
        "content": "Second post ever",
        "date": "September 7, 2021 ",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/help")
def help():
    return render_template("help.html", title="help")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pass = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            username=form.username.data, email=form.email.data, password=hash_pass
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login failed. Please check email or password.", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file)
