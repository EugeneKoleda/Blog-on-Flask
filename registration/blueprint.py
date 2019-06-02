from app import app, db

from flask import Blueprint, render_template, request, redirect, url_for

from app import user_datastore

from models import User, Role


registration = Blueprint('registration', __name__, template_folder='templates')


@registration.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'GET':
        return render_template('registration/index.html')
    else:
        full_name = request.form['full_name']
        email = request.form['email']
        login = request.form['login']
        password = request.form['password']

    user_email = User.query.filter(User.email == email).first()
    user_login = User.query.filter(User.login == login).first()

    if user_email and user_email.email == email:
        return render_template('registration/index.html', error_email="This email is already exist!")

    elif user_login and user_login.login == login:
        return render_template('registration/index.html', error_login="This login is already exist!")

    elif full_name and email and login and password:
        try:
            user = user_datastore.create_user(full_name=full_name, email=email, login=login, password=password)
            role = Role.query.filter(Role.name == 'user').first()
            user_datastore.add_role_to_user(user, role)
            db.session.add(user)
            db.session.commit()

        except:
            return render_template('registration/index.html', error_message="Something wrong, please try again!")


    return redirect(url_for('security.login'))



