from flask import render_template, url_for, flash, redirect
from diploma import app 
from diploma.forms import RegistrationForm, LoginForm 
from diploma.models import User, Post
 
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
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    #if form.validate_on_submit():
    return render_template("login.html", title="Login", form=form)