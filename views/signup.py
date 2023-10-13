# 1. import Blueprint
from flask import Blueprint, jsonify, render_template, request, url_for, session, redirect, flash
from models.user import User
from db_connect import db
from encryptor import check_hash, encrypt
# 2. Blueprint 초기화
# 'signup': Blueprint의 이름
#  url_prefix='/signup': signup으로 시작하는 모든 URL이 묶임.
bp = Blueprint('signup', __name__, url_prefix='/signup')


# 3. app을 bp로 교체
@bp.route('/', methods=['GET', 'POST'])
def signUp():
    print("signup페이지 이동")
    if request.method == 'POST':
        # print(request.form)
        username = request.form['username']
        nickname = request.form['nickname']
        email = request.form['email']
        password = request.form['password']

        # print(username, nickname, email, password)
        if checkEmailDuplicate(email):
            # 중복 이메일 있음
            print("이메일 중복", "error")
            return jsonify({'result': 'false', 'error': '이미 가입한 이메일입니다.'})
        elif checkNicknameDuplicate(nickname):
            print("닉네임 중복", "error")
            return jsonify({'result': 'false', 'error': '존재하는 닉네임입니다.'})
        else:
            # 비밀번호 암호화
            print("회원가입 유효성 검증 완료")
            hashedPassword = encrypt(password=password)
            print("해시된 비밀번호 : ", hashedPassword)
            newUser = User(username=username, nickname=nickname,
                           email=email, password=hashedPassword)
            db.session.add(newUser)
            db.session.commit()
            print('회원가입이 완료되었습니다!', 'success')
            return jsonify({'result': 'success'})

    print("get 요청시")
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
