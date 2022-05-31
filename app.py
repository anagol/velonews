from flask import Flask, redirect, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BikeNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(80))
    news_text = db.Column(db.String)
    news_photo = db.Column(db.String)

    def __int__(self, news_title, news_text):
        self.news_title = news_title
        self.news_text = news_text

    def __repr__(self):
        return '<User %r>' % self.news_title


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/culture')
def culture():
    return render_template('culture.html', title='Культура')


@app.route('/events')
def events():
    return render_template('events.html', title='События')


@app.route('/news')
def news():
    news = BikeNews.query.filter_by().all()
    return render_template('news.html', title='Новости', news=news)


@app.route('/<int:news_id>')
def news_bike(news_id):
    news_bike = BikeNews.query.filter_by(id=news_id).one()
    return render_template('news_bike.html', news=news_bike)


@app.route('/create_news', methods=['GET', 'POST'])
def create_product():
    if request.method == "POST":
        news_title = request.form["news_title"]
        news_text = request.form["news_text"]
        news_photo = request.form["news_photo"]

        news = BikeNews(news_title=news_title, news_text=news_text, news_photo=news_photo)
        db.session.add(news)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('news'))
    return render_template('create_news.html', title='Добавляем новость')


@app.route('/forum')
def forum():
    return render_template('forum.html', title='Форум')


@app.route('/about')
def about():
    return render_template('about.html', title='О проете')


if __name__ == '__main__':
    app.run(debug=True)
