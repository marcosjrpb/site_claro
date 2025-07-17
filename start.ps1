# start-dev.ps1

<#
.SYNOPSIS
    Inicia o ambiente de desenvolvimento para um projeto Python/Wagtail.

.DESCRIPTION
    Este script automatiza as seguintes etapas:
    1. Define o diretório do projeto com base na localização do script.
    2. Verifica a existência dos arquivos e pastas necessários (venv, requirements.txt, manage.py).
    3. Ativa o ambiente virtual Python.
    4. Instala ou atualiza as dependências do projeto via pip.
    5. Inicia o servidor de desenvolvimento do Django/Wagtail.
    O script para imediatamente se qualquer comando falhar.

.PARAMETER VenvName
    O nome da pasta do ambiente virtual. O padrão é "venv".

.EXAMPLE
    .\start-dev.ps1
    Inicia o ambiente usando a pasta "venv".

.EXAMPLE
    .\start-dev.ps1 -VenvName ".venv"
    Inicia o ambiente usando a pasta ".venv".
#>

param(
    [string]$VenvName = "venv"
)

# --- Configuração e Verificações Iniciais ---

# Garante que o script pare se um comando falhar
$ErrorActionPreference = 'Stop'

# Define o diretório raiz do projeto como a pasta onde o script está localizado
$ProjectRoot = $PSScriptRoot

# Define os caminhos completos que serão usados
$VenvPath = Join-Path $ProjectRoot $VenvName
$RequirementsFile = Join-Path $ProjectRoot "requirements.txt"
$ManagePyFile = Join-Path $ProjectRoot "manage.py"
$VenvActivateScript = Join-Path $VenvPath "Scripts\Activate.ps1"

# Função para exibir mensagens de status
function Write-Log {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] $Message" -ForegroundColor $Color
}

# Verifica se a pasta do ambiente virtual existe
if (-not (Test-Path -Path $VenvPath -PathType Container)) {
    Write-Log "Erro: O ambiente virtual '$VenvName' não foi encontrado em '$ProjectRoot'." -Color Red
    Write-Log "Execute 'python -m venv $VenvName' para criá-lo." -Color Yellow
    exit 1
}

# Verifica se o requirements.txt existe
if (-not (Test-Path -Path $RequirementsFile -PathType Leaf)) {
    Write-Log "Erro: Arquivo 'requirements.txt' não encontrado em '$ProjectRoot'." -Color Red
    exit 1
}

# Verifica se o manage.py existe
if (-not (Test-Path -Path $ManagePyFile -PathType Leaf)) {
    Write-Log "Erro: Arquivo 'manage.py' não encontrado. Este script deve ser executado na raiz de um projeto Django/Wagtail." -Color Red
    exit 1
}


# --- Execução ---

Write-Log "Ativando o ambiente virtual ($VenvName)..." -Color Green
. $VenvActivateScript

Write-Log "Instalando/verificando dependências (requirements.txt)..." -Color Green
pip install -r $RequirementsFile

Write-Log "Iniciando o servidor de desenvolvimento do Wagtail..." -Color Cyan
Write-Host "Acesse http://127.0.0.1:8000/ no seu navegador."
Write-Host "Pressione Ctrl+C para desligar o servidor." -ForegroundColor Yellow

# Muda para o diretório do projeto antes de executar, garantindo que o manage.py funcione corretamente
Set-Location $ProjectRoot
python manage.py runserver