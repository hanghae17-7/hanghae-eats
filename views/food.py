from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.food import Food
from db_connect import db


bp = Blueprint('food', __name__, url_prefix='/food')

@bp.route('/', methods=['GET', 'POST'])
def store():
    if request.method == 'GET':    
        context = {
            "food": []
        }

        # store_list 가져오기
        Foods = Food.query.all()
        
        for food in Foods:
            context['food'].append(
                {
                    "id": food.id,
                    "shop": food.shop,
                    "fname": food.fname,
                    "finfo": food.finfo,
                    "fprice": food.fprice,
                    "furl": food.furl
                }
            )

        
        return render_template("food.html", data=context)
    
