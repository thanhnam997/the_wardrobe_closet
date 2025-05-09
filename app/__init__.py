from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .extensions import db 
from .models import CartItem

login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # User loader
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Blueprint
    from . import routes
    app.register_blueprint(routes.bp)

    # Inject cart count
    @app.context_processor
    def inject_cart_count():
        from flask_login import current_user
        if current_user.is_authenticated:
            count = CartItem.query.filter_by(user_id=current_user.id).count()
        else:
            count = 0
        return dict(cart_count=count)

    return app
