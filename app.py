from flask import Flask, render_template
from app.routes.options import options_bp

def create_app():
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
    app.register_blueprint(options_bp, url_prefix='/api')

    @app.route("/", methods=["GET"])
    def index():
        return render_template('index.html')

    @app.route("/black_scholes", methods=["GET"])
    def black_scholes():
        return render_template('black_scholes.html')

    @app.route("/binomial", methods=["GET"])
    def binomial():
        return render_template('binomial.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)

