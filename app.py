from flask import request, jsonify
from flask import Flask, render_template, request, redirect, url_for
import os
import tempfile
from main import comparator

app = Flask(__name__)

# Define the directory to save the images
UPLOAD_FOLDER = 'static/temp_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/label1', methods=['GET', 'POST'])
def label1():
    return render_template('label1.html')


@app.route('/label2', methods=['GET', 'POST'])
def label2():
    return render_template('label2.html')


@app.route('/comparing', methods=['GET', 'POST'])
def comparing():
    return render_template('comparing.html')


# Route for saving picture from label1
@app.route('/save_label1', methods=['GET', 'POST'])
def save_label1():
    file = request.files['image']
    if file:
        filename = 'label1.png'  # Define the filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return 'Image from label1 saved successfully'

# Route for saving picture from label2


@app.route('/save_label2', methods=['GET', 'POST'])
def save_label2():
    file = request.files['image']
    if file:
        filename = 'label2.png'  # Define the filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return 'Image from label2 saved successfully'


@app.route('/right')
def right():
    return render_template('right.html')


@app.route('/wrong')
def wrong():
    return render_template('wrong.html')

# Route for serving the saved pictures


@app.route('/get_pictures', methods=['POST'])
def get_pictures():
    label1_filename = 'label1.png'
    label2_filename = 'label2.png'

    label1_filepath = os.path.join(
        app.config['UPLOAD_FOLDER'], label1_filename)
    label2_filepath = os.path.join(
        app.config['UPLOAD_FOLDER'], label2_filename)

    return jsonify({'label1': label1_filepath, 'label2': label2_filepath})


###################

@app.route('/process_images', methods=['POST'])
def process_images():
    # Die Bilder werden als JSON-Daten gesendet
    data = request.json
    image1_path = data['image1']
    image2_path = data['image2']

    # Hier kannst du den Algorithmus aufrufen, der die Bilder verarbeitet und das Ergebnis zurückgibt
    result = process_algorithm(image1_path, image2_path)

    return jsonify(result=result)


def process_algorithm(image1, image2):
    if comparator(image1, image2):
        return "right"
    else:
        return "wrong"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
