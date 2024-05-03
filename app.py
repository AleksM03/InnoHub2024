from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/label1')
def label1():
    return render_template('label1.html')


@app.route('/label2')
def label2():
    return render_template('label2.html')


@app.route('/comparing')
def comparing():
    return render_template('comparing.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
