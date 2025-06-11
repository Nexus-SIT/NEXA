import speech_recognition as sr
import pyttsx3

def speak(text):
    """Converts text to speech using pyttsx3."""
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 200)

        engine.say(text)
        engine.runAndWait()
        return text
    except Exception as e:
        return 0

def voice_to_text():
    """Captures audio from the microphone and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in') # 'en-in' for English (India)
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None
    except Exception as e:
        return None
