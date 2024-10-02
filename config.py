import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

       # Add database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add any other configuration variables your app might need
    DEBUG = os.environ.get('FLASK_DEBUG') or False
