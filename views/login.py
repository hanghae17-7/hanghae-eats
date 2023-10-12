import datetime
from flask import Blueprint, jsonify, render_template, request, url_for, session, redirect, flash
from jwt import encode
import jwt
from config import JWT_SECRET_KEY
from models.user import User

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password', False)
        print(email)
        print(password)
        user = User.query.filter_by(email=email).first()

        if user and validate_login(email, password):  # 로그인이 유효한 경우
            # TypeError: Object of type datetime is not JSON serializable 해결하기 위해 string으로 변환
            dateString = (datetime.datetime.now()
                          + datetime.timedelta(60*60*1)).strftime("%Y-%m-%d %H:%M:%S")
            print("asdfasdf", flush=True)

            payload = {'email': email, 'expire': dateString}
            token = encode(payload, JWT_SECRET_KEY,
                           algorithm='HS256')  # 응답 jsonify 객체 생성
            return jsonify({'result': 'success', 'token': token})
            # jwt 토큰?
        else:
            print("2 else")
            flash('비밀번호가 틀렸습니다', 'error')
            return render_template('login.html')

    print("1 else")
    return render_template('login.html')


def validate_login(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return True
    return False


@bp.route('/token-check', methods=["GET"])
def checkTokenVaild():
    # 쿠키에서 토큰 불러옴
    token_receive = request.cookies.get('mytoken')

    print(token_receive)
    try:
        # decode
        payload = jwt.decode(token_receive, JWT_SECRET_KEY,
                             algorithms=['HS256'])
        print(payload)
        expire_time = datetime.datetime.strptime(
            payload['expire'], '%Y-%m-%d %H:%M:%S')

        print(expire_time)
        if expire_time < datetime.datetime.now():
            # 만료 시간이 현재 시각보다 이전인 경우 로그인 페이지로 리디렉션
            print("Token has expired")
            return redirect('/login')
        else:
            # 로그인 성공
            print("로그인성공")
            return redirect('/storelist')
    except:
        print("except")
        return redirect('/login')
