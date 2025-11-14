"""
Plugin system for ARIS - allows dynamic loading of custom features
"""
from .plugin_manager import PluginManager
from .base_plugin import BasePlugin

__all__ = ['PluginManager', 'BasePlugin']
