"""
Custom command system - allows users to define their own voice commands
"""
import json
import os
import logging
from typing import Dict, List, Any
import subprocess

class CustomCommandManager:
    """Manages user-defined custom commands"""
    
    def __init__(self, config_file: str = "config/custom_commands.json"):
        self.config_file = config_file
        self.commands: Dict[str, Dict[str, Any]] = {}
        self.logger = logging.getLogger('CustomCommands')
        self.load_commands()
    
    def load_commands(self):
        """Load custom commands from config file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.commands = json.load(f)
                self.logger.info(f"Loaded {len(self.commands)} custom commands")
            except Exception as e:
                self.logger.error(f"Failed to load custom commands: {e}")
                self.commands = {}
        else:
            self.commands = self._get_default_commands()
            self.save_commands()
    
    def save_commands(self):
        """Save custom commands to config file"""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.commands, f, indent=2)
            self.logger.info("Saved custom commands")
        except Exception as e:
            self.logger.error(f"Failed to save custom commands: {e}")
    
    def add_command(self, trigger: str, action_type: str, action_data: Any, response: str = None):
        """
        Add a new custom command
        
        Args:
            trigger: The phrase that triggers this command
            action_type: Type of action (speak, execute, open_url, run_script)
            action_data: Data for the action
            response: Optional response to speak
        """
        self.commands[trigger.lower()] = {
            "action_type": action_type,
            "action_data": action_data,
            "response": response or f"Executing {trigger}"
        }
        self.save_commands()
        self.logger.info(f"Added custom command: {trigger}")
    
    def remove_command(self, trigger: str):
        """Remove a custom command"""
        if trigger.lower() in self.commands:
            del self.commands[trigger.lower()]
            self.save_commands()
            self.logger.info(f"Removed custom command: {trigger}")
            return True
        return False
    
    def execute_command(self, command: str) -> str:
        """Execute a custom command if it matches"""
        command_lower = command.lower()
        
        for trigger, cmd_data in self.commands.items():
            if trigger in command_lower:
                return self._execute_action(cmd_data)
        
        return None
    
    def _execute_action(self, cmd_data: Dict[str, Any]) -> str:
        """Execute the action defined in a custom command"""
        action_type = cmd_data.get("action_type")
        action_data = cmd_data.get("action_data")
        response = cmd_data.get("response", "Done")
        
        try:
            if action_type == "speak":
                return action_data
            
            elif action_type == "execute":
                subprocess.Popen(action_data, shell=True)
                return response
            
            elif action_type == "open_url":
                import webbrowser
                webbrowser.open(action_data)
                return response
            
            elif action_type == "run_script":
                subprocess.run(action_data, shell=True, capture_output=True)
                return response
            
            else:
                return f"Unknown action type: {action_type}"
                
        except Exception as e:
            self.logger.error(f"Failed to execute action: {e}")
            return f"Failed to execute command: {str(e)}"
    
    def get_all_commands(self) -> Dict[str, Dict[str, Any]]:
        """Get all custom commands"""
        return self.commands
    
    def _get_default_commands(self) -> Dict[str, Dict[str, Any]]:
        """Get default custom commands"""
        return {
            "good morning aris": {
                "action_type": "speak",
                "action_data": "Good morning! Ready to start the day?",
                "response": "Good morning! Ready to start the day?"
            },
            "open my project": {
                "action_type": "execute",
                "action_data": "code .",
                "response": "Opening your project in VS Code"
            }
        }
