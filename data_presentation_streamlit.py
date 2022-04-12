# integrar a analise de dados com a interação. 

import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('15dias_postagem_seguidroes.csv',header=0,index_col=0)

# st.set_page_config(layout="wide")
st.title('Perfis do Instagram que divulgam notícias sobre energias renováveis.')
st.header("Interação com o banco de dados que foi criado baseado na #MercadoLivreDeEnergia")


@st.cache()
def load_table():
    pth = "lista_ordenada_15dias.csv"
    
    return pd.read_csv(pth,header=0,index_col=0)

    
table = load_table()

sel_att = st.sidebar.selectbox('Escolha a coluna', table.keys())

sel_att2 = st.sidebar.selectbox('Escolha a segunda coluna', table.keys())

sigbtt = st.sidebar.button("Realizar o gŕafico.")

st.sidebar.write("Gráfico e tabela ao lado.")

if sigbtt:
    
    fig1 = px.bar(        
            table,
            x = "@Perfil",
            y = sel_att,
            title = f"{sel_att} vs @Perfil",
            color= sel_att2
    )

    st.plotly_chart(fig1)

st.write('Tabela do top 10 perfis com mais seguidores.')

st.markdown(table.head(10).to_markdown(), unsafe_allow_html=True)