from flask import Blueprint, render_template, request, url_for, session, redirect
from models.order import Order, OrderDetail


bp = Blueprint('storelist', __name__, url_prefix='/storelist')


@bp.route('/', methods=['GET'])
def order():

    return render_template("storelist.html")
