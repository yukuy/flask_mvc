# __init__.py o main.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)  # Cargar configuraciones desde la clase Config
db = SQLAlchemy(app)

from app import views


# Importa tus blueprints o rutas aquí
# from yourapplication import routes

if __name__ == '__main__':
    app.run(debug=True)
