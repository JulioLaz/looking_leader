import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# columnas=['Nombre','Promedio_Tecnicas','Promedio_Blandas','Experiencia  [En Data Science]','Experiencia  [En liderar grupos]','Puntaje_Liderazgo','Grupo']


def graficas(df,grupo):
    colors = px.colors.sequential.Inferno_r[:len(df)]

    fig = go.Figure()

    quadrants = [
        {'x': [0, 5, 5, 0], 'y': [0, 0, 5, 5], 'fillcolor': 'rgba(255, 0, 0, 0.5)', 'name': 'Bajo rendimiento'},
        {'x': [0, 5, 5, 0], 'y': [5, 5, 10, 10], 'fillcolor': 'rgba(246, 200, 15, 0.7)', 'name': 'Habilidades blandas fuertes'},
        {'x': [5, 10, 10, 5], 'y': [0, 0, 5, 5], 'fillcolor': 'rgba(246, 200, 15, 0.7)', 'name': 'Habilidades técnicas fuertes'},
        {'x': [5, 10, 10, 5], 'y': [5, 5, 10, 10], 'fillcolor': 'rgba(00, 255, 255, 0.6)', 'name': 'Alto rendimiento'},
    ]

    for quadrant in quadrants:
        fig.add_trace(go.Scatter(
            x=quadrant['x'], y=quadrant['y'],
            fill='toself',
            fillcolor=quadrant['fillcolor'],
            line=dict(color='rgba(255, 255, 255, 0)'),
            showlegend=False,
            hoverinfo='skip'
        ))

    # Add scatter plot
    fig.add_trace(go.Scatter(
        x=df['Promedio_Tecnicas'],
        y=df['Promedio_Blandas'],
        mode='markers+text',
        marker=dict(
            size=(df['Experiencia  [En Data Science]'] + df['Experiencia  [En liderar grupos]']) * 2,
            color=df['Puntaje_Liderazgo'],
            # colorscale=colors,
            # colorscale='Inferno_r',
            colorscale='Viridis_r',
            colorbar=dict(title='Liderazgo'),
            line=dict(width=1, color='black')
        ),
        text=df['Nombre'],
        textposition='bottom center',
        hoverinfo='text',
        hovertext=[f"{name}<br>Técnicas: {tech:.1f}<br>Blandas: {soft:.1f}<br>Liderazgo: {lead}"
                   for name, tech, soft, lead in zip(df['Nombre'], df['Promedio_Tecnicas'], 
                                                     df['Promedio_Blandas'], df['Puntaje_Liderazgo'])],
    ))

    fig.update_layout(
    title={
        'text': f"Analizando Liderazgo",
        'font': {'size': 22, 'color': 'skyblue', 'family': 'Arial, sans-serif'},
        'x': 0.5,  # Centrar el título
        'xanchor': 'center'
    },
    xaxis_title={
        'text': "Habilidades Técnicas",
        'font': {'size': 18, 'color': 'lime', 'family': 'Arial, sans-serif'}
    },
    yaxis_title={
        'text': "Habilidades Blandas",
        'font': {'size': 18, 'color': 'lime', 'family': 'Arial, sans-serif'}
    },
    showlegend=False,
    # width=600, 
    height=600, 
    paper_bgcolor='black',  # Fondo del gráfico
    plot_bgcolor='black',  # Fondo del área de trazado
    margin=dict(t=80, b=80, l=80, r=80)
    )
    

    # Add lines at x=5 and y=5
    fig.add_shape(type="line", x0=5, y0=0, x1=5, y1=10, line=dict(color="red", width=1, dash="dash"))
    fig.add_shape(type="line", x0=0, y0=5, x1=10, y1=5, line=dict(color="red", width=1, dash="dash"))

    # Update axes
    fig.update_xaxes(range=[0, 10], dtick=1)
    fig.update_yaxes(range=[0, 10], dtick=1)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    st.plotly_chart(fig, use_container_width=True)

    # st.subheader("Datos:")
def comment_00(df):
    columnas=['Nombre','Promedio_Tecnicas','Promedio_Blandas','Puntaje_Liderazgo']

    st.markdown('''<style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(7) > div{
                display: flex;
                justify-content:center;
                margin:10px 0;
                } </style>''', unsafe_allow_html=True)
    df=df[columnas]
    df.set_index('Nombre', inplace=True)
    st.dataframe(df)

# def comment_01():
#     st.markdown("""
#     Este gráfico muestra la evaluación de candidatos para liderazgo en Data Science:

#     - **Eje X**: Promedio de Habilidades Técnicas
#     - **Eje Y**: Promedio de Habilidades Blandas
#     - **Tamaño de los puntos**: Experiencia total (Data Science + Liderazgo de grupos)
#     - **Color de los puntos**: Puntaje de Liderazgo

#     Los cuadrantes representan:
#     - **Rojo**: Bajo rendimiento
#     - **Marrón (izquierda)**: Fuertes en habilidades blandas
#     - **Marrón (derecha)**: Fuertes en habilidades técnicas
#     - **Celeste**: Alto rendimiento

#     Pase el cursor sobre los puntos para ver más detalles de cada candidato.
#     """)

def comment_01():
    st.markdown("""
                        <style>
        td{
                text-align: center;}
        .tabla {
            width: 100% !important;
            max-width: 600px;
            # margin: auto;
            margin-left:10px!important;
                
        }
        @media (max-width: 600px) {
            .tabla {
                height: 400px !important;
                margin:10px !important;
            }
        }
        </style>


    <h4 style='display: flex; justify-content: center;'>Explicación de gráfica scatter</h4>
    <div style='display: flex;flex-direction: row; flex-wrap: wrap; align-items: center; justify-content: center;'>
    <table class='tabla' style="width:20vw; border-collapse: collapse;">
      <tr style="background-color: #f2f2f2;">
        <th style="font-size:1.3rem; border: 1px solid #ddd; padding: 8px; text-align: center;color:#000">Detalles del Gráfico</th>
      </tr>
      <tr>
         <td style="border: 1px solid #ddd; padding: 8px;"><strong>Eje X</strong>: Promedio de Habilidades Técnicas</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Eje Y</strong>: Promedio de Habilidades Blandas</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Tamaño de los puntos</strong>: Experiencia total</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><strong>Color de los puntos</strong>: Puntaje de Liderazgo</td>
      </tr>
    </table>
                
    <table class='tabla' style="width:50vw; border-collapse: collapse; margin-left: 10px;">
      <tr style="background-color: #f2f2f2;">
        <th style="font-size:1.3rem; border: 1px solid #ddd; padding: 8px; text-align: center;color:#000">Cuadrante</th>
        <th style="font-size:1.3rem; border: 1px solid #ddd; padding: 8px; text-align: center;color:#000">Descripción</th>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">Rojo</td>
        <td style="border: 1px solid #ddd; padding: 8px;">Bajo rendimiento</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">Marrón (izquierda)</td>
        <td style="border: 1px solid #ddd; padding: 8px;">Fuertes en habilidades blandas</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">Marrón (derecha)</td>
        <td style="border: 1px solid #ddd; padding: 8px;">Fuertes en habilidades técnicas</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;">Celeste</td>
        <td style="border: 1px solid #ddd; padding: 8px;">Alto rendimiento</td>
      </tr>
    </table>
    <br>
   </div>
    """, unsafe_allow_html=True)

