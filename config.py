class Configuration():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:jeka2000@127.0.0.1:5432/test1'
    SECRET_KEY = 'jeka2000'


    ###  FLASK SECURITY  ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'


    ### FLASK FEEDBACk ###
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'jecich209'
    MAIL_PASSWORD = 'jeka2000'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    ADMINS = ['jecich209@gmail.com']


