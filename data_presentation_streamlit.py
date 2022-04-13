# integrar a analise de dados com a interação. 

import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('15dias_postagem_seguidroes.csv',header=0,index_col=0)

st.set_page_config(layout="wide")
st.title('Perfis do Instagram que divulgam notícias sobre energias renováveis.')
st.header("Interação com o banco de dados que foi criado baseado na #MercadoLivreDeEnergia")


@st.cache()
def load_table():
    pth = "lista_ordenada_15dias.csv"
    
    return pd.read_csv(pth,header=0,index_col=0)

    
table = load_table()

sel_att = st.selectbox('Escolha uma das', ['@Perfil vs NumeroSeguidores','@Perfil vs NumeroPostagens','@Perfil vs relacaoSegPost'])
# @Perfil,NumeroSeguidores,NumeroPostagens,url,relacaoSegPost

fig1 = px.bar(        
        table,
        x = sel_att.split('vs')[1].strip(),
        y = "@Perfil",
        title = sel_att,
        orientation='h'
        )

fig1.update_layout(
    autosize=False,
    width = 100,
    height= 600,
    margin=dict(
        l=100,
        r=300,
        b=50,
        t=50,
        pad=3
    )
    )

st.plotly_chart(fig1, use_container_width=True)

sel_att2 = st.selectbox('Selecione ...', [" ","Toda Tabela","Top 10 Numero Seguidores","TOP 10 Numero de Postagens"])

if sel_att2 == "Top 10 Numero Seguidores":

    st.write('Tabela do top 10 perfis com mais seguidores.')
    st.markdown(table[['@Perfil','NumeroSeguidores','NumeroPostagens','relacaoSegPost','url']].head(10).to_markdown())

elif sel_att2 == "Top 10 Numero de Postagens":
    
    st.write('Tabela do top 10 perfis com mais postagens.')
    top10= table[['@Perfil','NumeroSeguidores','NumeroPostagens','relacaoSegPost','url']].sort_values('NumeroPostagens',ascending=False).reset_index().head(10)
    top10 = top10.drop('index',axis=1)
    st.markdown(top10.to_markdown())

elif sel_att2 == "Toda Tabela":

    st.write('Toda Tabela ordenda pelo perfil de maior numero de seguidores.')
    st.markdown(table[['@Perfil','NumeroSeguidores','NumeroPostagens','relacaoSegPost','url']].to_markdown())

else:
    pass