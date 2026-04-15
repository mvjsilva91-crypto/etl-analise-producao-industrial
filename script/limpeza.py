import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


# 1. LER EXCEL

df = pd.read_excel(r"producao_dados.xlsx")


print(" Dados iniciais:")
print(df.head())

print("\n Informações:")
print(df.info())

print("\n Valores nulos:")
print(df.isnull().sum())


# 2. LIMPEZA DE DADOS


# Padronizar máquinas
df["maquina"] = df["maquina"].str.upper()
df["maquina"] = df["maquina"].replace("MAQUINA3", "M3")
df["maquina"] = df["maquina"].str.upper().str.strip()
print(df["maquina"].unique())

# Corrigir datas
df["data"] = pd.to_datetime(df["data"], errors="coerce")

# Tratar valores nulos
df = df.fillna({
    "producao": 0,
    "tempo_parado": 0,
    "defeitos": 0
})

# Remover produção inválida
df = df[df["producao"] >= 0]


# 3. CRIAR MÉTRICA

df["eficiencia"] = df["producao"] / (df["tempo_parado"] + 1)


# 4. ANÁLISE


print("\n Produção por máquina:")
print(df.groupby("maquina")["producao"].sum())

print("\n Média tempo parado:")
print(df["tempo_parado"].mean())

print("\n Produção por turno:")
print(df.groupby("turno")["producao"].sum())


# 5. SALVAR EXCEL LIMPO

df.to_excel(r"producao_limpa.xlsx", index=False)



# 6. BANCO DE DADOS (SQLite)

engine = create_engine("sqlite:///producao.db")

df.to_sql("producao", engine, if_exists="replace", index=False)


# 7. CONSULTA SQL

query = """
SELECT maquina, SUM(producao) as total
FROM producao
GROUP BY maquina
"""

resultado = pd.read_sql(query, engine)

print("\n Consulta SQL:")
print(resultado)

print("\n Banco criado com sucesso!")



# 7. GRÀFICOS


# Gráfico de produção por máquina


# Agrupar dados
producao_maquina = df.groupby("maquina")["producao"].sum()

# Criar gráfico
plt.figure()
producao_maquina.plot(kind="bar")

# Títulos
plt.title("Produção Total por Máquina")
plt.xlabel("Máquina")
plt.ylabel("Produção")

# Mostrar gráfico
plt.show()


# Gráfico de produção por turno

producao_turno = df.groupby("turno")["producao"].sum()

plt.figure()
producao_turno.plot(kind="bar")

plt.title("Produção por Turno")
plt.xlabel("Turno")
plt.ylabel("Produção")

plt.show()



# Gráfico de eficiência 

eficiencia_media = df.groupby("maquina")["eficiencia"].mean()

plt.figure()
eficiencia_media.plot(kind="bar")

plt.title("Eficiência Média por Máquina")
plt.xlabel("Máquina")
plt.ylabel("Eficiência")

plt.show()



# SALVAR O GRÀFICO 

plt.savefig("grafico_producao.png")
