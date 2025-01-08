from flask import Flask, render_template, request

from markupsafe import escape
 
app = Flask(__name__)

@app.route("/")
def Index():    
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def Register_user():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/user")
def user_account():
    return "User account"

@app.route("/user/<username>")
def show_user_profile(username):
    return f'User {escape(username)}'



if __name__ == '__main__':
    app.run(debug=True)