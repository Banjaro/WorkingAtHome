from flask import Flask
 
 
def create_app(config):
    app = Flask(__name__)
    register_blueprints(app)
    return app
 
 
def register_blueprints(app):
 
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)