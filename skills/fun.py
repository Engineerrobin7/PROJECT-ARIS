"""
FunSkills: Fun and personality features.
"""

import random

class FunSkills:
    def tell_joke(self):
        jokes = [
            "Why did the computer go to the doctor? Because it had a virus!",
            "I would tell you a UDP joke, but you might not get it.",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
        return random.choice(jokes)