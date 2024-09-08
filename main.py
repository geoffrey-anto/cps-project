import wakeword
import speech
import yolo


speech = speech.Speech()


def main():
    speech.speak("Welcome")

    wakeword.wake_word(yolo.capture_and_send_photo)


if __name__ == "__main__":
    main()
