import pyttsx3

if __name__ == '__main__':
    print("Welcome to 'Text To Speech RoboSpeaker'. Type STOP to exit.")
    engine = pyttsx3.init()
    while True:
        text = input("Enter text to convert to speech: ")
        if text.lower() == "stop":
            engine.say("Thank you for using RoboSpeaker.")
            engine.runAndWait()
            break

        engine.say(text)
        engine.runAndWait()


