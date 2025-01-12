from flask import Flask
from ..server.routes.routes import phrase_route_bp, word_route_bp

app = Flask(__name__)

app.register_blueprint(phrase_route_bp)
app.register_blueprint(word_route_bp)