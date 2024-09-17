import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def graficas(df,grupo):
    colors = px.colors.sequential.Inferno_r[:len(df)]

    fig = go.Figure()

    quadrants = [
        {'x': [0, 5, 5, 0], 'y': [0, 0, 5, 5], 'fillcolor': 'rgba(255, 0, 0, 0.5)', 'name': 'Bajo rendimiento'},
        {'x': [0, 5, 5, 0], 'y': [5, 5, 10, 10], 'fillcolor': 'rgba(246, 200, 15, 0.7)', 'name': 'Habilidades blandas fuertes'},
        {'x': [5, 10, 10, 5], 'y': [0, 0, 5, 5], 'fillcolor': 'rgba(246, 200, 15, 0.7)', 'name': 'Habilidades técnicas fuertes'},
        {'x': [5, 10, 10, 5], 'y': [5, 5, 10, 10], 'fillcolor': 'rgba(00, 255, 255, 0.6)', 'name': 'Alto rendimiento'},
        {'x': [0, 11, 11, 0], 'y': [10, 10, 11, 11], 'fillcolor': 'rgba(156, 156, 156, 0.6)', 'name': 'Alto rendimiento'},
        {'x': [10, 11, 11, 10], 'y': [0, 0, 10, 10], 'fillcolor': 'rgba(156, 156, 156, 0.6)', 'name': 'Alto rendimiento'},
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
            colorscale='Viridis_r',
            colorbar=dict(title='Liderazgo'),
            line=dict(width=1, color='black')
        ),
        text=df['Nombre'],
        textfont=dict(size=12, color='white'),
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
        'y': 0.95,  # Centrar el título
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

    fig.add_shape(type="line", x0=5, y0=0, x1=5, y1=10, line=dict(color="red", width=1, dash="dash"))
    fig.add_shape(type="line", x0=0, y0=5, x1=10, y1=5, line=dict(color="red", width=1, dash="dash"))
    fig.update_xaxes(range=[0, 11], dtick=1)
    fig.update_yaxes(range=[0, 11], dtick=1)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    st.plotly_chart(fig, use_container_width=True)

def table_result(df):
    columnas = ['Nombre', 'Promedio_Tecnicas', 'Promedio_Blandas', 'Puntaje_Liderazgo']
    df = df[columnas]
    html = '<table class="tabla">'
    html += '<thead><tr>'
    columnas_name = ['Nombre', 'hab. Técnicas', 'hab. Blandas', 'Score']

    for col in columnas_name:
        html += f'<th>{col}</th>'
    html += '</tr></thead><tbody>'

    for _, row in df.iterrows():
        html += '<tr>'
        for col in columnas:
            html += f'<td>{row[col]}</td>'
        html += '</tr>'
    
    html += '</tbody></table>'
    st.markdown(html, unsafe_allow_html=True)    

def description():
    st.markdown("""
                        <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div:nth-child(2) > div > div > div > div:nth-child(2) > div{
                display: flex;
                justify-content: center;
                margin: 0;
                }
    tr:nth-child(even) {
                    background-color: #525252;
                }
    th {
                background-color: #00ffff;
                color: #000;
                font-size: calc(10px + .5vw);
                border: 1px solid white !important; 
                text-align: center;
                }
    tbody tr:hover {
                    background-color: #222;
                }                
        td{
                text-align: center;
                border: 1px solid white !important;
                padding: 5px 0px !important;
                font-size: calc(8px + .5vw);
                color: #fff;
                }

        .tabla {
            width: 96% !important;
            padding-bottom: 5px !important;
            margin: 0px 2%;
        }
        @media (max-width: 600px) {
            .tabla {
                padding-bottom: 5px !important;
                width: 100%;
            }
        }
        </style>


    <h4 style='display: flex; justify-content: center; color: #00ffff;'>Explicación de gráfica scatter</h4>
    <div style='display: flex;flex-direction: row; flex-wrap: wrap; align-items: center; justify-content: center'>
    <table class='tabla' style="border-collapse: collapse; margin: 5px 10px">
      <tr style="background-color: #f2f2f2;">
        <th>Detalles del Gráfico</th>
      </tr>
      <tr>
         <td><strong>Eje X</strong>: Promedio de Habilidades Técnicas</td>
      </tr>
      <tr>
        <td><strong>Eje Y</strong>: Promedio de Habilidades Blandas</td>
      </tr>
      <tr>
        <td><strong>Tamaño de los puntos</strong>: Experiencia total</td>
      </tr>
      <tr>
        <td><strong>Color de los puntos</strong>: Puntaje de Liderazgo</td>
      </tr>
    </table>
                
    <table class='tabla' style="border-collapse: collapse; margin: 0 10px">
      <tr style="background-color: #f2f2f2;">
        <th>Cuadrante</th>
        <th>Descripción</th>
      </tr>
      <tr>
        <td>Rojo</td>
        <td>Bajo rendimiento</td>
      </tr>
      <tr>
        <td>Marrón (izquierda)</td>
        <td>Fuertes en habilidades blandas</td>
      </tr>
      <tr>
        <td>Marrón (derecha)</td>
        <td>Fuertes en habilidades técnicas</td>
      </tr>
      <tr>
        <td>Celeste</td>
        <td>Alto rendimiento</td>
      </tr>
    </table>
    <br>
   </div>
    """, unsafe_allow_html=True)

