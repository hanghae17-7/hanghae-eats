from flask import Blueprint, render_template, request, url_for, session, redirect
from models.order import Order, OrderDetail

# 1 임포트
from myJWT import isTokenVaild  # 토큰 유효성 검증 함수 사용하기 위해


bp = Blueprint('storelist', __name__, url_prefix='/storelist')


@bp.route('/', methods=['GET'])
def storeList():
    # 2 유효성 검증
    if (isTokenVaild() == False):  # 현재 쿠키의 토큰이 유효하지 않으면
        return redirect("/login")  # 다시 로그인 페이지로

    return render_template("storelist.html")
