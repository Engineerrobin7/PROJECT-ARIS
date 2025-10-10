# orion_engine/personality.py
"""
Defines ARIS’s tone, humor, and voice style.
"""
import random

class Personality:
    """Manages ARIS's personality traits and responses."""
    def __init__(self):
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
        ]
        print("Personality module initialized.")

    def get_greeting(self):
        """Returns a random greeting."""
        greetings = ["Hello!", "Hi there!", "At your service.", "Yes?"]
        return random.choice(greetings)

    def get_joke(self):
        """Returns a random joke."""
        return random.choice(self.jokes)

    # TODO: Add more personality traits like emotional responses, different tones, etc.
