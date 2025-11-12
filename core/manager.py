"""
ARISManager: Orchestrates wake word, voice I/O, NLU, and skill routing.
"""

from core.wake_word import WakeWordDetector
from voice.input import VoiceInput
from voice.output import VoiceOutput
from core.nlu import NLU
from skills.system import SystemSkills
from skills.fun import FunSkills

class ARISManager:
    def __init__(self):
        self.voice_in = VoiceInput()
        self.voice_out = VoiceOutput()
        self.wake_word = WakeWordDetector("hey aris")
        self.nlu = NLU()
        self.system_skills = SystemSkills()
        self.fun_skills = FunSkills()
        # TODO: Add API and IoT modules here

    def run(self):
        self.voice_out.speak("ARIS is online and listening.")
        while True:
            if self.wake_word.listen():
                self.voice_out.speak("Hello, I am ARIS. How can I help you?")
                while True:
                    text = self.voice_in.listen()
                    if not text:
                        continue
                    intent, entities = self.nlu.parse(text)
                    response = self.route(intent, entities, text)
                    self.voice_out.speak(response)
                    if intent == "exit":
                        self.voice_out.speak("Goodbye!")
                        return

    def route(self, intent, entities, text):
        if intent == "open_app":
            return self.system_skills.open_app(entities)
        elif intent == "open_website":
            return self.system_skills.open_website(entities)
        elif intent == "joke":
            return self.fun_skills.tell_joke()
        elif intent == "shutdown":
            return self.system_skills.shutdown()
        elif intent == "lock":
            return self.system_skills.lock()
        elif intent == "exit":
            return "Shutting down."
        else:
            return "Sorry, I didn't understand that."