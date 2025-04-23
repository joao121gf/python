Perfeito! Como hoje é terça-feira e estamos na **Fase 1: Fundamentos**, o foco é:

- **Manhã:** Python (manipulação de dados)
- **Tarde:** Fundamentos de ETL (conceitos e pipelines simples)

### 🚀 Desafio do Dia — Terça-feira (Fase 1)

#### 🎯 Objetivo:

Criar um mini pipeline de ETL em Python para transformar dados brutos em dados limpos e prontos para análise.

---

### 📁 Descrição do Desafio

Você recebeu um arquivo CSV com dados de vendas, mas ele está desorganizado. Seu trabalho será:

1. **Extrair** os dados do CSV.
2. **Transformar** os dados (limpeza + enriquecimento).
3. **Carregar** os dados em um novo arquivo CSV ou banco de dados (DuckDB ou SQLite).

---

### 📦 Dataset (simulado)

Baixe ou crie um CSV com o seguinte conteúdo:

```csv
id,cliente,valor,produto,data_venda
1,Lucas,100,Notebook,2024/01/10
2,,250,Mouse,2024/01/12
3,Carla,abc,Fone,2024/01/13
4,João,300,,2024/01/15
5,Ana,150,Teclado,2024/01/18
```

---

### ✅ Tarefas

1. **Extração**

   - Leia o arquivo CSV com pandas.

2. **Transformação**

   - Remova linhas com valores nulos em campos essenciais (`cliente`, `produto`, `valor`).
   - Converta a coluna `valor` para numérico, tratando erros.
   - Adicione uma nova coluna `valor_com_imposto` com 12% de imposto aplicado.

3. **Carga**
   - Salve o resultado em um novo arquivo `vendas_processadas.csv` **ou** carregue os dados em um banco SQLite.

---

### ✨ Extra (opcional)

- Gera um pequeno gráfico com matplotlib ou seaborn mostrando a soma das vendas por produto.
- Versione o código no GitHub com um README explicando o pipeline.

Se quiser, posso te fornecer o código-base ou revisar o que você fizer. Bora praticar?
