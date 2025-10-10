# commands/system_commands.py
"""
Handles system-level commands like opening applications, file operations, etc.
"""
import os
import subprocess
import platform

def handle_command(command):
    """
    Handles system-related commands.
    
    Args:
        command (str): The user's command text
        
    Returns:
        str: The response to the command
    """
    print(f"System command received: '{command}'")
    
    # Process different types of system commands
    if "open" in command or "start" in command or "run" in command:
        app_name = extract_app_name(command)
        if app_name:
            return open_application(app_name)
        else:
            return "I couldn't determine which application to open."
    
    elif "close" in command or "exit" in command:
        app_name = extract_app_name(command)
        if app_name:
            return close_application(app_name)
        else:
            return "I couldn't determine which application to close."
    
    elif "time" in command or "date" in command:
        return get_time_date()
    
    else:
        return "I'm not sure how to handle that system command."

def extract_app_name(command):
    """
    Extracts the application name from the command.
    """
    # Simple extraction by looking for words after 'open', 'start', 'run', 'close', or 'exit'
    for keyword in ["open", "start", "run", "close", "exit"]:
        if keyword in command:
            parts = command.split(keyword, 1)
            if len(parts) > 1:
                return parts[1].strip()
    return None

def open_application(app_name):
    """
    Opens the specified application.
    """
    system = platform.system()
    
    # Common applications dictionary with platform-specific commands
    apps = {
        "notepad": {
            "Windows": "notepad.exe",
            "Darwin": "open -a TextEdit",
            "Linux": "gedit"
        },
        "browser": {
            "Windows": "start microsoft-edge:",
            "Darwin": "open -a Safari",
            "Linux": "xdg-open https://www.google.com"
        },
        "calculator": {
            "Windows": "calc.exe",
            "Darwin": "open -a Calculator",
            "Linux": "gnome-calculator"
        },
        "file explorer": {
            "Windows": "explorer",
            "Darwin": "open .",
            "Linux": "nautilus"
        }
    }
    
    # Check for common applications
    for app, commands in apps.items():
        if app in app_name.lower():
            try:
                if system in commands:
                    os.system(commands[system])
                    return f"Opening {app}."
            except Exception as e:
                return f"Error opening {app}: {str(e)}"
    
    # If not a common app, try to open directly (with caution)
    try:
        if system == "Windows":
            os.system(f"start {app_name}")
        elif system == "Darwin":  # macOS
            os.system(f"open -a {app_name}")
        elif system == "Linux":
            subprocess.Popen(app_name, shell=True)
        return f"Attempting to open {app_name}."
    except Exception as e:
        return f"Error opening {app_name}: {str(e)}"

def close_application(app_name):
    """
    Closes the specified application.
    """
    system = platform.system()
    
    try:
        if system == "Windows":
            os.system(f"taskkill /f /im {app_name}.exe")
        elif system == "Darwin":  # macOS
            os.system(f"pkill -f {app_name}")
        elif system == "Linux":
            os.system(f"pkill -f {app_name}")
        return f"Attempting to close {app_name}."
    except Exception as e:
        return f"Error closing {app_name}: {str(e)}"

def get_time_date():
    """
    Returns the current time and date.
    """
    from datetime import datetime
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M')} and the date is {now.strftime('%Y-%m-%d')}."
