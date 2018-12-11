from flask import Flask, render_template

app = Flask(__name__)


# Whenever the path  is http://127.0.0.1:5000/, it will pass value=0 in home.html
@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('home.html', value=0)

# Take the exising value and increment by 1
@app.route('/update/<int:value>')
def update(value):
    value = value + 1
    return render_template('home.html', value=value)

if __name__ == '__main__':
    app.run()
