import wakeword
import speech
import yolo


speech = speech.Speech()


def main():
    print("Welcome to In My Sight")
    speech.speak(
        "Welcome to In My Sight, To activate the camera say 'Hey Jarvis'")

    wakeword.wake_word(yolo.capture_and_send_photo)


if __name__ == "__main__":
    main()
