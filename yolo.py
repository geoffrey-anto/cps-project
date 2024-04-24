import cv2
import requests
import speech


speech = speech.Speech()


def capture_and_send_photo():
    # Access the webcam
    api_url = "http://localhost:5000/upload"
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Unable to access the webcam")
        return

    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Unable to capture frame from the webcam")
        return

    # Release the webcam
    cap.release()

    # Convert the frame to JPEG format
    _, img_encoded = cv2.imencode('.jpg', frame)

    # Create a dictionary to store the image data
    files = {'file': img_encoded.tobytes()}

    try:
        # Send the image to the API endpoint
        response = requests.post(api_url, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            sentences = response.json()
            s = (" Also, ".join(sentences))+". Over."
            speech.speak(s)

        else:
            print("Failed to send photo. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the photo:", str(e))
