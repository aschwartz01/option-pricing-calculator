from flask import Flask, render_template
from app.routes.options import options_bp

def create_app():
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
    app.register_blueprint(options_bp, url_prefix='/api')

    @app.route("/", methods=["GET"])
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
