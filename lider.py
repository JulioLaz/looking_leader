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
    st.markdown(f"<div style='display:flex;justify-content:center; flex-direction: column'><h1 style='text-align: center;'>Bienvenido al clasificador de liderazgo</h1><h5 style='width: 100%;padding: 0 2rem 2rem 2rem; word-wrap: break-word;text-align:center;color:gray'>Esto es una ayuda para definir al líder, en principio el de mayor score será el primer candidato y si acepta y tiene disponibilidad será el designado!</h5></div>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Ingresa el nombre que pusiste en el formulario:", value=st.session_state.nombre)
    styles.text_input()
    grupos_disponibles = list(df['Grupo'].sort_values(ascending=True).unique())

    if grupos_disponibles:
        st.session_state.selected_group = st.radio(f"Grupo:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", df['Grupo'].sort_values(ascending=True).unique(), index=0 if st.session_state.selected_group is None else list(df['Grupo'].sort_values(ascending=True).unique()).index(st.session_state.selected_group), horizontal=True)
    else: st.info('Aún ningún miembro llenó el formulario!')
    # st.session_state.selected_group = st.radio(f"Grupo:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", [1,2,3,4], index=0 if st.session_state.selected_group is None else list(df['Grupo'].sort_values(ascending=True).unique()).index(st.session_state.selected_group), horizontal=True)
    styles.radio()

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
    styles.graficas()
    
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
            ]
            for link in links:
                st.markdown(f"[{link['name']}]({link['url']})")

    volver_btn = st.button("Volver a la página inicial")
    if volver_btn:
            st.session_state.authenticated = False
            st.rerun()