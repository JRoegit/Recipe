from flask import Flask
from app.routes import main_bp
from app.api.recipes import recipes_bp
from app.api.users import users_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(users_bp)

    return app