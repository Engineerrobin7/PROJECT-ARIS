# commands/fun_commands.py
"""
Handles fun commands like jokes, greetings, easter eggs, etc.
"""
import random
from orion_engine.personality import Personality

def handle_command(command):
    """
    Handles fun and entertainment commands.
    
    Args:
        command (str): The user's command text
        
    Returns:
        str: The response to the command
    """
    print(f"Fun command received: '{command}'")
    
    personality = Personality()
    
    # Process different types of fun commands
    if "joke" in command or "funny" in command:
        return tell_joke(personality)
    
    elif "hello" in command or "hi" in command or "hey" in command:
        return greet_user(personality)
    
    elif "sing" in command or "song" in command:
        return sing_song()
    
    elif "thank" in command:
        return respond_to_thanks()
    
    else:
        return "I'm not sure how to respond to that, but I hope it brightens your day!"

def tell_joke(personality):
    """
    Tells a random joke.
    """
    return personality.get_joke()

def greet_user(personality):
    """
    Greets the user with a random greeting.
    """
    return personality.get_greeting()

def sing_song():
    """
    Sings a short song or verse.
    """
    songs = [
        "🎵 Daisy, Daisy, give me your answer do... 🎵",
        "🎵 I'm afraid I can't do that, Dave... 🎵",
        "🎵 Happy Birthday to you! Happy Birthday to you! 🎵",
        "🎵 Do-Re-Mi-Fa-So-La-Ti-Do! 🎵"
    ]
    return random.choice(songs)

def respond_to_thanks():
    """
    Responds to user's thanks.
    """
    responses = [
        "You're welcome!",
        "Anytime!",
        "Happy to help!",
        "My pleasure!",
        "No problem at all!"
    ]
    return random.choice(responses)
