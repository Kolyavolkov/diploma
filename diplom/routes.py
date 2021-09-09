from flask import render_template, url_for, flash, redirect
from diplom import app, db, bcrypt
from diplom.forms import RegistrationForm, LoginForm 
from diplom.models import User, Post
 
posts = [
    {
        "author": "Kolya Volkov",
        "title": "Blog post 1",
        "content": "First post ever",
        "date": "September 6, 2021 "
    },
    {
        "author": "Dick Tracy",
        "title": "Blog post 2",
        "content": "Second post ever",
        "date": "September 7, 2021 "
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts )

@app.route("/help")
def help():
    return render_template("help.html", title="help")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pass = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hash_pass)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    #if form.validate_on_submit():
    return render_template("login.html", title="Login", form=form)