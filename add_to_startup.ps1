# PowerShell script to add ARIS to Windows startup

# Check for administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Warning "You need to run this script as an Administrator!"
    Write-Warning "Please right-click on the script and select 'Run as Administrator'."
    Pause
    Exit
}

# Get the current directory
$ProjectPath = (Get-Location).Path
$StartupFolder = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
$BackgroundScript = "$ProjectPath\start_aris_background.vbs"
$ShortcutPath = "$StartupFolder\ARIS Assistant.lnk"

# Create the shortcut in the startup folder
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $BackgroundScript
$Shortcut.Description = "ARIS Voice Assistant (Background)"
$Shortcut.WorkingDirectory = $ProjectPath
$Shortcut.IconLocation = "$env:SystemRoot\System32\SHELL32.dll,173"
$Shortcut.Save()

Write-Host "ARIS has been added to Windows startup!"
Write-Host "It will now start automatically when you log in to Windows."
Write-Host "You can say 'wake up aris' anytime without manually starting the assistant."
Write-Host ""
Write-Host "To remove from startup, delete the shortcut from:"
Write-Host "$StartupFolder"
Write-Host ""

Pause