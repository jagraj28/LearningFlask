from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)

