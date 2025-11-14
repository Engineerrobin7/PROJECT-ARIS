"""
Conversation context and history management
"""
import json
import os
import logging
from datetime import datetime
from typing import List, Dict, Any
from collections import deque

class ConversationContext:
    """Manages conversation history and context awareness"""
    
    def __init__(self, history_file: str = "data/conversation_history.json", max_context: int = 10):
        self.history_file = history_file
        self.max_context = max_context
        self.current_context = deque(maxlen=max_context)
        self.full_history: List[Dict[str, Any]] = []
        self.logger = logging.getLogger('ConversationContext')
        self.current_topic = None
        self.user_preferences = {}
        self.load_history()
    
    def load_history(self):
        """Load conversation history from file"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    data = json.load(f)
                    self.full_history = data.get("history", [])
                    self.user_preferences = data.get("preferences", {})
                self.logger.info(f"Loaded {len(self.full_history)} conversation entries")
            except Exception as e:
                self.logger.error(f"Failed to load history: {e}")
    
    def save_history(self):
        """Save conversation history to file"""
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        try:
            data = {
                "history": self.full_history[-1000:],  # Keep last 1000 entries
                "preferences": self.user_preferences,
                "last_updated": datetime.now().isoformat()
            }
            with open(self.history_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            self.logger.error(f"Failed to save history: {e}")
    
    def add_interaction(self, user_input: str, assistant_response: str, metadata: Dict[str, Any] = None):
        """Add a new interaction to the conversation history"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "assistant": assistant_response,
            "topic": self.current_topic,
            "metadata": metadata or {}
        }
        
        self.current_context.append(interaction)
        self.full_history.append(interaction)
        self.save_history()
        
        # Update topic based on interaction
        self._update_topic(user_input)
    
    def get_context(self, num_interactions: int = None) -> List[Dict[str, Any]]:
        """Get recent conversation context"""
        if num_interactions is None:
            return list(self.current_context)
        return list(self.current_context)[-num_interactions:]
    
    def get_context_string(self, num_interactions: int = 5) -> str:
        """Get context as a formatted string for AI prompts"""
        context = self.get_context(num_interactions)
        if not context:
            return ""
        
        context_str = "Recent conversation:\n"
        for interaction in context:
            context_str += f"User: {interaction['user']}\n"
            context_str += f"Assistant: {interaction['assistant']}\n"
        
        return context_str
    
    def search_history(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search conversation history for specific content"""
        query_lower = query.lower()
        results = []
        
        for interaction in reversed(self.full_history):
            if (query_lower in interaction['user'].lower() or 
                query_lower in interaction['assistant'].lower()):
                results.append(interaction)
                if len(results) >= limit:
                    break
        
        return results
    
    def get_topic_history(self, topic: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get interactions related to a specific topic"""
        results = []
        for interaction in reversed(self.full_history):
            if interaction.get('topic') == topic:
                results.append(interaction)
                if len(results) >= limit:
                    break
        return results
    
    def set_preference(self, key: str, value: Any):
        """Set a user preference"""
        self.user_preferences[key] = value
        self.save_history()
    
    def get_preference(self, key: str, default: Any = None) -> Any:
        """Get a user preference"""
        return self.user_preferences.get(key, default)
    
    def clear_context(self):
        """Clear current conversation context"""
        self.current_context.clear()
        self.current_topic = None
    
    def _update_topic(self, user_input: str):
        """Update current conversation topic based on input"""
        user_lower = user_input.lower()
        
        # Simple topic detection
        topics = {
            "weather": ["weather", "temperature", "forecast", "rain", "snow"],
            "news": ["news", "headlines", "current events"],
            "music": ["play", "music", "song", "spotify", "youtube"],
            "time": ["time", "date", "day", "calendar"],
            "email": ["email", "message", "inbox"],
            "reminder": ["remind", "schedule", "task", "todo"],
            "search": ["search", "google", "find", "look up"],
            "system": ["open", "close", "launch", "shutdown"]
        }
        
        for topic, keywords in topics.items():
            if any(keyword in user_lower for keyword in keywords):
                self.current_topic = topic
                return
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get conversation statistics"""
        if not self.full_history:
            return {}
        
        total_interactions = len(self.full_history)
        topics = {}
        
        for interaction in self.full_history:
            topic = interaction.get('topic', 'general')
            topics[topic] = topics.get(topic, 0) + 1
        
        first_interaction = self.full_history[0]['timestamp']
        last_interaction = self.full_history[-1]['timestamp']
        
        return {
            "total_interactions": total_interactions,
            "topics": topics,
            "first_interaction": first_interaction,
            "last_interaction": last_interaction,
            "preferences_set": len(self.user_preferences)
        }
