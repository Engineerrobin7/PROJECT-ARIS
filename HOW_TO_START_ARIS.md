# How to Start ARIS Voice Assistant

There are several ways to start ARIS. Choose the method that works best for you:

## Method 1: GUI Launcher (Recommended for Beginners)

1. Double-click the `launch_aris_gui.bat` file in the project folder
2. The ARIS Launcher window will open with buttons to start, stop, and manage ARIS
3. Click "Start ARIS" to launch the assistant
4. Say "wake up aris" to activate the assistant
5. You can also use the launcher to add ARIS to Windows startup or install as a service

## Method 2: Using the Batch File (Simple)

1. Simply double-click the `start_aris.bat` file in the project folder
2. ARIS will start automatically
3. Say "wake up aris" to activate the assistant

## Method 3: Create a Desktop Shortcut

1. Right-click on `create_shortcut.ps1` in the project folder
2. Select "Run with PowerShell"
3. A shortcut named "ARIS Assistant" will be created on your desktop
4. Double-click this shortcut anytime to start ARIS
5. Say "wake up aris" to activate the assistant

## Method 4: Run in Background (No Console Window)

1. Double-click the `start_aris_background.vbs` file in the project folder
2. ARIS will start silently in the background without showing a console window
3. Say "wake up aris" to activate the assistant
4. To stop ARIS, you'll need to use Task Manager to end the Python process

## Method 5: Add to Windows Startup (Automatic Login Startup)

1. Right-click on `add_to_startup.ps1` in the project folder
2. Select "Run as Administrator"
3. ARIS will be added to your Windows startup programs
4. It will now start automatically when you log in to Windows
5. You can say "wake up aris" anytime without manually starting the assistant

## Method 6: Install as Windows Service (System-level Automatic Startup)

1. Right-click on `install_aris_service.ps1` in the project folder
2. Select "Run as Administrator"
3. ARIS will be installed as a Windows service that starts automatically when your computer boots
4. You can now say "wake up aris" anytime without manually starting the assistant
5. To manage the service, open Windows Services (services.msc) and look for "ARIS Voice Assistant"

## Method 7: Using Python Command

1. Open a command prompt or terminal
2. Navigate to the ARIS project folder
3. Run the command: `python main.py`
4. Say "wake up aris" to activate the assistant

## Troubleshooting

If ARIS is not responding to "wake up aris":

1. Make sure your microphone is working properly
2. Check that the wake word is set correctly in `config/config.env`
3. Speak clearly and a bit louder when saying the wake phrase
4. Try adjusting your microphone settings in Windows

Enjoy using ARIS!