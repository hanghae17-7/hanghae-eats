from db_connect import db  # 1. 상단에 db_connect db import하기

# 2. 모델 정의하기.
# 3. app에 가서 model import 하기


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    nickname = db.Column(db.String, unique=True, nullable=False)  # 중복 x
    email = db.Column(db.String, unique=True, nullable=False)  # 중복 x
    # 암호화 구현?
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f' {self.id} {self.nickname} '
