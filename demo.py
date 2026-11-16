# demo.py - mostra o controle financeiro com saida elegante

from app.database import criar_tabela, listar_transacoes, calcular_saldo

criar_tabela()

print("\n=== CONTROLE FINANCEIRO ===\n")

# Lista elegante
for t in listar_transacoes():
    # Escolhe o sinal: + pra receita, - pra despesa
    sinal = "+" if t["tipo"] == "receita" else "-"
    print(f"{sinal} {t['categoria']:10} | R$ {t['valor']:.2f} | {t['descricao']}")

print("\n---------------------------")

# Saldo elegante
resumo = calcular_saldo()
print(f"Receitas: R$ {resumo['receitas']:.2f}")
print(f"Despesas: R$ {resumo['despesas']:.2f}")
print(f"Saldo:    R$ {resumo['saldo']:.2f}")
print("\n")