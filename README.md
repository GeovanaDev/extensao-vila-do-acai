# 🍇 Extensão Universitária — Análise de Dados | Vila do Açaí

Projeto de extensão desenvolvido para a disciplina de **Análise de Dados** do curso de Análise e Desenvolvimento de Sistemas — Estácio de Sá.

## 📋 Sobre o projeto

Parceria com a **Vila do Açaí Ltda** (CNPJ 12.066.473/0001-70), localizada em Vila Velha/ES, com o objetivo de transformar registros de vendas em informações visuais e acionáveis para apoiar a gestão do negócio.

## 🗂️ Estrutura

```
📁 extensao-vila-do-acai/
├── vendas_vila_do_acai.csv   # Dados de vendas (Out/2025 – Mar/2026)
├── limpeza_dados.py           # Limpeza e padronização dos dados
├── analise_vendas.py          # Análise exploratória e insights
├── gerar_graficos.py          # Geração dos gráficos (PNG)
├── dashboard.html             # Dashboard interativo no navegador
└── README.md
```

## ▶️ Como executar

**1. Instale as dependências:**
```bash
pip install pandas matplotlib seaborn
```

**2. Execute na ordem:**
```bash
python limpeza_dados.py    # Gera vendas_limpo.csv
python analise_vendas.py   # Exibe análise no terminal
python gerar_graficos.py   # Gera pasta graficos/ com os PNGs
```

**3. Abra o dashboard:**

Abra o arquivo `dashboard.html` diretamente no navegador.

## 📊 Gráficos gerados

| Arquivo | Descrição |
|---|---|
| `01_faturamento_produto.png` | Faturamento por produto |
| `02_evolucao_mensal.png` | Evolução mensal do faturamento |
| `03_dia_semana.png` | Vendas por dia da semana |
| `04_canal_venda.png` | Balcão vs Delivery |
| `05_heatmap.png` | Faturamento por dia e horário |

## 🛠️ Tecnologias

- Python 3 — `pandas`, `matplotlib`, `seaborn`
- HTML / CSS / JavaScript — `Chart.js`

## 👩‍💻 Autora

**Geovana Teixeira** — Análise e Desenvolvimento de Sistemas | Estácio de Sá  
Projeto de Extensão — 2026
