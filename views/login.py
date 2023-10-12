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
            # jwt 토큰 생성
            token = encode(payload, JWT_SECRET_KEY,
                           algorithm='HS256')

            # 응답 jsonify 객체 반환
            return jsonify({'result': 'success', 'token': token})

        else:
            print("비밀번호가 틀림")
            return jsonify({'result': 'fail', 'error': "비밀번호가 틀렸습니다."})

    print("get 요청시")
    return render_template('login.html')


def validate_login(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return True
    return False
