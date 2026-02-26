from flask import Flask
from extensions import db, migrate, login

from config import config
import os


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Import models here to ensure they are registered
    from models import user, lesson, challenge, progress, badge


    # Register Blueprints
    from routes.auth_routes import auth_bp
    from routes.lesson_routes import lesson_bp
    from routes.challenge_routes import challenge_bp
    from routes.ai_routes import ai_bp
    from routes.leaderboard_routes import leaderboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(lesson_bp, url_prefix='/lessons')
    app.register_blueprint(challenge_bp, url_prefix='/challenges')
    app.register_blueprint(ai_bp, url_prefix='/ai')
    app.register_blueprint(leaderboard_bp, url_prefix='/leaderboard')

    # Custom Error Pages
    @app.errorhandler(404)
    def not_found_error(error):
        return "404 - Not Found", 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return "500 - Internal Server Error", 500

    return app

app = create_app(os.getenv('FLASK_CONFIG', 'default'))

if __name__ == '__main__':
    app.run()
