from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel
from flask_login import LoginManager
import cloudinary
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'sfsjfffehr4$#$@$@$%^^^$^%@$GG'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:phuc12345@localhost/newdata?charset=utf8mb4"
app.config['COMMENT_SIZE'] = 4

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
migrate = Migrate(app, db)
babel = Babel(app=app)
@babel.localeselector
def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        return 'vi'


cloudinary.config(cloud_name='dwgjmgf6o', api_key='963493837729524', api_secret='ra068pqFPrbpRrMDgE-Lua2hDZ8')

#1954052027hieu@ou.edu.vn

login = LoginManager(app=app)