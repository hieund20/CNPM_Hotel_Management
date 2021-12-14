from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel

app = Flask(__name__)
app.secret_key = 'sfsjfffehr4$#$@$@$%^^^$^%@$GG'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Duchieu200301@localhost/hotel_management_db?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
babel = Babel(app=app)
@babel.localeselector
def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        return 'vi'



