# orion_engine/nlp_module.py
"""
Handles Natural Language Processing (NLP) tasks, including interfacing with GPT/OpenAI.
"""
import openai
import os

class NLPModule:
    """Handles language understanding and generation."""
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            print("WARNING: OpenAI API key not found. NLP features will be limited.")
        print("NLP Module initialized.")

    def get_response(self, prompt):
        """
        Gets a response from the OpenAI GPT model.
        """
        print(f"Sending prompt to GPT: '{prompt}'")
        
        if not openai.api_key:
            return "I'm sorry, but my AI capabilities are currently limited. Please check the OpenAI API key configuration."
            
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",  # Using the latest available model
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return f"I encountered an error while processing your request. {str(e)}"
            
    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the given text.
        Returns a simple sentiment label: positive, negative, or neutral.
        """
        prompt = f"Analyze the sentiment of this text and respond with only one word (positive, negative, or neutral): '{text}'"
        return self.get_response(prompt).lower()
        
    def summarize_text(self, text, max_length=50):
        """
        Summarizes the given text to the specified maximum length.
        """
        prompt = f"Summarize this text in {max_length} words or less: '{text}'"
        return self.get_response(prompt)
