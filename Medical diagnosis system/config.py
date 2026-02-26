import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # ML Models Paths
    DISEASE_MODEL_PATH = os.path.join(basedir, 'models', 'disease_model.pkl')
    CLUSTER_MODEL_PATH = os.path.join(basedir, 'models', 'cluster_model.pkl')
    DATASET_PATH = os.path.join(basedir, 'dataset.csv')
    
    # AI API Keys
    GROK_API_KEY = os.environ.get('GROK_API_KEY')
    
    # Pagination
    POSTS_PER_PAGE = 10
