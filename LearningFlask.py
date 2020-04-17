from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import User, Post

app = Flask(__name__)
app.config["SECRET_KEY"] = "2a7a99b002192c5cdde859a03a018c0f"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)

posts = [   
    {
        'author': 'Jagraj Singh',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '16/04/2020'
    },
    {
        'author': 'Kalraj Singh',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '18/04/2020',
    }   
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful!", 'danger')
    return render_template("login.html", title="login", form=form)

if __name__ == '__main__':
    app.run(debug=True)

