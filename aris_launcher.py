# ARIS Launcher - A simple GUI to start and manage ARIS

import tkinter as tk
import subprocess
import os
import sys
import threading
import psutil

class ARISLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("ARIS Voice Assistant Launcher")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Set icon (using system icon)
        if os.name == 'nt':  # Windows
            self.root.iconbitmap(default="shell32.dll,173")
        
        # ARIS process
        self.aris_process = None
        self.is_running = False
        
        self.create_widgets()
        self.check_aris_status()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="ARIS Voice Assistant", font=("Arial", 18, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)
        
        # Status frame
        status_frame = tk.Frame(self.root, bg="#f0f0f0")
        status_frame.pack(pady=10, fill="x", padx=20)
        
        status_label = tk.Label(status_frame, text="Status:", font=("Arial", 12), bg="#f0f0f0")
        status_label.pack(side="left")
        
        self.status_value = tk.Label(status_frame, text="Checking...", font=("Arial", 12, "bold"), fg="#888888", bg="#f0f0f0")
        self.status_value.pack(side="left", padx=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        # Start button
        self.start_button = tk.Button(button_frame, text="Start ARIS", command=self.start_aris, 
                                    font=("Arial", 12), width=15, height=2, bg="#4CAF50", fg="white")
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Stop button
        self.stop_button = tk.Button(button_frame, text="Stop ARIS", command=self.stop_aris, 
                                   font=("Arial", 12), width=15, height=2, bg="#F44336", fg="white")
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Restart button
        restart_button = tk.Button(button_frame, text="Restart ARIS", command=self.restart_aris, 
                                 font=("Arial", 12), width=15, height=2, bg="#2196F3", fg="white")
        restart_button.grid(row=1, column=0, padx=10, pady=10)
        
        # Hide button
        hide_button = tk.Button(button_frame, text="Hide to Tray", command=self.minimize_to_tray, 
                              font=("Arial", 12), width=15, height=2, bg="#9E9E9E", fg="white")
        hide_button.grid(row=1, column=1, padx=10, pady=10)
        
        # Autostart options
        autostart_frame = tk.LabelFrame(self.root, text="Autostart Options", font=("Arial", 12), bg="#f0f0f0")
        autostart_frame.pack(pady=20, padx=20, fill="x")
        
        add_startup_button = tk.Button(autostart_frame, text="Add to Windows Startup", 
                                     command=self.add_to_startup, font=("Arial", 10))
        add_startup_button.pack(pady=10, padx=10, fill="x")
        
        install_service_button = tk.Button(autostart_frame, text="Install as Windows Service", 
                                         command=self.install_as_service, font=("Arial", 10))
        install_service_button.pack(pady=10, padx=10, fill="x")
        
        # Instructions
        instructions = tk.Label(self.root, text="Say 'wake up aris' to activate the assistant", 
                              font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#555555")
        instructions.pack(pady=10)
    
    def check_aris_status(self):
        # Check if ARIS is running by looking for Python processes with main.py
        self.is_running = False
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] == 'python.exe' and any('main.py' in cmd for cmd in proc.info['cmdline'] if cmd):
                    self.is_running = True
                    self.aris_process = proc
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Update status and buttons
        if self.is_running:
            self.status_value.config(text="Running", fg="#4CAF50")
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
        else:
            self.status_value.config(text="Stopped", fg="#F44336")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
        
        # Schedule next check
        self.root.after(2000, self.check_aris_status)
    
    def start_aris(self):
        if not self.is_running:
            # Get the project directory
            project_dir = os.path.dirname(os.path.abspath(__file__))
            start_script = os.path.join(project_dir, "start_aris_background.vbs")
            
            # Start ARIS in the background
            if os.path.exists(start_script):
                subprocess.Popen(["wscript.exe", start_script], 
                                shell=True, 
                                creationflags=subprocess.CREATE_NO_WINDOW)
                
                self.status_value.config(text="Starting...", fg="#2196F3")
    
    def stop_aris(self):
        if self.is_running and self.aris_process:
            try:
                # Try to terminate the process
                self.aris_process.terminate()
                self.status_value.config(text="Stopping...", fg="#FF9800")
            except:
                # If termination fails, try to kill
                try:
                    self.aris_process.kill()
                except:
                    pass
    
    def restart_aris(self):
        self.stop_aris()
        # Wait a moment before starting again
        self.root.after(1000, self.start_aris)
    
    def minimize_to_tray(self):
        # This is a placeholder - implementing a system tray icon requires additional libraries
        # For simplicity, we'll just minimize the window
        self.root.iconify()
    
    def add_to_startup(self):
        # Run the add_to_startup.ps1 script with admin privileges
        project_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(project_dir, "add_to_startup.ps1")
        
        if os.path.exists(script_path):
            # Use PowerShell to run the script with admin privileges
            cmd = f'powershell -Command "Start-Process powershell -ArgumentList \"-ExecutionPolicy Bypass -File \\\"{script_path}\\\"\" -Verb RunAs"'
            subprocess.Popen(cmd, shell=True)
    
    def install_as_service(self):
        # Run the install_aris_service.ps1 script with admin privileges
        project_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(project_dir, "install_aris_service.ps1")
        
        if os.path.exists(script_path):
            # Use PowerShell to run the script with admin privileges
            cmd = f'powershell -Command "Start-Process powershell -ArgumentList \"-ExecutionPolicy Bypass -File \\\"{script_path}\\\"\" -Verb RunAs"'
            subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ARISLauncher(root)
    root.mainloop()