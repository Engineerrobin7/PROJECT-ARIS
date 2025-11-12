"""
VoiceOutput: Handles text-to-speech.
"""

import pyttsx3

class VoiceOutput:
    def __init__(self, rate=180):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)

    def speak(self, text):
        print(f"ARIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()