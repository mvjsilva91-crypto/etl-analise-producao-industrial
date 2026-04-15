# 🚀 etl-analise-producao-industrial

Projeto de ETL (Extract, Transform, Load) desenvolvido com foco em análise de dados industriais, utilizando **Python** e **SQL** para processamento, tratamento e armazenamento de dados.

---

## 📊 Objetivo

Simular um cenário real de indústria, onde dados de produção são coletados via Excel, tratados e armazenados em banco de dados para análise e geração de insights.

---

## 🧩 Tecnologias utilizadas

* 🐍 Python
* 🗄️ SQL (SQLite)
* 📊 Pandas
* 🔗 SQLAlchemy
* 📈 Matplotlib
* 📁 Excel (entrada e saída de dados)

---

## ⚙️ Funcionalidades

✔️ Leitura de dados a partir de arquivo Excel
✔️ Tratamento de dados inconsistentes (nulos, formatos incorretos, valores inválidos)
✔️ Padronização de informações (ex: nomes de máquinas)
✔️ Criação de métricas (eficiência de produção)
✔️ Análise de dados (agrupamentos e estatísticas)
✔️ Geração de gráficos para visualização de dados
✔️ Exportação de dados tratados para novo arquivo Excel
✔️ Armazenamento em banco de dados SQLite
✔️ Consultas SQL para geração de insights

---

## 🔄 Pipeline ETL

1. **Extract (Extração)**

   * Leitura de dados do Excel

2. **Transform (Transformação)**

   * Limpeza de dados
   * Tratamento de valores nulos
   * Conversão de datas
   * Remoção de dados inválidos
   * Criação de métricas

3. **Load (Carga)**

   * Inserção dos dados no banco SQLite
   * Geração de relatórios e consultas SQL

---

## 📁 Estrutura do projeto

```
📦 etl-analise-producao-industrial
 ┣ 📂 dados
 ┃ ┗ producao_dados.xlsx
 ┣ 📂 output
 ┃ ┣ eficiencia_media_maquina.png
   ┣ producao.db
 ┃ ┣ producao_limpa.xlsx
 ┃ ┣ producao_total_maquinas.png
 ┃ ┗ producao_turno.png
 ┣ 📂 script
 ┃ ┗ limpeza.py
 ┗ README.md
```

---

## 📈 Visualização de Dados

O projeto gera gráficos para análise dos dados:

* 📊 Produção total por máquina
* 📊 Produção por turno
* 📊 Eficiência média por máquina

---

## 📊 Exemplos de visualização

### Produção por Máquina

![Produção por Máquina](output/grafico_producao_maquina.png)

### Eficiência Média por Máquina

![Eficiência Média](output/grafico_eficiencia.png)

---

## 🗄️ Banco de Dados

O projeto utiliza um banco de dados SQLite para armazenar os dados tratados.

O banco é criado automaticamente ao executar o script Python, não sendo necessária nenhuma configuração manual.

📂 Arquivo gerado:

* `producao.db`

📍 Local:

* O arquivo será salvo na mesma pasta onde o script for executado ou conforme o caminho definido no código.

---

## 🔍 Como visualizar o banco

Para visualizar os dados, recomenda-se o uso do software:

**DB Browser for SQLite**

Passos:

1. Abrir o programa
2. Clicar em “Open Database”
3. Selecionar o arquivo `producao.db`
4. Acessar a aba “Browse Data”

---

## 💻 Consulta SQL (exemplo)

```sql
SELECT maquina, SUM(producao) as total
FROM producao
GROUP BY maquina;
```

---

## 🧠 Aprendizados

Este projeto permitiu aprofundar conhecimentos em:

* Manipulação de dados com Python
* Processos de ETL
* Integração com banco de dados
* Escrita e execução de consultas SQL
* Visualização de dados com gráficos
* Organização de projetos de dados

---

## 🚀 Como executar

1. Instale as dependências:

```
pip install pandas openpyxl sqlalchemy matplotlib
```

2. Execute o script:

```
python limpeza.py
```

3. Resultados:

* Arquivo Excel tratado será gerado
* Banco de dados SQLite será criado automaticamente
* Gráficos serão exibidos na tela

---

## 💡 Próximos passos

* Criação de dashboard interativo
* Integração com API backend
* Automação do pipeline

---

## 👨‍💻 Autor

Desenvolvido por Marcos Vinícius
