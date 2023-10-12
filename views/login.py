import datetime
from flask import Blueprint, jsonify, render_template, request, url_for, session, redirect, flash
from jwt import encode
import jwt
from config import JWT_SECRET_KEY
from models.user import User
from db_connect import db


bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and validate_login(email, password):  # 로그인이 유효한 경우

            # TypeError: Object of type datetime is not JSON serializable 해결하기 위해 string으로 변환
            dateString = (datetime.datetime.now()
                          + datetime.timedelta(seconds=60*60*1)).strftime("%Y-%m-%d %H:%M:%S")

            payload = {'email': email, 'expire': dateString}
            print(payload)

            token = encode(payload, JWT_SECRET_KEY,
                           algorithm='HS256')  # 응답 jsonify 객체 생성

            return jsonify({'result': 'success', 'token': token})
            # jwt 토큰?
        else:
            flash('비밀번호가 틀렸습니다', 'error')
            return render_template('login.html')

    return render_template('login.html')


def validate_login(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return True
    return False


@bp.route('/token-check')
def checkTokenVaild():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, JWT_SECRET_KEY,
                             algorithms=['HS256'])
        print(payload)
        return render_template('storelist.html')
    except jwt.ExpiredSignatureError:
        return render_template('login.html')
    except:
        return render_template('login.html')
