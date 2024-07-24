from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/myhome')
def myhome():
    return "Hello, Flask! this is Home Page"

@app.route('/register')
def register():
    return "Hello, Flask! this is registration page"

@app.route('/admin')
def admin():
    return "Hello, Flask! this is Admin page"

@app.route('/user')
def user():
    return "Hello, Flask! this is user page"


@app.route('/about')
def about():
    return "Hello, Flask! this is About page"

@app.route('/contact')
def contact():
    return "Hello, Flask! this is Contact page"


if __name__ == '__main__':
    app.run(debug=True)
