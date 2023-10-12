from db_connect import db
from sqlalchemy.orm import relationship

# from models.food import Food
# flask run - 자동으로 db 테이블 형성

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    fname = db.Column(db.String(100), nullable=False)
    fprice = db.Column(db.Integer, nullable=False)
    finfo = db.Column(db.String(10000), nullable=False)
    furl = db.Column(db.String, nullable=False)

    def __init__(self, store_id, fname, fprice, finfo, furl):
        self.store_id = store_id
        self.fname = fname
        self.fprice = fprice
        self.finfo = finfo
        self.furl = furl


# food1 = Food(store_id=1, 
#             fname="후라이드 치킨", fprice=19000,
#             finfo="환상의 바삭함", furl="https://news.nateimg.co.kr/orgImg/it/2021/12/18/2021121800550_0.jpg")

# food2 = Food(store_id=1, 
#             fname="양념 치킨", fprice=21000,
#             finfo="환상의 고소함", furl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKg2-F6ZiWZiiZIke3U80HrkuZsTlrfcV3Yg&usqp=CAU")

# food3 = Food(store_id=1, 
#             fname="치즈가루 치킨", fprice=21000,
#             finfo="환상의 달달함", furl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY0Utdp7qMQwYg6DJBpMpeXQtE7CinD66BQQ&usqp=CAU")

# db.session.add(food1)
# db.session.add(food2)
# db.session.add(food3)

# db.session.commit()
