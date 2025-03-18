# Importando os pacotes que serão utilizados

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# Carregando o arquivo CSV

df_original = pd.read_csv('d:/Program Files (x86)/Projetos VSCode/Portifólio/Price cars/car_price_dataset.csv')

# 1 - Avaliar o conjunto de dados de forma macro para compreender os dados
# Verificando as primeiras linhas do DataFrame
df_original.head()

# Verificando dimensões do arquivo
df_original.shape

# Verificando informações do arquivo
df_original.info()

# 2 - Verificar se existe valores nulos (em branco) nos dados
# Verificando se há valores nulos
df_original.isnull().sum()

# 3 - Verificar os valores únicos em cada Variável
# Total de valores únicos de cada variável
valores_unicos = []
for i in df_original.columns[0:10].tolist():
    print(i, ':', len(df_original[i].astype(str).value_counts()))
    valores_unicos.append(len(df_original[i].astype(str).value_counts()))

# 4 - Verificando duplicatas em todo o DataFrame
duplicadas = df_original.duplicated()
print("Número de linhas duplicadas:", duplicadas.sum())

# Visualizando as linhas duplicadas
linhas_duplicadas = df_original[duplicadas]
print(linhas_duplicadas)

# 5 - Visualizar as medidas estatísticas principais do conjunto de dados
# Visualizando algumas medidas estatísticas(Média, Mediana, Desvio Padrão, Quartis, Valores Mínimos e Máximos)
df_original.describe()

# 6 - Avaliar as variáveis de forma individual através de dados e gráficos para melhor entender os dados
# Quantidade de observações por Marca
df_original.groupby(['Brand']).size()

# Vizualizando através do gráfico
df_original.Brand.value_counts().plot(kind='bar', title='Marca', color = ['#219ebc', '#023047']);
plt.show()

# Quantidade de observações por Modelo
df_original.groupby(['Model']).size()

# Vizualizando através do gráfico
df_original.Model.value_counts().plot(kind='bar', title='Modelo', color = ['#219ebc', '#023047']);
plt.show()

# Quantidade de observações por Ano
df_original.groupby(['Year']).size()

# Vizualizando através do gráfico
df_original.Year.value_counts().plot(kind='bar', title='Ano', color = ['#219ebc', '#023047']);
plt.show()

# Quantidade de observações por Tamanho do Motor
df_original.groupby(['Engine_Size']).size()

# Vizualizando através do Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df_original['Engine_Size'], bins=30)
plt.title('Distribuição do Tamanho do Motor')
plt.xlabel('Tamanho do Motor')
plt.ylabel('Frequência')
plt.show()

# Quantidade de observações por Tamanho do Tipo de Combustível
df_original.groupby(['Fuel_Type']).size()

# Vizualizando através do gráfico
df_original.Fuel_Type.value_counts().plot(kind='bar', title='Tipo de Combustível', color = ['#219ebc', '#023047']);
plt.show()

# Quantidade de observações por Transmissor
df_original.groupby(['Transmission']).size()

# Vizualizando através do gráfico
df_original.Transmission.value_counts().plot(kind='bar', title='Transmissor', color = ['#219ebc', '#023047']);
plt.show()

# Quantidade de observações por Quilometragem
df_original.groupby(['Mileage']).size()

# Vizualizando através do gráfico
sns.histplot(data=df_original, x="Mileage", bins=30)
plt.title("Distribuição da Quilometragem")
plt.xlabel("Quilometragem")
plt.ylabel("Contagem")
plt.show()

# Quantidade de observações por quantidade de portas
df_original.groupby(['Doors']).size()

# Vizualizando através do gráfico
df_original.Doors.value_counts().plot(kind='bar', title='Portas', color = ['#219ebc', '#023047']);
plt.show()

# Quantidade de observações por Proprietários
df_original.groupby(['Owner_Count']).size()

# Vizualizando através do gráfico
df_original.Owner_Count.value_counts().plot(kind='bar', title='Proprietários', color = ['#219ebc', '#023047']);
plt.show()

# 7 - Avaliar o balanceamento da variável ALVO (Target)
plt.figure(figsize=(10, 6))
sns.histplot(df_original['Price'], bins=30)
plt.title('Distribuição dos Preços')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

# 8 - Analisar a relação de cada Variável x Variável Alvo
# Formatando o tamanho do plot
plt.rcParams["figure.figsize"] = [8.00, 4.00]
plt.rcParams["figure.autolayout"] = True

# Visualizando a Variável Marca x Preço
sns.boxplot(x='Brand', y='Price', data=df_original)
plt.title('Comparação de Preços por Marca')
plt.xlabel('Marca')
plt.ylabel('Preço')
plt.xticks(rotation=45)
plt.show()

# Visualizando a Variável Modelo x Preço
sns.scatterplot(data=df_original, x='Model', y='Price')
plt.title('Relação entre Preço e Modelo')
plt.xlabel('Modelo')
plt.ylabel('Preço')
plt.show()

# Visualizando a Variável Ano x Preço
sns.scatterplot(data=df_original, x='Year', y='Price')
plt.title('Relação entre Preço e Ano')
plt.xlabel('Ano')
plt.ylabel('Preço')
plt.show()

# Visualizando a Variável Motor x Preço
sns.scatterplot(data=df_original, x='Engine_Size', y='Price')
plt.title('Relação entre Preço e Tamanho do Motor')
plt.xlabel('Tamanho do Motor')
plt.ylabel('Preço')
plt.show()

# Visualizando a Variável Combustível x Preço
sns.boxplot(x='Fuel_Type', y='Price', data=df_original)
plt.title('Comparação de Preços por Combustível')
plt.xlabel('Combustível')
plt.ylabel('Preço')
plt.xticks(rotation=45)
plt.show()

# Visualizando a Variável Transmissor x Preço
sns.boxplot(x='Transmission', y='Price', data=df_original)
plt.title('Comparação de Preços por Transmissor')
plt.xlabel('Transmissor')
plt.ylabel('Preço')
plt.xticks(rotation=45)
plt.show()

# Visualizando a Variável Quilometragem x Preço
sns.scatterplot(data=df_original, x='Mileage', y='Price')
plt.title('Relação entre Preço e Quilometragem')
plt.xlabel('Quilometragem')
plt.ylabel('Preço')
plt.show()

# Visualizando a Variável Portas x Preço
sns.scatterplot(data=df_original, x='Doors', y='Price')
plt.title('Relação entre Preço e Portas')
plt.xlabel('Portas')
plt.ylabel('Preço')
plt.show()

# Visualizando a Variável Proprietário único x Preço
sns.scatterplot(data=df_original, x='Owner_Count', y='Price')
plt.title('Relação entre Preço e Proprietários')
plt.xlabel('Proprietários')
plt.ylabel('Preço')
plt.show()

# 9 - Analisar possíveis outliers
# Carregar variáveis para plot
variaveis_numericas = []
for i in df_original.columns[0:9].tolist():
    if df_original.dtypes[i] == 'int64' or df_original.dtypes[i] == 'float64':
        variaveis_numericas.append(i)

print(variaveis_numericas)
len(variaveis_numericas)

#Podemos observar nos boxplot abaixo que as variáveis numéricas apresentam uma grande quantidade de "possíveis" outliers
#Precisamos avaliar cada uma dessas variáveis dentro do contexto dos dados para saber se realmente iremos tratalos como outlier
plt.rcParams["figure.figsize"] = [14.00, 20.00]
plt.rcParams["figure.autolayout"] = True
f, axes = plt.subplots(3, 2) # 3 linhas e 2 colunas

linha = 0
coluna = 0
for i in variaveis_numericas:
    sns.boxplot(data = df_original, y = i, ax = axes[linha][coluna])
    coluna += 1
    if coluna == 2:
        linha += 1
        coluna = 0
plt.show()

#Podemos observar nos boxplot abaixo que as variáveis numéricas apresentam uma grande quantidade de "possíveis" outliers
#Precisamos avaliar cada uma dessas variáveis dentro do contexto dos dados para saber se realmente iremos tratalos como outlier
plt.rcParams["figure.figsize"] = [14.00, 20.00]
plt.rcParams["figure.autolayout"] = True
f, axes = plt.subplots(3, 2) # 3 linhas e 2 colunas

linha = 0
coluna = 0
for i in variaveis_numericas:
    sns.histplot(data = df_original, x = i, ax = axes[linha][coluna])
    coluna += 1
    if coluna == 2:
        linha += 1
        coluna = 0
plt.show()

# Selecionar apenas colunas numéricas
numeric_columns = df_original.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df_original[numeric_columns].corr()

# Calcular a matriz de correlação somente para colunas numéricas
corr_matrix = df_original.corr(numeric_only=True) 
sns.heatmap(corr_matrix, annot=True)
plt.show()
