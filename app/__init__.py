from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate() 

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # or set SECRET_KEY directly if not using config file
    app.config['SECRET_KEY'] = 'your-secret-key'  # Ensure this is set

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # User loader for Flask-Login
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register your blueprint
    from . import routes
    app.register_blueprint(routes.bp)

    return app
