from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')


@app.route('/catalog.html')
def catalog():
	return render_template('catalog.html')


@app.route('/energy.html')
def energy():
	return render_template('energy.html')


@app.route('/card01.html')
def card01():
	return render_template('card01.html')


@app.route('/card02.html')
def card02():
	return render_template('card02.html')


@app.route('/user/<string:name>')
def user(name):
	return f'Hello {name.capitalize()}'


if __name__ == '__main__':
	app.run(debug=True)
