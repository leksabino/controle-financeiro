# app/main.py - API do controle financeiro

from fastapi import FastAPI
from app.database import criar_tabela, adicionar_transacao, listar_transacoes, calcular_saldo

# Cria a API
app = FastAPI(title="Controle Financeiro")

# Cria a tabela quando a API sobe
criar_tabela()

@app.get("/")
def home():
    return {"mensagem": "Controle Financeiro API - use /transacoes e /saldo"}

@app.get("/transacoes")
def get_transacoes():
    return listar_transacoes()

@app.get("/saldo")
def get_saldo():
    return calcular_saldo()

@app.post("/transacoes")
def post_transacao(tipo: str, categoria: str, valor: float, descricao: str = ""):
    return adicionar_transacao(tipo, categoria, valor, descricao)