"""
Example plugin demonstrating the plugin system
"""
from plugins.base_plugin import BasePlugin
from typing import Dict, Any

class ExamplePlugin(BasePlugin):
    """Example plugin that adds custom functionality"""
    
    def __init__(self):
        super().__init__()
        self.name = "Example Plugin"
        self.version = "1.0.0"
        self.description = "Demonstrates plugin capabilities"
        self.counter = 0
    
    def initialize(self) -> bool:
        """Initialize the plugin"""
        print(f"Initializing {self.name}")
        return True
    
    def get_commands(self) -> Dict[str, callable]:
        """Return command patterns this plugin handles"""
        return {
            "count": self.handle_count,
            "plugin test": self.handle_test,
            "example": self.handle_example
        }
    
    def execute(self, command: str, context: Dict[str, Any]) -> str:
        """Execute a command"""
        command_lower = command.lower()
        
        if "count" in command_lower:
            return self.handle_count(command, context)
        elif "plugin test" in command_lower:
            return self.handle_test(command, context)
        elif "example" in command_lower:
            return self.handle_example(command, context)
        
        return "Command not recognized by Example Plugin"
    
    def handle_count(self, command: str, context: Dict[str, Any]) -> str:
        """Handle count command"""
        self.counter += 1
        return f"Counter is now at {self.counter}"
    
    def handle_test(self, command: str, context: Dict[str, Any]) -> str:
        """Handle test command"""
        return "Plugin test successful! The plugin system is working."
    
    def handle_example(self, command: str, context: Dict[str, Any]) -> str:
        """Handle example command"""
        return "This is an example response from the plugin system."
    
    def shutdown(self):
        """Clean up when plugin is disabled"""
        print(f"Shutting down {self.name}")
