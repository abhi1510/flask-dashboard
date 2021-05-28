from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buttons')
def buttons():
    return render_template('buttons.html')


@app.route('/cards')
def cards():
    return render_template('cards.html')


@app.route('/utilities/<target>')
def utilities(target):
    return render_template(f'utilities-{target}.html')


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/blank')
def blank():
    return render_template('blank.html')


@app.route('/404')
def error_404():
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
