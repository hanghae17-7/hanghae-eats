from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.order import Order, OrderDetail
from models.user import User
from db_connect import db
from datetime import datetime
from models.food import Food

bp = Blueprint('foods', __name__, url_prefix='/food')

@bp.route('/', methods=['GET', 'POST'])
def food():
    
    if request.method == 'GET':
    
        foods =Food.query.all()
        print(foods)
        return render_template('food.html', data=foods)

    else:
        print("else")
        return None
