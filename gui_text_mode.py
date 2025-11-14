#!/usr/bin/env python3
# gui_text_mode.py
"""
Text-only mode for ARIS - No voice required, just type commands.
"""
from datetime import datetime
from orion_engine.brain import Brain
from orion_engine.memory import Memory

def print_header():
    """Print the header."""
    print("\n" + "=" * 70)
    print("  ARIS - Your AI Assistant (Text Mode)")
    print("=" * 70)
    print("\n  Type your commands below. Type 'exit' or 'quit' to stop.")
    print("  Type 'help' for example commands.\n")

def print_help():
    """Print help with example commands."""
    print("\n" + "-" * 70)
    print("  Example Commands:")
    print("-" * 70)
    print("\n  Basic:")
    print("    - what time is it")
    print("    - tell me a joke")
    print("    - hello aris")
    print("\n  Games:")
    print("    - flip a coin")
    print("    - roll the dice")
    print("    - let's play a number game")
    print("    - magic 8 ball will I succeed")
    print("\n  Translation:")
    print("    - translate hello to spanish")
    print("    - how do you say thank you in french")
    print("\n  Information (requires API keys):")
    print("    - what's the weather in london")
    print("    - latest news")
    print("    - wikipedia search for python")
    print("    - what's apple stock price")
    print("\n  System:")
    print("    - open notepad")
    print("    - open calculator")
    print("-" * 70 + "\n")

def main():
    """Main text mode loop."""
    print_header()
    
    # Initialize brain
    print("  Initializing ARIS...")
    brain = Brain()
    memory = Memory()
    print("  ✓ ARIS is ready!\n")
    
    # Main loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                print("\nARIS: Goodbye! Have a great day! 👋\n")
                break
            
            # Check for help
            if user_input.lower() in ['help', '?']:
                print_help()
                continue
            
            # Process command
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"\n[{timestamp}] Processing...", end="", flush=True)
            
            response = brain.route_command(user_input)
            
            print(f"\r[{timestamp}] ARIS: {response}\n")
            
            # Save to memory
            memory.add_to_history(user_input, response)
            
        except KeyboardInterrupt:
            print("\n\nARIS: Goodbye! Have a great day! 👋\n")
            break
        except Exception as e:
            print(f"\n\nARIS: Sorry, I encountered an error: {str(e)}\n")

if __name__ == "__main__":
    main()
