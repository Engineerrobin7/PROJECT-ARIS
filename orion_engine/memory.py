# orion_engine/memory.py
"""
(Future) Stores user context, preferences, and conversation history.
"""

class Memory:
    """A simple memory store for ARIS."""
    def __init__(self):
        self.history = []
        self.preferences = {}
        print("Memory module initialized.")

    def remember(self, key, value):
        """Stores a preference."""
        print(f"Remembering '{key}' = '{value}'")
        self.preferences[key] = value

    def recall(self, key):
        """Recalls a preference."""
        return self.preferences.get(key)

    def add_to_history(self, text):
        """Adds an entry to the conversation history."""
        self.history.append(text)

    # TODO: Add methods for saving/loading memory to/from a file.
