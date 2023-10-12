from db_connect import db
from sqlalchemy.orm import relationship


# TODO: shop_id 추가, total_price 추가
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # shop_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    # total_price = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.String(30), nullable=False)


    def __init__(self, user_id, shop_id, order_date):
        self.user_id = user_id
        self.shop_id = shop_id
        self.order_date = order_date

# TODO: food_price 수정, 
class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    food_name = db.Column(db.String, nullable=False)
    food_count = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False) # food_price 수정
    # food_img = db.Column(db.String(50))

    def __init__(self, order_id, food_name, food_count, price):
        self.order_id = order_id
        self.food_name = food_name
        self.food_count = food_count
        self.price = price
    # TODO: 지우기
    order = relationship('Order')  # Order 모델과의 관계를 설정