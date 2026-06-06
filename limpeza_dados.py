# ============================================================
# limpeza_dados.py
# Projeto de Extensão | Vila do Açaí - Vila Velha/ES
# CNPJ: 12.066.473/0001-70
# Autor: Geovana Teixeira | Março/2026
# ============================================================

import pandas as pd

print("=" * 50)
print("LIMPEZA DE DADOS - VILA DO AÇAÍ")
print("=" * 50)

df = pd.read_csv("vendas_vila_do_acai.csv")
print(f"\nRegistros carregados: {len(df)}")

# Verificar nulos
nulos = df.isnull().sum().sum()
print(f"Valores nulos: {nulos}")
if nulos > 0:
    df = df.dropna()

# Converter tipos
df["data"] = pd.to_datetime(df["data"])
df["valor_unitario"] = df["valor_unitario"].astype(float)
df["quantidade"] = df["quantidade"].astype(int)

# Padronizar textos
df["produto"] = df["produto"].str.strip().str.title()
df["canal"] = df["canal"].str.strip().str.lower()

# Colunas calculadas
df["faturamento"] = df["quantidade"] * df["valor_unitario"]
df["dia_semana"] = df["data"].dt.day_name()
df["mes_ano"] = df["data"].dt.to_period("M").astype(str)
df["hora"] = pd.to_datetime(df["horario"], format="%H:%M").dt.hour

# Remover duplicatas
df = df.drop_duplicates()

# Salvar
df.to_csv("vendas_limpo.csv", index=False)

# Resumo
print(f"\nPeríodo: {df['data'].min():%d/%m/%Y} a {df['data'].max():%d/%m/%Y}")
print(f"Registros finais: {len(df)}")
print(f"Produtos: {df['produto'].nunique()}")
print(f"Total vendido: {df['quantidade'].sum()} unidades")
print(f"Faturamento: R$ {df['faturamento'].sum():,.2f}")
print("\nSalvo em 'vendas_limpo.csv'")
