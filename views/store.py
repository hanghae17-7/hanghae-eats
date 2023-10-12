from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.store import Store
from db_connect import db
from myJWT import isTokenVaild, getUserEmail
from datetime import datetime
from pytz import timezone


bp = Blueprint('store', __name__, url_prefix='/store')

@bp.route('/', methods=['GET', 'POST'])
def store():
    if request.method == 'GET':    
        context = {
            "store": []
        }

        # store_list 가져오기
        store_list = Store.query.all()

        for store in store_list:
            context['store'].append(
                {
                    "id": store.id,
                    "title": store.title,
                    "contents": store.contents,
                    "image_url": store.image_url,
                }
            )

        
        return render_template("store.html", data=context)
    
