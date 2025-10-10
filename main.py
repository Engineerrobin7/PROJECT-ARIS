# main.py
"""
Entry point for ARIS: boots the assistant, connects all modules, and starts the wake word listener.
"""
import os
import time
import logging
from dotenv import load_dotenv

# Import core modules
from core.wake_word import WakeWordDetector
from core.speech_input import SpeechInput
from core.speech_output import TTSEngine

# Import Orion Engine modules
from orion_engine.brain import Brain
from orion_engine.memory import Memory
from orion_engine.personality import Personality

# Setup logging
def setup_logging():
    """Configure logging for ARIS."""
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        filename='logs/aris.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)
    
    return logging.getLogger('ARIS')

def main():
    """Initializes ARIS, loads configuration, and starts the main loop."""
    # Setup logging
    logger = setup_logging()
    logger.info("Starting ARIS...")
    
    # Load environment variables from config/config.env
    dotenv_path = os.path.join('config', 'config.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    user_name = os.getenv("USER_NAME", "User")
    wake_word = os.getenv("WAKE_WORD", "wake up aris")
    
    logger.info(f"Loaded configuration for user: {user_name}")
    
    try:
        # Initialize core modules
        logger.info("Initializing core modules...")
        wake_word_detector = WakeWordDetector(wake_word=wake_word)
        speech_input = SpeechInput()
        tts_engine = TTSEngine()
        
        # Initialize Orion Engine modules
        logger.info("Initializing Orion Engine...")
        memory = Memory()
        personality = Personality()
        brain = Brain()
        
        # Startup greeting
        startup_message = f"Hello {user_name}, ARIS online. How can I assist you today?"
        logger.info(f"Startup message: {startup_message}")
        tts_engine.speak(startup_message)
        
        # Main interaction loop
        logger.info("Entering main interaction loop...")
        running = True
        while running:
            # Wait for wake word
            logger.info("Listening for wake word...")
            if wake_word_detector.detect():
                # Play activation sound (future enhancement)
                logger.info("Wake word detected!")
                
                # Listen for command
                tts_engine.speak("I'm listening.")
                user_command = speech_input.listen()
                
                if user_command:
                    logger.info(f"User command: {user_command}")
                    
                    # Process command through brain
                    response = brain.route_command(user_command)
                    
                    # Speak response
                    logger.info(f"ARIS response: {response}")
                    tts_engine.speak(response)
                    
                    # Add to memory
                    memory.add_to_history(user_command, response)
                else:
                    logger.warning("Failed to recognize command")
                    tts_engine.speak("Sorry, I didn't catch that.")
            
            # Small delay to prevent CPU overuse
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        logger.info("Keyboard interrupt received, shutting down...")
        tts_engine.speak(f"Goodbye, {user_name}.")
    except Exception as e:
        logger.error(f"Error in main loop: {e}")
        tts_engine.speak("I've encountered an error and need to shut down.")
    finally:
        logger.info("ARIS shutting down...")

if __name__ == "__main__":
    main()
