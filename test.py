import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something")
    audio = r.listen(source)
    try:
        print("Google Speech Recognition thinks you said: " + r.recognize_google(audio).lower())
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

