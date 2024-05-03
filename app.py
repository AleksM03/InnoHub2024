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


@app.route('/right')
def right():
    return render_template('right.html')


@app.route('/wrong')
def wrong():
    return render_template('wrong.html')


@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.json
    image1 = data['image1']
    image2 = data['image2']

    # Hier kannst du den Algorithmus aufrufen, der die Bilder verarbeitet und das Ergebnis zurückgibt
    result = process_algorithm(image1, image2)

    return jsonify(result=result)

# Beispiel-Funktion zum Verarbeiten der Bilder


def process_algorithm(image1, image2):
    # Hier implementierst du den Algorithmus zur Verarbeitung der Bilder und Rückgabe des Ergebnisses
    # Dies ist nur ein Platzhalter, bitte ersetze es durch deinen tatsächlichen Code
    # Zum Beispiel könntest du hier eine Bildverarbeitungs-Bibliothek wie OpenCV verwenden
    # und eine Funktion aufrufen, die die Bilder vergleicht und das Ergebnis zurückgibt
    # In diesem Beispiel geben wir einfach ein statisches Ergebnis zurück
    return "right"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
