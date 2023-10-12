from db_connect import db

# shop, fname, finfo, fprice, furl = 찬희님
# contents, title, image_url = store
class Store(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String, nullable=False) 
    contents = db.Column(db.String, nullable=False) 
    image_url = db.Column(db.String, nullable=False) 