import traceback

from flask import Flask, jsonify, render_template, request

from vulndesk import config
from vulndesk.db import initialize_database
from vulndesk.routes.admin_routes import bp as admin_bp
from vulndesk.routes.auth_routes import bp as auth_bp
from vulndesk.routes.file_routes import bp as file_bp
from vulndesk.routes.network_routes import bp as network_bp
from vulndesk.routes.system_routes import bp as system_bp
from vulndesk.routes.template_routes import bp as template_bp
from vulndesk.routes.ticket_routes import bp as ticket_bp
from vulndesk.routes.user_routes import bp as user_bp


def create_app():
    app = Flask(__name__)

    # LAB-SESSION-201: secreto de sesión débil/hardcodeado.
    app.secret_key = config.FLASK_SECRET_KEY

    initialize_database()

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(ticket_bp, url_prefix="/api")
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api")
    app.register_blueprint(file_bp, url_prefix="/api")
    app.register_blueprint(system_bp, url_prefix="/api")
    app.register_blueprint(network_bp, url_prefix="/api")
    app.register_blueprint(template_bp, url_prefix="/api")

    @app.after_request
    def permissive_cors(response):
        # LAB-CORS-201: política CORS deliberadamente permisiva.
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        return response

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.errorhandler(Exception)
    def expose_error(exc):
        # LAB-INFO-201: devuelve stack trace e información interna al cliente.
        return jsonify({
            "error": str(exc),
            "type": type(exc).__name__,
            "path": request.path,
            "traceback": traceback.format_exc(),
        }), 500

    return app
