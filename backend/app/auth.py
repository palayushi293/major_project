from flask import render_template, Blueprint,request,redirect,url_for


auth=Blueprint('auth',__name__)


@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def sign_post():
   
    email=request.form.get('email')
    password=request.form.get('password')
    print(email)
    
    print(password)
    return redirect(url_for('auth.login'))

