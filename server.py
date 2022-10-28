from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

from users import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all_users())

@app.route('/create_user')
def create():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def add():
    User.new_user(request.form)
    return redirect('/users')


#ALWAYS INCLUDE!! 
if __name__=="__main__":
    app.run(debug=True) 