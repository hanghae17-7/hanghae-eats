from db_connect import db # 1. 상단에 db_connect db import하기


# 2. 모델 정의하기.
# 3. app에 가서 model import 하기
class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)