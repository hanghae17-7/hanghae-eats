from flask import Blueprint, render_template, request, url_for, session, redirect 
from models.store import Store
from db_connect import db 

bp = Blueprint('store', __name__, url_prefix='/store') 


@bp.route('/', methods=['GET', 'POST'])
def store():
    if request.method == 'GET':
        return render_template('stores.html')