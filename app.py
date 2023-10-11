from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from db_connect import db
import config

from models.song import Song # 3.

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
Migrate().init_app(app, db)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """
    메인 페이지
    """
    return render_template('index.html')



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
        "song_list" : song_list
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
    song = Song(username=username_receive, title=title_receive, artist=artist_receive, image_url=image_url_receive)
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