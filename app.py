from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/label1')
def label1():
    return render_template('label1.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
