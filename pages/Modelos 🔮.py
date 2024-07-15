import streamlit as st
import pandas as pd
import io
import plotly.express as px
from workalendar.america import Brazil
from prophet import Prophet
import plotly.graph_objects as go
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller as adf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf

# Função para renderizar a subaba ARIMA
def render_arima():
    st.header(":orange[Modelo ARIMA 🤖]", divider="blue")
    st.write("Modelo ARIMA é utilizado para modelar e prever séries temporais com base em suas dependências auto-regressivas e de médias móveis.")

    st.subheader('Seleção de Datas para o Modelo ARIMA')

    default_start_date = datetime.strptime('2010-06-01', '%Y-%m-%d')
    default_end_date = datetime.strptime('2024-06-01', '%Y-%m-%d')

    start_date = st.date_input('Selecione a data de início para ARIMA', value=default_start_date, format="DD/MM/YYYY")
    end_date = st.date_input('Selecione a data de término para ARIMA', value=default_end_date, format="DD/MM/YYYY")

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    st.write(f'Data de início selecionada: {start_date.strftime("%d/%m/%Y")}')
    st.write(f'Data de término selecionada: {end_date.strftime("%d/%m/%Y")}')

    df = pd.read_csv('ipea_df.csv')
    df = df.rename(columns={'Preco_petroleo': 'y'})
    df = df.rename(columns={'Data': 'ds'})
    df['ds'] = pd.to_datetime(df['ds'], format='%d/%m/%Y', errors='coerce')
    df['y'] = df['y'].astype(int)
    df['y'] = df['y'].apply(lambda x: float(f"{x // 100}.{x % 100:02}"))

    # Filtrar o DataFrame usando as datas selecionadas
    df_filtered = df.loc[(df['ds'] >= start_date) & (df['ds'] <= end_date)]
    df_filtered.set_index('ds', inplace=True)
    df_resample = df_filtered.resample('M').mean()
    st.markdown("")
    st.markdown('## Série Temporal')
    st.write('Séries temporais são sequências de dados coletados ou registrados em intervalos de tempo regulares. Elas capturam a evolução de um fenômeno ao longo do tempo, permitindo a análise de tendências, sazonalidades e outras características temporais. Exemplos incluem preços de ações, dados climáticos e volumes de vendas mensais.')
    st.markdown('## Modelo de Decomposição')
    st.write("Decomposição Multiplicativa: A série temporal é modelada como o produto dos componentes de tendência, sazonalidade e resíduos. Este modelo é útil quando a variação sazonal muda proporcionalmente ao nível da série temporal.")
    st.write("Decomposição Aditiva: A série temporal é modelada como a soma dos componentes de tendência, sazonalidade e resíduos. Este modelo é útil quando a variação sazonal é aproximadamente constante ao longo do tempo.")
    st.markdown("")
    st.markdown("### Analisando a tendência, sazonalidade e resíduos")
    st.write('Tendência: Refere-se ao movimento geral da série temporal ao longo do tempo, representando um aumento ou diminuição a longo prazo. É a componente que capta a direção geral em que os dados se movem.')
    st.write('Sazonalidade: Refere-se aos padrões repetitivos e previsíveis que ocorrem em intervalos regulares, como diariamente, semanalmente, mensalmente ou anualmente. Captura as flutuações que se repetem de forma consistente.')
    st.write('Sazonalidade Diária: Analisa variações diárias utilizando o parâmetro period=1.')
    st.write('Sazonalidade Semanal: Identifica padrões que se repetem semanalmente, com um período sazonal de 7 dias. Exemplos incluem flutuações de tráfego web dependendo do dia da semana.')
    st.write('Sazonalidade Mensal: Observa variações mensais, com um período sazonal de 30 dias (em média). Exemplos incluem vendas sazonais e flutuações na demanda por energia elétrica.')
    st.write('Sazonalidade Anual: Detecta padrões que se repetem anualmente, com um período sazonal de 365 dias. Exemplos incluem variações sazonais nas temperaturas ao longo das estações do ano.')
    st.write('Resíduos: São as variações aleatórias ou imprevisíveis que sobram depois de remover a tendência e a sazonalidade. Representam o "ruído" ou as flutuações inexplicáveis nos dados.')
    seasonal_analysis = seasonal_decompose(df_filtered['y'], model='multiplicative', period=25)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15,10))
    seasonal_analysis.observed.plot(ax=ax1)
    seasonal_analysis.trend.plot(ax=ax2)
    seasonal_analysis.seasonal.plot(ax=ax3)
    seasonal_analysis.resid.plot(ax=ax4)

    date_format = mdates.DateFormatter('%Y')
    for ax in [ax1, ax2, ax3, ax4]:
        ax.xaxis.set_major_formatter(date_format)
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_minor_locator(mdates.MonthLocator())

    plt.tight_layout()
    st.pyplot(fig)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("### Analisando o ACF e PACF")
    # Plot ACF e PACF
    st.write('ACF (Função de Autocorrelação): Mede a correlação entre uma série temporal e versões defasadas dela mesma, ajudando a identificar a presença e a extensão de padrões repetitivos ao longo do tempo.')

    fig_acf = plot_acf(df_filtered['y'], lags=50)
    st.pyplot(fig_acf)
    st.write('PACF (Função de Autocorrelação Parcial): Mede a correlação entre a série temporal e suas defasagens, removendo os efeitos das defasagens intermediárias, permitindo uma análise mais precisa das relações diretas entre pontos em diferentes tempos.')

    fig_pacf = plot_pacf(df_filtered['y'], lags=50)
    st.pyplot(fig_pacf)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("### Analisando a Série Temporal")
    # Analisando a série temporal
    df_mean = df_filtered.rolling(window=12).mean()
    df_std = df_filtered.rolling(window=12).std()

    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df_filtered, color='blue', label='Série Normal')
    ax.plot(df_mean, color='red', label='Média')
    ax.plot(df_std, color='black', label='Desvio Padrão')
    ax.xaxis.set_major_locator(mdates.YearLocator())
    plt.title('Série Temporal')
    plt.legend(loc='lower right')
    st.pyplot(fig)
    st.write('Aparentemente a serie temporal não é estacionaria devido a distância bem notoria do desvio padrão.')
    
    # Validando a estacionariedade da série temporal através do teste de Dickey-Fuller
    
    adf_result = adf(df_filtered['y'])
    st.markdown('## Testes Estatísticos')
    st.write('Teste de Dickey-Fuller Aumentado (ADF): É um teste estatístico usado para verificar se uma série temporal é estacionária, implementado na função adfuller do pacote statsmodels em Python.')
    st.write('Série Temporal Estacionária: Uma série é considerada estacionária se suas propriedades estatísticas, como média e variância, permanecem constantes ao longo do tempo, sem padrões sistemáticos ou tendências que afetem essas propriedades.')
  
    st.write(f'ADF: {adf_result[0]}')
    st.write(f'Valor p: {adf_result[1]}')
    st.write('****VALORES CRITICOS****')
    for key, value in adf_result[4].items():
        st.write(f'   {key}: {value}')
    st.write('Série não é estacionária: valor p > 0.05. Valores críticos abaixo do ADF ')
 
    # Fazendo a diferenciação através de logaritmos
    indexedDataset_logScale = np.log(df_filtered)

    movingAverage = indexedDataset_logScale.rolling(window=12).mean()
    movingSTD = indexedDataset_logScale.rolling(window=12).std()

    datasetLogScaleMinusMovingAverage = indexedDataset_logScale - movingAverage
    datasetLogScaleMinusMovingAverage.dropna(inplace=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("### Analisando a Série Temporal Estacionária")
    def test_stationarity(timeseries):
        movingAverage = timeseries.rolling(window=12).mean()
        movingSTD = timeseries.rolling(window=12).std()

        fig, ax = plt.subplots(figsize=(10,6))
        ax.plot(timeseries, color='blue', label='Série Normal')
        ax.plot(movingAverage, color='red', label='Média')
        ax.plot(movingSTD, color='black', label='Desvio Padrão')
        ax.xaxis.set_major_locator(mdates.YearLocator())
        plt.title('Série Temporal Estacionária')
        plt.legend(loc='upper right')
        st.pyplot(fig)

        dftest = adf(timeseries['y'], autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput[f'Critical Value ({key})'] = value
        st.write(dfoutput)
        st.write('Série estacionária, pois o p value < 0.05')

    test_stationarity(datasetLogScaleMinusMovingAverage)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("### Analisando o ACF e PACF Após Diferenciação")
    # ACF e PACF após diferenciação
    lag_acf = acf(datasetLogScaleMinusMovingAverage['y'], nlags=20)
    lag_pacf = pacf(datasetLogScaleMinusMovingAverage['y'], nlags=20, method='ols')

    fig, ax = plt.subplots(1, 2, figsize=(15,6))
    ax[0].plot(lag_acf)
    ax[0].axhline(y=0, linestyle='--', color='gray')
    ax[0].axhline(y=-1.96/np.sqrt(len(datasetLogScaleMinusMovingAverage)), linestyle='--', color='gray')
    ax[0].axhline(y=1.96/np.sqrt(len(datasetLogScaleMinusMovingAverage)), linestyle='--', color='gray')
    ax[0].set_title('Autocorrelation Function')

    ax[1].plot(lag_pacf)
    ax[1].axhline(y=0, linestyle='--', color='gray')
    ax[1].axhline(y=-1.96/np.sqrt(len(datasetLogScaleMinusMovingAverage)), linestyle='--', color='gray')
    ax[1].axhline(y=1.96/np.sqrt(len(datasetLogScaleMinusMovingAverage)), linestyle='--', color='gray')
    ax[1].set_title('Partial Autocorrelation Function')
    st.pyplot(fig)

    model = ARIMA(datasetLogScaleMinusMovingAverage, order=(2,1,18))  # (p,d,q)
    results_AR = model.fit()
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("### Plot do Modelo ARIMA")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(datasetLogScaleMinusMovingAverage, label='Série Original')
    ax.plot(results_AR.fittedvalues, color='red', label='Valores Ajustados')
    ax.set_title(f'RSS: {sum((results_AR.fittedvalues - datasetLogScaleMinusMovingAverage["y"])**2):.4f}')
    st.pyplot(fig)

    predictions = results_AR.fittedvalues
    predictions.index = datasetLogScaleMinusMovingAverage.index
    predicted_values = indexedDataset_logScale['y'].iloc[0] + np.cumsum(predictions)

    mape = np.mean(np.abs((datasetLogScaleMinusMovingAverage['y'] - predicted_values) / datasetLogScaleMinusMovingAverage['y'])) * 100
    mae = mean_absolute_error(datasetLogScaleMinusMovingAverage['y'], predicted_values)
    mse = mean_squared_error(datasetLogScaleMinusMovingAverage['y'], predicted_values)
    rmse = np.sqrt(mse)

    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    with col1:
        st.metric(label="MSE", value=f"{mse:.2f}")
        
    with col2:
        st.metric(label="RMSE", value=f"{rmse:.2f}")

    with col3:
        st.metric(label="MAE", value=f"{mae:.2f}")

    with col4:
        st.metric(label="MAPE", value=f"{mape:.2f}%")

    #with col5:
    #    st.metric(label="Acurácia", value=f"{100-mape:.2f}%")

# Função para renderizar a subaba Prophet
def render_prophet():
    st.header(":orange[Modelo Prophet 🔮]", divider="blue")
    st.write("Nesta análise, utilizamos o modelo Prophet, desenvolvido pelo Facebook, para prever os preços futuros do petróleo Brent. O Prophet é ideal para lidar com séries temporais com componentes de tendência e sazonalidade, e é especialmente útil para dados que apresentam sazonalidade anual, diária ou semanal.")
    st.write("A seguir, apresentamos a comparação entre os valores reais e as previsões geradas pelo modelo, destacando a tendência e a margem de confiança das previsões.")
    st.write("")
    st.write("")
    # Título do aplicativo
    st.subheader('Seleção de Datas para o Modelo Prophet')

    # Data inicial e final padrão
    default_start_date = datetime.strptime('2010-06-01', '%Y-%m-%d')
    default_end_date = datetime.strptime('2024-06-01', '%Y-%m-%d')

    # Widget para seleção de datas
    start_date = st.date_input('Selecione a data de início para Prophet', value=default_start_date, format="DD/MM/YYYY")
    end_date = st.date_input('Selecione a data de término para Prophet', value=default_end_date, format="DD/MM/YYYY")
    st.write("")
    st.write("")
    # Converter datas selecionadas para datetime64[ns]
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    # Exibir as datas selecionadas no formato brasileiro (dd/mm/yyyy)
    st.write(f'Data de início selecionada: {start_date.strftime("%d/%m/%Y")}')
    st.write(f'Data de término selecionada: {end_date.strftime("%d/%m/%Y")}')
    st.write("")

    # Carregar e preparar o dataframe
    df = pd.read_csv('ipea_df.csv')
    df = df.rename(columns={'Preco_petroleo': 'y'})
    df = df.rename(columns={'Data': 'ds'})
    df['ds'] = pd.to_datetime(df['ds'], format='%d/%m/%Y', errors='coerce')
    df['y'] = df['y'].astype(int)
    df['y'] = df['y'].apply(lambda x: float(f"{x // 100}.{x % 100:02}"))
    
    # Filtrar o DataFrame usando as datas selecionadas
    df5anos = df.loc[(df['ds'] >= start_date) & (df['ds'] <= end_date)]
    anos = end_date.year - start_date.year - ((end_date.month, end_date.day) < (start_date.month, start_date.day))
    st.write(f'A base de dados utilizada no modelo tem :blue[{df5anos.shape[0]}] linhas e :blue[{df5anos.shape[1]}] colunas. Sendo assim, foram considerados dados históricos de :blue[{anos}] anos.')
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f'### Série Histórica Utilizada no Modelo - {anos} anos')    
    # Gráfico
    fig = px.line(df5anos, x='ds', y='y')
    st.plotly_chart(fig)

    # Capturar a saída do df.info() em um buffer de string
    buffer = io.StringIO()
    df5anos.info(buf=buffer)
    info_str = buffer.getvalue()

    # Processar a string para extrair informações e criar um DataFrame
    info_lines = info_str.split('\n')
    info_dict = {
        "Valores Não Nulos": [],
        "Coluna": [],
        "Dtype": []
    }
    for line in info_lines[5:-2]:
        parts = line.split() 
        if len(parts) >= 5:
            column_name = ' '.join(parts[:-4])  # Pega tudo até os últimos 4 elementos
            non_null_count = parts[-4]
            dtype = parts[-1]
            
            info_dict["Valores Não Nulos"].append(parts[2])
            info_dict["Coluna"].append(non_null_count)
            info_dict["Dtype"].append(dtype)
        else:
            # Caso a linha não tenha partes suficientes, pula para a próxima linha
            continue
    info_df = pd.DataFrame(info_dict)
    st.markdown('')
    st.markdown('')
    st.markdown('### Informações do Dataframe Utilizado no Modelo')
    st.dataframe(info_df)

    # Dividindo a base em treino (75%) e teste (25%)
    train_data = df5anos.sample(frac=0.75, random_state=0)
    test_data = df5anos.drop(train_data.index)
    st.write(f'A base de treinamento terá :red[{train_data.shape[0]}] linhas e a base de testes terá :red[{test_data.shape[0]}] linhas. Ambas terão as duas colunas inciais do dataframe, data diária e preço do petróleo.')

    # Importando uma biblioteca que consolida os dias úteis do Brasil para eliminar da previsão os feriados e finais de semana, uma vez que a bolsa não opera nesses dias.
    calendario_brasileiro = Brazil()
    # Pegando os feriados brasileiros apenas de 2024
    feriados_2024 = calendario_brasileiro.holidays(2024)
    # Convertendo as datas dos feriados
    df_feriados = pd.DataFrame(feriados_2024, columns=['Data', 'Feriado'])
    # Criando um DF com todas as datas de 2024
    datas_2024 = pd.date_range(start='2024-01-01', end='2024-12-31')
    # Aqui ele filtra todos os dias que são finais de semana
    dias_nao_uteis = datas_2024[(~datas_2024.isin(df_feriados['Data'])) & (datas_2024.weekday >= 5)]
    # Cria a base com os dias de sábado e domingo
    df_dias_nao_uteis = pd.DataFrame({'Data': dias_nao_uteis, 'Dia útil': False})
    # Juntando os DFs de feriados e finais de semana
    df_feriados['Data'] = pd.to_datetime(df_feriados['Data'])
    df_dias_nao_uteis['Data'] = pd.to_datetime(df_dias_nao_uteis['Data'])

    # Concatenando e ordenando os dataframes
    df_dias_nao_uteis = pd.concat([df_feriados, df_dias_nao_uteis]).sort_values(by='Data').reset_index(drop=True)
    modelo = Prophet(daily_seasonality=True)
    modelo.fit(train_data)
    dataFramefuture = modelo.make_future_dataframe(periods=150, freq='D')
    dataFramefuture = dataFramefuture[~dataFramefuture['ds'].isin(df_dias_nao_uteis['Data'])]
    previsao = modelo.predict(dataFramefuture)

    st.markdown('')
    st.markdown('')
    st.markdown('### Valores Reais e Previstos pelo Modelo')
    fig = px.line(previsao, x='ds', y='yhat', labels={'ds': 'Fechamento Anual', 'yhat': 'Preço Diário Petróleo'})

    # Adicionar os valores reais
    fig.add_trace(go.Scatter(x=test_data['ds'], y=test_data['y'], mode='markers', name='Valores Reais', marker=dict(color='red')))

    # Adicionar a tendência prevista e margem de confiança com cores explícitas
    fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat'], mode='lines', name='Tendência Prevista', line=dict(color='lightblue')))
    fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_upper'], mode='lines', name='Margem de Confiança Superior', line=dict(color='yellow', dash='dash')))
    fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_lower'], mode='lines', name='Margem de Confiança Inferior', line=dict(color='green', dash='dash')))

    # Adicionar título e rótulos dos eixos
    fig.update_layout(
        xaxis_title='Fechamento Anual',
        yaxis_title='Preço Diário Petróleo',
        legend_title='Legenda',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        width=1000,  # Ajustar largura do gráfico
        height=600   # Ajustar altura do gráfico
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

    st.markdown('')
    st.markdown('')
    st.markdown('### Métricas de Avaliação do Modelo')

    previsao_cols = ['ds', 'yhat']
    valores_reais_cols = ['ds', 'y']

    previsao = previsao[previsao_cols]
    valores_reais = train_data[valores_reais_cols]

    resultados = pd.merge(previsao, valores_reais, on='ds', how='inner')
    resultados['erro_percentual_absoluto'] = np.abs((resultados['y'] - resultados['yhat']) / resultados['y']) * 100

    mape = np.mean(resultados['erro_percentual_absoluto'])

    # Calcular o MSE (Erro Quadrático Médio)
    mse = mean_squared_error(resultados['y'], previsao.loc[:len(resultados)-1, 'yhat'])

    # Calcular o MAE (Erro Absoluto Médio)
    mae = mean_absolute_error(resultados['y'], previsao.loc[:len(resultados)-1, 'yhat'])

    # Calcular o MdAPE (Erro Percentual Absoluto Médio na Mediana)
    mediana_y = resultados['y'].median()
    mdape = np.mean(np.abs((resultados['y'] - resultados['yhat']) / mediana_y)) * 100

    # Calcular o RMSE
    rmse = np.sqrt(mean_squared_error(resultados['y'], previsao.loc[:len(resultados)-1, 'yhat']))
    acuracia = 100 - mape

    # Organizar as métricas em colunas para melhor visualização
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    with col1:
        st.metric(label="MSE", value=f"{mse:.2f}")
        
    with col2:
        st.metric(label="RMSE", value=f"{rmse:.2f}")

    with col3:
        st.metric(label="MAE", value=f"{mae:.2f}")

    with col4:
        st.metric(label="MAPE", value=f"{mape:.2f}%")

    with col5:
        st.metric(label="Acurácia", value=f"{acuracia:.2f}%")

# Criação das abas
tab1, tab2 = st.tabs(["Arima", "Prophet"])
with tab1:
    render_arima()
with tab2:
    render_prophet()
