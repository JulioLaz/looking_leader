from PIL import Image
import streamlit as st
import data
import graf_01 as g1
import graf_bar_pie as bp
import forms
import styles

icon = Image.open("leader.png")

st.set_page_config(page_title="Leadership Dashboard", page_icon=icon, layout="wide")

df = data.feature()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'group' not in st.session_state:
    st.session_state.group = None
if 'nombre' not in st.session_state:
    st.session_state.nombre = ""
if 'selected_group' not in st.session_state:
    st.session_state.selected_group = None

def check_credentials(nombre, grupo):
   #  nombre = nombre.lower()
    user_data = df[(df['Nombre'] == nombre) & (df['Grupo'] == grupo)]
    return not user_data.empty

if not st.session_state.authenticated:
    st.markdown(f"<h1 style='text-align: center;'>Bienvenido al clasificador de liderazgo</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Ingresa tu nombre, el del formulario:", value=st.session_state.nombre)
    st.markdown('''
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(3),
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) {
        display: flex;
        justify-content: center;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(3) > div,
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div {
        width: 20rem !important;
      #   display: flex;
    }
    /* Estilos para el input de texto */
    .stTextInput > div > div > input {
        width: 20rem;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
    }
    .stRadio > div > div > div {
            display:flex !important;
            justify-content: center !important}
    .stButton > button {
        width: 20rem;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(7) > div{
               display: flex;
                justify-content: center;}
    .stButton > button:hover {
        background-color: #45a049;
    }
                /*  centrar link de forms  */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(10) > div > div,                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div{
            display:flex !important;
            justify-content: center !important}
                /*  hidden navbar initial */
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0{
                display: none !important}    
                }                
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0{
            display: none !important;
            background:none !important;
                } 
#root > div:nth-child(1) > div.withScreencast > div > div > header{
            display: none !important;
            background:none !important;
                } 


                }                               
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
padding-top: 0px !important}                
    </style>
    ''', unsafe_allow_html=True)    

    st.session_state.selected_group = st.radio("Selecciona tu grupo:", df['Grupo'].sort_values(ascending=True).unique(), index=0 if st.session_state.selected_group is None else list(df['Grupo'].sort_values(ascending=True).unique()).index(st.session_state.selected_group), horizontal=True)

    st.markdown("""
    <style>
    .stColumns {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-end;
    }
    .stColumn {
        width: 48%;  /* Ajusta este valor según sea necesario */
    }
                /* centrar txt del error  */ 
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8) > div > div > div > div > div > div > p{
    text-align: center !important;
                }
    </style>
    """, unsafe_allow_html=True)

    if st.button("Acceder"):
        if check_credentials(st.session_state.nombre, st.session_state.selected_group):
            st.session_state.authenticated = True
            st.session_state.group = st.session_state.selected_group
            st.rerun()
        else:
            st.error(f"Nombre o grupo incorrecto.\nPor favor, verifica tus datos e intenta de nuevo.")

    styles.style_gen()           
    forms.forms()            

if st.session_state.authenticated:
    df_filtered = df[df['Grupo'] == st.session_state.group]

    grupo = int(df_filtered.Grupo.unique()[0])

    columnas=['Nombre','Promedio_Tecnicas','Promedio_Blandas','Experiencia  [En Data Science]','Experiencia  [En liderar grupos]','Puntaje_Liderazgo','Grupo']

    df=df[df['Grupo']==grupo]
    df = df[columnas]
    df['Puntaje_Liderazgo'] = (df['Puntaje_Liderazgo']*10).astype('int8')
    df['Promedio_Tecnicas'] = df['Promedio_Tecnicas'].round(1)
    df['Promedio_Blandas'] = df['Promedio_Blandas'].round(1)
    df.sort_values(by='Puntaje_Liderazgo',ascending=False, inplace=True)

    st.markdown(f"<h1 style='text-align: center;'>Grupo {grupo} - Evaluación de Candidatos para Liderazgo en Data Science</h1>", unsafe_allow_html=True)

    st.markdown('''<style>
    /* bordes de graf scatter pie & bar */            
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2),
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div > div > div > div > div > div > div > svg:nth-child(1){
            border: 1px solid #00ff00;
            border-radius: 5px;
            padding: 0 0 10px 0;
            text-align: center !important;
            font-size:10px !important;
            background-color:black;
    }            
    /* bordes de graf embudo */            
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div > div > svg:nth-child(5){
            border: 1px solid #00ff00;
            border-radius: 5px;
            padding: 5px;
    }            
    #tabs-bui3-tabpanel-0 > div > div > div > div > div > div > div > div > svg:nth-child(1){
            padding:0 20px;
                }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8),
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div{
                display: flex;
                justify-content: center;
                }
    /*  btn inicio */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(6) > div{
    display: flex;
    justify-content:end
                }
             
                <style>''', unsafe_allow_html=True)


    col1, col2 = st.columns(2)
    with col1:
        g1.graficas(df,grupo)
    with col2:
        tab1, tab2 = st.tabs(["Distribución puntos","Explicación de gráfica scatter"])
        with tab1: 
            bp.grafica_pie(df,grupo)
        with tab2:
            g1.description()

    col1, col2 = st.columns(2)
    with col1:
        bp.graf_embudo(df)
    with col2:
        tab1, tab2 = st.tabs(["Tabla de resultados","Info útil"])
        with tab1: 
            # st.markdown(f"<h3 style='text-align: center; color:#00ffff'>Tabla de resultados</h3>", unsafe_allow_html=True)
            g1.table_result(df)
        with tab2:
            st.markdown("### Recursos útiles Bootcamp-Xperience")
            links = [
                {"name": "Web BX alumno", "url": "https://bootcampxperience.com/bootcamp-alumno"},
                {"name": "LinkedIn BX", "url": "https://www.linkedin.com/company/bootcampxperience"},
                {"name": "YouTube BX", "url": "https://www.youtube.com/@BootcampXperience"},
                {"name": "GitHub BX", "url": "https://github.com/BootcampXperience"},
                {"name": "WhatsApp BX", "url": "https://www.whatsapp.com/channel/0029VakultYHbFV2IaSQwm1J"},
                {"name": "Discord BX", "url": "https://discord.com/channels/1142901240523669616/1143720307450978464"},
                {"name": "Contactar a Julio en Discord", "url": "https://discord.com/users/992155311056097360"},
                # Add more links as needed id usuario discord julio: Discordapp/user/992155311056097350
            ]
            for link in links:
                st.markdown(f"[{link['name']}]({link['url']})")

    volver_btn = st.button("Volver a la página inicial")
    if volver_btn:
            st.session_state.authenticated = False
            st.rerun()
    
    # info_btn = st.button("Más información")
    # if info_btn:
    #         st.markdown("#### Información adicional")
    #         st.write("Este clasificador de liderazgo...")
