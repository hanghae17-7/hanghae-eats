from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.order import Order, OrderDetail
from models.user import User
from models.cart import Cart
from models.food import Food
from models.store import Store
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
        print('order_data : ', data)
        store_id = data['cart_list'][0]['store_id']
        order_date = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
        total_price = data['total_price']
        order_address = data['address']
        print("order_address : ", order_address)

        print('user_id, store_id, order_date, total_price : ', user_id, store_id, order_date, total_price)
        [ print("data['food'] : ", i) for i in data['cart_list'][0]['food']] 

        order = Order(user_id=user_id, store_id=store_id, order_address=order_address, order_date=order_date, total_price=total_price)
        db.session.add(order)
        db.session.commit()

        latest_order = Order.query.order_by(Order.id.desc()).first()
        for food_data in data['cart_list'][0]['food']:
            food_name = food_data['food_name']
            food_count = food_data['food_count']
            food_price = food_data['food_price']
            food_image = food_data['food_image']
            print('food_name : ', food_name)
            print('food_count : ', food_count)
            print('food_price : ', food_price)

            order_detail = OrderDetail(order_id=latest_order.id, food_name=food_name, food_count=food_count, food_price=food_price, food_img=food_image)
            db.session.add(order_detail)

        db.session.commit()

        # 주문이 완료되면 cart 테이블의 데이터를 삭제
        # Cart.query.delete()

        return redirect(url_for('order.order_list'))
    
    elif request.method == "GET":
        context = {
            'cart_list' : []
        }

        # token을 가져와 user 판별.
        user_email = getUserEmail()
        user_id = User.query.filter_by(email=user_email).first().id

        cart_list = Cart.query.filter_by(user_id=user_id).all()
        # cart_list에 담긴 food 정보 찾기
        foods = []
        for cart in cart_list:
            food_id = cart.food_id 
            food = Food.query.filter_by(id=food_id).first()
            store_id = cart.store_id
            store = Store.query.filter_by(id=store_id).first()
            foods.append({
                'id':food.id,
                'food_name': food.fname,
                'food_price': food.fprice,
                "food_image": food.furl,
                'food_count' : cart.food_count,
            })

            context['cart_list'].append({
                "store_id": store.id,
                "store_name": store.title,
                "food": foods,
            })
            


        total_price = 0  # 총 가격 초기화

        for cart in context['cart_list']:
            for food in cart['food']:
                # 각 음식 항목의 수량과 가격을 곱하여 총 가격을 계산
                total_price += food['food_price'] * food['food_count']

        context['total_price'] = total_price
        
        return render_template("order.html", data=context)