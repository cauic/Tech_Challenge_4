
import streamlit as st
import streamlit.components.v1 as components
st.header(":orange[Eventos Históricos]", divider="blue")




# Embed URL of the Power BI report
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiNWY1MGFkNjgtMTA2Yi00NTNiLTg2OTktMjViZTgxNmNhZGU2IiwidCI6ImY2NWZlYThhLWI5ODgtNDE0NC05NWVmLTRmOWJlY2NkMTRiNSJ9"

# Set the width and height as per your requirements
width = 700
height = 380

# Title of the Streamlit app
st.title("Analise Dados Preço Combustivel")

# Embed the Power BI dashboard using streamlit's HTML component
components.html(
    f"""
    <iframe width="{width}" height="{height}" src="{powerbi_embed_url}" frameborder="0" allowFullScreen="true"></iframe>
    """,
    height=height,
    width=width  # Adjust the iframe height to match the Power BI report's height
)

# Add a small disclaimer text below the dashboard
st.markdown(
    '<p style="text-align: center; color: gray; font-size: 12px;">Alguns gráficos podem estar indisponíveis nesta versão web. Para visualizar o dashboard completo, acesse o link da versão desktop no arquivo "LEIA-ME".</p>',
    unsafe_allow_html=True
)
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

evento = st.selectbox("Selecione um evento:", [
    "Guerra do Golfo (1991)",
    "Crise Financeira Asiática (1999)",
    "Restrições de Produção pela OPEP (2000)",
    "Ataques Terroristas de 11 de Setembro (2001)",
    "Guerra do Iraque (2003)",
    "Crise Financeira Global (2008)",
    "Pandemia de COVID-19 (2020)"
])
if evento == "Guerra do Golfo (1991)":
    st.subheader(":red[Guerra do Golfo (1991)]", divider="blue")
    st.markdown('A Guerra do Golfo teve um impacto significativo nos preços do petróleo Brent. Este conflito começou quando o Iraque invadiu o Kuwait em agosto de 1990, levando a uma resposta internacional liderada pelos Estados Unidos. Os preços do petróleo reagiram fortemente às incertezas relacionadas ao fornecimento de petróleo proveniente do Oriente Médio.')
    st.markdown('Em 16 de janeiro de 1991, houve um aumento substancial de 43.51% no preço do petróleo Brent. Este foi o segundo maior aumento nos registros da série histórica, ocorrendo no dia em que a operação "Tempestade no Deserto" foi iniciada, marcando o começo dos combates diretos na Guerra do Golfo.')
    st.markdown('Os dados indicam que as preocupações com uma possível interrupção no fornecimento de petróleo devido ao conflito causaram volatilidade extrema nos mercados. Além disso, o medo de que o conflito pudesse se espalhar para outros países produtores de petróleo na região também contribuiu para o aumento nos preços.')
    st.markdown('Após a liberação do Kuwait e o fim dos combates, os preços começaram a se estabilizar, mas o evento deixou uma marca duradoura na história do mercado de petróleo, demonstrando como conflitos geopolíticos podem influenciar drasticamente os preços globais do petróleo.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('A invasão do Kuwait pelo Iraque em 1990 levou a um aumento sem precedentes nos preços do petróleo Brent, ressaltando como a segurança energética global depende diretamente da estabilidade política em regiões que são vitais para a produção mundial de petróleo.')


elif evento == "Crise Financeira Asiática (1999)":
    st.subheader(":red[Crise Financeira Asiática (1999)]", divider="blue")
    st.markdown('A Crise Financeira Asiática, iniciada em 1997, teve repercussões significativas nos mercados globais, afetando os preços do petróleo Brent em 1999. A recuperação econômica dos países asiáticos aumentou a demanda por petróleo, levando a um aumento nos preços.')
    st.markdown('Em 12 de março de 1999, o preço do petróleo Brent subiu 16.69%. Este aumento significativo ocorreu durante um período de estabilização e recuperação econômica na Ásia, que impulsionou a demanda global por petróleo.')
    st.markdown('A volatilidade nos preços durante este período reflete a sensibilidade do mercado de petróleo às mudanças econômicas globais, especialmente em regiões de rápido crescimento econômico como a Ásia.')
    st.markdown('Este evento destaca como crises econômicas regionais podem ter um impacto prolongado nos mercados globais de petróleo, afetando preços e políticas energéticas internacionais.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('O aumento dos preços do petróleo em 1999 após a crise financeira asiática ilustrou como mercados emergentes têm crescente influência na demanda global por energia, sinalizando uma mudança no epicentro econômico mundial para a Ásia, particularmente a China.')
    

elif evento == "Restrições de Produção pela OPEP (2000)":
    st.subheader(":red[Restrições de Produção pela OPEP (2000)]", divider="blue")
    st.markdown('No ano 2000, a OPEP implementou várias restrições de produção com o objetivo de estabilizar e aumentar os preços do petróleo. Essas decisões tiveram um impacto imediato nos mercados globais.')
    st.markdown('Em 13 de setembro de 2000, o preço do petróleo Brent registrou um aumento de 18.76%, refletindo a resposta direta do mercado às políticas da OPEP. Este foi um dos maiores aumentos percentuais registrados na série histórica.')
    st.markdown('Os cortes na produção limitaram a oferta no mercado global, causando um aumento nos preços e evidenciando o poder da OPEP como um influenciador chave no mercado de petróleo.')
    st.markdown('Esse evento é um exemplo claro de como decisões políticas de grandes cartéis podem manipular mercados globais e influenciar diretamente os preços do petróleo internacionalmente.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('As restrições de produção impostas pela OPEP em 2000 destacaram a importância vital de manter reservas estratégicas de petróleo. Essas reservas são essenciais para mitigar os efeitos da volatilidade dos preços e garantir a segurança energética, permitindo que os países consumidores respondam de forma mais eficaz a choques de oferta e mantenham a estabilidade econômica durante períodos de incerteza no mercado de petróleo.')


elif evento == "Ataques Terroristas de 11 de Setembro (2001)":
    st.subheader(":red[Ataques Terroristas de 11 de Setembro (2001)]", divider="blue")
    st.markdown('Os ataques de 11 de setembro de 2001 nos Estados Unidos tiveram um impacto imediato e dramático nos mercados globais, incluindo os preços do petróleo. A incerteza gerada pelos ataques levou a aumentos voláteis nos preços.')
    st.markdown('Em 12 de setembro de 2001, um dia após os ataques, o preço do petróleo Brent aumentou 17.88%. Este aumento reflete o medo de interrupções no fornecimento de petróleo e as preocupações com a estabilidade geopolítica global.')
    st.markdown('A volatilidade dos preços neste período destaca como eventos geopolíticos súbitos e significativos podem afetar rapidamente os mercados de energia.')
    st.markdown('Este evento reforçou a vulnerabilidade dos mercados de petróleo a choques externos e alterou permanentemente as políticas de segurança e energia em todo o mundo.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('Os ataques de 11 de setembro demonstraram como eventos de segurança que não estão diretamente ligados à produção de petróleo ainda podem causar aumentos significativos nos preços. Este impacto ocorre devido ao efeito desses eventos na percepção de risco global, influenciando diretamente os mercados energéticos.')


elif evento == "Guerra do Iraque (2003)":
    st.subheader(":red[Guerra do Iraque (2003)]", divider="blue")
    st.markdown('A invasão do Iraque em março de 2003 pelos Estados Unidos e aliados, sob alegações de armas de destruição em massa, provocou incertezas significativas no mercado de petróleo.')
    st.markdown('Em 17 de março de 2003, o preço do petróleo Brent experimentou um aumento significativo de 19.23%, refletindo as tensões antes do início do conflito e as preocupações com o fornecimento de petróleo da região.')
    st.markdown('A guerra levou a uma reconfiguração do mercado de petróleo no Oriente Médio e mostrou como conflitos armados podem impactar os preços globais do petróleo a curto e longo prazo.')
    st.markdown('A instabilidade continuada na região manteve os preços em níveis elevados e destacou a importância da região para o mercado energético global.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('O início da Guerra do Iraque reflete como as preocupações geopolíticas sobre a estabilidade em regiões produtoras de petróleo podem levar a um aumento prolongado dos preços, destacando a interdependência entre segurança regional e mercados energéticos.')

elif evento == "Crise Financeira Global (2008)":
    st.subheader(":red[Crise Financeira Global (2008)]", divider="blue")
    st.markdown('A crise financeira de 2008, desencadeada pelo colapso do mercado imobiliário nos EUA, teve um impacto profundo nos mercados globais, incluindo o petróleo.')
    st.markdown('Durante o pico da crise, em 10 de outubro de 2008, o preço do petróleo Brent caiu 16.66%, refletindo a forte redução na demanda global à medida que a economia mundial desacelerava.')
    st.markdown('A crise ressaltou a interdependência entre os mercados financeiros e de energia, e como uma desaceleração econômica global pode levar a uma queda acentuada na demanda por petróleo.')
    st.markdown('Esta crise levou a mudanças significativas nas políticas econômicas e regulatórias em todo o mundo, com efeitos duradouros nos mercados de energia.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('A crise financeira de 2008 levou a uma significativa queda nos preços do petróleo, refletindo a redução da demanda global à medida que a economia mundial enfrentava uma recessão profunda. Esse evento destacou como a saúde econômica global está diretamente ligada ao consumo de petróleo.')

    
elif evento == "Pandemia de COVID-19 (2020)":
    st.subheader(":red[Pandemia de COVID-19 (2020)]", divider="blue")
    st.markdown('A pandemia de COVID-19 causou um impacto sem precedentes nos mercados globais em 2020, com fechamentos de fronteiras, lockdowns e uma redução drástica na demanda por petróleo.')
    st.markdown('Os dias mais impactantes foram 20 de abril de 2020, com um aumento de 90.35%, e 21 de abril de 2020, com uma queda de 33.77%. Esses movimentos extremos refletem a volatilidade causada pela pandemia e pela guerra de preços entre a Rússia e a Arábia Saudita.')
    st.markdown('Além disso, outras quedas significativas ocorreram em 1 de abril de 2020 (-26.04%), 4 de maio de 2020 (-19.87%), e 2 de abril de 2020 (-16.81%), todas influenciadas pela continuidade da baixa demanda e pelo excesso de oferta.')
    st.markdown('Este evento demonstrou como uma crise de saúde global pode influenciar drasticamente os mercados de energia, levando a reavaliações das estratégias energéticas e de sustentabilidade em todo o mundo.')
    st.subheader(":violet[Insight]", divider='')
    st.markdown('A pandemia de COVID-19 provocou uma das maiores disrupções no mercado de petróleo da história, com o preço do petróleo Brent caindo para valores negativos em abril de 2020. Este evento sem precedentes destacou a vulnerabilidade dos mercados globais a choques de demanda súbitos e severos, impulsionando uma reavaliação urgente das estratégias de resiliência e sustentabilidade energética.')
