import streamlit as st
import pandas as pd
# Função para renderizar a página de Análise de Dados

st.header(":orange[Análise Exploratória de Dados]", divider="blue")
#st.write("Bem-vindo à página de Análise de Dados!")
df = pd.read_csv('ipea_df.csv')
# Título da página
st.markdown('# Base de Dados Analisada')
st.write('A base de dados analisada, extraída do site do Ipea considera o preço por barril do petróleo bruto tipo Brent. Produzido no Mar do Norte (Europa), Brent é uma classe de petróleo bruto que serve como benchmark para o preço internacional de diferentes tipos de petróleo. Neste caso, é valorado no chamado preço FOB (free on board), que não inclui despesa de frete e seguro no preço.')
# Mostrar os dados
st.dataframe(df)

st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

st.markdown('# Série Histórica')
st.image('preco_petroleo.png', caption='Gráfico criado no PowerBI', use_column_width=True)
st.write('Podemos ver a variação diária do preço do petróleo ao longo do tempo, que será explicada mais detalhadamente na aba "Eventos Históricos". Observa-se uma tendência geral de aumento, especialmente nos últimos meses. Há picos significativos e quedas ocasionais, sugerindo volatilidade no mercado de petróleo!')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('# Preço Médio Anual')
st.image('preco_medio_petroleo.png', caption='Gráfico criado no PowerBI', use_column_width=True)
st.write("O gráfico acima representa a média anual do preço do petróleo. Nota-se uma tendência de alta nos preços médios anuais, com os valores mais recentes sendo consistentemente superiores aos anos anteriores. Isso pode indicar um aumento na demanda ou diminuição na oferta de petróleo.")
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('# Boxplot')
st.image('boxplot.png', caption='Gráfico criado no PowerBI', use_column_width=True)
st.write("O boxplot ilustra a distribuição dos preços do petróleo ao longo de todo o período analisado. A mediana está relativamente alta, sugerindo que metade dos valores estão acima de um preço significativo. A presença de outliers indica que houve períodos de preços excepcionalmente altos ou baixos.")

nulos = df.isnull().sum()
nulos_df = pd.DataFrame(nulos, columns=['Qtd dados nulos'])
nulos_df.index.name = 'Coluna'

# Calcular a quantidade de dados duplicados
duplicados = df.duplicated().sum()
duplicados_df = pd.DataFrame([duplicados], columns=['Qtd dados duplicados'])
duplicados_df.index = ['Total']

# Exibir os dados nulos e duplicados no Streamlit
st.markdown('### Dados Nulos')
st.write(nulos_df)
st.markdown('')
st.markdown('')

st.markdown('### Dados Duplicados')
st.write(duplicados_df)

st.markdown('')
st.markdown('')

df = df.rename(columns={'Preco_petroleo': 'y'})
df = df.rename(columns={'Data': 'ds'})
df['ds'] = pd.to_datetime(df['ds'], format='%d/%m/%Y', errors='coerce')
df['y'] = df['y'].astype(int)
df['y'] = df['y'].apply(lambda x: float(f"{x // 100}.{x % 100:02}"))

df1 = df
df1.rename(columns={'ds': 'Data', 'y': 'Preço do Petróleo (em Dólar)'}, inplace=True)

# Formatar a data para dd/mm/aaaa
df1['Data'] = pd.to_datetime(df1['Data']).dt.strftime('%d/%m/%Y')

# Calcular a variação percentual nos preços
df1['Variação Percentual'] = df1['Preço do Petróleo (em Dólar)'].pct_change() * 100
df1['Variação Percentual'] = df1['Variação Percentual'].round(2)  # Arredondar para duas casas decimais

# Adicionar o símbolo '$' na frente do número na coluna 'preço do petróleo (em dólar)'
df1['Preço do Petróleo (Em Dólar)'] = df1['Preço do Petróleo (em Dólar)'].apply(lambda x: f'${x:.2f}')

# Encontrar os 10 maiores aumentos e 10 maiores quedas
maiores_aumentos = df1.nlargest(10, 'Variação Percentual')
maiores_quedas = df1.nsmallest(10, 'Variação Percentual')

# Exibir os resultados sem índice
st.markdown("### 10 Maiores Aumentos nos Preços do Petróleo Brent")
st.write(maiores_aumentos[['Data', 'Preço do Petróleo (em Dólar)', 'Variação Percentual']].reset_index(drop=True))

st.markdown("### 10 Maiores Quedas nos Preços do Petróleo Brent")
st.write(maiores_quedas[['Data', 'Preço do Petróleo (em Dólar)', 'Variação Percentual']].reset_index(drop=True))


st.markdown('')
st.markdown('')

st.markdown('### Resumo Estatístico')
st.write(df.describe().round(2))