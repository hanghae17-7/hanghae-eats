from flask import Blueprint, render_template, request, url_for, session, redirect, flash
from models.user import User
from db_connect import db


bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    """
    메인 페이지
    """
    return render_template('index.html')