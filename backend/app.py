from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config
from extensions import db
from routes.auth import auth_bp
from routes.rooms import rooms_bp
from routes.bookings import bookings_bp
from models import User 
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_url_path="/", static_folder="./client/dist")
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": Config.CORS_ORIGINS}})

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(rooms_bp)
app.register_blueprint(bookings_bp)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.errorhandler(404)
def not_found(err):
    return app.send_static_file("index.html")



if __name__ == '__main__':

    app.run(debug=False, port=5000)