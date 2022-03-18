from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<name>')
@app.route('/index/<name>')
def start_page(name):
    return render_template('base.html', name=name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
