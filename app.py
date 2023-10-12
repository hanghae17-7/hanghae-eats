from flask import Flask
from flask_migrate import Migrate
from db_connect import db
import config
# 4. views 폴더에 만든 파일이름
from views import index, signup, login, order


def create_app():
    app = Flask(__name__)

    # db 연결
    app.config.from_object(config)  # config에서 가져온 파일 사용
    db.init_app(app)  # SQLAlchemy 객체를 app 객체와 이어준다.
    Migrate().init_app(app, db)

    with app.app_context():
        db.create_all()

    # 5. 만든 기능 작성 blueprint에 등록
    app.register_blueprint(index.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(order.bp)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
