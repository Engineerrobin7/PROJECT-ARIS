"""
ARIS Main Entry Point
Boots the assistant, listens for wake word, and routes commands.
"""

from core.manager import ARISManager

def main():
    aris = ARISManager()
    aris.run()

if __name__ == "__main__":
    main()