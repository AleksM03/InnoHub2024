from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)

# Definiere das Verzeichnis für die temporären Bilder
TEMP_IMAGE_DIR = 'static/temp_images'


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
    # Aufrufen der Funktion, um die Bildpfade zu erhalten
    image1_path, image2_path = get_both_pictures()
    return render_template('comparing.html', image1=image1_path, image2=image2_path)


def get_both_pictures():
    # Get the paths of the two images
    image1_path = os.path.join(TEMP_IMAGE_DIR, 'label1.png')
    image2_path = os.path.join(TEMP_IMAGE_DIR, 'label2.png')
    return image1_path, image2_path


@app.route('/upload', methods=['POST'])
def upload():
    # Überprüfe, ob die Anfrage ein Bild enthält
    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)

    # Bestimme den Dateinamen basierend auf der Seite, von der das Bild aufgenommen wurde
    # Extrahiere den letzten Teil der Referrer-URL
    page = request.referrer.split("/")[-1]
    if page == 'label1':
        filename = 'label1.png'
    elif page == 'label2':
        filename = 'label2.png'
    else:
        filename = 'image.png'

    # Überprüfe, ob die Datei bereits existiert und ob sie überschrieben werden muss
    image_path = os.path.join(TEMP_IMAGE_DIR, filename)
    if os.path.exists(image_path) and (page == 'label1' or not os.path.exists(os.path.join(TEMP_IMAGE_DIR, 'label1.png'))) \
            and (page == 'label2' or not os.path.exists(os.path.join(TEMP_IMAGE_DIR, 'label2.png'))):
        os.remove(image_path)

    # Speichere das Bild im temporären Verzeichnis
    image.save(image_path)

    # Weiterleitung zur Ergebnisseite
    return redirect(url_for('result'))


@app.route('/right')
def right():
    return render_template('right.html')


@app.route('/wrong')
def wrong():
    return render_template('wrong.html')


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
    # Hier implementierst du den Algorithmus zur Verarbeitung der Bilder und Rückgabe des Ergebnisses
    # Dies ist nur ein Platzhalter, bitte ersetze es durch deinen tatsächlichen Code
    # Zum Beispiel könntest du hier eine Bildverarbeitungs-Bibliothek wie OpenCV verwenden
    # und eine Funktion aufrufen, die die Bilder vergleicht und das Ergebnis zurückgibt
    # In diesem Beispiel geben wir einfach ein statisches Ergebnis zurück
    return "right"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
