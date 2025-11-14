"""
Base plugin class that all plugins must inherit from
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Any

class BasePlugin(ABC):
    """Base class for all ARIS plugins"""
    
    def __init__(self):
        self.name = "BasePlugin"
        self.version = "1.0.0"
        self.description = "Base plugin class"
        self.enabled = True
        
    @abstractmethod
    def initialize(self) -> bool:
        """Initialize the plugin. Return True if successful."""
        pass
    
    @abstractmethod
    def get_commands(self) -> Dict[str, callable]:
        """Return a dictionary of command patterns and their handlers"""
        pass
    
    @abstractmethod
    def execute(self, command: str, context: Dict[str, Any]) -> str:
        """Execute a command and return the response"""
        pass
    
    def shutdown(self):
        """Clean up resources when plugin is disabled"""
        pass
    
    def get_info(self) -> Dict[str, str]:
        """Return plugin information"""
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "enabled": self.enabled
        }
