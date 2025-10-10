# commands/ai_commands.py
"""
Handles AI-powered commands like GPT responses, writing, Q&A.
"""

def handle_command(command, nlp_module=None):
    """
    Handles AI-related commands using the NLP module.
    
    Args:
        command (str): The user's command text
        nlp_module (NLPModule): The NLP module for processing
        
    Returns:
        str: The response to the command
    """
    print(f"AI command received: '{command}'")
    
    if not nlp_module:
        return "I'm sorry, but my AI capabilities are currently limited."
    
    # Process different types of AI commands
    if "tell me about" in command or "what is" in command or "who is" in command:
        # Extract the query from the command
        query = command.replace("tell me about", "").replace("what is", "").replace("who is", "").strip()
        return get_information(query, nlp_module)
    
    elif "write" in command or "create" in command or "generate" in command:
        # Extract the writing task from the command
        task = command.replace("write", "").replace("create", "").replace("generate", "").strip()
        return generate_content(task, nlp_module)
    
    elif "summarize" in command:
        # Extract the text to summarize from the command
        text = command.replace("summarize", "").strip()
        return nlp_module.summarize_text(text)
    
    else:
        # Default to general conversation
        return nlp_module.get_response(command)

def get_information(query, nlp_module):
    """
    Gets information about a topic using the NLP module.
    """
    prompt = f"Provide a brief, informative explanation about: {query}"
    return nlp_module.get_response(prompt)

def generate_content(task, nlp_module):
    """
    Generates content based on the given task using the NLP module.
    """
    prompt = f"Please create the following: {task}"
    return nlp_module.get_response(prompt)
