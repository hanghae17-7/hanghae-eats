from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from db_connect import db
import config
from models.store import Store

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
Migrate().init_app(app, db)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/stores')
def stores():
    store_list = Store.query.all()

    return render_template('stores.html', data=store_list)