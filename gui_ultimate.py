"""
Ultimate GUI for ARIS with all features integrated
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import logging
from datetime import datetime

# Import enhanced ARIS
from aris_enhanced import ARISEnhanced

class ARISUltimateGUI:
    """Ultimate GUI with all ARIS features"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ARIS Ultimate Control Center")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1e1e2e')
        
        # Initialize ARIS
        self.aris = None
        self.init_thread = None
        
        self.setup_ui()
        self.start_aris()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Create notebook for tabs
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#1e1e2e', borderwidth=0)
        style.configure('TNotebook.Tab', background='#2e2e3e', foreground='white', 
                       padding=[20, 10], font=('Arial', 10, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', '#667eea')])
        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_main_tab()
        self.create_plugins_tab()
        self.create_smart_home_tab()
        self.create_scheduler_tab()
        self.create_custom_commands_tab()
        self.create_file_manager_tab()
        self.create_settings_tab()
    
    def create_main_tab(self):
        """Create main control tab"""
        main_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(main_frame, text='💬 Main')
        
        # Title
        title = tk.Label(main_frame, text="ARIS Ultimate Control Center", 
                        font=('Arial', 24, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Status
        self.status_label = tk.Label(main_frame, text="● Initializing...", 
                                     font=('Arial', 12), bg='#1e1e2e', fg='#4CAF50')
        self.status_label.pack()
        
        # Chat area
        chat_frame = tk.Frame(main_frame, bg='#2e2e3e')
        chat_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, 
                                                       font=('Arial', 11), bg='#2e2e3e', 
                                                       fg='white', insertbackground='white')
        self.chat_display.pack(fill='both', expand=True)
        
        # Input area
        input_frame = tk.Frame(main_frame, bg='#1e1e2e')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        self.command_entry = tk.Entry(input_frame, font=('Arial', 12), bg='#2e2e3e', 
                                      fg='white', insertbackground='white')
        self.command_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        self.command_entry.bind('<Return>', lambda e: self.send_command())
        
        send_btn = tk.Button(input_frame, text="Send", command=self.send_command,
                            bg='#667eea', fg='white', font=('Arial', 12, 'bold'),
                            relief='flat', padx=20)
        send_btn.pack(side='right')
        
        voice_btn = tk.Button(input_frame, text="🎤 Voice", command=self.voice_input,
                             bg='#764ba2', fg='white', font=('Arial', 12, 'bold'),
                             relief='flat', padx=20)
        voice_btn.pack(side='right', padx=(0, 10))
    
    def create_plugins_tab(self):
        """Create plugins management tab"""
        plugins_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(plugins_frame, text='🔌 Plugins')
        
        title = tk.Label(plugins_frame, text="Plugin Manager", 
                        font=('Arial', 20, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Plugin list
        list_frame = tk.Frame(plugins_frame, bg='#2e2e3e')
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.plugin_listbox = tk.Listbox(list_frame, font=('Arial', 11), bg='#2e2e3e', 
                                         fg='white', selectbackground='#667eea')
        self.plugin_listbox.pack(fill='both', expand=True)
        
        # Buttons
        btn_frame = tk.Frame(plugins_frame, bg='#1e1e2e')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Refresh", command=self.refresh_plugins,
                 bg='#667eea', fg='white', font=('Arial', 11), relief='flat', padx=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Enable", command=self.enable_plugin,
                 bg='#4CAF50', fg='white', font=('Arial', 11), relief='flat', padx=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Disable", command=self.disable_plugin,
                 bg='#f44336', fg='white', font=('Arial', 11), relief='flat', padx=15).pack(side='left', padx=5)
    
    def create_smart_home_tab(self):
        """Create smart home control tab"""
        smart_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(smart_frame, text='🏠 Smart Home')
        
        title = tk.Label(smart_frame, text="Smart Home Control", 
                        font=('Arial', 20, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Device list
        self.device_frame = tk.Frame(smart_frame, bg='#1e1e2e')
        self.device_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Button(smart_frame, text="Discover Devices", command=self.discover_devices,
                 bg='#667eea', fg='white', font=('Arial', 12, 'bold'), 
                 relief='flat', padx=20, pady=10).pack(pady=10)
    
    def create_scheduler_tab(self):
        """Create scheduler tab"""
        scheduler_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(scheduler_frame, text='⏰ Scheduler')
        
        title = tk.Label(scheduler_frame, text="Task Scheduler", 
                        font=('Arial', 20, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Add task section
        add_frame = tk.Frame(scheduler_frame, bg='#2e2e3e')
        add_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(add_frame, text="Task Name:", bg='#2e2e3e', fg='white', 
                font=('Arial', 11)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.task_name_entry = tk.Entry(add_frame, font=('Arial', 11), bg='#1e1e2e', 
                                        fg='white', width=30)
        self.task_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_frame, text="Time:", bg='#2e2e3e', fg='white', 
                font=('Arial', 11)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.task_time_entry = tk.Entry(add_frame, font=('Arial', 11), bg='#1e1e2e', 
                                        fg='white', width=30)
        self.task_time_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(add_frame, text="Add Task", command=self.add_task,
                 bg='#667eea', fg='white', font=('Arial', 11), 
                 relief='flat', padx=15).grid(row=2, column=1, pady=10)
        
        # Task list
        self.task_listbox = tk.Listbox(scheduler_frame, font=('Arial', 11), 
                                       bg='#2e2e3e', fg='white', height=15)
        self.task_listbox.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Button(scheduler_frame, text="Refresh Tasks", command=self.refresh_tasks,
                 bg='#667eea', fg='white', font=('Arial', 11), 
                 relief='flat', padx=15).pack(pady=10)
    
    def create_custom_commands_tab(self):
        """Create custom commands tab"""
        custom_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(custom_frame, text='⚡ Custom Commands')
        
        title = tk.Label(custom_frame, text="Custom Commands", 
                        font=('Arial', 20, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Add command section
        add_frame = tk.Frame(custom_frame, bg='#2e2e3e')
        add_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(add_frame, text="Trigger:", bg='#2e2e3e', fg='white', 
                font=('Arial', 11)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.cmd_trigger_entry = tk.Entry(add_frame, font=('Arial', 11), 
                                          bg='#1e1e2e', fg='white', width=30)
        self.cmd_trigger_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(add_frame, text="Response:", bg='#2e2e3e', fg='white', 
                font=('Arial', 11)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.cmd_response_entry = tk.Entry(add_frame, font=('Arial', 11), 
                                           bg='#1e1e2e', fg='white', width=30)
        self.cmd_response_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(add_frame, text="Add Command", command=self.add_custom_command,
                 bg='#667eea', fg='white', font=('Arial', 11), 
                 relief='flat', padx=15).grid(row=2, column=1, pady=10)
        
        # Command list
        self.custom_cmd_listbox = tk.Listbox(custom_frame, font=('Arial', 11), 
                                             bg='#2e2e3e', fg='white', height=15)
        self.custom_cmd_listbox.pack(fill='both', expand=True, padx=20, pady=10)
    
    def create_file_manager_tab(self):
        """Create file manager tab"""
        file_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(file_frame, text='📁 Files')
        
        title = tk.Label(file_frame, text="File Manager", 
                        font=('Arial', 20, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Quick actions
        action_frame = tk.Frame(file_frame, bg='#2e2e3e')
        action_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Button(action_frame, text="📂 Open File Manager", 
                 command=self.open_file_manager_window,
                 bg='#667eea', fg='white', font=('Arial', 12, 'bold'),
                 relief='flat', padx=20, pady=10).pack(pady=10)
        
        # Voice commands info
        info_frame = tk.Frame(file_frame, bg='#2e2e3e')
        info_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Label(info_frame, text="Voice Commands:", bg='#2e2e3e', fg='#667eea',
                font=('Arial', 14, 'bold')).pack(anchor='w', padx=10, pady=10)
        
        commands = [
            "• List files - Show files in current directory",
            "• Create file [name] - Create a new file",
            "• Create folder [name] - Create a new folder",
            "• Delete file [name] - Delete a file",
            "• Rename [old] to [new] - Rename a file",
            "• Copy file [source] to [dest] - Copy a file",
            "• Move file [source] to [dest] - Move a file",
            "• Search for [query] - Search for files",
            "• File info [name] - Get file information",
            "• Organize files - Organize by file type",
            "• Folder size - Get current folder size"
        ]
        
        for cmd in commands:
            tk.Label(info_frame, text=cmd, bg='#2e2e3e', fg='white',
                    font=('Arial', 10), anchor='w').pack(anchor='w', padx=20, pady=2)
    
    def create_settings_tab(self):
        """Create settings tab"""
        settings_frame = tk.Frame(self.notebook, bg='#1e1e2e')
        self.notebook.add(settings_frame, text='⚙️ Settings')
        
        title = tk.Label(settings_frame, text="Settings", 
                        font=('Arial', 20, 'bold'), bg='#1e1e2e', fg='#667eea')
        title.pack(pady=20)
        
        # Language selection
        lang_frame = tk.Frame(settings_frame, bg='#2e2e3e')
        lang_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(lang_frame, text="Language:", bg='#2e2e3e', fg='white', 
                font=('Arial', 12)).pack(side='left', padx=10)
        
        self.language_var = tk.StringVar(value="English")
        languages = ["English", "Español", "Français", "Deutsch", "Italiano"]
        lang_menu = ttk.Combobox(lang_frame, textvariable=self.language_var, 
                                values=languages, state='readonly', font=('Arial', 11))
        lang_menu.pack(side='left', padx=10)
        
        # Stats
        stats_frame = tk.Frame(settings_frame, bg='#2e2e3e')
        stats_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.stats_text = scrolledtext.ScrolledText(stats_frame, wrap=tk.WORD, 
                                                     font=('Arial', 11), bg='#2e2e3e', 
                                                     fg='white', height=15)
        self.stats_text.pack(fill='both', expand=True)
        
        tk.Button(settings_frame, text="Show Statistics", command=self.show_stats,
                 bg='#667eea', fg='white', font=('Arial', 12), 
                 relief='flat', padx=20, pady=10).pack(pady=10)
    
    def start_aris(self):
        """Start ARIS in background thread"""
        def init():
            try:
                self.aris = ARISEnhanced()
                self.status_label.config(text="● Online", fg='#4CAF50')
                self.add_chat_message("System", "ARIS Enhanced is online and ready!")
            except Exception as e:
                self.status_label.config(text="● Error", fg='#f44336')
                self.add_chat_message("System", f"Error initializing: {str(e)}")
        
        self.init_thread = threading.Thread(target=init, daemon=True)
        self.init_thread.start()
    
    def send_command(self):
        """Send command to ARIS"""
        command = self.command_entry.get().strip()
        if not command:
            return
        
        self.add_chat_message("You", command)
        self.command_entry.delete(0, tk.END)
        
        def process():
            if self.aris:
                response = self.aris.process_command(command)
                self.add_chat_message("ARIS", response)
            else:
                self.add_chat_message("System", "ARIS not initialized yet")
        
        threading.Thread(target=process, daemon=True).start()
    
    def voice_input(self):
        """Handle voice input"""
        self.add_chat_message("System", "Listening...")
        
        def listen():
            if self.aris:
                command = self.aris.speech_input.listen()
                if command:
                    self.command_entry.delete(0, tk.END)
                    self.command_entry.insert(0, command)
                    self.send_command()
                else:
                    self.add_chat_message("System", "No speech detected")
        
        threading.Thread(target=listen, daemon=True).start()
    
    def add_chat_message(self, sender, message):
        """Add message to chat display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"[{timestamp}] {sender}: {message}\n\n")
        self.chat_display.see(tk.END)
    
    def refresh_plugins(self):
        """Refresh plugin list"""
        if not self.aris:
            return
        
        self.plugin_listbox.delete(0, tk.END)
        plugins = self.aris.plugin_manager.get_all_plugins()
        for name, info in plugins.items():
            status = "✓" if info['enabled'] else "✗"
            self.plugin_listbox.insert(tk.END, f"{status} {name} - {info['description']}")
    
    def enable_plugin(self):
        """Enable selected plugin"""
        selection = self.plugin_listbox.curselection()
        if selection and self.aris:
            plugin_name = self.plugin_listbox.get(selection[0]).split()[1]
            self.aris.plugin_manager.enable_plugin(plugin_name)
            self.refresh_plugins()
    
    def disable_plugin(self):
        """Disable selected plugin"""
        selection = self.plugin_listbox.curselection()
        if selection and self.aris:
            plugin_name = self.plugin_listbox.get(selection[0]).split()[1]
            self.aris.plugin_manager.disable_plugin(plugin_name)
            self.refresh_plugins()
    
    def discover_devices(self):
        """Discover smart home devices"""
        if not self.aris:
            return
        
        devices = self.aris.smart_home.discover_devices()
        
        # Clear existing widgets
        for widget in self.device_frame.winfo_children():
            widget.destroy()
        
        # Add device controls
        for device in devices:
            device_card = tk.Frame(self.device_frame, bg='#2e2e3e')
            device_card.pack(fill='x', padx=10, pady=5)
            
            tk.Label(device_card, text=device['name'], bg='#2e2e3e', fg='white', 
                    font=('Arial', 12)).pack(side='left', padx=10)
            
            tk.Button(device_card, text="Control", bg='#667eea', fg='white',
                     relief='flat', padx=10).pack(side='right', padx=10)
    
    def add_task(self):
        """Add scheduled task"""
        if not self.aris:
            return
        
        task_name = self.task_name_entry.get().strip()
        task_time = self.task_time_entry.get().strip()
        
        if task_name and task_time:
            result = self.aris.scheduler.add_task(task_name, task_time)
            messagebox.showinfo("Task Added", result)
            self.task_name_entry.delete(0, tk.END)
            self.task_time_entry.delete(0, tk.END)
            self.refresh_tasks()
    
    def refresh_tasks(self):
        """Refresh task list"""
        if not self.aris:
            return
        
        self.task_listbox.delete(0, tk.END)
        tasks = self.aris.scheduler.get_upcoming_tasks(hours=168)  # 1 week
        for task in tasks:
            time_str = datetime.fromisoformat(task['scheduled_time']).strftime("%Y-%m-%d %H:%M")
            self.task_listbox.insert(tk.END, f"{task['name']} - {time_str}")
    
    def add_custom_command(self):
        """Add custom command"""
        if not self.aris:
            return
        
        trigger = self.cmd_trigger_entry.get().strip()
        response = self.cmd_response_entry.get().strip()
        
        if trigger and response:
            self.aris.custom_commands.add_command(trigger, "speak", response, response)
            messagebox.showinfo("Command Added", f"Custom command '{trigger}' added")
            self.cmd_trigger_entry.delete(0, tk.END)
            self.cmd_response_entry.delete(0, tk.END)
    
    def show_stats(self):
        """Show conversation statistics"""
        if not self.aris:
            return
        
        stats = self.aris.context.get_statistics()
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(tk.END, "=== ARIS Statistics ===\n\n")
        for key, value in stats.items():
            self.stats_text.insert(tk.END, f"{key}: {value}\n")
    
    def open_file_manager_window(self):
        """Open file manager in new window"""
        from file_manager.gui_file_manager import FileManagerGUI
        FileManagerGUI(parent=self.root)
    
    def run(self):
        """Run the GUI"""
        self.root.mainloop()

def main():
    """Main entry point"""
    app = ARISUltimateGUI()
    app.run()

if __name__ == "__main__":
    main()
