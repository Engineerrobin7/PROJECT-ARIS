# PowerShell script to install ARIS as a Windows service

# Check for administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Warning "You need to run this script as an Administrator!"
    Write-Warning "Please right-click on the script and select 'Run as Administrator'."
    Pause
    Exit
}

# Get the current directory
$ProjectPath = (Get-Location).Path

# Create a Windows service using NSSM (Non-Sucking Service Manager)
Write-Host "Installing ARIS as a Windows service..."
Write-Host "This will allow ARIS to start automatically when you turn on your computer."
Write-Host ""

# Check if NSSM is installed, if not download it
$nssmPath = "$ProjectPath\nssm.exe"
if (-not (Test-Path $nssmPath)) {
    Write-Host "Downloading NSSM (Non-Sucking Service Manager)..."
    $nssmUrl = "https://nssm.cc/release/nssm-2.24.zip"
    $nssmZip = "$ProjectPath\nssm.zip"
    
    # Download NSSM
    Invoke-WebRequest -Uri $nssmUrl -OutFile $nssmZip
    
    # Extract NSSM
    Expand-Archive -Path $nssmZip -DestinationPath "$ProjectPath\nssm-temp" -Force
    Copy-Item "$ProjectPath\nssm-temp\nssm-2.24\win64\nssm.exe" -Destination $nssmPath
    
    # Clean up
    Remove-Item -Path $nssmZip -Force
    Remove-Item -Path "$ProjectPath\nssm-temp" -Recurse -Force
}

# Create the service
& $nssmPath install ARIS "$ProjectPath\start_aris.bat"
& $nssmPath set ARIS DisplayName "ARIS Voice Assistant"
& $nssmPath set ARIS Description "ARIS Voice Assistant that activates with 'wake up aris'"
& $nssmPath set ARIS Start SERVICE_AUTO_START

Write-Host ""
Write-Host "ARIS has been installed as a Windows service!"
Write-Host "It will start automatically when you turn on your computer."
Write-Host "You can also start/stop it manually from the Services app."
Write-Host "Just say 'wake up aris' to activate the assistant anytime."
Write-Host ""

Pause