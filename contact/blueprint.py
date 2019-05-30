from app import app, db

from flask import Blueprint, render_template, request, redirect, url_for
from flask_mail import Mail, Message

from config import Configuration


from models import Messages

# from .forms import PostForm


contact = Blueprint('contact', __name__, template_folder='templates')
mail = Mail()
mail.init_app(app)

@contact.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'GET':
        return render_template('contact/index.html')
    else:
        name = request.form['name']
        email = request.form['email']
        title = request.form['title']
        text = request.form['message']

    if name and email and title and text:
        try:
            message = Messages(name=name, title=title, email=email, text=text)
            db.session.add(message)
            db.session.commit()
        except:
            print('Something wrong! Please, try again.')
            return render_template('contact/index.html')

    feedback_message = Message('Thank you for your attention!', sender=Configuration.ADMINS[0],
              recipients=[email])
    feedback_message.body = render_template("contact/feedback_message.txt",
            name=name)

    customer_message = Message(title, sender=Configuration.ADMINS[0],
                               recipients=[Configuration.ADMINS[0]])
    customer_message.body = render_template("contact/customer_message.txt",
                                            name=name, title=title, email=email, text=text)

    with app.app_context():
        mail.send(feedback_message)
        mail.send(customer_message)

    return redirect(url_for('index'))
