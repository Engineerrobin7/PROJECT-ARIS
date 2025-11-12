"""
SystemSkills: Handles system-level commands.
"""

import os
import webbrowser

class SystemSkills:
    def open_app(self, entities):
        app = entities.get("app")
        if app == "notepad":
            os.system("start notepad")
            return "Opening Notepad."
        if app == "calculator":
            os.system("start calc")
            return "Opening Calculator."
        if app == "paint":
            os.system("start mspaint")
            return "Opening Paint."
        if app == "cmd":
            os.system("start cmd")
            return "Opening Command Prompt."
        return "App not recognized."

    def open_website(self, entities):
        url = entities.get("url")
        if url:
            webbrowser.open(url)
            return f"Opening {url}."
        return "Website not recognized."

    def shutdown(self):
        os.system("shutdown /s /t 1")
        return "Shutting down the computer."

    def lock(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking the computer."