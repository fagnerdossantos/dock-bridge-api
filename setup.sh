#!/bin/bash

# Definir nome do ambiente virtual
VENV_DIR="dock_bridge_api_venv"

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python não encontrado. Por favor, instale o Python antes de continuar."
    exit 1
fi

# Verificar se o pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "Pip não encontrado. Por favor, instale o pip antes de continuar."
    exit 1
fi

# Verificar se o ambiente virtual já existe
if [ -d "$VENV_DIR" ]; then
    echo "O ambiente virtual já existe. Ativando..."
else
    echo "Criando o ambiente virtual..."
    python3 -m venv $VENV_DIR
fi

# Ativar o ambiente virtual
echo "Ativando o ambiente virtual..."
# Verificando se o sistema é Windows ou Unix
if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    source $VENV_DIR/bin/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    source $VENV_DIR/Scripts/activate
else
    echo "Sistema operacional não suportado para ativação automática."
    exit 1
fi

# Instalar as dependências do projeto
echo "Instalando as dependências do projeto..."
pip install -r requirements.txt

# Limpa o terminal
clear

# Rodar o script Python automaticamente
echo "Rodando o script Python..."
python src/main.py

echo "Ambiente virtual configurado e script Python rodando!"

