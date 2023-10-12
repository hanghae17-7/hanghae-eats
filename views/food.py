from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.food import Food


bp = Blueprint('food', __name__, url_prefix='/food')

@bp.route('/<int:store_id>/', methods=['GET', 'POST'])
def food(store_id):
    if request.method == 'GET':    
        print('store_id : ', store_id)
        # store_list 가져오기
        foods = Food.query.filter_by(store_id=store_id).all()
        
        return render_template("food.html", data=foods, store_id=store_id)
    

# @bp.route('/', methods=['GET', 'POST'])
# def food():
    
#     if request.method == 'GET':
    
#         foods =Food.query.all()
#         print(foods)
#         return render_template('food.html', data=foods)

#     else:
#         print("else")
#         return None
