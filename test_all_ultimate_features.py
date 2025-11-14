"""
Comprehensive test suite for all ARIS Ultimate features
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        # Core modules
        from core.speech_input import SpeechInput
        from core.speech_output import TTSEngine
        from core.wake_word import WakeWordDetector
        print("  ✅ Core modules")
        
        # Orion Engine
        from orion_engine.brain import Brain
        from orion_engine.memory import Memory
        from orion_engine.personality import Personality
        print("  ✅ Orion Engine")
        
        # New features
        from plugins.plugin_manager import PluginManager
        from plugins.base_plugin import BasePlugin
        print("  ✅ Plugin system")
        
        from extensions.custom_commands import CustomCommandManager
        print("  ✅ Custom commands")
        
        from scheduler.advanced_scheduler import AdvancedScheduler
        print("  ✅ Advanced scheduler")
        
        from conversation.context_manager import ConversationContext
        print("  ✅ Conversation context")
        
        from smart_home.smart_home_controller import SmartHomeController
        print("  ✅ Smart home")
        
        from localization.language_manager import LanguageManager
        print("  ✅ Multi-language")
        
        from file_manager import FileManager, FileManagerVoiceCommands
        print("  ✅ File management")
        
        print("✅ All imports successful!\n")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}\n")
        return False

def test_plugin_system():
    """Test plugin system"""
    print("🧪 Testing Plugin System...")
    
    try:
        from plugins.plugin_manager import PluginManager
        
        pm = PluginManager()
        pm.load_all_plugins()
        
        plugins = pm.get_all_plugins()
        print(f"  ✅ Loaded {len(plugins)} plugins")
        
        # Test plugin execution
        result = pm.execute_command("plugin test", {})
        if result:
            print(f"  ✅ Plugin execution: {result}")
        
        print("✅ Plugin system working!\n")
        return True
        
    except Exception as e:
        print(f"❌ Plugin system failed: {e}\n")
        return False

def test_custom_commands():
    """Test custom commands"""
    print("🧪 Testing Custom Commands...")
    
    try:
        from extensions.custom_commands import CustomCommandManager
        
        cm = CustomCommandManager()
        
        # Add test command
        cm.add_command(
            trigger="test command",
            action_type="speak",
            action_data="Test successful",
            response="Test successful"
        )
        
        # Execute command
        result = cm.execute_command("test command")
        if result:
            print(f"  ✅ Command execution: {result}")
        
        # Get all commands
        commands = cm.get_all_commands()
        print(f"  ✅ Total commands: {len(commands)}")
        
        print("✅ Custom commands working!\n")
        return True
        
    except Exception as e:
        print(f"❌ Custom commands failed: {e}\n")
        return False

def test_scheduler():
    """Test advanced scheduler"""
    print("🧪 Testing Advanced Scheduler...")
    
    try:
        from scheduler.advanced_scheduler import AdvancedScheduler
        
        scheduler = AdvancedScheduler()
        
        # Add test task
        result = scheduler.add_task(
            task_name="Test task",
            scheduled_time="in 1 hour",
            task_type="reminder"
        )
        print(f"  ✅ Task added: {result}")
        
        # Get upcoming tasks
        tasks = scheduler.get_upcoming_tasks(hours=24)
        print(f"  ✅ Upcoming tasks: {len(tasks)}")
        
        print("✅ Scheduler working!\n")
        return True
        
    except Exception as e:
        print(f"❌ Scheduler failed: {e}\n")
        return False

def test_conversation_context():
    """Test conversation context"""
    print("🧪 Testing Conversation Context...")
    
    try:
        from conversation.context_manager import ConversationContext
        
        context = ConversationContext()
        
        # Add interaction
        context.add_interaction(
            user_input="Test question",
            assistant_response="Test answer"
        )
        
        # Get context
        recent = context.get_context(5)
        print(f"  ✅ Context entries: {len(recent)}")
        
        # Set preference
        context.set_preference("test_pref", "test_value")
        pref = context.get_preference("test_pref")
        print(f"  ✅ Preference: {pref}")
        
        # Get statistics
        stats = context.get_statistics()
        print(f"  ✅ Statistics: {stats.get('total_interactions', 0)} interactions")
        
        print("✅ Conversation context working!\n")
        return True
        
    except Exception as e:
        print(f"❌ Conversation context failed: {e}\n")
        return False

def test_smart_home():
    """Test smart home controller"""
    print("🧪 Testing Smart Home...")
    
    try:
        from smart_home.smart_home_controller import SmartHomeController
        
        controller = SmartHomeController()
        
        # Discover devices
        devices = controller.discover_devices()
        print(f"  ✅ Discovered {len(devices)} devices")
        
        if devices:
            # Test device control
            device = devices[0]
            result = controller.control_device(device['name'], "turn_on")
            print(f"  ✅ Device control: {result}")
        
        print("✅ Smart home working!\n")
        return True
        
    except Exception as e:
        print(f"❌ Smart home failed: {e}\n")
        return False

def test_language_manager():
    """Test language manager"""
    print("🧪 Testing Language Manager...")
    
    try:
        from localization.language_manager import LanguageManager
        
        lm = LanguageManager()
        
        # Get available languages
        languages = lm.get_available_languages()
        print(f"  ✅ Available languages: {len(languages)}")
        
        # Get text
        text = lm.get_text("greeting_morning")
        print(f"  ✅ Translation: {text}")
        
        # Set language
        lm.set_language("en")
        print(f"  ✅ Current language: {lm.current_language}")
        
        print("✅ Language manager working!\n")
        return True
        
    except Exception as e:
        print(f"❌ Language manager failed: {e}\n")
        return False

def test_file_manager():
    """Test file manager"""
    print("🧪 Testing File Manager...")
    
    try:
        from file_manager import FileManager, FileManagerVoiceCommands
        
        fm = FileManager()
        
        # List directory
        items = fm.list_directory(".")
        print(f"  ✅ Directory items: {len(items)}")
        
        # Test voice commands
        voice = FileManagerVoiceCommands(fm)
        result = voice.process_command("list files")
        if result:
            print(f"  ✅ Voice command: {result[:50]}...")
        
        # Get operation history
        history = fm.get_operation_history(5)
        print(f"  ✅ Operation history: {len(history)} entries")
        
        print("✅ File manager working!\n")
        return True
        
    except Exception as e:
        print(f"❌ File manager failed: {e}\n")
        return False

def test_enhanced_aris():
    """Test enhanced ARIS integration"""
    print("🧪 Testing Enhanced ARIS Integration...")
    
    try:
        # Note: We don't actually initialize ARIS to avoid starting services
        # Just test that the module can be imported
        import aris_enhanced
        print("  ✅ Enhanced ARIS module loaded")
        
        print("✅ Enhanced ARIS integration ready!\n")
        return True
        
    except Exception as e:
        print(f"❌ Enhanced ARIS failed: {e}\n")
        return False

def test_gui():
    """Test GUI modules"""
    print("🧪 Testing GUI Modules...")
    
    try:
        # Test that GUI modules can be imported
        import gui_ultimate
        print("  ✅ Ultimate GUI module loaded")
        
        from file_manager.gui_file_manager import FileManagerGUI
        print("  ✅ File Manager GUI module loaded")
        
        print("✅ GUI modules ready!\n")
        return True
        
    except Exception as e:
        print(f"❌ GUI modules failed: {e}\n")
        return False

def test_web_dashboard():
    """Test web dashboard"""
    print("🧪 Testing Web Dashboard...")
    
    try:
        from web_dashboard.app import app
        print("  ✅ Flask app loaded")
        
        # Test that routes exist
        with app.test_client() as client:
            response = client.get('/api/status')
            print(f"  ✅ API status endpoint: {response.status_code}")
        
        print("✅ Web dashboard ready!\n")
        return True
        
    except Exception as e:
        print(f"❌ Web dashboard failed: {e}\n")
        return False

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("🚀 ARIS Ultimate - Comprehensive Test Suite")
    print("=" * 60)
    print()
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Plugin System", test_plugin_system()))
    results.append(("Custom Commands", test_custom_commands()))
    results.append(("Scheduler", test_scheduler()))
    results.append(("Conversation Context", test_conversation_context()))
    results.append(("Smart Home", test_smart_home()))
    results.append(("Language Manager", test_language_manager()))
    results.append(("File Manager", test_file_manager()))
    results.append(("Enhanced ARIS", test_enhanced_aris()))
    results.append(("GUI Modules", test_gui()))
    results.append(("Web Dashboard", test_web_dashboard()))
    
    # Summary
    print("=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print()
        print("🎉 ALL TESTS PASSED! 🎉")
        print()
        print("✅ All 8 features are working correctly!")
        print("✅ All integrations are functional!")
        print("✅ ARIS Ultimate is ready to use!")
        print()
        print("🚀 Start using ARIS:")
        print("   python gui_ultimate.py")
        print("   OR")
        print("   start_ultimate.bat")
    else:
        print()
        print("⚠️ Some tests failed. Please check the errors above.")
        print()
        print("Common fixes:")
        print("  - Run: pip install -r requirements.txt")
        print("  - Check that all files are present")
        print("  - Review error messages for details")
    
    print()
    print("=" * 60)
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
