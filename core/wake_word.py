# core/wake_word.py
"""
Handles wake word detection.
"""
import speech_recognition as sr
import os
from dotenv import load_dotenv

class WakeWordDetector:
    """Listens for a specific wake word or phrase."""
    def __init__(self, wake_word=None):
        # Load environment variables to get the wake word
        dotenv_path = os.path.join('config', 'config.env')
        load_dotenv(dotenv_path=dotenv_path)
        
        # Get wake word from environment or use default
        self.wake_word = wake_word or os.getenv("WAKE_WORD", "wake up aris").lower()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print(f"Wake Word Detector initialized with wake word: '{self.wake_word}'.")

    def detect(self):
        """
        Listens for the wake word from the microphone.
        Returns True if the wake word is detected.
        """
        print(f"Waiting for wake word: '{self.wake_word}'")
        with self.microphone as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            print(f"Heard: {text}")
            if self.wake_word in text.lower():
                print("Wake word detected!")
                return True
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return False
