from flask import Flask, render_template, url_for

app = Flask(__name__)


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


@app.route('/energy.html')
def energy():
	return render_template('energy.html')


@app.route('/card_art.html')
def card_art():
	return render_template('card_art.html')


@app.route('/card_en.html')
def card_en():
	return render_template('card_en.html')


@app.route('/user/<string:name>')
def user(name):
	return f'Hello {name.capitalize()}'


if __name__ == '__main__':
	app.run(debug=True)
