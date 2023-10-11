import datetime
import os
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import *  # jwt 서드파티 등록
from jwt import encode
from werkzeug.security import generate_password_hash, check_password_hash

from db_connect import db
import config

from models.song import Song  # 3.

from models.user import User

SECRET_KEY = "hanghaeJWT"
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = os.urandom(24)


db.init_app(app)
Migrate().init_app(app, db)

with app.app_context():
    db.create_all()


jwt = JWTManager(app)  # jwtmanager 등록


@app.route('/')
def index():
    """
    메인 페이지
    """
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signUp():

    if request.method == 'POST':
        username = request.form['username']
        nickname = request.form['nickname']
        email = request.form['email']
        password = request.form['password']
        print(username, nickname, email, password)
        if checkEmailDuplicate(email):
            # 중복 이메일 있음
            print("이메일 중복", "error")
        elif checkNicknameDuplicate(nickname):
            print("닉네임 중복", "error")
        else:
            newUser = User(username=username, nickname=nickname,
                           email=email, password=password)
            db.session.add(newUser)
            db.session.commit()
            print('회원가입이 완료되었습니다!', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')


def checkNicknameDuplicate(nickname):
    if User.query.filter_by(nickname=nickname).first():
        print(User.query.filter_by(nickname=nickname).first())
        return True
    return False


def checkEmailDuplicate(email):
    if User.query.filter_by(email=email).first():
        return True
    return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and validate_login(email, password):  # 로그인이 유효한 경우

            dateString = (datetime.datetime.utcnow(  # TypeError: Object of type datetime is not JSON serializable 해결하기 위해
            ) + datetime.timedelta(seconds=60)).strftime("%Y-%m-%d %H:%M:%S")

            payload = {'email': email, 'expire': dateString
                       }
            token = encode(payload, SECRET_KEY,
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


@app.route('/token-check')
def checkTokenVaild():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)
        return render_template('storelist.html')
    except jwt.ExpiredSignatureError:
        return render_template('login.html')
    except:
        return render_template('login.html')

# @app.route('/profile')
# def profile():
#     if 'username'


###############
# 예시 데이터  #
###############


@app.route('/song')
def song():
    """
    음악 리스트 데이터
    """
    song_list = Song.query.all()
    context = {
        "song_list": song_list
    }
    return render_template('song.html', data=context)


@app.route("/music/create/")
def music_create():
    """
    음악 추가
    """
    # form에서 보낸 데이터 받아오기
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_url_receive = request.args.get("image_url")

    # 데이터를 DB에 저장하기
    song = Song(username=username_receive, title=title_receive,
                artist=artist_receive, image_url=image_url_receive)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for('song'))


@app.route("/music/delete/<id>/")
def music_delete(id):
    """
    음악 삭제
    """
    delete_music = Song.query.filter_by(id=id).first()

    db.session.delete(delete_music)
    db.session.commit()

    return redirect(url_for('song'))
