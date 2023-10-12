from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.user import User
from db_connect import db


bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_login(username, password):
            # jwt 토큰?

            return redirect(url_for('/storelist')) # TODO: mainpage.함수명 수정
        else:
            error = '비밀번호가 틀렸습니다.'
            return render_template('login.html', error=error)
    return render_template('login.html')


def validate_login(email, password):
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return True
    return False