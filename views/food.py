from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.food import Food
from db_connect import db


bp = Blueprint('food', __name__, url_prefix='/food')

@bp.route('/<id>/', methods=['GET', 'POST'])
def food(id):
    if request.method == 'GET':    
        print('store_id : ', id)
        # store_list 가져오기
        foods = Food.query.filter_by(store_id=id).all()
        
        return render_template("food2.html", data=foods)
    

# @bp.route('/', methods=['GET', 'POST'])
# def food():
    
#     if request.method == 'GET':
    
#         foods =Food.query.all()
#         print(foods)
#         return render_template('food.html', data=foods)

#     else:
#         print("else")
#         return None
