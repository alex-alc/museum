from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

host = 'ext7.mysql.pythonanywhere-services.com'
user = 'ext7'
password = 'm123123MM'
db_name = 'ext7$ideas'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Idea(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	author = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(50), nullable=False)
	phone = db.Column(db.String(50), nullable=False)
	category = db.Column(db.String(50), nullable=False)
	title = db.Column(db.String(100), nullable=False)
	intro = db.Column(db.String(350), nullable=False)
	description = db.Column(db.Text, nullable=False)
	date_ = db.Column(db.DateTime, default=datetime.now)
	published = db.Column(db.Boolean, default=False)
	archive = db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<Idea %r>' % self.id


@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')


@app.route('/catalog.html')
def catalog():
	return render_template('catalog.html')


@app.route('/art.html')
def art():
	return render_template('art.html')


@app.route('/it.html')
def it():
	ideas = Idea.query.filter_by(category='IT', published=True).order_by(Idea.date_.desc()).all()
	return render_template('it.html', ideas=ideas)


@app.route('/energy.html')
def energy():
	return render_template('energy.html')


@app.route('/card_art.html')
def card_art():
	return render_template('card_art.html')


@app.route('/card_en.html')
def card_en():
	return render_template('card_en.html')


@app.route('/create-idea.html', methods=['GET', 'POST'])
def create_idea():
	if request.method == 'POST':
		author = request.form['author']
		email = request.form['email']
		phone = request.form['phone']
		category = request.form['category']
		title = request.form['title']
		intro = request.form['intro']
		description = request.form['description']
		new_idea = Idea(author=author,
		                email=email,
		                phone=phone,
		                category=category,
		                title=title,
		                intro=intro,
		                description=description,
		                published=True,
		                archive=False)
		try:
			db.session.add(new_idea)
			db.session.commit()
			return redirect('index.html#catalog')
		except Exception as ex:
			return f'Помилка при створенні нової ідеї: {ex}'
	else:
		return render_template('create-idea.html')


@app.route('/ideas/<int:id>')
def get_idea(id):
	idea = Idea.query.get(id)
	return render_template('idea.html', idea=idea)


@app.route('/admin.html')
def admin():
	ideas = Idea.query.filter_by(category='IT', published=False).order_by(Idea.date_.desc()).all()
	return render_template('admin.html', ideas=ideas)


@app.route('/admin/<int:id>')
def admin_idea(id):
	idea = Idea.query.get(id)
	return render_template('admin_idea.html', idea=idea)


@app.route('/admin/<int:id>/publish')
def idea_publish(id):
	idea = Idea.query.get(id)
	idea.published = True
	try:
		db.session.commit()
		return redirect('/admin.html')
	except Exception as ex:
		return f'Помилка при публікації ідеї: {ex}'


@app.route('/admin/<int:id>/edit', methods=['GET', 'POST'])
def idea_edit(id):
	idea = Idea.query.get(id)
	if request.method == 'POST':
		idea.author = request.form['author']
		idea.email = request.form['email']
		idea.phone = request.form['phone']
		idea.category = request.form['category']
		idea.title = request.form['title']
		idea.intro = request.form['intro']
		idea.description = request.form['description']
		try:
			db.session.commit()
			return redirect('/admin.html')
		except Exception as ex:
			return f'Помилка при створенні нової ідеї: {ex}'
	else:
		return render_template('/edit-idea.html', idea=idea)


@app.route('/admin/<int:id>/delete')
def idea_delete(id):
	idea = Idea.query.get_or_404(id)
	try:
		db.session.delete(idea)
		db.session.commit()
		return redirect('/admin.html')
	except Exception as ex:
		return f'Помилка при видаленні ідеї: {ex}'


if __name__ == '__main__':
	app.run()
