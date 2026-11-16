# app/database.py - banco SQLite do controle financeiro

import sqlite3

# Nome do arquivo do banco
DB = "financeiro.db"

def criar_tabela():
    # Conecta no banco, se não existir, ele cria o arquivo
    conn = sqlite3.connect(DB)
    # Cursor é quem executa os comandos SQL
    cur = conn.cursor()
    # Cria a tabela só se ainda não existir
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            valor REAL NOT NULL,
            descricao TEXT
        )
    """)
    # Salva e fecha
    conn.commit()
    conn.close()

def adicionar_transacao(tipo: str, categoria: str, valor: float, descricao: str = ""):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transacoes (tipo, categoria, valor, descricao) VALUES (?, ?, ?, ?)",
        (tipo, categoria, valor, descricao)
    )
    conn.commit()
    conn.close()
    return {"sucesso": f"{tipo} de R$ {valor:.2f} adicionado"}