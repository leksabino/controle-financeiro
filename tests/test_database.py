# tests/test_database.py - testes do controle financeiro

from app.database import criar_tabela, adicionar_transacao, listar_transacoes, calcular_saldo
import os

def setup_function():
    # Apaga o banco de teste antes de cada teste, pra começar limpo
    if os.path.exists("financeiro.db"):
        os.remove("financeiro.db")
    criar_tabela()

def test_adicionar_receita():
    resultado = adicionar_transacao("receita", "salario", 1000, "Teste")
    assert "sucesso" in resultado
    assert "R$ 1000.00" in resultado["sucesso"]

def test_calcular_saldo():
    adicionar_transacao("receita", "salario", 1000, "")
    adicionar_transacao("despesa", "mercado", 200, "")
    resumo = calcular_saldo()
    assert resumo["receitas"] == 1000
    assert resumo["despesas"] == 200
    assert resumo["saldo"] == 800

def test_listar_transacoes():
    adicionar_transacao("receita", "salario", 1000, "")
    lista = listar_transacoes()
    assert len(lista) == 1
    assert lista[0]["categoria"] == "salario"