import os

class Config():
    SECRET_KEY = "b1bfdfa7de598f29a8ff605c93a9e16c"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "testuserflask1010@gmail.com"
    MAIL_PASSWORD = "testuserpassword10101"
