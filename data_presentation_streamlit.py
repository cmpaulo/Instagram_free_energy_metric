# integrar a analise de dados com a interação. 

import pandas as pd
from regex import X
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

st.header("Compare o número de publicações e seguidores de cada um dos pefis listados")

list_pro = table['@Perfil'].sort_values().to_list()
perfil2 = st.selectbox('Selecione um perfil', list_pro)

perfil1 = st.selectbox('Selecione outro perfil', list_pro)


# Create fig

fig = go.Figure()
fig.add_trace(go.Bar(y = ['NumeroSeguidores','NumeroPostagens'] , x = table.set_index('@Perfil').loc[perfil1, ['NumeroSeguidores','NumeroPostagens']].values, name=perfil1,orientation='h'))

fig.add_trace(go.Bar(y = ['NumeroSeguidores','NumeroPostagens'] , x = table.set_index('@Perfil').loc[perfil2, ['NumeroSeguidores','NumeroPostagens']].values, name=perfil2,orientation='h'))

chkbx = st.checkbox('barras empilhadas')
if chkbx:
    fig.update_layout(barmode='stack')  

fig.update_layout(
    title_text=f"Comparação do número de seguidores e postagens entre os perfis {perfil2} vs {perfil1}"
    )   

st.plotly_chart(fig, use_container_width=True)

############################################### tabels

st.header("Tabelas com os valores de cada perfil")

sel_att2 = st.selectbox('Selecione para ver a lista de perfis', ["TOP 10 Seguidores","TOP 10 Postagens", "Toda Tabela"])

st.markdown("Tabela disponível para baixar no [link](https://github.com/cmpaulo/Instagram_free_energy_metric/blob/main/lista_ordenada_15dias.csv)")

if sel_att2 == "TOP 10 Seguidores":
    
    st.write('Tabela do top 10 perfis com mais seguidores.')
    st.markdown(table[['@Perfil','NumeroSeguidores','url']].head(10).to_markdown())

if sel_att2 == "Toda Tabela":
    
    st.write('Toda Tabela ordenda pelo perfil de maior numero de seguidores.')
    st.markdown(table[['@Perfil','NumeroSeguidores','NumeroPostagens','relacaoSegPost','url']].to_markdown())


if sel_att2 == "TOP 10 Postagens":
    st.write('Tabela do top 10 perfis com mais postagens.')
    top = table[['@Perfil','NumeroPostagens','url']].sort_values('NumeroPostagens',ascending=False).reset_index().head(10)
    top10 = top.drop('index',axis='columns')
    st.markdown(top10.to_markdown())