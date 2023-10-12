import os
from flask import Flask
from flask_migrate import Migrate
from db_connect import db
import config

# 4. views 폴더에 만든 파일이름
from views import index, signup, login, order, myaccount, storelist, cart, store, food


def create_app():
    app = Flask(__name__)

    # db 연결
    app.config.from_object(config)  # config에서 가져온 파일 사용
    db.init_app(app)  # SQLAlchemy 객체를 app 객체와 이어준다.
    Migrate().init_app(app, db)

    app.secret_key = os.urandom(177)  # flash 사용으로 session secret key 필요

    with app.app_context():
        db.create_all()

    # 5. 만든 기능 작성 blueprint에 등록
    app.register_blueprint(index.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(order.bp)
    app.register_blueprint(myaccount.bp)
    app.register_blueprint(storelist.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(store.bp)
    app.register_blueprint(food.bp)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
