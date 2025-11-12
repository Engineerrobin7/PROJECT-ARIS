"""
VoiceInput: Handles speech-to-text.
"""

import speech_recognition as sr

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self, timeout=5, phrase_time_limit=5):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening for command...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            except sr.WaitTimeoutError:
                return ""
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"User: {text}")
            return text.lower()
        except Exception:
            print("Sorry, I didn't catch that.")
            return ""