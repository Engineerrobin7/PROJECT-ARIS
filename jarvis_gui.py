# jarvis_gui.py
"""
JARVIS-style GUI for ARIS with futuristic design and animations.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from datetime import datetime
from core.speech_input import SpeechInput
from core.speech_output import TTSEngine
from orion_engine.brain import Brain
from orion_engine.memory import Memory

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ARIS - J.A.R.V.I.S Interface")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set window size (80% of screen)
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        
        # Center window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg="#000000")
        
        # Initialize components
        self.brain = Brain()
        self.memory = Memory()
        self.speech_input = SpeechInput()
        self.tts_engine = TTSEngine()
        self.is_listening = False
        self.pulse_state = 0
        
        self._create_widgets()
        self._start_animations()
    
    def _create_widgets(self):
        """Create JARVIS-style widgets."""
        
        # Top frame with title and status
        top_frame = tk.Frame(self.root, bg="#000000", height=100)
        top_frame.pack(fill=tk.X, pady=20)
        top_frame.pack_propagate(False)
        
        # ARIS Title with glow effect
        title_label = tk.Label(
            top_frame,
            text="A.R.I.S",
            font=("Courier New", 48, "bold"),
            fg="#00ffff",
            bg="#000000"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            top_frame,
            text="Advanced Responsive Intelligence System",
            font=("Courier New", 12),
            fg="#00aaaa",
            bg="#000000"
        )
        subtitle_label.pack()
        
        # Main container with border
        main_container = tk.Frame(self.root, bg="#001a1a", bd=2, relief=tk.RIDGE)
        main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        # Status indicator (circular)
        status_frame = tk.Frame(main_container, bg="#001a1a", height=80)
        status_frame.pack(fill=tk.X, pady=10)
        
        self.status_canvas = tk.Canvas(
            status_frame,
            width=60,
            height=60,
            bg="#001a1a",
            highlightthickness=0
        )
        self.status_canvas.pack()
        
        # Draw status circle
        self.status_circle = self.status_canvas.create_oval(
            10, 10, 50, 50,
            fill="#003333",
            outline="#00ffff",
            width=2
        )
        
        # Chat display with custom styling
        chat_frame = tk.Frame(main_container, bg="#001a1a")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg="#000a0a",
            fg="#00ff00",
            insertbackground="#00ffff",
            relief=tk.FLAT,
            padx=15,
            pady=15,
            selectbackground="#003333",
            selectforeground="#00ffff"
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)
        
        # Input frame with futuristic design
        input_container = tk.Frame(main_container, bg="#001a1a", height=100)
        input_container.pack(fill=tk.X, padx=20, pady=20)
        input_container.pack_propagate(False)
        
        # Input field with border
        input_frame = tk.Frame(input_container, bg="#00ffff", bd=1)
        input_frame.pack(fill=tk.X, pady=10)
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Consolas", 13),
            bg="#001a1a",
            fg="#00ffff",
            insertbackground="#00ffff",
            relief=tk.FLAT,
            bd=5
        )
        self.input_field.pack(fill=tk.X, padx=2, pady=2)
        self.input_field.bind("<Return>", lambda e: self.send_message())
        self.input_field.focus()
        
        # Buttons frame
        buttons_frame = tk.Frame(input_container, bg="#001a1a")
        buttons_frame.pack(fill=tk.X)
        
        # Send button
        self.send_button = tk.Button(
            buttons_frame,
            text="⚡ SEND",
            command=self.send_message,
            bg="#003333",
            fg="#00ffff",
            font=("Courier New", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            activebackground="#004444",
            activeforeground="#00ffff"
        )
        self.send_button.pack(side=tk.LEFT, padx=5)
        
        # Voice button
        self.voice_button = tk.Button(
            buttons_frame,
            text="🎤 VOICE",
            command=self.toggle_voice,
            bg="#003333",
            fg="#00ff00",
            font=("Courier New", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            activebackground="#004400",
            activeforeground="#00ff00"
        )
        self.voice_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_button = tk.Button(
            buttons_frame,
            text="🗑 CLEAR",
            command=self.clear_chat,
            bg="#003333",
            fg="#ffaa00",
            font=("Courier New", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            activebackground="#443300",
            activeforeground="#ffaa00"
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Status bar at bottom
        self.status_bar = tk.Label(
            self.root,
            text="● ONLINE | READY FOR COMMANDS",
            font=("Courier New", 10),
            fg="#00ff00",
            bg="#000000",
            anchor=tk.W,
            padx=20,
            pady=10
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Welcome message
        self.add_system_message("SYSTEM INITIALIZED")
        self.add_message("ARIS", "Good evening, Sir. ARIS online and ready to assist.")
        self.add_system_message("All systems operational. Awaiting your command.")
    
    def _start_animations(self):
        """Start pulsing animations."""
        self.pulse_animation()
    
    def pulse_animation(self):
        """Animate the status circle."""
        if self.is_listening:
            # Pulsing effect when listening
            colors = ["#00ffff", "#00aaaa", "#005555", "#00aaaa"]
            color = colors[self.pulse_state % len(colors)]
            self.status_canvas.itemconfig(self.status_circle, outline=color, width=3)
            self.pulse_state += 1
            self.root.after(200, self.pulse_animation)
        else:
            # Steady glow when idle
            self.status_canvas.itemconfig(self.status_circle, outline="#00ffff", width=2)
            self.root.after(1000, self.pulse_animation)
    
    def add_system_message(self, message):
        """Add a system message."""
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
        self.chat_display.insert(tk.END, f"[SYSTEM] ", "system")
        self.chat_display.insert(tk.END, f"{message}\n", "system_msg")
        
        self.chat_display.tag_config("timestamp", foreground="#006666")
        self.chat_display.tag_config("system", foreground="#ffaa00", font=("Courier New", 10, "bold"))
        self.chat_display.tag_config("system_msg", foreground="#ffaa00")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def add_message(self, sender, message):
        """Add a message to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if sender == "ARIS":
            self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, f"ARIS: ", "aris")
            self.chat_display.insert(tk.END, f"{message}\n", "aris_msg")
            
            self.chat_display.tag_config("aris", foreground="#00ffff", font=("Courier New", 11, "bold"))
            self.chat_display.tag_config("aris_msg", foreground="#00ffff")
        else:
            self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, f"YOU: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n", "user_msg")
            
            self.chat_display.tag_config("user", foreground="#00ff00", font=("Courier New", 11, "bold"))
            self.chat_display.tag_config("user_msg", foreground="#00ff00")
        
        self.chat_display.tag_config("timestamp", foreground="#006666")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def send_message(self):
        """Send a text message."""
        message = self.input_field.get().strip()
        if not message:
            return
        
        self.input_field.delete(0, tk.END)
        self.add_message("YOU", message)
        self.status_bar.config(text="● PROCESSING | Analyzing command...", fg="#ffaa00")
        
        # Process in thread
        threading.Thread(target=self._process_command, args=(message,), daemon=True).start()
    
    def _process_command(self, command):
        """Process command through brain."""
        try:
            response = self.brain.route_command(command)
            self.root.after(0, self.add_message, "ARIS", response)
            self.root.after(0, self.tts_engine.speak, response)
            self.root.after(0, self.status_bar.config, {
                "text": "● ONLINE | READY FOR COMMANDS",
                "fg": "#00ff00"
            })
        except Exception as e:
            error_msg = f"Error processing command: {str(e)}"
            self.root.after(0, self.add_message, "ARIS", error_msg)
            self.root.after(0, self.status_bar.config, {
                "text": "● ERROR | System malfunction detected",
                "fg": "#ff0000"
            })
    
    def toggle_voice(self):
        """Toggle voice input."""
        if not self.is_listening:
            self.is_listening = True
            self.voice_button.config(text="⏹ STOP", bg="#440000", fg="#ff0000")
            self.status_bar.config(text="● LISTENING | Speak your command...", fg="#00ffff")
            self.add_system_message("Voice recognition activated. Listening...")
            threading.Thread(target=self._listen_voice, daemon=True).start()
        else:
            self.is_listening = False
            self.voice_button.config(text="🎤 VOICE", bg="#003333", fg="#00ff00")
            self.status_bar.config(text="● ONLINE | READY FOR COMMANDS", fg="#00ff00")
    
    def _listen_voice(self):
        """Listen for voice input."""
        try:
            command = self.speech_input.listen()
            if command and self.is_listening:
                self.root.after(0, self.add_message, "YOU", command)
                self.root.after(0, self.status_bar.config, {
                    "text": "● PROCESSING | Analyzing voice command...",
                    "fg": "#ffaa00"
                })
                threading.Thread(target=self._process_command, args=(command,), daemon=True).start()
        except Exception as e:
            error_msg = f"Voice input error: {str(e)}"
            self.root.after(0, self.add_message, "ARIS", error_msg)
        finally:
            self.is_listening = False
            self.root.after(0, self.voice_button.config, {
                "text": "🎤 VOICE",
                "bg": "#003333",
                "fg": "#00ff00"
            })
    
    def clear_chat(self):
        """Clear the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.add_system_message("Chat cleared. Ready for new commands.")

def main():
    """Launch the JARVIS GUI."""
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
