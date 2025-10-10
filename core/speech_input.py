# core/speech_input.py
"""
Converts speech to text.
"""
import speech_recognition as sr

class SpeechInput:
    """Captures audio from the microphone and transcribes it to text."""
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print("Speech Input module initialized.")

    def listen(self):
        """
        Listens for user speech and returns the transcribed text.
        """
        print("Listening for a command...")
        with self.microphone as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None
