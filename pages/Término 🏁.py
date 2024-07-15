import streamlit as st
import base64

def get_image_download_link(img_path, link, width):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f'<a href="{link}" target="_blank"><img src="data:image/jpeg;base64,{encoded_string}" alt="Link Image" style="width:{width}px;"></a>'



def render_conclusao():
    st.header(":orange[Conclusão]", divider="blue")
    #st.write("Bem-vindo à página de Conclusão!")
    st.write("Este projeto apresentou uma análise detalhada dos preços do petróleo Brent e a criação de um dashboard interativo para apoiar decisões estratégicas no setor petrolífero.")
    st.write("Utilizando dados do IPEA, realizamos uma análise exploratória para identificar padrões e eventos que influenciaram os preços. A previsão dos preços foi realizada utilizando os modelos ARIMA e Prophet, sendo o Prophet o modelo selecionado devido ao seu menor erro percentual médio absoluto (MAPE) de 9,98% (considerando o período dos últimos 10 anos). A análise e o desenvolvimento foram conduzidos com ferramentas como Power BI e Python, e o resultado foi disponibilizado através de um deploy no Streamlit.")

def render_referencias():
    st.header(":orange[Sobre o Projeto]", divider="blue")
    st.header(':violet[Pipeline de Análise de Dados e Machine Learning]')
    st.markdown('')
    st.image('ipea_eda_pipeline.drawio.png', caption='Pipeline de Dados', use_column_width=True)

    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.write("""
    
    ### 1. Web Scraping e Criação do DataFrame
    Como primeira etapa e ponto inicial, fizemos web scraping dos dados do site do IPEA com Python e transformamos em DataFrame.

    ### 2. Ajustes no DataFrame
    Após realizar alguns ajustes como renomear as colunas e desconsiderar algumas colunas, subimos o arquivo ao Google Storage utilizando o bucket como repositório.

    ### 3. Upload e Leitura do Arquivo no Bucket
    Depois de realizar o upload dos arquivos ao bucket, realizamos a leitura dele para dar sequência no projeto. Esse passo é importante visando uma estrutura mais escalável, uma vez que o bucket suporta arquivos estruturados e não estruturados. Além disso, no futuro podemos utilizar esse serviço para alimentar um Data Warehouse ou Data Lake.

    ### 4. Limpeza e Tratamento dos Dados
    Após a leitura do arquivo, começamos o processo de limpeza e tratamento dos dados (remoção de nulos, duplicatas, alteração no tipo de dados, etc.).

    ### 5. Análise Exploratória de Dados (EDA)
    Depois de tratados, começamos a fazer algumas análises exploratórias visando extrair pontos relevantes daquele dataset, como picos de máxima e baixa.

    ### 6. Desenvolvimento do Dashboard
    Após a EDA, começamos o desenvolvimento do dashboard no Power BI utilizando o DataFrame já tratado.

    ### 7. Machine Learning Flow
    Iniciamos o Machine Learning Flow para dar continuidade a uma das requisições do projeto, que consiste em desenvolver um modelo de machine learning que realize a previsão do preço diariamente.

    ### 8. Aplicação com Streamlit
    Como estrutura final, sumarizamos todas as informações dentro de uma aplicação utilizando o Streamlit.
    """)
    
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.header(':violet[Links Úteis]', divider='blue')
    # Caminho da imagem local
    img_path1 = "linkedin.jpeg"
    img_path2 = "github.jpg"

    # Defina o link para onde deseja que a imagem redirecione
    link1 = "https://www.linkedin.com/in/emerson-cauic-8a7a37113/"
    link2 = "https://www.linkedin.com/in/laio-soares/"
    link3 = "https://github.com/cauic/"
    link4 = "https://github.com/soareslaio"

    # Defina a largura desejada em pixels
    width = 50
 

    # Exibir a imagem como um hiperlink com tamanho ajustado
    st.markdown('#### LinkedIn')
 

    st.markdown(get_image_download_link(img_path1, link1, width), unsafe_allow_html=True)
    st.write('Emerson')
    st.markdown(get_image_download_link(img_path1, link2, width), unsafe_allow_html=True)
    st.write('Laio')

    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('#### GitHub')


    st.markdown(get_image_download_link(img_path2, link3, width), unsafe_allow_html=True)
    st.write('Emerson')
    st.markdown(get_image_download_link(img_path2, link4, width), unsafe_allow_html=True)
    st.write('Laio + LEIA-ME')






    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.header(':violet[Referências Externas]')
    st.markdown("[- Preço do petróleo: 4 momentos em que a alta impactou a economia](https://einvestidor.estadao.com.br/comportamento/preco-petroleo-impactos-economia/)")
    st.markdown('')
    st.markdown("[- 2000, Opep busca consenso para acordo sobre produção](https://www1.uol.com.br/economia/reuters/ult15032000174.htm)")
    st.markdown('')
    st.markdown("[- 2008, o ano em que o petróleo enlouqueceu o mercado](https://g1.globo.com/Noticias/Economia_Negocios/0,,MUL940136-9356,00-O+ANO+EM+QUE+O+PETROLEO+ENLOUQUECEU+O+MERCADO.html)")
    st.markdown('')
    st.markdown("[- COVID-19 e os impactos sobre o mercado de petróleo](https://www.ibp.org.br/observatorio-do-setor/analises/covid-19-e-os-impactos-sobre-o-mercado-de-petroleo/)")


tab1, tab2 = st.tabs(["Término", "Sobre o Projeto"])
with tab1:
    render_conclusao()
with tab2:
    render_referencias()
