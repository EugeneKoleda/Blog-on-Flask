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



    if full_name and email and login and password:
        try:
            user = user_datastore.create_user(full_name=full_name, email=email, login=login, password=password)
            role = Role.query.filter(Role.name == 'user').first()
            user_datastore.add_role_to_user(user, role)
            db.session.add(user)
            db.session.commit()

        except:
            return render_template('registration/index.html', error_message="This login or email already exist!")


    return redirect(url_for('security.login'))



