# gui_enhanced.py
"""
Enhanced GUI for ARIS with modern design and all features.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from datetime import datetime
from core.speech_input import SpeechInput
from core.speech_output import TTSEngine
from orion_engine.brain import Brain
from orion_engine.memory import Memory

class ARISEnhancedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ARIS - Advanced AI Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")
        
        # Initialize components
        self.brain = Brain()
        self.memory = Memory()
        self.speech_input = SpeechInput()
        self.tts_engine = TTSEngine()
        self.is_listening = False
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create GUI widgets."""
        # Title
        title_frame = tk.Frame(self.root, bg="#1e1e1e")
        title_frame.pack(pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="ARIS Assistant",
            font=("Arial", 24, "bold"),
            fg="#00d4ff",
            bg="#1e1e1e"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Your AI Companion",
            font=("Arial", 12),
            fg="#888888",
            bg="#1e1e1e"
        )
        subtitle_label.pack()
        
        # Chat display
        chat_frame = tk.Frame(self.root, bg="#1e1e1e")
        chat_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="#2d2d2d",
            fg="#ffffff",
            insertbackground="#00d4ff",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#1e1e1e")
        input_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#2d2d2d",
            fg="#ffffff",
            insertbackground="#00d4ff",
            relief=tk.FLAT
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", lambda e: self.send_message())
        
        # Buttons frame
        buttons_frame = tk.Frame(input_frame, bg="#1e1e1e")
        buttons_frame.pack(side=tk.RIGHT)
        
        self.send_button = tk.Button(
            buttons_frame,
            text="Send",
            command=self.send_message,
            bg="#00d4ff",
            fg="#1e1e1e",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        self.send_button.pack(side=tk.LEFT, padx=5)
        
        self.voice_button = tk.Button(
            buttons_frame,
            text="🎤 Voice",
            command=self.toggle_voice,
            bg="#4CAF50",
            fg="#ffffff",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2"
        )
        self.voice_button.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 9),
            fg="#888888",
            bg="#1e1e1e",
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=5)
        
        # Welcome message
        self.add_message("ARIS", "Hello! I'm ARIS, your AI assistant. How can I help you today?")
    
    def add_message(self, sender, message):
        """Add a message to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M")
        
        if sender == "ARIS":
            self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, f"ARIS: ", "aris")
            self.chat_display.insert(tk.END, f"{message}\n\n", "message")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, f"You: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n\n", "message")
        
        # Configure tags
        self.chat_display.tag_config("timestamp", foreground="#888888")
        self.chat_display.tag_config("aris", foreground="#00d4ff", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("user", foreground="#4CAF50", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("message", foreground="#ffffff")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def send_message(self):
        """Send a text message."""
        message = self.input_field.get().strip()
        if not message:
            return
        
        self.input_field.delete(0, tk.END)
        self.add_message("You", message)
        self.status_bar.config(text="Processing...")
        
        # Process in thread to avoid blocking GUI
        threading.Thread(target=self._process_command, args=(message,), daemon=True).start()
    
    def _process_command(self, command):
        """Process command through brain."""
        try:
            response = self.brain.route_command(command)
            self.root.after(0, self.add_message, "ARIS", response)
            self.root.after(0, self.tts_engine.speak, response)
            self.root.after(0, self.status_bar.config, {"text": "Ready"})
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.root.after(0, self.add_message, "ARIS", error_msg)
            self.root.after(0, self.status_bar.config, {"text": "Error occurred"})
    
    def toggle_voice(self):
        """Toggle voice input."""
        if not self.is_listening:
            self.is_listening = True
            self.voice_button.config(text="⏹ Stop", bg="#f44336")
            self.status_bar.config(text="Listening...")
            threading.Thread(target=self._listen_voice, daemon=True).start()
        else:
            self.is_listening = False
            self.voice_button.config(text="🎤 Voice", bg="#4CAF50")
            self.status_bar.config(text="Ready")
    
    def _listen_voice(self):
        """Listen for voice input."""
        try:
            command = self.speech_input.listen()
            if command and self.is_listening:
                self.root.after(0, self.add_message, "You", command)
                self.root.after(0, self.status_bar.config, {"text": "Processing..."})
                # Process command in a separate thread
                threading.Thread(target=self._process_command, args=(command,), daemon=True).start()
        except Exception as e:
            error_msg = f"Voice input error: {str(e)}"
            self.root.after(0, self.add_message, "ARIS", error_msg)
        finally:
            self.is_listening = False
            self.root.after(0, self.voice_button.config, {"text": "🎤 Voice", "bg": "#4CAF50"})
            if not self.is_listening:
                self.root.after(0, self.status_bar.config, {"text": "Ready"})

def main():
    """Launch the enhanced GUI."""
    root = tk.Tk()
    app = ARISEnhancedGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
