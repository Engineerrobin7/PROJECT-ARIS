# commands/games_commands.py
"""
Handles game and entertainment commands.
"""
import random

class GamesCommands:
    def __init__(self):
        self.number_to_guess = None
        self.guesses_left = 0
    
    def handle_command(self, command):
        """Handle game-related commands."""
        if "number game" in command or "guess the number" in command:
            return self.start_number_game()
        elif "guess" in command and self.number_to_guess:
            return self.process_guess(command)
        elif "coin flip" in command or "flip a coin" in command:
            return self.flip_coin()
        elif "dice" in command or "roll dice" in command:
            return self.roll_dice()
        elif "magic 8 ball" in command or "eight ball" in command:
            return self.magic_8_ball()
        elif "trivia" in command or "quiz" in command:
            return self.trivia_question()
        else:
            return "I can play number guessing, flip coins, roll dice, or answer magic 8 ball questions!"
    
    def start_number_game(self):
        """Start a number guessing game."""
        self.number_to_guess = random.randint(1, 100)
        self.guesses_left = 7
        return "I'm thinking of a number between 1 and 100. You have 7 guesses. What's your guess?"
    
    def process_guess(self, command):
        """Process a guess in the number game."""
        if not self.number_to_guess:
            return "We're not playing a game right now. Say 'start number game' to begin."
        
        try:
            # Extract number from command
            words = command.split()
            guess = None
            for word in words:
                if word.isdigit():
                    guess = int(word)
                    break
            
            if not guess:
                return "Please say a number."
            
            self.guesses_left -= 1
            
            if guess == self.number_to_guess:
                self.number_to_guess = None
                return f"Correct! You guessed it! The number was {guess}."
            elif self.guesses_left == 0:
                correct = self.number_to_guess
                self.number_to_guess = None
                return f"Game over! The number was {correct}."
            elif guess < self.number_to_guess:
                return f"Too low! You have {self.guesses_left} guesses left."
            else:
                return f"Too high! You have {self.guesses_left} guesses left."
        except Exception as e:
            return f"Error processing guess: {str(e)}"
    
    def flip_coin(self):
        """Flip a coin."""
        result = random.choice(["Heads", "Tails"])
        return f"The coin landed on: {result}!"
    
    def roll_dice(self):
        """Roll a dice."""
        result = random.randint(1, 6)
        return f"You rolled a {result}!"
    
    def magic_8_ball(self):
        """Magic 8 ball responses."""
        responses = [
            "It is certain.",
            "Without a doubt.",
            "Yes, definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        return random.choice(responses)
    
    def trivia_question(self):
        """Ask a trivia question."""
        questions = [
            "What is the capital of France? (Answer: Paris)",
            "What is 2 + 2? (Answer: 4)",
            "What planet is known as the Red Planet? (Answer: Mars)",
            "Who painted the Mona Lisa? (Answer: Leonardo da Vinci)",
            "What is the largest ocean on Earth? (Answer: Pacific Ocean)"
        ]
        return random.choice(questions)

# Global instance for maintaining game state
_games_instance = GamesCommands()

def handle_command(command):
    """Entry point for game commands."""
    return _games_instance.handle_command(command)
