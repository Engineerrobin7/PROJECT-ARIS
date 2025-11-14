"""
Enhanced ARIS with all new features integrated
"""
import os
import time
import logging
from dotenv import load_dotenv

# Core modules
from core.wake_word import WakeWordDetector
from core.speech_input import SpeechInput
from core.speech_output import TTSEngine

# Orion Engine
from orion_engine.brain import Brain
from orion_engine.memory import Memory
from orion_engine.personality import Personality

# New feature modules
from plugins.plugin_manager import PluginManager
from extensions.custom_commands import CustomCommandManager
from scheduler.advanced_scheduler import AdvancedScheduler
from conversation.context_manager import ConversationContext
from smart_home.smart_home_controller import SmartHomeController
from localization.language_manager import LanguageManager
from file_manager.voice_commands import FileManagerVoiceCommands

class ARISEnhanced:
    """Enhanced ARIS with all new features"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.logger.info("Initializing Enhanced ARIS...")
        
        # Load configuration
        load_dotenv(dotenv_path=os.path.join('config', 'config.env'))
        self.user_name = os.getenv("USER_NAME", "User")
        self.wake_word = os.getenv("WAKE_WORD", "wake up aris")
        
        # Initialize core modules
        self.wake_word_detector = WakeWordDetector(wake_word=self.wake_word)
        self.speech_input = SpeechInput()
        self.tts_engine = TTSEngine()
        
        # Initialize Orion Engine
        self.memory = Memory()
        self.personality = Personality()
        self.brain = Brain()
        
        # Initialize new features
        self.plugin_manager = PluginManager()
        self.custom_commands = CustomCommandManager()
        self.scheduler = AdvancedScheduler()
        self.context = ConversationContext()
        self.smart_home = SmartHomeController()
        self.language = LanguageManager()
        self.file_manager = FileManagerVoiceCommands()
        
        # Load plugins
        self.plugin_manager.load_all_plugins()
        
        # Start scheduler
        self.scheduler.start_scheduler(callback=self._handle_scheduled_task)
        
        self.logger.info("Enhanced ARIS initialized successfully")
    
    def _setup_logging(self):
        """Setup logging configuration"""
        os.makedirs('logs', exist_ok=True)
        logging.basicConfig(
            filename='logs/aris_enhanced.log',
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logging.getLogger('').addHandler(console)
        return logging.getLogger('ARIS-Enhanced')
    
    def start(self):
        """Start the enhanced ARIS system"""
        startup_msg = self.language.get_text("startup")
        self.logger.info(startup_msg)
        self.tts_engine.speak(f"Hello {self.user_name}, {startup_msg}")
        
        try:
            self._main_loop()
        except KeyboardInterrupt:
            self.shutdown()
    
    def _main_loop(self):
        """Main interaction loop"""
        self.logger.info("Entering main loop...")
        running = True
        
        while running:
            # Wait for wake word
            if self.wake_word_detector.detect():
                self.logger.info("Wake word detected")
                self.tts_engine.speak(self.language.get_text("listening"))
                
                # Listen for command
                user_command = self.speech_input.listen()
                
                if user_command:
                    response = self.process_command(user_command)
                    self.tts_engine.speak(response)
                else:
                    self.tts_engine.speak(self.language.get_text("command_not_understood"))
            
            time.sleep(0.1)
    
    def process_command(self, command: str) -> str:
        """Process a command through all systems"""
        self.logger.info(f"Processing command: {command}")
        
        # Build context
        context = {
            "user_name": self.user_name,
            "conversation_history": self.context.get_context(3),
            "preferences": self.context.user_preferences
        }
        
        # Try custom commands first
        response = self.custom_commands.execute_command(command)
        if response:
            self._log_interaction(command, response)
            return response
        
        # Try plugins
        response = self.plugin_manager.execute_command(command, context)
        if response:
            self._log_interaction(command, response)
            return response
        
        # Check for smart home commands
        if any(word in command.lower() for word in ["light", "thermostat", "device", "turn on", "turn off"]):
            response = self._handle_smart_home(command)
            if response:
                self._log_interaction(command, response)
                return response
        
        # Check for scheduler commands
        if any(word in command.lower() for word in ["remind", "schedule", "task", "in", "at", "tomorrow"]):
            response = self._handle_scheduler(command)
            if response:
                self._log_interaction(command, response)
                return response
        
        # Check for language commands
        if any(word in command.lower() for word in ["language", "translate", "speak"]):
            response = self._handle_language(command)
            if response:
                self._log_interaction(command, response)
                return response
        
        # Check for file management commands
        response = self.file_manager.process_command(command)
        if response:
            self._log_interaction(command, response)
            return response
        
        # Fall back to brain
        response = self.brain.route_command(command)
        self._log_interaction(command, response)
        return response
    
    def _handle_smart_home(self, command: str) -> str:
        """Handle smart home commands"""
        command_lower = command.lower()
        
        if "discover" in command_lower or "find devices" in command_lower:
            devices = self.smart_home.discover_devices()
            return f"Found {len(devices)} devices"
        
        # Extract device name and action
        if "turn on" in command_lower:
            device_name = command_lower.split("turn on")[-1].strip()
            return self.smart_home.control_device(device_name, "turn_on")
        
        if "turn off" in command_lower:
            device_name = command_lower.split("turn off")[-1].strip()
            return self.smart_home.control_device(device_name, "turn_off")
        
        return None
    
    def _handle_scheduler(self, command: str) -> str:
        """Handle scheduler commands"""
        command_lower = command.lower()
        
        if "remind me" in command_lower:
            # Parse reminder
            parts = command_lower.split("remind me to")
            if len(parts) > 1:
                task_and_time = parts[1].strip()
                # Simple parsing - can be enhanced
                return self.scheduler.add_task(task_and_time, "in 1 hour")
        
        if "schedule" in command_lower:
            return self.scheduler.add_task(command, "in 1 hour")
        
        if "upcoming tasks" in command_lower or "my tasks" in command_lower:
            tasks = self.scheduler.get_upcoming_tasks()
            if tasks:
                return f"You have {len(tasks)} upcoming tasks"
            return "No upcoming tasks"
        
        return None
    
    def _handle_language(self, command: str) -> str:
        """Handle language commands"""
        command_lower = command.lower()
        
        if "change language" in command_lower or "set language" in command_lower:
            # Extract language code
            languages = self.language.get_available_languages()
            for code, name in languages.items():
                if name.lower() in command_lower or code in command_lower:
                    if self.language.set_language(code):
                        return f"Language changed to {name}"
            return "Language not recognized"
        
        return None
    
    def _handle_scheduled_task(self, task: dict):
        """Handle a scheduled task execution"""
        self.logger.info(f"Executing scheduled task: {task['name']}")
        self.tts_engine.speak(f"Reminder: {task['name']}")
    
    def _log_interaction(self, command: str, response: str):
        """Log interaction to conversation context"""
        self.context.add_interaction(command, response)
        self.memory.add_to_history(command, response)
    
    def shutdown(self):
        """Shutdown ARIS gracefully"""
        self.logger.info("Shutting down Enhanced ARIS...")
        self.scheduler.stop_scheduler()
        self.tts_engine.speak(f"Goodbye, {self.user_name}")
        self.logger.info("Shutdown complete")

def main():
    """Main entry point"""
    aris = ARISEnhanced()
    aris.start()

if __name__ == "__main__":
    main()
