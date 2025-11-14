# jarvis_advanced.py
"""
Advanced JARVIS-style GUI with animations, sound visualizer, and holographic effects.
"""
import tkinter as tk
from tkinter import scrolledtext
import threading
import math
from datetime import datetime
from core.speech_input import SpeechInput
from core.speech_output import TTSEngine
from orion_engine.brain import Brain
from orion_engine.memory import Memory

class JarvisAdvanced:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S - ARIS Interface")
        
        # Fullscreen option
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
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
        self.animation_angle = 0
        
        self._create_widgets()
        self._start_animations()
    
    def _create_widgets(self):
        """Create advanced JARVIS interface."""
        
        # Header with animated circle
        header_frame = tk.Frame(self.root, bg="#000000", height=150)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Animated canvas for circle
        self.header_canvas = tk.Canvas(
            header_frame,
            width=120,
            height=120,
            bg="#000000",
            highlightthickness=0
        )
        self.header_canvas.pack(pady=15)
        
        # Draw concentric circles
        self.circles = []
        for i in range(3):
            radius = 20 + (i * 15)
            circle = self.header_canvas.create_oval(
                60 - radius, 60 - radius,
                60 + radius, 60 + radius,
                outline=f"#{0:02x}{255-i*50:02x}{255-i*50:02x}",
                width=2
            )
            self.circles.append(circle)
        
        # Center dot
        self.center_dot = self.header_canvas.create_oval(
            55, 55, 65, 65,
            fill="#00ffff",
            outline="#00ffff"
        )
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="J.A.R.V.I.S",
            font=("Arial Black", 36, "bold"),
            fg="#00ffff",
            bg="#000000"
        )
        title_label.pack()
        
        # Subtitle with typing effect
        self.subtitle_label = tk.Label(
            header_frame,
            text="Just A Rather Very Intelligent System",
            font=("Courier New", 11, "italic"),
            fg="#00aaaa",
            bg="#000000"
        )
        self.subtitle_label.pack()
        
        # Main content area
        content_frame = tk.Frame(self.root, bg="#000000")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Left panel - System info
        left_panel = tk.Frame(content_frame, bg="#001a1a", width=250, bd=1, relief=tk.RIDGE)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # System status
        status_title = tk.Label(
            left_panel,
            text="SYSTEM STATUS",
            font=("Courier New", 10, "bold"),
            fg="#00ffff",
            bg="#001a1a"
        )
        status_title.pack(pady=10)
        
        # Status items
        self.status_items = []
        statuses = [
            ("CORE", "ONLINE"),
            ("NEURAL NET", "ACTIVE"),
            ("VOICE", "READY"),
            ("MEMORY", "OPTIMAL"),
            ("APIS", "CONNECTED")
        ]
        
        for label, status in statuses:
            frame = tk.Frame(left_panel, bg="#001a1a")
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(
                frame,
                text=label,
                font=("Courier New", 9),
                fg="#00aaaa",
                bg="#001a1a",
                anchor=tk.W
            ).pack(side=tk.LEFT)
            
            status_label = tk.Label(
                frame,
                text=status,
                font=("Courier New", 9, "bold"),
                fg="#00ff00",
                bg="#001a1a",
                anchor=tk.E
            )
            status_label.pack(side=tk.RIGHT)
            self.status_items.append(status_label)
        
        # Separator
        tk.Frame(left_panel, bg="#00ffff", height=1).pack(fill=tk.X, padx=10, pady=15)
        
        # Quick stats
        stats_title = tk.Label(
            left_panel,
            text="STATISTICS",
            font=("Courier New", 10, "bold"),
            fg="#00ffff",
            bg="#001a1a"
        )
        stats_title.pack(pady=10)
        
        self.stats_label = tk.Label(
            left_panel,
            text="Commands: 0\nUptime: 00:00\nResponse: 0ms",
            font=("Courier New", 8),
            fg="#00aaaa",
            bg="#001a1a",
            justify=tk.LEFT
        )
        self.stats_label.pack(padx=10)
        
        # Center panel - Chat
        center_panel = tk.Frame(content_frame, bg="#001a1a", bd=1, relief=tk.RIDGE)
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Chat header
        chat_header = tk.Frame(center_panel, bg="#002a2a", height=40)
        chat_header.pack(fill=tk.X)
        chat_header.pack_propagate(False)
        
        tk.Label(
            chat_header,
            text="◉ COMMUNICATION INTERFACE",
            font=("Courier New", 11, "bold"),
            fg="#00ffff",
            bg="#002a2a"
        ).pack(pady=10)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            center_panel,
            wrap=tk.WORD,
            font=("Consolas", 11),
            bg="#000a0a",
            fg="#00ff00",
            insertbackground="#00ffff",
            relief=tk.FLAT,
            padx=20,
            pady=20,
            selectbackground="#003333",
            selectforeground="#00ffff"
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        self.chat_display.config(state=tk.DISABLED)
        
        # Input area
        input_frame = tk.Frame(center_panel, bg="#002a2a", height=80)
        input_frame.pack(fill=tk.X)
        input_frame.pack_propagate(False)
        
        # Input field
        input_container = tk.Frame(input_frame, bg="#00ffff", bd=1)
        input_container.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_field = tk.Entry(
            input_container,
            font=("Consolas", 12),
            bg="#001a1a",
            fg="#00ffff",
            insertbackground="#00ffff",
            relief=tk.FLAT,
            bd=5
        )
        self.input_field.pack(fill=tk.X, padx=1, pady=1)
        self.input_field.bind("<Return>", lambda e: self.send_message())
        self.input_field.focus()
        
        # Control buttons
        button_frame = tk.Frame(input_frame, bg="#002a2a")
        button_frame.pack(fill=tk.X, padx=10)
        
        # Send button
        self.send_btn = tk.Button(
            button_frame,
            text="▶ EXECUTE",
            command=self.send_message,
            bg="#003333",
            fg="#00ffff",
            font=("Courier New", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2",
            activebackground="#005555",
            activeforeground="#00ffff"
        )
        self.send_btn.pack(side=tk.LEFT, padx=3)
        
        # Voice button
        self.voice_btn = tk.Button(
            button_frame,
            text="🎤 VOICE",
            command=self.toggle_voice,
            bg="#003333",
            fg="#00ff00",
            font=("Courier New", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2",
            activebackground="#004400",
            activeforeground="#00ff00"
        )
        self.voice_btn.pack(side=tk.LEFT, padx=3)
        
        # Clear button
        tk.Button(
            button_frame,
            text="⟲ CLEAR",
            command=self.clear_chat,
            bg="#003333",
            fg="#ffaa00",
            font=("Courier New", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2",
            activebackground="#443300",
            activeforeground="#ffaa00"
        ).pack(side=tk.LEFT, padx=3)
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="█ SYSTEM ONLINE | ALL SYSTEMS OPERATIONAL | AWAITING COMMAND",
            font=("Courier New", 9, "bold"),
            fg="#00ff00",
            bg="#000000",
            anchor=tk.W,
            padx=20,
            pady=8
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Welcome messages
        self.add_system_message("JARVIS INTERFACE INITIALIZED")
        self.add_system_message("All systems operational. Neural network active.")
        self.add_message("JARVIS", "Good evening. I am JARVIS, your virtual assistant. How may I be of service?")
    
    def _start_animations(self):
        """Start all animations."""
        self.animate_circles()
        self.update_time()
    
    def animate_circles(self):
        """Animate the header circles."""
        self.animation_angle += 5
        
        for i, circle in enumerate(self.circles):
            # Rotate effect
            offset = i * 120
            angle = math.radians(self.animation_angle + offset)
            
            # Pulsing opacity effect (simulated with color)
            intensity = int(155 + 100 * math.sin(angle))
            color = f"#{0:02x}{intensity:02x}{intensity:02x}"
            
            self.header_canvas.itemconfig(circle, outline=color)
        
        # Pulse center dot
        if self.is_listening:
            size_offset = int(5 * math.sin(math.radians(self.animation_angle * 2)))
            self.header_canvas.coords(
                self.center_dot,
                55 - size_offset, 55 - size_offset,
                65 + size_offset, 65 + size_offset
            )
        
        self.root.after(50, self.animate_circles)
    
    def update_time(self):
        """Update time display."""
        current_time = datetime.now().strftime("%H:%M:%S")
        # Update can be added to status bar if needed
        self.root.after(1000, self.update_time)
    
    def add_system_message(self, message):
        """Add system message."""
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
        self.chat_display.insert(tk.END, "[SYSTEM] ", "system")
        self.chat_display.insert(tk.END, f"{message}\n", "system_msg")
        
        self.chat_display.tag_config("timestamp", foreground="#006666", font=("Courier New", 9))
        self.chat_display.tag_config("system", foreground="#ffaa00", font=("Courier New", 10, "bold"))
        self.chat_display.tag_config("system_msg", foreground="#ffaa00")
        
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def add_message(self, sender, message):
        """Add message to chat."""
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if sender == "JARVIS":
            self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, "JARVIS: ", "jarvis")
            self.chat_display.insert(tk.END, f"{message}\n", "jarvis_msg")
            
            self.chat_display.tag_config("jarvis", foreground="#00ffff", font=("Courier New", 11, "bold"))
            self.chat_display.tag_config("jarvis_msg", foreground="#00ffff")
        else:
            self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, "SIR: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n", "user_msg")
            
            self.chat_display.tag_config("user", foreground="#00ff00", font=("Courier New", 11, "bold"))
            self.chat_display.tag_config("user_msg", foreground="#00ff00")
        
        self.chat_display.tag_config("timestamp", foreground="#006666", font=("Courier New", 9))
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def send_message(self):
        """Send message."""
        message = self.input_field.get().strip()
        if not message:
            return
        
        self.input_field.delete(0, tk.END)
        self.add_message("SIR", message)
        self.status_bar.config(text="█ PROCESSING | Analyzing command...", fg="#ffaa00")
        
        threading.Thread(target=self._process_command, args=(message,), daemon=True).start()
    
    def _process_command(self, command):
        """Process command."""
        try:
            response = self.brain.route_command(command)
            self.root.after(0, self.add_message, "JARVIS", response)
            self.root.after(0, self.tts_engine.speak, response)
            self.root.after(0, self.status_bar.config, {
                "text": "█ SYSTEM ONLINE | ALL SYSTEMS OPERATIONAL | AWAITING COMMAND",
                "fg": "#00ff00"
            })
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.root.after(0, self.add_message, "JARVIS", error_msg)
            self.root.after(0, self.status_bar.config, {
                "text": "█ ERROR | System malfunction detected",
                "fg": "#ff0000"
            })
    
    def toggle_voice(self):
        """Toggle voice input."""
        if not self.is_listening:
            self.is_listening = True
            self.voice_btn.config(text="⏹ STOP", bg="#440000", fg="#ff0000")
            self.status_bar.config(text="█ LISTENING | Voice recognition active...", fg="#00ffff")
            self.add_system_message("Voice recognition activated. Listening...")
            threading.Thread(target=self._listen_voice, daemon=True).start()
        else:
            self.is_listening = False
            self.voice_btn.config(text="🎤 VOICE", bg="#003333", fg="#00ff00")
            self.status_bar.config(text="█ SYSTEM ONLINE | AWAITING COMMAND", fg="#00ff00")
    
    def _listen_voice(self):
        """Listen for voice."""
        try:
            command = self.speech_input.listen()
            if command and self.is_listening:
                self.root.after(0, self.add_message, "SIR", command)
                threading.Thread(target=self._process_command, args=(command,), daemon=True).start()
        except Exception as e:
            self.root.after(0, self.add_message, "JARVIS", f"Voice error: {str(e)}")
        finally:
            self.is_listening = False
            self.root.after(0, self.voice_btn.config, {
                "text": "🎤 VOICE",
                "bg": "#003333",
                "fg": "#00ff00"
            })
    
    def clear_chat(self):
        """Clear chat."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.add_system_message("Communication log cleared.")

def main():
    """Launch JARVIS."""
    root = tk.Tk()
    app = JarvisAdvanced(root)
    root.mainloop()

if __name__ == "__main__":
    main()
