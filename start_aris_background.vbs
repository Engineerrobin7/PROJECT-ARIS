' VBScript to start ARIS in the background without showing a console window

Option Explicit

Dim WshShell, ProjectPath, StartBatPath

' Get the project path (same directory as this script)
ProjectPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Path to the start_aris.bat file
StartBatPath = ProjectPath & "\start_aris.bat"

' Create shell object
Set WshShell = CreateObject("WScript.Shell")

' Run the batch file with window hidden (0)
WshShell.Run """" & StartBatPath & """", 0, False

' Clean up
Set WshShell = Nothing