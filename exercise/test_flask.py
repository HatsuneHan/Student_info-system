from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return 'hello world'
# url_for('css', filename='index.css')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
