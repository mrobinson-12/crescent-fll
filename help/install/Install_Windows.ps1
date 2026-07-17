$ErrorActionPreference = "Stop"

function Write-Success($Message) {
    Write-Host $Message -ForegroundColor Green
}

function Write-Step($Message) {
    Write-Host "`n$Message" -ForegroundColor Cyan
}

function Check-Command($Command) {
    if (!(Get-Command $Command -ErrorAction SilentlyContinue)) {
        throw "$Command was not found. Please restart PowerShell and try again."
    }
}

# Create working directory
Write-Step "Creating FLL workspace..."

$FLLFolder = "$HOME\fll"

New-Item -ItemType Directory -Path $FLLFolder -Force | Out-Null

# Install required software
Write-Step "Checking Git and Python..."

if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Git..."
    winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements
}

if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Installing Python..."
    winget install --id Python.Python3 -e --accept-source-agreements --accept-package-agreements
}

Write-Success "Git and Python are installed."

# Navigate to workspace
Set-Location $FLLFolder

# Clone repository
Write-Step "Cloning FLL repository..."

$RepoURL = "https://github.com/mrobinson-12/fll-2026-missions.git"

if (Test-Path "$FLLFolder\fll-2026-missions") {
    Write-Host "Repository already exists. Pulling latest changes..."
    Set-Location "$FLLFolder\fll-2026-missions"
    git pull
}
else {
    git clone $RepoURL

    if ($LASTEXITCODE -ne 0) {
        throw "Failed to clone repository."
    }

    Set-Location "$FLLFolder\fll-2026-missions"
}

Write-Success "Repository ready."

# Setup Python environment
Write-Step "Setting up Python environment..."

if (!(Test-Path ".venv")) {
    python -m venv .venv
}

# Allow activation scripts
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install pybricks pybricksdev

Write-Success "Python environment configured."

# Configure Git
Write-Step "Configuring Git..."

$GitUsername = Read-Host "Enter your GitHub username"
$GitEmail = Read-Host "Enter your GitHub email"

git config --global user.name $GitUsername
git config --global user.email $GitEmail

Write-Success "Git configured."

# Hackatime
Write-Step "Hackatime setup"

$InstallHackatime = Read-Host "Would you like to install Hackatime? (y/n)"

if ($InstallHackatime -eq "y") {

    $HackatimeKey = Read-Host "Enter your Hackatime API key"

    Invoke-RestMethod `
        https://raw.githubusercontent.com/hackclub/hackatime-setup/main/install.ps1 `
        | Invoke-Expression

    hackatime-setup --yes -- $HackatimeKey

    Write-Success "Hackatime installed."
}

# Finished
Write-Host ""
Write-Success "Installation complete!"

Write-Host @"

Next steps:
1. Open VS Code
2. Open this folder:

$FLLFolder\fll-2026-missions

3. Activate your environment if needed:

.\.venv\Scripts\Activate.ps1

Happy coding! 🤖

"@
