from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.cart import Cart
from db_connect import db

from datetime import datetime
from pytz import timezone

bp = Blueprint('cart', __name__, url_prefix='/cart')

@bp.route('/', methods=['GET', 'POST'])
def cart():
    if request.method == 'GET':
        # TODO: 로그인한 유저
        cart_list = Cart.query.filter(user_id=1).all()
        
        context = {

        }
        return render_template("cart.html", data=context)
    elif request.method == 'POST':

        return
    
    elif request.method == 'DELETE':

        return None