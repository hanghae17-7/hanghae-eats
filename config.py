import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
JWT_SECRET_KEY = "hanghaeJWT"  # jwt 시크릿 키

