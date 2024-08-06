from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

# Create an instance of SQLAlchemy to manage database operations
db = SQLAlchemy()
# Creating an instance of Migrate to handle database migrations
migrate = Migrate()
# define name of database file
DB_NAME = "grocery_list.db"

# Function to create and configure Flask application
def create_app():
    app = Flask(__name__) #initializing the flask application
    app.config['SECRET_KEY'] = 'Mburu_R' #setting secret key for session mgmgt and security
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #setting database uri for SQLAlchemy
    
    db.init_app(app) # initialize the database
    migrate.init_app(app, db) #initialize migration support with the app and database
    
    #import blueprints
    from .login import login
    
    #register the blueprints with the app
    app.register_blueprint(login, url_prefix='/login')
    
    # Create database tables if it doesn't exist
    with app.app_context():
        db.create_all()
        
    # set up the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #specify the login view
    login_manager.init_app(app) #Initializing login manager with the app
    
    # user loader by their ID
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) # query the database for the user with the given ID
    
    return app # return the configured Flask app instance

# function to create the database file if it doesn't exist
def create_database(app):
    if not path.exists('store/' + DB_NAME): #checks if the database file already exists
        db.create_all(app=app) #create all database tables
        print('Created Database!') #prints a message indicating the database was created