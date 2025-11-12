# commands/automation_commands.py
"""
Handles automation and scheduling commands.
"""
import os
import json
from datetime import datetime, timedelta

class AutomationCommands:
    def __init__(self):
        self.tasks_file = "data/automation_tasks.json"
        self._ensure_tasks_file()
    
    def _ensure_tasks_file(self):
        """Ensure tasks file exists."""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'w') as f:
                json.dump({"tasks": []}, f)
    
    def handle_command(self, command):
        """Handle automation-related commands."""
        if "schedule" in command or "remind me" in command:
            return self.schedule_task(command)
        elif "list tasks" in command or "show tasks" in command:
            return self.list_tasks()
        elif "cancel task" in command or "delete task" in command:
            return self.cancel_task(command)
        else:
            return "I can help you schedule tasks, set reminders, or list your tasks."
    
    def schedule_task(self, command):
        """Schedule a new task or reminder."""
        try:
            with open(self.tasks_file, 'r') as f:
                data = json.load(f)
            
            task = {
                "id": len(data["tasks"]) + 1,
                "command": command,
                "created": datetime.now().isoformat(),
                "status": "pending"
            }
            
            data["tasks"].append(task)
            
            with open(self.tasks_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return f"Task scheduled: {command}"
        except Exception as e:
            return f"Error scheduling task: {str(e)}"
    
    def list_tasks(self):
        """List all pending tasks."""
        try:
            with open(self.tasks_file, 'r') as f:
                data = json.load(f)
            
            pending = [t for t in data["tasks"] if t["status"] == "pending"]
            
            if not pending:
                return "No pending tasks."
            
            task_list = [f"{t['id']}. {t['command']}" for t in pending]
            return "Your tasks: " + ". ".join(task_list)
        except Exception as e:
            return f"Error listing tasks: {str(e)}"
    
    def cancel_task(self, command):
        """Cancel a task by ID."""
        try:
            # Extract task ID from command
            words = command.split()
            task_id = None
            for word in words:
                if word.isdigit():
                    task_id = int(word)
                    break
            
            if not task_id:
                return "Please specify a task ID to cancel."
            
            with open(self.tasks_file, 'r') as f:
                data = json.load(f)
            
            for task in data["tasks"]:
                if task["id"] == task_id:
                    task["status"] = "cancelled"
            
            with open(self.tasks_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return f"Task {task_id} cancelled."
        except Exception as e:
            return f"Error cancelling task: {str(e)}"

def handle_command(command):
    """Entry point for automation commands."""
    automation = AutomationCommands()
    return automation.handle_command(command)
