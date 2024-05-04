<!DOCTYPE html >
<html lang = "en" >

<head >
    <link rel = "stylesheet" href = '/static/style.css' / >
    <meta charset = "UTF-8" >
    <meta name = "viewport" content = "width=device-width, initial-scale=1.0" >
    <title > My BMW Flask Application < /title >
    <style >
        /* Neue Stile für den Startbildschirm * /
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            / * Vollständige Höhe des Viewports * /
            background-color:  # f2f2f2;
            / * Leicht grauer Hintergrund * /
        }

        .container {
            width: 75 % ;
            / * 75 % der Bildschirmbreite * /
            max-width: 800px;
            / * Maximale Breite von 800px * /
            padding: 20px;
            text-align: center;
        }

        .start-screen {
            padding-top: 10 % ;
            padding-bottom: 10 % ;
            / * Höhe des Startbildschirms 50 % der Bildschirmhöhe * /
        }

        .container h2 {
            font-family: Helvetica, Arial, sans-serif;
            / * Verwende Helvetica * /
            font-size: 24px;
            / * Größere Schriftgröße * /
            margin-bottom: 30px;
            / * Abstand zum Logo * /
        }

        /* Video styles * /
        # video {
            width: 100 % ;
            /* Make the video element fill its container * /
            height: auto;
            /* Maintain aspect ratio * /
            margin-top: 80px;
            margin-bottom: 20px;
            /* Add some space below the video * /
        }

        / * Bild-Vorschau-Stile * /
        # cameraImage {
            max-width: 100 % ;
            / * Vollständige Breite * /
            margin-top: 60px;
            margin-bottom: 20px;
            / * Abstand zum nächsten Element * /
        }

        / * Button styles * /
        .button-group {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        button {
            background-color:  # 002d72;
            / * BMW Blue * /
            color:  # fff;
            / * Weißer Text * /
            font-size: 20px;
            / * Mittelgroße Schrift * /
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            / * Abgerundete Ecken * /
            cursor: pointer;
            margin-top: 20px;
            / * Abstand nach oben * /
        }

        / * Stile für den Cancel Button * /
        .cancel-button {
            position: absolute;
            top: 30px;
            left: 20px;
            width: 20px;
            height: 20px;
            / * Hinzugefügt, um die Höhe des Buttons festzulegen * /
            background: transparent;
            / * Änderung der Hintergrundfarbe auf transparent * /
            background-image: url('/static/x_icon.png');
            background-size: contain;
            background-repeat: no-repeat;
            cursor: pointer;
            border: none;
        }
    < /style >
< / head >

< body >

    < div class = "container" >
        <!-- Cancel Button - ->
        < button class = "cancel-button" onclick = "goBack()" aria-label = "Cancel" > </button >
        < h2 > Shipping Label < /h2 >
        < video id = "video" autoplay > </video > <!-- Removed width and height attributes - ->
        < img id = "cameraImage" src = "/static/camera.png" >
        < div class = "button-group" >
            < button id = "capture" > Capture < /button >
            < button id = "nextButton" > Next < /button >
        < / div >
        < button id = "requestPermission" > Request Camera Permission < /button >
    < / div >

    < script >
        // Funktion zum Zurückgehen zur vorherigen Seite
        function goBack() {
            window.history.back();
        }
        // Get the video element
        let video = document.getElementById('video');

        // Access user's camera
        navigator.mediaDevices.getUserMedia({
            video: {facingMode: {ideal: 'environment'}}
        })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            })
            .catch(function (err) {
                console.log("Error: " + err);
            });

        // Get the Capture button
        let captureButton = document.getElementById('capture');

        // Function to capture the image and save it
        captureButton.addEventListener('click', function () {
            let canvas = document.createElement('canvas');
            let context = canvas.getContext('2d');
            canvas.width = video.videoWidth; // Set canvas dimensions to match video
            canvas.height = video.videoHeight;
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            // Display the captured image
            let imgData = canvas.toDataURL('image/png');
            document.getElementById('cameraImage').src = imgData;
            
            // Save the image
            saveImage(imgData);
        });

        // Function to save the image
        function saveImage(imgData) {
            // Send the image data to the server to save it
            fetch('/save_image', {
                method: 'POST',
                body: imgData,
                headers: {
                    'Content-Type': 'image/png'
                }
            })
                .then(response => {
                    if (response.ok) {
                        console.log('Bild erfolgreich gespeichert.');
                    } else {
                        console.error('Fehler beim Speichern des Bildes.');
                    }
                })
                .catch(error => {
                    console.error('Fehler beim Speichern des Bildes:', error);
                });
        }

        // Get the button to request camera permission
        let requestPermissionButton = document.getElementById('requestPermission');

        // Function to request camera permission
        requestPermissionButton.addEventListener('click', function () {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function (stream) {
                    console.log('Camera permission granted.');
                })
                .catch(function (err) {
                    console.error('Error requesting camera permission:', err);
                });
        });

        // Next button event
        let nextButton = document.getElementById('nextButton');
        nextButton.addEventListener('click', function () {
            window.location.href = 'label2'; // Change this to your desired URL
        });
    </script>
</body>

</html>
