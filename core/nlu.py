"""
NLU: Simple intent and entity parser (expandable with transformers).
"""

class NLU:
    def parse(self, text):
        text = text.lower()
        if "notepad" in text and "open" in text:
            return "open_app", {"app": "notepad"}
        if "calculator" in text and "open" in text:
            return "open_app", {"app": "calculator"}
        if "paint" in text and "open" in text:
            return "open_app", {"app": "paint"}
        if ("command prompt" in text or "cmd" in text) and "open" in text:
            return "open_app", {"app": "cmd"}
        if "google" in text and ("open" in text or "search" in text):
            return "open_website", {"url": "https://www.google.com"}
        if "joke" in text:
            return "joke", {}
        if "shutdown" in text:
            return "shutdown", {}
        if "lock" in text and "computer" in text:
            return "lock", {}
        if "exit" in text or "goodbye" in text or "quit" in text:
            return "exit", {}
        return "unknown", {}