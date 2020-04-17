from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "2a7a99b002192c5cdde859a03a018c0f"

posts = [   
    {
        'Author': 'Jagraj Singh',
        'Title': 'Blog Post 1',
        'Content': 'First Post Content',
        'Date': '16/04/2020'
    },
    {
        'Author': 'Kalraj Singh',
        'Title': 'Blog Post 2',
        'Content': 'Second Post Content',
        'Date': '18/04/2020',
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
        flash(f"Account created for {form.username.data}!", "sucess")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)

if __name__ == '__main__':
    app.run(debug=True)

