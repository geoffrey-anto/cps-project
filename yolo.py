import cv2
import requests
import speech


speech = speech.Speech()


def capture_and_send_photo():
    api_url = "http://localhost:5000/upload"
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Unable to access the webcam")
        return

    ret, frame = cap.read()

    if not ret:
        print("Unable to capture frame from the webcam")
        return

    cap.release()

    _, img_encoded = cv2.imencode('.jpg', frame)

    files = {'file': img_encoded.tobytes()}

    try:
        response = requests.post(api_url, files=files)

        if response.status_code == 200:
            sentences = response.json()
            s = (" Also, ".join(sentences))+". Over."
            print("Response: ", s)
            speech.speak(s)

        else:
            print("Failed to send photo. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the photo:", str(e))
