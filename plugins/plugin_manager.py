"""
Plugin manager for loading, managing, and executing plugins
"""
import os
import importlib
import logging
from typing import Dict, List, Any
from .base_plugin import BasePlugin

class PluginManager:
    """Manages all plugins for ARIS"""
    
    def __init__(self, plugin_dir: str = "plugins"):
        self.plugin_dir = plugin_dir
        self.plugins: Dict[str, BasePlugin] = {}
        self.logger = logging.getLogger('PluginManager')
        
    def discover_plugins(self) -> List[str]:
        """Discover all available plugins in the plugin directory"""
        discovered = []
        if not os.path.exists(self.plugin_dir):
            return discovered
            
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith('_plugin.py'):
                plugin_name = filename[:-3]  # Remove .py
                discovered.append(plugin_name)
        
        return discovered
    
    def load_plugin(self, plugin_name: str) -> bool:
        """Load a specific plugin"""
        try:
            module = importlib.import_module(f"{self.plugin_dir}.{plugin_name}")
            
            # Find the plugin class
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, BasePlugin) and attr != BasePlugin:
                    plugin_instance = attr()
                    if plugin_instance.initialize():
                        self.plugins[plugin_name] = plugin_instance
                        self.logger.info(f"Loaded plugin: {plugin_name}")
                        return True
            
            self.logger.warning(f"No valid plugin class found in {plugin_name}")
            return False
            
        except Exception as e:
            self.logger.error(f"Failed to load plugin {plugin_name}: {e}")
            return False
    
    def load_all_plugins(self):
        """Discover and load all available plugins"""
        plugins = self.discover_plugins()
        for plugin_name in plugins:
            self.load_plugin(plugin_name)
    
    def unload_plugin(self, plugin_name: str):
        """Unload a specific plugin"""
        if plugin_name in self.plugins:
            self.plugins[plugin_name].shutdown()
            del self.plugins[plugin_name]
            self.logger.info(f"Unloaded plugin: {plugin_name}")
    
    def execute_command(self, command: str, context: Dict[str, Any] = None) -> str:
        """Try to execute a command using loaded plugins"""
        if context is None:
            context = {}
            
        for plugin_name, plugin in self.plugins.items():
            if not plugin.enabled:
                continue
                
            commands = plugin.get_commands()
            for pattern, handler in commands.items():
                if pattern.lower() in command.lower():
                    try:
                        return plugin.execute(command, context)
                    except Exception as e:
                        self.logger.error(f"Plugin {plugin_name} error: {e}")
                        return f"Plugin error: {str(e)}"
        
        return None  # No plugin handled the command
    
    def get_all_plugins(self) -> Dict[str, Dict[str, str]]:
        """Get information about all loaded plugins"""
        return {name: plugin.get_info() for name, plugin in self.plugins.items()}
    
    def enable_plugin(self, plugin_name: str):
        """Enable a plugin"""
        if plugin_name in self.plugins:
            self.plugins[plugin_name].enabled = True
    
    def disable_plugin(self, plugin_name: str):
        """Disable a plugin"""
        if plugin_name in self.plugins:
            self.plugins[plugin_name].enabled = False
