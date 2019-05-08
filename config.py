import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    #  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:233@localhost:3306/talentsite?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
