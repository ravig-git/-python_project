from flask import Flask, request, render_template
from models import Artist, Album, Song, Book, db
import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)


@app.route('/')
def home():
    # return render_template('index.html')
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 10:
        greeting = 'Доброе утро'
    elif now.hour >= 10 and now.hour < 18:
        greeting = 'Добрый день'
    elif now.hour >= 18 and now.hour < 24:
        greeting = 'Добрый вечер'
    else:
        greeting = 'Доброй ночи'
    return render_template('index.html', greeting=greeting)

@app.route('/php')
def php():
    return render_template('test.php')

@app.route('/user/<username>')
def user_profile(username):
    return f"Это профиль пользователя {username}"

@app.route('/<user>')
def user_page(user):
    user_level = user
    return render_template('welcome.html', user_level=user_level)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return 'Вы вошли в систему!'
    else:
        return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return "This is the contact page."


@app.route('/task_list')
def task_list():
    tasks = ["Выгулять собаку", "Погладить рубашку", "Зайти в супермаркет",
    "Убрать на кухне", "Дописать статью", "Позвонить тимлиду"]
    return render_template('task_list.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)