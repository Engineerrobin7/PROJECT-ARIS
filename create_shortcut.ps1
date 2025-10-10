# PowerShell script to create a desktop shortcut for ARIS

$WshShell = New-Object -ComObject WScript.Shell
$ProjectPath = (Get-Location).Path
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$ShortcutPath = Join-Path -Path $DesktopPath -ChildPath "ARIS Assistant.lnk"

$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = Join-Path -Path $ProjectPath -ChildPath "start_aris.bat"
$Shortcut.Description = "ARIS Voice Assistant"
$Shortcut.WorkingDirectory = $ProjectPath
$Shortcut.IconLocation = "$env:SystemRoot\System32\SHELL32.dll,173"
$Shortcut.Save()

Write-Host "Desktop shortcut created successfully at: $ShortcutPath"
Write-Host "You can now start ARIS by double-clicking the shortcut on your desktop."
Write-Host "Say 'wake up aris' to activate the assistant."

Pause