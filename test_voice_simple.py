#!/usr/bin/env python3
# test_voice_simple.py
"""
Simple test for voice commands without GUI.
"""
from core.speech_input import SpeechInput
from orion_engine.brain import Brain

def main():
    print("\n" + "=" * 60)
    print("  ARIS Voice Command Test")
    print("=" * 60)
    print("\nThis will test voice input and command processing.")
    print("Speak a command when prompted.\n")
    
    # Initialize components
    print("Initializing components...")
    speech_input = SpeechInput()
    brain = Brain()
    print("Ready!\n")
    
    # Test loop
    while True:
        try:
            print("\n" + "-" * 60)
            print("Listening for your command... (Ctrl+C to exit)")
            print("-" * 60)
            
            # Listen for command
            command = speech_input.listen()
            
            if command:
                print(f"\n✓ Heard: '{command}'")
                print("\nProcessing command...")
                
                # Process through brain
                response = brain.route_command(command)
                
                print(f"\n✓ ARIS Response:")
                print(f"  {response}")
                
            else:
                print("\n✗ No command recognized. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")

if __name__ == "__main__":
    main()
