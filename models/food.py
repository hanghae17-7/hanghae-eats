from db_connect import db

# shop, fname, finfo, fprice, furl = 찬희님
# contents, title, image_url = store
class Food(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    shop = db.Column(db.String, nullable=False) 
    fname = db.Column(db.String, nullable=False) 
    finfo = db.Column(db.String, nullable=False) 
    fprice = db.Column(db.Integer, nullable=False) 
    furl = db.Column(db.String, nullable=False)