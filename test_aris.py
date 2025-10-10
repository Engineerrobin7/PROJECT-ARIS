#!/usr/bin/env python3
# test_aris.py
"""
Test script for ARIS voice assistant.
This script tests the basic functionality of ARIS components.
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
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('ARIS_TEST')

# Load environment variables
dotenv_path = os.path.join('config', 'config.env')
load_dotenv(dotenv_path=dotenv_path)

def test_tts_engine():
    """Test the text-to-speech engine."""
    logger.info("Testing TTS Engine...")
    try:
        tts = TTSEngine()
        tts.speak("This is a test of the ARIS text-to-speech system.")
        logger.info("TTS Engine test completed successfully.")
        return True
    except Exception as e:
        logger.error(f"TTS Engine test failed: {e}")
        return False

def test_speech_input():
    """Test the speech input module."""
    logger.info("Testing Speech Input...")
    try:
        speech_input = SpeechInput()
        logger.info("Please speak a test phrase when prompted...")
        print("\nPlease speak a test phrase now...")
        text = speech_input.listen()
        logger.info(f"Recognized text: {text}")
        if text:
            logger.info("Speech Input test completed successfully.")
            return True
        else:
            logger.warning("Speech Input test completed but no text was recognized.")
            return False
    except Exception as e:
        logger.error(f"Speech Input test failed: {e}")
        return False

def test_wake_word():
    """Test the wake word detection."""
    logger.info("Testing Wake Word Detection...")
    try:
        wake_word_detector = WakeWordDetector()
        logger.info("Please say 'Wake up ARIS' when prompted...")
        print("\nPlease say 'Wake up ARIS' now...")
        detected = wake_word_detector.detect()
        if detected:
            logger.info("Wake Word Detection test completed successfully.")
            return True
        else:
            logger.warning("Wake Word not detected.")
            return False
    except Exception as e:
        logger.error(f"Wake Word Detection test failed: {e}")
        return False

def test_brain():
    """Test the brain module with a simple command."""
    logger.info("Testing Brain Module...")
    try:
        brain = Brain()
        test_commands = [
            "What time is it?",
            "Tell me a joke",
            "What is the capital of France?"
        ]
        
        for command in test_commands:
            logger.info(f"Testing command: '{command}'")
            response = brain.route_command(command)
            logger.info(f"Response: {response}")
            
        logger.info("Brain Module test completed.")
        return True
    except Exception as e:
        logger.error(f"Brain Module test failed: {e}")
        return False

def run_all_tests():
    """Run all tests and report results."""
    logger.info("Starting ARIS component tests...")
    
    results = {
        "TTS Engine": test_tts_engine(),
        "Speech Input": test_speech_input(),
        "Wake Word Detection": test_wake_word(),
        "Brain Module": test_brain()
    }
    
    print("\n===== TEST RESULTS =====")
    all_passed = True
    for test, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f"{test}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\nAll tests passed! ARIS is functioning correctly.")
    else:
        print("\nSome tests failed. Please check the logs for details.")

if __name__ == "__main__":
    run_all_tests()