from flask import Flask
from src.main.routes.routes import user_route_bp

app = Flask(__name__)

#register Blueprints
app.register_blueprint(user_route_bp)
