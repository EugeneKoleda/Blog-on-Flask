from app import app
from app import db
import view

from posts.blueprint import posts
from contact.blueprint import contact
from services.blueprint import services
from registration.blueprint import registration


app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(contact, url_prefix='/contact')
app.register_blueprint(services, url_prefix='/services')
app.register_blueprint(registration, url_prefix='/signin')



if __name__ == '__main__':
    app.run()
