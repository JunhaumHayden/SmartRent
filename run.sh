#!/bin/bash
# Instala as dependências (comentar após a primeira vez)
pip install -r requirements.txt

# Inicia o servidor Uvicorn:
# O app principal é `main`, e o objeto FastAPI é chamado de `app`.
echo "Iniciando FastAPI..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000