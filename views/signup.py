# 1. import Blueprint 
from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.user import User
from db_connect import db

# 2. Blueprint 초기화
# 'signup': Blueprint의 이름
#  url_prefix='/signup': signup으로 시작하는 모든 URL이 묶임.
bp = Blueprint('signup', __name__, url_prefix='/signup')


# 3. app을 bp로 교체
@bp.route('/', methods=['GET', 'POST'])
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