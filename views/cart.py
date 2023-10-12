from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.cart import Cart
from models.user import User
from models.store import Store
from models.food import Food
# from models.food import Food
from db_connect import db
from myJWT import isTokenVaild, getUserEmail  # 토큰 유효성 검증 함수 사용하기 위해

from datetime import datetime
from pytz import timezone


bp = Blueprint('cart', __name__, url_prefix='/cart')

@bp.route('/', methods=['GET', 'POST'])
def cart():
    if request.method == 'GET':
        # 유효성 검증
        if (isTokenVaild() == False):  # 현재 쿠키의 토큰이 유효하지 않으면
            print("로그인 하세요.")
            return redirect("/login")  # 다시 로그인 페이지로
        
        context = {
            'cart': []
        }
                
        # token을 가져와 user 판별.
        user_email = getUserEmail()
        user_id = User.query.filter_by(email=user_email).first().id
        context['user_id'] = user_id
        print('cart_user_id : ', user_id)
        
        cart_list = Cart.query.filter_by(user_id=user_id).all()

        
        for cart in cart_list:
            food = Food.query.filter_by(id=cart.food_id).first()
            shop = Store.query.filter_by(id=cart.shop_id).first()
            context['cart'].append({
                'cart_id': cart.id,
                'shop_id': shop.id,
                'shop_name': shop.name,
                'food_id': food.id,
                'food_name': food.name,
                'food_image': food.image,
            })
        
        
        return render_template("cart.html", data=context)
    elif request.method == 'POST':

        return
    
    elif request.method == 'DELETE':

        return None