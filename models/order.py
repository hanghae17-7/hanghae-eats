from db_connect import db
from sqlalchemy.orm import relationship



class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    order_address = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.String(30), nullable=False)



class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    food_name = db.Column(db.String, nullable=False)
    food_count = db.Column(db.Integer, nullable=False)
    food_price = db.Column(db.Integer, nullable=False)
    food_img = db.Column(db.String(50))

