import streamlit as st
import data
import plotly.express as px
import graf_02 as g2
import graf_01 as g1
import graf_bar_pie as bp

st.set_page_config(page_title="Leadership Dashboard", page_icon="📊", layout="wide")
df = data.feature()
grupo=1
columnas=['Nombre','Promedio_Tecnicas','Promedio_Blandas','Experiencia  [En Data Science]','Experiencia  [En liderar grupos]','Puntaje_Liderazgo','Grupo']

df = df[columnas]
df['Puntaje_Liderazgo'] = (df['Puntaje_Liderazgo']*10).astype('int8')
df['Promedio_Tecnicas'] = df['Promedio_Tecnicas'].round(1)
df.sort_values(by='Puntaje_Liderazgo',ascending=False, inplace=True)
df=df[df['Grupo']==grupo]

st.markdown(f"<h1 style='text-align: center;'>Grupo {grupo} - Evaluación de Candidatos para Liderazgo en Data Science</h1>", unsafe_allow_html=True)

st.markdown('''<style>
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2),
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div > div > div > div > div > div > div > svg:nth-child(1){
      border: 1px solid #00ff00;
      border-radius: 5px;
      padding: 3px;
      text-align: center !important;
      font-size:10px !important;
}            
#tabs-bui3-tabpanel-0 > div > div > div > div > div > div > div > div > svg:nth-child(1){
      padding:0 20px;
            }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div{
            display: flex;
            justify-content: center;
            }            
            <style>''', unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
   g1.graficas(df,grupo)
with col2:


   tab1, tab2 = st.tabs(["Puntuación", "Distribución puntos"])

   with tab1: 
      bp.grafica_bar_00(df,grupo)
   with tab2:
      bp.grafica_pie(df,grupo)

g1.comment(df)