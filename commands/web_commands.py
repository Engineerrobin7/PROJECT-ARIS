# commands/web_commands.py
"""
Handles web-related commands like searches, opening URLs, etc.
"""
import webbrowser
import urllib.parse

def handle_command(command):
    """
    Handles web-related commands.
    
    Args:
        command (str): The user's command text
        
    Returns:
        str: The response to the command
    """
    print(f"Web command received: '{command}'")
    
    # Process different types of web commands
    if "search for" in command or "google" in command:
        query = extract_search_query(command)
        if query:
            return search_web(query)
        else:
            return "I couldn't determine what to search for."
    
    elif "open" in command and ("website" in command or ".com" in command or ".org" in command):
        url = extract_url(command)
        if url:
            return open_website(url)
        else:
            return "I couldn't determine which website to open."
    
    elif "youtube" in command:
        query = extract_youtube_query(command)
        if query:
            return search_youtube(query)
        else:
            return "I couldn't determine what to search for on YouTube."
    
    else:
        return "I'm not sure how to handle that web command."

def extract_search_query(command):
    """
    Extracts the search query from the command.
    """
    if "search for" in command:
        return command.split("search for", 1)[1].strip()
    elif "google" in command:
        return command.split("google", 1)[1].strip()
    return None

def extract_url(command):
    """
    Extracts the URL from the command.
    """
    words = command.split()
    for word in words:
        if ".com" in word or ".org" in word or ".net" in word:
            # Ensure it has http:// or https:// prefix
            if not word.startswith("http"):
                word = "https://" + word
            return word
    
    # If no direct URL found, check for "open website" pattern
    if "open website" in command:
        site = command.split("open website", 1)[1].strip()
        return "https://" + site
    
    return None

def extract_youtube_query(command):
    """
    Extracts the YouTube search query from the command.
    """
    if "search youtube for" in command:
        return command.split("search youtube for", 1)[1].strip()
    elif "youtube" in command:
        return command.split("youtube", 1)[1].strip()
    return None

def search_web(query):
    """
    Searches the web for the given query.
    """
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open(search_url)
    return f"Searching the web for '{query}'."

def open_website(url):
    """
    Opens the specified website.
    """
    webbrowser.open(url)
    return f"Opening {url}."

def search_youtube(query):
    """
    Searches YouTube for the given query.
    """
    youtube_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    webbrowser.open(youtube_url)
    return f"Searching YouTube for '{query}'."
