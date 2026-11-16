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

def listar_transacoes():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Pega tudo, do mais novo pro mais antigo
    cur.execute("SELECT id, tipo, categoria, valor, descricao FROM transacoes ORDER BY id DESC")
    linhas = cur.fetchall()
    conn.close()
    # Transforma cada linha em dicionário, pra ficar fácil de ler
    resultado = []
    for id, tipo, categoria, valor, descricao in linhas:
        resultado.append({
            "id": id,
            "tipo": tipo,
            "categoria": categoria,
            "valor": valor,
            "descricao": descricao
        })
    return resultado

def calcular_saldo():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    # Soma tudo que é receita
    cur.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = 'receita'")
    total_receitas = cur.fetchone()[0] or 0
    # Soma tudo que é despesa
    cur.execute("SELECT SUM(valor) FROM transacoes WHERE tipo = 'despesa'")
    total_despesas = cur.fetchone()[0] or 0
    conn.close()
    saldo = total_receitas - total_despesas
    return {
        "receitas": total_receitas,
        "despesas": total_despesas,
        "saldo": saldo
    }   