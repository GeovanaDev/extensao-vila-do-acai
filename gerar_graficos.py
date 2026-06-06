# ============================================================
# gerar_graficos.py
# Projeto de Extensão | Vila do Açaí - Vila Velha/ES
# CNPJ: 12.066.473/0001-70
# Autor: Geovana Teixeira | Abril/2026
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
os.makedirs("graficos", exist_ok=True)

df = pd.read_csv("vendas_limpo.csv")
df["data"] = pd.to_datetime(df["data"])

DIAS_PT = {"Monday":"Seg","Tuesday":"Ter","Wednesday":"Qua",
           "Thursday":"Qui","Friday":"Sex","Saturday":"Sáb","Sunday":"Dom"}
fmt_brl = lambda x, _: f"R$ {x:,.0f}"

# 1. Faturamento por produto
print("1/5 - Faturamento por produto...")
fig, ax = plt.subplots(figsize=(10, 6))
fat = df.groupby("produto")["faturamento"].sum().sort_values()
fat.plot(kind="barh", ax=ax, color=sns.color_palette("viridis", len(fat)))
ax.set_title("Faturamento por Produto — Vila do Açaí", fontsize=15, fontweight="bold")
ax.set_xlabel("Faturamento (R$)"); ax.set_ylabel("")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(fmt_brl))
for i, v in enumerate(fat.values):
    ax.text(v + 20, i, f"R$ {v:,.0f}", va="center", fontsize=10)
plt.tight_layout(); plt.savefig("graficos/01_faturamento_produto.png", dpi=150); plt.close()

# 2. Evolução mensal
print("2/5 - Evolução mensal...")
fig, ax = plt.subplots(figsize=(10, 6))
mensal = df.groupby("mes_ano")["faturamento"].sum().sort_index()
ax.plot(mensal.index, mensal.values, marker="o", lw=2.5, color="#6C3483", ms=8)
ax.fill_between(mensal.index, mensal.values, alpha=0.15, color="#6C3483")
ax.set_title("Evolução Mensal — Vila do Açaí", fontsize=15, fontweight="bold")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_brl))
plt.xticks(rotation=45)
for x, y in zip(mensal.index, mensal.values):
    ax.annotate(f"R$ {y:,.0f}", (x, y), textcoords="offset points", xytext=(0, 12), ha="center", fontsize=9)
plt.tight_layout(); plt.savefig("graficos/02_evolucao_mensal.png", dpi=150); plt.close()

# 3. Dia da semana
print("3/5 - Vendas por dia...")
fig, ax = plt.subplots(figsize=(10, 6))
dia = df.groupby("dia_semana")["faturamento"].sum()
ordem = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
dia = dia.reindex(ordem).fillna(0)
dia.index = [DIAS_PT[d] for d in dia.index]
cores = sns.color_palette("YlOrRd", len(dia))
idx_ord = dia.values.argsort()
cores_map = [None]*len(dia)
for rank, idx in enumerate(idx_ord): cores_map[idx] = cores[rank]
ax.bar(dia.index, dia.values, color=cores_map, edgecolor="white", lw=1.5)
ax.set_title("Faturamento por Dia da Semana — Vila do Açaí", fontsize=15, fontweight="bold")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_brl))
for i, v in enumerate(dia.values):
    ax.text(i, v + 30, f"R$ {v:,.0f}", ha="center", fontsize=10, fontweight="bold")
plt.tight_layout(); plt.savefig("graficos/03_dia_semana.png", dpi=150); plt.close()

# 4. Balcão vs Delivery
print("4/5 - Canais de venda...")
fig, ax = plt.subplots(figsize=(8, 8))
canal = df.groupby("canal")["faturamento"].sum()
ax.pie(canal.values, labels=[c.upper() for c in canal.index], autopct="%1.1f%%",
       colors=["#2ECC71","#E74C3C"], explode=(0.05,0.05), startangle=90,
       textprops={"fontsize":14, "fontweight":"bold"})
ax.set_title("Balcão vs Delivery — Vila do Açaí", fontsize=15, fontweight="bold")
plt.tight_layout(); plt.savefig("graficos/04_canal_venda.png", dpi=150); plt.close()

# 5. Heatmap
print("5/5 - Heatmap horário...")
fig, ax = plt.subplots(figsize=(12, 6))
df["dia_pt"] = df["dia_semana"].map(DIAS_PT)
hm = df.pivot_table(values="faturamento", index="dia_pt", columns="hora", aggfunc="sum", fill_value=0)
hm = hm.reindex([d for d in ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"] if d in hm.index])
sns.heatmap(hm, annot=True, fmt=".0f", cmap="YlOrRd", lw=0.5, ax=ax,
            cbar_kws={"label":"Faturamento (R$)"})
ax.set_title("Faturamento por Dia e Horário — Vila do Açaí", fontsize=15, fontweight="bold")
ax.set_xlabel("Hora"); ax.set_ylabel("")
plt.tight_layout(); plt.savefig("graficos/05_heatmap.png", dpi=150); plt.close()

print("\nGráficos salvos em graficos/")
