from flask import Flask
from app.routes.options import options_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(options_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
