from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.order import Order, OrderDetail
from models.user import User
from db_connect import db
from myJWT import isTokenVaild, getUserEmail
from datetime import datetime
from pytz import timezone


bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/list', methods=['GET', 'POST'])
def order_list():
    """
    주문 목록
    """
    # 유효성 검증
    if (isTokenVaild() == False):  # 현재 쿠키의 토큰이 유효하지 않으면
        print("로그인 하세요.")
        return redirect("/login")  # 다시 로그인 페이지로
    
    if request.method == 'GET':    
        # token을 가져와 user 판별.
        user_email = getUserEmail()
        user_id = User.query.filter_by(email=user_email).first().id
        
        # 주문 목록 가져오기
        orders = Order.query.filter_by(user_id=user_id).all()

        context = {
            "order": []
        }

        

        for order in orders:
            order_details = OrderDetail.query.filter_by(order_id=order.id).all()
            result = {
                "order_id": order.id,
                "order_date": order.order_date,
                "order_address": order.order_address,
            }
            foods = []
            for order_detail_food in order_details:
                food = {
                    "id": order_detail_food.id,
                    "food_name": order_detail_food.food_name,
                    "food_price": order_detail_food.food_price,
                    "food_img": order_detail_food.food_img,
                }
                foods.append(food)
            result["food"] = foods
            context["order"].append(result)
        # print(context)

        return render_template("order_list.html", data=context)
    
@bp.route('/', methods=['GET', 'POST'])
def order():
    """
    주문
    """
    # 유효성 검증
    if (isTokenVaild() == False):  # 현재 쿠키의 토큰이 유효하지 않으면
        print("로그인 하세요.")
        return redirect("/login")  # 다시 로그인 페이지로
    
    if request.method == 'POST':
        # token을 가져와 user 판별.
        user_email = getUserEmail()
        user_id = User.query.filter_by(email=user_email).first().id

        data = request.get_json()
        shop_id = data['cart_list'][0]['shop_id']
        order_date = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
        total_price = data['total_price']    

        print('user_id, shop_id, order_date, total_price : ', user_id, shop_id, order_date, total_price)
        [ print("data['food'] : ", i) for i in data['cart_list'][0]['food']] 
        # TODO: shop_id
        # order = Order(user_id=user_id, shop_id=shop_id, order_date=order_date, total_price=total_price)
        # db.session.add(order)

        for food_data in data['cart_list'][0]['food']:
            food_name = food_data['food_name']
            food_count = food_data['food_count']
            food_price = food_data['food_price']
            print('food_name : ', food_name)
            print('food_count : ', food_count)
            print('food_price : ', food_price)
            # order_detail = OrderDetail(order=order, food_name=food_name, food_count=food_count, food_price=food_price)
            # db.session.add(order_detail)

        # db.session.commit()

        return redirect(url_for('order.order_list'))
    
    # TODO: cart_data 가져오기로 변경
    context = {
        'cart_list': [
            {
                "shop_id": 1,
                "shop_name": "테스트음식",
                'food':[
                    {
                    'id':1,
                    'food_name':'테스트',
                    'food_price':6000,
                    'food_count' : 2
                    },
                    {
                    'id':2,
                    'food_name':'테스트2',
                    'food_price':3000,
                    'food_count' : 2,
                    },
                    {
                    'id':3,
                    'food_name':'테스트3',
                    'food_price':1000,
                    'food_count' : 2
                    }
                ]
            },
        ]
    }

    total_price = 0  # 총 가격 초기화

    for cart in context['cart_list']:
        for food in cart['food']:
            # 각 음식 항목의 수량과 가격을 곱하여 총 가격을 계산
            total_price += food['food_price'] * food['food_count']

    context['total_price'] = total_price
    
    return render_template("order.html", data=context)