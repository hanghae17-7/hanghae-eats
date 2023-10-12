from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.store import Store


bp = Blueprint('store', __name__, url_prefix='/store')

@bp.route('/', methods=['GET', 'POST'])
def store():
    if request.method == 'GET':    

        # store_list 가져오기
        store_list = Store.query.all()
        
        return render_template("stores.html", data=store_list)
