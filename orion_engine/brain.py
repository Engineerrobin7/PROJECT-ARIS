# orion_engine/brain.py
"""
Core decision logic for ARIS. Routes commands to the appropriate modules.
"""
from commands import system_commands, web_commands, ai_commands, fun_commands
from orion_engine.nlp_module import NLPModule
from orion_engine.memory import Memory
from orion_engine.personality import Personality

class Brain:
    """The core logic unit of ARIS. It processes commands and delegates tasks."""
    def __init__(self):
        self.nlp = NLPModule()
        self.memory = Memory()
        self.personality = Personality()
        print("Orion Engine Brain initialized.")

    def route_command(self, command_text):
        """
        Analyzes the command text and routes it to the correct module.
        """
        if not command_text:
            return "I didn't catch that. Could you please repeat?"
            
        command_text = command_text.lower()
        print(f"Brain received command: '{command_text}'")
        
        # Add to memory
        self.memory.add_to_history(command_text)
        
        # Simple keyword-based routing
        response = None
        
        if "open" in command_text or "start" in command_text or "run" in command_text:
            response = system_commands.handle_command(command_text)
        elif "search" in command_text or "google" in command_text or "find" in command_text:
            response = web_commands.handle_command(command_text)
        elif "joke" in command_text or "sing" in command_text or "funny" in command_text:
            response = fun_commands.handle_command(command_text)
        else:
            # Default to AI for general queries and conversations
            response = ai_commands.handle_command(command_text, self.nlp)
        
        return response
