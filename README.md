# Controle Financeiro

Controle de dinheiro em Python + SQLite + FastAPI.

## O que faz
- Adiciona receita e despesa com categoria
- Lista todas as transações
- Calcula saldo, total de receitas e despesas
- API REST com FastAPI
- Testes com pytest

## Como rodar

    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload

## Endpoints
- GET / - Mensagem inicial
- GET /transacoes - Lista transações
- GET /saldo - Mostra receitas, despesas e saldo
- POST /transacoes - Adiciona transação

## Demo

    python demo.py

## Testes

    pytest -v

## Tecnologias
Python, SQLite, FastAPI, pytest