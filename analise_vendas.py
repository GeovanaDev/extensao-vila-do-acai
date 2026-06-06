# ============================================================
# analise_vendas.py
# Projeto de Extensão | Vila do Açaí - Vila Velha/ES
# CNPJ: 12.066.473/0001-70
# Autor: Geovana Teixeira | Abril/2026
# ============================================================

import pandas as pd

df = pd.read_csv("vendas_limpo.csv")
df["data"] = pd.to_datetime(df["data"])

DIAS_PT = {
    "Monday": "Segunda", "Tuesday": "Terça", "Wednesday": "Quarta",
    "Thursday": "Quinta", "Friday": "Sexta", "Saturday": "Sábado",
    "Sunday": "Domingo"
}

print("=" * 55)
print("ANÁLISE DE VENDAS - VILA DO AÇAÍ")
print("=" * 55)

# 1. Faturamento por produto
print("\n--- FATURAMENTO POR PRODUTO ---")
fat = df.groupby("produto")["faturamento"].sum().sort_values(ascending=False)
total = fat.sum()
for i, (prod, val) in enumerate(fat.items(), 1):
    print(f"  {i}. {prod}: R$ {val:,.2f} ({val/total*100:.1f}%)")

# 2. Canal de venda
print("\n--- BALCÃO vs DELIVERY ---")
canal = df.groupby("canal")["faturamento"].sum()
for c, v in canal.items():
    print(f"  {c.upper()}: R$ {v:,.2f} ({v/total*100:.1f}%)")

# 3. Dia da semana
print("\n--- VENDAS POR DIA DA SEMANA ---")
dia = df.groupby("dia_semana")["faturamento"].sum()
for d in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]:
    if d in dia.index:
        barra = "█" * int(dia[d] / 100)
        print(f"  {DIAS_PT[d]:10s} R$ {dia[d]:>8,.2f}  {barra}")

# 4. Evolução mensal
print("\n--- EVOLUÇÃO MENSAL ---")
mensal = df.groupby("mes_ano")["faturamento"].sum().sort_index()
for mes, val in mensal.items():
    print(f"  {mes}: R$ {val:,.2f}")

# 5. Horário de pico
print("\n--- VENDAS POR HORÁRIO ---")
hora = df.groupby("hora")["faturamento"].sum().sort_index()
for h, val in hora.items():
    barra = "█" * int(val / 150)
    print(f"  {int(h):02d}:00  R$ {val:>8,.2f}  {barra}")

# Insights
print("\n" + "=" * 55)
print("INSIGHTS")
print("=" * 55)
print(f"  Produto top: {fat.index[0]} (R$ {fat.iloc[0]:,.2f})")
print(f"  Melhor dia: {DIAS_PT[dia.idxmax()]}")
print(f"  Canal principal: {canal.idxmax().upper()}")
print(f"  Horário pico: {int(hora.idxmax()):02d}:00")
print(f"  Melhor mês: {mensal.idxmax()}")
