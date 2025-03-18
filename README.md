# Análise e Visualização de Dados de Preços de Carros

Este repositório contém um projeto de **Análise Exploratória de Dados (EDA)** sobre um conjunto de dados de preços de carros. O código realiza uma análise detalhada do dataset, incluindo inspeção de dados, visualização de distribuições, identificação de possíveis outliers e análise das relações entre as variáveis e o preço dos carros.

---

## 📂 Estrutura do Projeto

- **`car_price_dataset.csv`**: Conjunto de dados com informações sobre preços e características dos carros.
- **`car_price_analysis.py`**: Script principal que carrega, processa e executa a análise exploratória de dados.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada.
- **Pandas**: Para manipulação de dados e operações no DataFrame.
- **Matplotlib** e **Seaborn**: Para visualização de dados e geração de gráficos.
- **Numpy**: Para manipulação de arrays e operações numéricas.

---

## 📊 Análise do Conjunto de Dados

### 1. **Carregamento dos Dados**

O conjunto de dados é carregado a partir do arquivo `car_price_dataset.csv`, que contém informações sobre os preços e características dos carros. O processo inicial envolve a leitura do arquivo e a configuração para manipulação dos dados.

---

### 2. **Análise Inicial**

- **Visão Geral**: Exibe as primeiras linhas do dataset, as dimensões e informações gerais sobre o conjunto de dados.
- **Valores Nulos e Duplicados**: O script verifica se existem valores ausentes ou linhas duplicadas no dataset.
- **Valores Únicos**: Conta o número de valores únicos para as primeiras variáveis, permitindo uma visão sobre a diversidade de dados presentes.

---

### 3. **Exploração das Variáveis**

A análise de distribuição das variáveis permite entender melhor a estrutura dos dados:

- **Variáveis Categóricas**: O script gera gráficos de barras para visualizar a distribuição de variáveis categóricas, como:
  - **Marca**
  - **Modelo**
  - **Ano**
  - **Tipo de Combustível**
  - **Transmissão**, entre outras.
  
- **Variáveis Numéricas**: Histograma para variáveis como:
  - **Tamanho do Motor**
  - **Quilometragem**
  - **Preço**

---

### 4. **Análise das Relações Entre Variáveis e o Preço**

O código explora as relações entre as variáveis independentes e a variável alvo **Preço**:

- **Preço vs Marca**
- **Preço vs Modelo**
- **Preço vs Ano**
- **Preço vs Tamanho do Motor**
- **Preço vs Quilometragem**
- **Preço vs Tipo de Combustível**

Essas visualizações ajudam a identificar padrões e entender como diferentes características dos carros influenciam o preço.

---

### 5. **Identificação de Outliers**

O script identifica possíveis outliers nas variáveis numéricas utilizando **Boxplots** e **Histogramas**. Isso ajuda a detectar valores extremos que podem afetar a análise e os resultados dos modelos.

---

### 6. **Análise de Correlação**

O script calcula a **matriz de correlação** entre as variáveis numéricas e gera um **mapa de calor (heatmap)**. Esse gráfico ajuda a visualizar as relações entre as variáveis e identificar correlações fortes ou fracas.

---

## 📌 Resultados Esperados

Após a execução do script, você obterá:

- **Relatórios no Terminal**: Informações sobre valores nulos, duplicados e a contagem de valores únicos.
- **Gráficos de Distribuição**: Visualizações das distribuições das variáveis categóricas e numéricas.
- **Análises de Correlação**: Um mapa de calor mostrando a correlação entre as variáveis numéricas.
- **Identificação de Outliers**: Boxplots e histogramas para identificar possíveis outliers nas variáveis numéricas.
