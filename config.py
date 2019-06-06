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

    SECURITY_POST_LOGIN_VIEW = '/blog'
    SECURITY_POST_LOGOUT_VIEW = '/blog'

    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = "6LcvjqcUAAAAANrzXAh1m7GxNzfT7nYDE-z6lJL7"
    RECAPTCHA_SECRET_KEY = "6LcvjqcUAAAAAPEaRX4M3yBvhv1sEfALoWCLg4_N"
    RECAPTCHA_THEME = "light"
    RECAPTCHA_TYPE = "image"
    RECAPTCHA_SIZE = "normal"
    RECAPTCHA_RTABINDEX = 10



