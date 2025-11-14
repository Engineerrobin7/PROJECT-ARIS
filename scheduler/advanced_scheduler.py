"""
Advanced scheduling system with recurring tasks and reminders
"""
import json
import os
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any
import threading
import time

class AdvancedScheduler:
    """Advanced task scheduling and reminder system"""
    
    def __init__(self, data_file: str = "data/scheduled_tasks.json"):
        self.data_file = data_file
        self.tasks: List[Dict[str, Any]] = []
        self.logger = logging.getLogger('Scheduler')
        self.running = False
        self.scheduler_thread = None
        self.callback = None
        self.load_tasks()
    
    def load_tasks(self):
        """Load scheduled tasks from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
                self.logger.info(f"Loaded {len(self.tasks)} scheduled tasks")
            except Exception as e:
                self.logger.error(f"Failed to load tasks: {e}")
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        """Save scheduled tasks to file"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            self.logger.error(f"Failed to save tasks: {e}")
    
    def add_task(self, task_name: str, scheduled_time: str, task_type: str = "reminder", 
                 recurrence: str = None, action: str = None) -> str:
        """
        Add a new scheduled task
        
        Args:
            task_name: Name/description of the task
            scheduled_time: When to execute (ISO format or relative like "in 5 minutes")
            task_type: Type of task (reminder, execute, speak)
            recurrence: Recurrence pattern (daily, weekly, monthly, or None)
            action: Action to perform
        """
        try:
            # Parse scheduled time
            exec_time = self._parse_time(scheduled_time)
            
            task = {
                "id": len(self.tasks) + 1,
                "name": task_name,
                "scheduled_time": exec_time.isoformat(),
                "type": task_type,
                "recurrence": recurrence,
                "action": action or task_name,
                "completed": False,
                "created_at": datetime.now().isoformat()
            }
            
            self.tasks.append(task)
            self.save_tasks()
            
            time_str = exec_time.strftime("%I:%M %p on %B %d")
            return f"Task '{task_name}' scheduled for {time_str}"
            
        except Exception as e:
            self.logger.error(f"Failed to add task: {e}")
            return f"Failed to schedule task: {str(e)}"
    
    def remove_task(self, task_id: int) -> bool:
        """Remove a task by ID"""
        self.tasks = [t for t in self.tasks if t.get("id") != task_id]
        self.save_tasks()
        return True
    
    def get_upcoming_tasks(self, hours: int = 24) -> List[Dict[str, Any]]:
        """Get tasks scheduled within the next X hours"""
        now = datetime.now()
        cutoff = now + timedelta(hours=hours)
        
        upcoming = []
        for task in self.tasks:
            if task.get("completed"):
                continue
            
            task_time = datetime.fromisoformat(task["scheduled_time"])
            if now <= task_time <= cutoff:
                upcoming.append(task)
        
        return sorted(upcoming, key=lambda x: x["scheduled_time"])
    
    def start_scheduler(self, callback=None):
        """Start the scheduler background thread"""
        if self.running:
            return
        
        self.callback = callback
        self.running = True
        self.scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self.scheduler_thread.start()
        self.logger.info("Scheduler started")
    
    def stop_scheduler(self):
        """Stop the scheduler"""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=2)
        self.logger.info("Scheduler stopped")
    
    def _scheduler_loop(self):
        """Main scheduler loop"""
        while self.running:
            try:
                self._check_tasks()
                time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                self.logger.error(f"Scheduler error: {e}")
    
    def _check_tasks(self):
        """Check for tasks that need to be executed"""
        now = datetime.now()
        
        for task in self.tasks:
            if task.get("completed"):
                continue
            
            task_time = datetime.fromisoformat(task["scheduled_time"])
            
            # Check if task should be executed (within 1 minute window)
            if abs((task_time - now).total_seconds()) < 60:
                self._execute_task(task)
                
                # Handle recurrence
                if task.get("recurrence"):
                    self._reschedule_task(task)
                else:
                    task["completed"] = True
                
                self.save_tasks()
    
    def _execute_task(self, task: Dict[str, Any]):
        """Execute a scheduled task"""
        self.logger.info(f"Executing task: {task['name']}")
        
        if self.callback:
            self.callback(task)
    
    def _reschedule_task(self, task: Dict[str, Any]):
        """Reschedule a recurring task"""
        current_time = datetime.fromisoformat(task["scheduled_time"])
        recurrence = task.get("recurrence")
        
        if recurrence == "daily":
            new_time = current_time + timedelta(days=1)
        elif recurrence == "weekly":
            new_time = current_time + timedelta(weeks=1)
        elif recurrence == "monthly":
            new_time = current_time + timedelta(days=30)
        else:
            return
        
        task["scheduled_time"] = new_time.isoformat()
        self.logger.info(f"Rescheduled task '{task['name']}' to {new_time}")
    
    def _parse_time(self, time_str: str) -> datetime:
        """Parse time string into datetime object"""
        time_str = time_str.lower().strip()
        now = datetime.now()
        
        # Relative time parsing
        if "in" in time_str:
            if "minute" in time_str:
                minutes = int(''.join(filter(str.isdigit, time_str)))
                return now + timedelta(minutes=minutes)
            elif "hour" in time_str:
                hours = int(''.join(filter(str.isdigit, time_str)))
                return now + timedelta(hours=hours)
            elif "day" in time_str:
                days = int(''.join(filter(str.isdigit, time_str)))
                return now + timedelta(days=days)
        
        # Specific time today
        elif "at" in time_str:
            time_part = time_str.split("at")[-1].strip()
            try:
                parsed_time = datetime.strptime(time_part, "%I:%M %p")
                scheduled = now.replace(hour=parsed_time.hour, minute=parsed_time.minute, second=0)
                if scheduled < now:
                    scheduled += timedelta(days=1)
                return scheduled
            except:
                pass
        
        # Tomorrow
        if "tomorrow" in time_str:
            return now + timedelta(days=1)
        
        # Try ISO format
        try:
            return datetime.fromisoformat(time_str)
        except:
            pass
        
        # Default to 1 hour from now
        return now + timedelta(hours=1)
