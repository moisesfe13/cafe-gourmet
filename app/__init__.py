from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # Substitua por uma chave secreta segura

    # Importa as rotas
    from .routes import app

    return app
