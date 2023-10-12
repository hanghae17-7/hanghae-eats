from flask import Blueprint, render_template
from models.user import User


bp = Blueprint('myaccount', __name__, url_prefix='/myaccount')


@bp.route('/')
def myaccount():
    # email 받음
    email = "test@test"
    user = User.query.filter_by(email=email).first()
    return render_template('myaccount.html', user=user)
