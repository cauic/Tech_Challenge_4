import pandas as pd
import plotly.express as px
import streamlit as st
import locale

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

# Função para renderizar a subaba Tech Challenger 4
def render_tech_challenger_4():
    st.header(":orange[Tech Challenge 4]", divider="blue")
    st.markdown("## Análise e Previsão do Preço do Petróleo Brent")
    st.write("")
    st.markdown('### Objetivo') 
    st.markdown('Esse é um projeto da pós-graduação em Data Analytics pela FIAP.')
    st.markdown('Nele, simulamos que fomos contratados por uma consultoria para analisar os dados de preço do petróleo Brent, disponíveis no site do IPEA.')
    st.markdown('O desafio envolve desenvolver um dashboard interativo que gere insights relevantes para a tomada de decisão e um modelo de Machine Learning para fazer o forecasting dos preços do petróleo. Além disso, criar um plano para fazer o deploy do modelo e fazer o MVP utilizando o streamlit.')
    st.markdown('### Autores')
    st.markdown('Laio Soares')
    st.markdown('Emerson Cauic')

# Função para renderizar a subaba Introdução
def render_introducao():
    st.header(":orange[Introdução]", divider="blue")
    st.markdown(' O objetivo deste projeto de consultoria é analisar os dados de preço do petróleo Brent, disponíveis no site do IPEA, e desenvolver um dashboard para embasar decisões estratégicas no mercado de petróleo. A base de dados utilizada contém duas colunas: data e preço em dólares.')
    st.markdown('Inicialmente, realizamos uma análise exploratória dos dados, identificando os períodos com os maiores aumentos e quedas abruptas dos preços. Esses períodos foram analisados e correlacionados com eventos significativos que possam ter influenciado tais variações. Para prever os preços futuros, utilizamos dois modelos, Prophet e ARIMA, selecionando o modelo com o menor MAPE (Mean Absolute Percentage Error) para o forecast.')
    st.markdown('Os dados foram armazenados no Google Cloud Platform, a análise foi conduzida utilizando Power BI e Python, e o resultado final foi disponibilizado através de um deploy no Streamlit.')

tab1, tab2 = st.tabs(["Tech Challenger 4", "Introdução"])
with tab1:
    render_tech_challenger_4()
with tab2:
    render_introducao()
