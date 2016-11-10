import os # is instantiated for used in database configuration
WTF_CSRF_ENABLED = True
SECRET_KEY = "you-will-never-guess"

OPENID_PROVIDERS = [
    {'name': 'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo','url':'https://me.yahoo.com'},
    {'name': 'AOL','url':'http://openid.aol.com/<username>'},
    {'name': 'Flickr','url':'http://www.flickr.com/<username>'},
    {'name': 'MyOpenId','url':'https://www.myopenid.com'}
]
#-----------------------------------------------------------------------------
# database configuration section
basedir = os.path.abspath(os.path.dirname(__file__))
#this is the path of the database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#Is the folder where is stored the SQLAlchemy-migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#event system of Flask-SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = True
#-----------------------------------------------------------------------------