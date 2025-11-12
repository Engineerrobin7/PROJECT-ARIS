# api/calendar_api.py
"""
Calendar integration for managing events and reminders.
"""
import json
import os
from datetime import datetime, timedelta

class CalendarAPI:
    def __init__(self):
        self.calendar_file = "data/calendar.json"
        self._ensure_calendar_file()
    
    def _ensure_calendar_file(self):
        """Ensure calendar file exists."""
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.calendar_file):
            with open(self.calendar_file, 'w') as f:
                json.dump({"events": []}, f)
    
    def add_event(self, title, date_str, time_str=None):
        """
        Add an event to the calendar.
        
        Args:
            title (str): Event title
            date_str (str): Date in format YYYY-MM-DD
            time_str (str): Optional time in format HH:MM
        """
        try:
            with open(self.calendar_file, 'r') as f:
                data = json.load(f)
            
            event = {
                "id": len(data["events"]) + 1,
                "title": title,
                "date": date_str,
                "time": time_str,
                "created": datetime.now().isoformat()
            }
            
            data["events"].append(event)
            
            with open(self.calendar_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            time_info = f" at {time_str}" if time_str else ""
            return f"Event '{title}' added for {date_str}{time_info}."
        except Exception as e:
            return f"Error adding event: {str(e)}"
    
    def get_events(self, days_ahead=7):
        """Get upcoming events."""
        try:
            with open(self.calendar_file, 'r') as f:
                data = json.load(f)
            
            today = datetime.now().date()
            end_date = today + timedelta(days=days_ahead)
            
            upcoming = []
            for event in data["events"]:
                event_date = datetime.fromisoformat(event["date"]).date()
                if today <= event_date <= end_date:
                    time_info = f" at {event['time']}" if event.get('time') else ""
                    upcoming.append(f"{event['title']} on {event['date']}{time_info}")
            
            if not upcoming:
                return f"No events in the next {days_ahead} days."
            
            return "Upcoming events: " + ". ".join(upcoming)
        except Exception as e:
            return f"Error fetching events: {str(e)}"
    
    def delete_event(self, event_id):
        """Delete an event by ID."""
        try:
            with open(self.calendar_file, 'r') as f:
                data = json.load(f)
            
            data["events"] = [e for e in data["events"] if e["id"] != event_id]
            
            with open(self.calendar_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            return f"Event {event_id} deleted."
        except Exception as e:
            return f"Error deleting event: {str(e)}"
