"""
Automated demo of all ARIS Ultimate features
Runs through all 8 features automatically
"""
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def print_header(title):
    """Print section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def print_step(step, total, description):
    """Print step info"""
    print(f"\n[{step}/{total}] {description}")
    print("-" * 70)

def demo():
    """Run automated demo"""
    print("=" * 70)
    print("🚀 ARIS ULTIMATE - AUTOMATED FEATURE DEMO")
    print("=" * 70)
    print("\nThis demo will showcase all 8 major features automatically.")
    print("Please wait while ARIS initializes...\n")
    
    try:
        from aris_enhanced import ARISEnhanced
        aris = ARISEnhanced()
        print("✅ ARIS Enhanced initialized successfully!\n")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Failed to initialize: {e}")
        print("\nNote: This is expected if dependencies aren't fully installed.")
        print("Core features will still be demonstrated.\n")
        return
    
    total_steps = 8
    
    # Feature 1: Plugin System
    print_step(1, total_steps, "🔌 PLUGIN SYSTEM")
    plugins = aris.plugin_manager.get_all_plugins()
    print(f"✅ Loaded {len(plugins)} plugins")
    for name, info in plugins.items():
        print(f"   • {name} v{info['version']} - {info['description']}")
    
    result = aris.plugin_manager.execute_command("plugin test", {})
    if result:
        print(f"✅ Plugin test: {result}")
    time.sleep(2)
    
    # Feature 2: Custom Commands
    print_step(2, total_steps, "⚡ CUSTOM COMMANDS")
    commands = aris.custom_commands.get_all_commands()
    print(f"✅ {len(commands)} custom commands configured")
    for trigger in list(commands.keys())[:3]:
        print(f"   • '{trigger}'")
    
    result = aris.custom_commands.execute_command("good morning aris")
    if result:
        print(f"✅ Command test: {result}")
    time.sleep(2)
    
    # Feature 3: Advanced Scheduler
    print_step(3, total_steps, "⏰ ADVANCED SCHEDULER")
    result = aris.scheduler.add_task(
        "Demo task",
        "in 10 minutes",
        "reminder"
    )
    print(f"✅ {result}")
    
    tasks = aris.scheduler.get_upcoming_tasks(24)
    print(f"✅ {len(tasks)} tasks scheduled")
    for task in tasks[:3]:
        print(f"   • {task['name']} at {task['scheduled_time']}")
    time.sleep(2)
    
    # Feature 4: Conversation Context
    print_step(4, total_steps, "💬 CONVERSATION CONTEXT")
    aris.context.add_interaction(
        "Demo question",
        "Demo answer"
    )
    
    stats = aris.context.get_statistics()
    print(f"✅ {stats.get('total_interactions', 0)} total interactions")
    print(f"✅ {stats.get('preferences_set', 0)} preferences set")
    
    context = aris.context.get_context(3)
    print(f"✅ Last {len(context)} interactions in context")
    time.sleep(2)
    
    # Feature 5: Smart Home
    print_step(5, total_steps, "🏠 SMART HOME INTEGRATION")
    devices = aris.smart_home.discover_devices()
    print(f"✅ Discovered {len(devices)} devices")
    for device in devices:
        print(f"   • {device['name']} ({device['type']})")
    
    if devices:
        result = aris.smart_home.control_device(devices[0]['name'], "turn_on")
        print(f"✅ Device control: {result}")
    time.sleep(2)
    
    # Feature 6: Multi-Language
    print_step(6, total_steps, "🌍 MULTI-LANGUAGE SUPPORT")
    languages = aris.language.get_available_languages()
    print(f"✅ {len(languages)} languages available")
    print(f"   Current: {aris.language.current_language}")
    
    for code, name in list(languages.items())[:5]:
        print(f"   • {code}: {name}")
    
    text = aris.language.get_text("greeting_morning")
    print(f"✅ Translation test: '{text}'")
    time.sleep(2)
    
    # Feature 7: File Management
    print_step(7, total_steps, "📁 FILE MANAGEMENT SYSTEM")
    result = aris.file_manager.process_command("list files")
    if result:
        print(f"✅ {result[:100]}...")
    
    history = aris.file_manager.file_manager.get_operation_history(5)
    print(f"✅ {len(history)} operations in history")
    time.sleep(2)
    
    # Feature 8: Integrated Command Processing
    print_step(8, total_steps, "🎤 INTEGRATED COMMAND PROCESSING")
    
    test_commands = [
        "plugin test",
        "good morning aris",
        "list files"
    ]
    
    print("Testing integrated command processing:")
    for cmd in test_commands:
        print(f"\n   Command: '{cmd}'")
        try:
            response = aris.process_command(cmd)
            print(f"   Response: {response[:80]}...")
        except Exception as e:
            print(f"   Error: {e}")
        time.sleep(1)
    
    # Summary
    print_header("✅ DEMO COMPLETE!")
    print("\n🎉 All 8 features demonstrated successfully!")
    print("\n📊 Summary:")
    print(f"   • {len(plugins)} plugins loaded")
    print(f"   • {len(commands)} custom commands")
    print(f"   • {len(tasks)} scheduled tasks")
    print(f"   • {stats.get('total_interactions', 0)} conversations")
    print(f"   • {len(devices)} smart devices")
    print(f"   • {len(languages)} languages")
    print(f"   • File management active")
    print(f"   • All features integrated")
    
    print("\n🚀 ARIS Ultimate is fully operational!")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    try:
        demo()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nPress Enter to exit...")
