# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/tienda_gomotos_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
