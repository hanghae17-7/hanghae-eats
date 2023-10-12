from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.order import Order, OrderDetail


bp = Blueprint('order', __name__, url_prefix='/order')

@bp.route('/', methods=['GET', 'POST'])
def order():
    if request.method == 'GET':    
        login_user = 1 # session or jwt or parameter

        context = {
            "order": []
        }

        # 주문 목록 가져오기
        orders = Order.query.filter_by(user_id=1).all()

        for order in orders:
            order_details = OrderDetail.query.filter_by(order_id=order.id).all()
            result = {
                "order_id": order.id,
                "order_date": order.order_date
            }
            foods = []
            for order_detail in order_details:
                food = {
                    "id": order_detail.id,
                    "food_name": order_detail.food_name,
                    "food_price": order_detail.price,
                    # "food_img": order_detail.food_img,
                }
                foods.append(food)
            result["food"] = foods
            context["order"].append(result)
        print(context)

        return render_template("order.html", data=context)
    
    elif request.method == 'POST':

        return None