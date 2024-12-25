from flask import render_template, Blueprint


main=Blueprint('main',__name__)
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/user')
def user():
    return 'this is a user page'