from flask import Blueprint, redirect, render_template
from models.user import User
from myJWT import getUserEmail, isTokenVaild


bp = Blueprint('myaccount', __name__, url_prefix='/myaccount')


@bp.route('/')
def myaccount():
    # 2 유효성 검증
    if (isTokenVaild() == False):  # 현재 쿠키의 토큰이 유효하지 않으면
        return redirect("/login")  # 다시 로그인 페이지로
    # 3 필요하다면,  user email 토큰에서 꺼내기
    email = getUserEmail()

    user = User.query.filter_by(email=email).first()
    return render_template('myaccount.html', user=user)
