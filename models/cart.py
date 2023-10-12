from db_connect import db

# TODO: shop_id 추가
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # shop_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    # food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    food_count = db.Column(db.Integer, nullable=False)
