from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from backend.config import config


#TODO: Put more models here, such as ones for Dash etc
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()




def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = config.SECRET_KEY
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # sets sqlalchemy modifications to false, https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from database.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(str(user_id))

    with app.app_context():
        from backend.auth import auth as auth_blueprint
        from main import main as main_blueprint

        # blueprint for auth routes in our app
        app.register_blueprint(auth_blueprint)

        # blueprint for non-auth parts of app
        app.register_blueprint(main_blueprint)

        # Create Database Models
        db.create_all()

        print(User.query.filter_by(id='b8632881').first())


        # #NOTE: I put temp variable a so python wont get salty :smile:
        # if app.config['FLASK_ENV'] == 'development':
        #     # Do stuff for dev
        #     a = 2
        # elif app.config['FLASK_ENV'] == 'production':
        #     # Do stuff for production
        #     a = 1
        # else:
        #     # Do stuff for local
        #     a = 3

        return app

