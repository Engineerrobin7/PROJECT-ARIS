"""
Text-mode testing interface for ARIS Ultimate
Test all 8 features through text commands
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aris_enhanced import ARISEnhanced

class TextModeARIS:
    """Text-mode interface for testing ARIS"""
    
    def __init__(self):
        print("=" * 70)
        print("🤖 ARIS Ultimate - Text Mode Testing Interface")
        print("=" * 70)
        print("\nInitializing ARIS Enhanced...")
        print("(This may take a moment...)\n")
        
        try:
            self.aris = ARISEnhanced()
            print("✅ ARIS Enhanced initialized successfully!\n")
        except Exception as e:
            print(f"❌ Failed to initialize ARIS: {e}")
            print("\nNote: Some features may not work without proper setup.")
            print("This is normal for testing. Core features will still work.\n")
            self.aris = None
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "=" * 70)
        print("🎯 ARIS ULTIMATE - FEATURE TESTING MENU")
        print("=" * 70)
        print("\n📋 Test Features:")
        print("  1. 🔌 Plugin System")
        print("  2. ⚡ Custom Commands")
        print("  3. ⏰ Advanced Scheduler")
        print("  4. 💬 Conversation Context")
        print("  5. 🏠 Smart Home Integration")
        print("  6. 🌍 Multi-Language Support")
        print("  7. 📁 File Management System")
        print("  8. 🎤 Process Text Command (All Features)")
        print("\n🔧 Other Options:")
        print("  9. 📊 Show Statistics")
        print("  0. 🚪 Exit")
        print("\n" + "=" * 70)
    
    def test_plugins(self):
        """Test plugin system"""
        print("\n" + "=" * 70)
        print("🔌 TESTING PLUGIN SYSTEM")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Get loaded plugins
        plugins = self.aris.plugin_manager.get_all_plugins()
        print(f"\n✅ Loaded Plugins: {len(plugins)}")
        
        for name, info in plugins.items():
            status = "✓ Enabled" if info['enabled'] else "✗ Disabled"
            print(f"  • {name}")
            print(f"    Version: {info['version']}")
            print(f"    Status: {status}")
            print(f"    Description: {info['description']}")
        
        # Test plugin command
        print("\n🧪 Testing plugin command...")
        result = self.aris.plugin_manager.execute_command("plugin test", {})
        if result:
            print(f"✅ Plugin Response: {result}")
        else:
            print("ℹ️  No plugin handled the test command")
    
    def test_custom_commands(self):
        """Test custom commands"""
        print("\n" + "=" * 70)
        print("⚡ TESTING CUSTOM COMMANDS")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Show existing commands
        commands = self.aris.custom_commands.get_all_commands()
        print(f"\n✅ Custom Commands: {len(commands)}")
        
        for trigger, cmd_data in list(commands.items())[:5]:
            print(f"  • '{trigger}' → {cmd_data.get('response', 'N/A')}")
        
        if len(commands) > 5:
            print(f"  ... and {len(commands) - 5} more")
        
        # Test a command
        print("\n🧪 Testing custom command...")
        result = self.aris.custom_commands.execute_command("good morning aris")
        if result:
            print(f"✅ Response: {result}")
        else:
            print("ℹ️  Command not found or not configured")
    
    def test_scheduler(self):
        """Test scheduler"""
        print("\n" + "=" * 70)
        print("⏰ TESTING ADVANCED SCHEDULER")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Add a test task
        print("\n🧪 Adding test task...")
        result = self.aris.scheduler.add_task(
            task_name="Test reminder",
            scheduled_time="in 5 minutes",
            task_type="reminder"
        )
        print(f"✅ {result}")
        
        # Show upcoming tasks
        tasks = self.aris.scheduler.get_upcoming_tasks(hours=24)
        print(f"\n📋 Upcoming Tasks (next 24 hours): {len(tasks)}")
        
        for task in tasks[:5]:
            print(f"  • {task['name']}")
            print(f"    Time: {task['scheduled_time']}")
            print(f"    Type: {task['type']}")
            if task.get('recurrence'):
                print(f"    Recurrence: {task['recurrence']}")
        
        if len(tasks) > 5:
            print(f"  ... and {len(tasks) - 5} more")
    
    def test_conversation(self):
        """Test conversation context"""
        print("\n" + "=" * 70)
        print("💬 TESTING CONVERSATION CONTEXT")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Add test interaction
        print("\n🧪 Adding test interaction...")
        self.aris.context.add_interaction(
            user_input="What is the weather?",
            assistant_response="The weather is sunny and 72°F"
        )
        print("✅ Interaction added")
        
        # Get recent context
        context = self.aris.context.get_context(5)
        print(f"\n📝 Recent Context: {len(context)} interactions")
        
        for interaction in context[-3:]:
            print(f"\n  User: {interaction['user']}")
            print(f"  ARIS: {interaction['assistant']}")
            if interaction.get('topic'):
                print(f"  Topic: {interaction['topic']}")
        
        # Show statistics
        stats = self.aris.context.get_statistics()
        print(f"\n📊 Statistics:")
        print(f"  Total Interactions: {stats.get('total_interactions', 0)}")
        print(f"  Preferences Set: {stats.get('preferences_set', 0)}")
        
        topics = stats.get('topics', {})
        if topics:
            print(f"  Topics: {', '.join(list(topics.keys())[:5])}")
    
    def test_smart_home(self):
        """Test smart home"""
        print("\n" + "=" * 70)
        print("🏠 TESTING SMART HOME INTEGRATION")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Discover devices
        print("\n🔍 Discovering devices...")
        devices = self.aris.smart_home.discover_devices()
        print(f"✅ Found {len(devices)} devices")
        
        for device in devices:
            print(f"\n  • {device['name']}")
            print(f"    Type: {device['type']}")
            print(f"    ID: {device['id']}")
            print(f"    Capabilities: {', '.join(device.get('capabilities', []))}")
        
        # Test device control
        if devices:
            print("\n🧪 Testing device control...")
            device = devices[0]
            result = self.aris.smart_home.control_device(device['name'], "turn_on")
            print(f"✅ {result}")
    
    def test_language(self):
        """Test multi-language"""
        print("\n" + "=" * 70)
        print("🌍 TESTING MULTI-LANGUAGE SUPPORT")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Show available languages
        languages = self.aris.language.get_available_languages()
        print(f"\n✅ Available Languages: {len(languages)}")
        
        for code, name in languages.items():
            current = " (current)" if code == self.aris.language.current_language else ""
            print(f"  • {code}: {name}{current}")
        
        # Test translations
        print("\n🧪 Testing translations...")
        print(f"\nCurrent language: {self.aris.language.current_language}")
        
        keys = ["greeting_morning", "listening", "success", "error"]
        for key in keys:
            text = self.aris.language.get_text(key)
            print(f"  • {key}: {text}")
    
    def test_file_manager(self):
        """Test file management"""
        print("\n" + "=" * 70)
        print("📁 TESTING FILE MANAGEMENT SYSTEM")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # List files
        print("\n📂 Listing current directory...")
        result = self.aris.file_manager.process_command("list files")
        print(f"✅ {result}")
        
        # Show operation history
        history = self.aris.file_manager.file_manager.get_operation_history(5)
        print(f"\n📜 Recent Operations: {len(history)}")
        
        for op in history[-3:]:
            print(f"  • {op['operation']} - {op['path']}")
            print(f"    Status: {op['status']}")
            print(f"    Time: {op['timestamp']}")
        
        # Test voice commands
        print("\n🧪 Testing file commands...")
        commands = [
            "What files are here?",
            "Folder size"
        ]
        
        for cmd in commands:
            result = self.aris.file_manager.process_command(cmd)
            if result:
                print(f"\n  Command: '{cmd}'")
                print(f"  Response: {result[:100]}...")
    
    def test_command(self):
        """Test processing a text command"""
        print("\n" + "=" * 70)
        print("🎤 PROCESS TEXT COMMAND (ALL FEATURES)")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        print("\nEnter a command to test (or 'back' to return):")
        print("\nExamples:")
        print("  • What time is it?")
        print("  • List files")
        print("  • Turn on living room light")
        print("  • Remind me to take a break in 5 minutes")
        print("  • Plugin test")
        print("  • Good morning aris")
        
        command = input("\n> ").strip()
        
        if command.lower() == 'back':
            return
        
        if not command:
            print("❌ No command entered")
            return
        
        print(f"\n🔄 Processing: '{command}'")
        print("-" * 70)
        
        try:
            response = self.aris.process_command(command)
            print(f"\n✅ ARIS Response:")
            print(f"   {response}")
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    def show_statistics(self):
        """Show overall statistics"""
        print("\n" + "=" * 70)
        print("📊 ARIS ULTIMATE - STATISTICS")
        print("=" * 70)
        
        if not self.aris:
            print("❌ ARIS not initialized")
            return
        
        # Plugins
        plugins = self.aris.plugin_manager.get_all_plugins()
        print(f"\n🔌 Plugins: {len(plugins)} loaded")
        
        # Custom Commands
        commands = self.aris.custom_commands.get_all_commands()
        print(f"⚡ Custom Commands: {len(commands)} defined")
        
        # Scheduled Tasks
        tasks = self.aris.scheduler.get_upcoming_tasks(hours=168)
        print(f"⏰ Scheduled Tasks: {len(tasks)} upcoming")
        
        # Conversation
        stats = self.aris.context.get_statistics()
        print(f"💬 Conversations: {stats.get('total_interactions', 0)} interactions")
        
        # Smart Home
        devices = self.aris.smart_home.discover_devices()
        print(f"🏠 Smart Devices: {len(devices)} discovered")
        
        # Languages
        languages = self.aris.language.get_available_languages()
        print(f"🌍 Languages: {len(languages)} available")
        
        # File Operations
        history = self.aris.file_manager.file_manager.get_operation_history(100)
        print(f"📁 File Operations: {len(history)} in history")
        
        print("\n" + "=" * 70)
    
    def run(self):
        """Main loop"""
        while True:
            self.show_menu()
            
            try:
                choice = input("\n👉 Enter your choice (0-9): ").strip()
                
                if choice == '0':
                    print("\n👋 Goodbye! Thanks for testing ARIS Ultimate!")
                    break
                elif choice == '1':
                    self.test_plugins()
                elif choice == '2':
                    self.test_custom_commands()
                elif choice == '3':
                    self.test_scheduler()
                elif choice == '4':
                    self.test_conversation()
                elif choice == '5':
                    self.test_smart_home()
                elif choice == '6':
                    self.test_language()
                elif choice == '7':
                    self.test_file_manager()
                elif choice == '8':
                    self.test_command()
                elif choice == '9':
                    self.show_statistics()
                else:
                    print("\n❌ Invalid choice. Please enter 0-9.")
                
                input("\n⏸️  Press Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\n⏸️  Press Enter to continue...")

def main():
    """Main entry point"""
    try:
        app = TextModeARIS()
        app.run()
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        print("\nPlease ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
